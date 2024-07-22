import pluggy

from meta_form import app_name

hookspec = pluggy.HookspecMarker(app_name)
plugin_manager = pluggy.PluginManager(app_name)


@hookspec
def meta_data_download_format(meta_data):
    """Transform research_metadata into specific format
        :param meta_data: ResearchMetadataModel
        :return file_content: str, file_name_with_format: str"""