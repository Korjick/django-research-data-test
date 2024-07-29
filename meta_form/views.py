import zipfile

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from meta_form.forms import ResearchMetadataForm
from meta_form.models import ResearchMetadata
from meta_form.pluggy_specs import plugin_manager


def index(req):
    form = ResearchMetadataForm()

    if req.method == 'POST':
        form = ResearchMetadataForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('meta_form:index')

    research = ResearchMetadata.objects.all().select_related('data_format', 'degree_of_aggregation')
    return HttpResponse(render(req, 'index.html', context={
        'form': form,
        'research': research
    }))


def download_all_metadata(request, metadata_id: int):
    research_meta_data = get_object_or_404(ResearchMetadata.objects.select_related('data_format', 'degree_of_aggregation'),
                                           pk=metadata_id)
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="metadata_files.zip"'
    with zipfile.ZipFile(response, 'w') as zf:
        res = plugin_manager.hook.meta_data_download_format(meta_data=research_meta_data)
        for (content, format_with_name) in res:
            zf.writestr(format_with_name, content)

    return response
