from django import forms

from meta_form.models import ResearchMetadata


class ResearchMetadataForm(forms.ModelForm):
    class Meta:
        model = ResearchMetadata
        fields = '__all__'
