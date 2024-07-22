import pluggy

from meta_form import app_name

hookimpl = pluggy.HookimplMarker(app_name)


@hookimpl(specname='meta_data_download_format')
def meta_data_download_dublin_core_html_format(meta_data):
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
        <title>Dublin Core Metadata for {meta_data.data_provider}</title>
        <meta name="DC.title" content="{meta_data.data_provider}" />
        <meta name="DC.description" content="{meta_data.degree_of_aggregation.description}" />
        <meta name="DC.date" content="{meta_data.updated_at.strftime('%Y-%m-%d')}" />
        <meta name="DC.type" content="{meta_data.degree_of_aggregation.name}" />
        <meta name="DC.format" content="{meta_data.data_format.name}" />
        <meta name="DC.identifier" content="{meta_data.data_provider}#{meta_data.pk}" />
        <meta name="DC.language" content="en" />
        </head>
        <body>
            <h1>Metadata for {meta_data.data_provider}</h1>
            <p>See the document head for metadata in Dublin Core format.</p>
        </body>
        </html>
        """
    return html_content, 'README.txt'
