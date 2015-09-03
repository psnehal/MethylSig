# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1433361600.0885601
_template_filename='templates/admin/tool_shed_repository/select_tool_panel_section.mako'
_template_uri='/admin/tool_shed_repository/select_tool_panel_section.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f9020037e90', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f9020037e90')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7f90200374d0', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f90200374d0')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f9020037cd0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f9020037cd0')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f90200370d0', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f90200370d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f9020037e90')._populate(_import_ns, [u'render_readme_section'])
        _mako_get_namespace(context, '__anon_0x7f90200374d0')._populate(_import_ns, [u'render_dependencies_section'])
        _mako_get_namespace(context, '__anon_0x7f9020037cd0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f90200370d0')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        encoded_updated_metadata = _import_ns.get('encoded_updated_metadata', context.get('encoded_updated_metadata', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        render_readme_section = _import_ns.get('render_readme_section', context.get('render_readme_section', UNDEFINED))
        install_repository_dependencies_check_box = _import_ns.get('install_repository_dependencies_check_box', context.get('install_repository_dependencies_check_box', UNDEFINED))
        shed_tool_conf = _import_ns.get('shed_tool_conf', context.get('shed_tool_conf', UNDEFINED))
        encoded_repo_info_dicts = _import_ns.get('encoded_repo_info_dicts', context.get('encoded_repo_info_dicts', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        includes_tool_dependencies = _import_ns.get('includes_tool_dependencies', context.get('includes_tool_dependencies', UNDEFINED))
        updating_repository_id = _import_ns.get('updating_repository_id', context.get('updating_repository_id', UNDEFINED))
        tool_shed_url = _import_ns.get('tool_shed_url', context.get('tool_shed_url', UNDEFINED))
        containers_dict = _import_ns.get('containers_dict', context.get('containers_dict', UNDEFINED))
        has_repository_dependencies = _import_ns.get('has_repository_dependencies', context.get('has_repository_dependencies', UNDEFINED))
        includes_tools_for_display_in_tool_panel = _import_ns.get('includes_tools_for_display_in_tool_panel', context.get('includes_tools_for_display_in_tool_panel', UNDEFINED))
        shed_tool_conf_select_field = _import_ns.get('shed_tool_conf_select_field', context.get('shed_tool_conf_select_field', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        updating_to_changeset_revision = _import_ns.get('updating_to_changeset_revision', context.get('updating_to_changeset_revision', UNDEFINED))
        tool_panel_section_select_field = _import_ns.get('tool_panel_section_select_field', context.get('tool_panel_section_select_field', UNDEFINED))
        includes_tools = _import_ns.get('includes_tools', context.get('includes_tools', UNDEFINED))
        install_tool_dependencies_check_box = _import_ns.get('install_tool_dependencies_check_box', context.get('install_tool_dependencies_check_box', UNDEFINED))
        updating = _import_ns.get('updating', context.get('updating', UNDEFINED))
        render_dependencies_section = _import_ns.get('render_dependencies_section', context.get('render_dependencies_section', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        new_tool_panel_section_label = _import_ns.get('new_tool_panel_section_label', context.get('new_tool_panel_section_label', UNDEFINED))
        updating_to_ctx_rev = _import_ns.get('updating_to_ctx_rev', context.get('updating_to_ctx_rev', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18

    # Handle the case where an uninstalled repository encountered errors during the process of being reinstalled.  In
    # this case, the repository metadata is an empty dictionary, but one or both of has_repository_dependencies
    # and includes_tool_dependencies may be True.  If either of these are True but we have no metadata, we cannot install
    # repository dependencies on this pass.
        if has_repository_dependencies:
            repository_dependencies = containers_dict[ 'repository_dependencies' ]
            missing_repository_dependencies = containers_dict[ 'missing_repository_dependencies' ]
            if repository_dependencies or missing_repository_dependencies:
                can_display_repository_dependencies = True
            else:
                can_display_repository_dependencies = False
        else:
            can_display_repository_dependencies = False
        if includes_tool_dependencies:
            tool_dependencies = containers_dict[ 'tool_dependencies' ]
            missing_tool_dependencies = containers_dict[ 'missing_tool_dependencies' ]
            if tool_dependencies or missing_tool_dependencies:
                can_display_tool_dependencies = True
            else:
                can_display_tool_dependencies = False
        else:
            can_display_tool_dependencies = False
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_display_tool_dependencies','missing_tool_dependencies','missing_repository_dependencies','repository_dependencies','can_display_repository_dependencies','tool_dependencies'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        if message:
            # SOURCE LINE 44
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 46
        __M_writer(u'\n<div class="warningmessage">\n    <p>\n        The Galaxy development team does not maintain the contents of many Galaxy Tool Shed repositories.  Some\n        repository tools may include code that produces malicious behavior, so be aware of what you are installing.\n    </p>\n    <p>\n        If you discover a repository that causes problems after installation, contact <a href="https://wiki.galaxyproject.org/Support" target="_blank">Galaxy support</a>,\n        sending all necessary information, and appropriate action will be taken.\n    </p>\n    <p>\n        <a href="https://wiki.galaxyproject.org/ToolShedRepositoryFeatures#Contact_repository_owner" target="_blank">Contact the repository owner</a> for \n        general questions or concerns.\n    </p>\n</div>\n<div class="toolForm">\n    <div class="toolFormBody">\n        <form name="select_tool_panel_section" id="select_tool_panel_section" action="')
        # SOURCE LINE 63
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='prepare_for_install' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <input type="hidden" name="includes_tools" value="')
        # SOURCE LINE 65
        __M_writer(unicode(includes_tools))
        __M_writer(u'" />\n                <input type="hidden" name="includes_tool_dependencies" value="')
        # SOURCE LINE 66
        __M_writer(unicode(includes_tool_dependencies))
        __M_writer(u'" />\n                <input type="hidden" name="includes_tools_for_display_in_tool_panel" value="')
        # SOURCE LINE 67
        __M_writer(unicode(includes_tools_for_display_in_tool_panel))
        __M_writer(u'" />\n                <input type="hidden" name="tool_shed_url" value="')
        # SOURCE LINE 68
        __M_writer(unicode(tool_shed_url))
        __M_writer(u'" />\n                <input type="hidden" name="encoded_repo_info_dicts" value="')
        # SOURCE LINE 69
        __M_writer(unicode(encoded_repo_info_dicts))
        __M_writer(u'" />\n                <input type="hidden" name="updating" value="')
        # SOURCE LINE 70
        __M_writer(unicode(updating))
        __M_writer(u'" />\n                <input type="hidden" name="updating_repository_id" value="')
        # SOURCE LINE 71
        __M_writer(unicode(updating_repository_id))
        __M_writer(u'" />\n                <input type="hidden" name="updating_to_ctx_rev" value="')
        # SOURCE LINE 72
        __M_writer(unicode(updating_to_ctx_rev))
        __M_writer(u'" />\n                <input type="hidden" name="updating_to_changeset_revision" value="')
        # SOURCE LINE 73
        __M_writer(unicode(updating_to_changeset_revision))
        __M_writer(u'" />\n                <input type="hidden" name="encoded_updated_metadata" value="')
        # SOURCE LINE 74
        __M_writer(unicode(encoded_updated_metadata))
        __M_writer(u'" />\n            </div>\n            <div style="clear: both"></div>\n            ')
        # SOURCE LINE 77
        readme_files_dict = containers_dict.get( 'readme_files', None ) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['readme_files_dict'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 78
        if readme_files_dict:
            # SOURCE LINE 79
            __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <th bgcolor="#EBD9B2">Repository README file - may contain important installation or license information</th>\n                    </table>\n                </div>\n                ')
            # SOURCE LINE 84
            __M_writer(unicode(render_readme_section( containers_dict )))
            __M_writer(u'\n                <div style="clear: both"></div>\n')
            pass
        # SOURCE LINE 87
        if can_display_repository_dependencies or can_display_tool_dependencies:
            # SOURCE LINE 88
            __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <th bgcolor="#EBD9B2">Confirm dependency installation</th>\n                    </table>\n                </div>\n                ')
            # SOURCE LINE 93
            __M_writer(unicode(render_dependencies_section( install_repository_dependencies_check_box, install_tool_dependencies_check_box, containers_dict, revision_label=None, export=False )))
            __M_writer(u'\n                <div style="clear: both"></div>\n')
            pass
        # SOURCE LINE 96
        if shed_tool_conf_select_field:
            # SOURCE LINE 97
            __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <th bgcolor="#EBD9B2">Choose the tool panel section to contain the installed tools (optional)</th>\n                    </table>\n                </div>\n                ')
            # SOURCE LINE 102

            if len( shed_tool_conf_select_field.options ) == 1:
                select_help = "Your Galaxy instance is configured with 1 shed-related tool configuration file, so repositories will be "
                select_help += "installed using its <b>tool_path</b> setting."
            else:
                select_help = "Your Galaxy instance is configured with %d shed-related tool configuration files, " % len( shed_tool_conf_select_field.options )
                select_help += "so select the file whose <b>tool_path</b> setting you want used for installing repositories."
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['select_help'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 109
            __M_writer(u'\n                <div class="form-row">\n                    <label>Shed tool configuration file:</label>\n                    ')
            # SOURCE LINE 112
            __M_writer(unicode(shed_tool_conf_select_field.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        ')
            # SOURCE LINE 114
            __M_writer(unicode(select_help))
            __M_writer(u'\n                    </div>\n                </div>\n                <div style="clear: both"></div>\n')
            # SOURCE LINE 118
        else:
            # SOURCE LINE 119
            __M_writer(u'                <input type="hidden" name="shed_tool_conf" value="')
            __M_writer(unicode(shed_tool_conf))
            __M_writer(u'"/>\n')
            pass
        # SOURCE LINE 121
        __M_writer(u'            <div class="form-row">\n                <label>Add new tool panel section:</label>\n                <input name="new_tool_panel_section_label" type="textfield" value="')
        # SOURCE LINE 123
        __M_writer(unicode(new_tool_panel_section_label))
        __M_writer(u'" size="40"/>\n                <div class="toolParamHelp" style="clear: both;">\n                    Add a new tool panel section to contain the installed tools (optional).\n                </div>\n            </div>\n            <div class="form-row">\n                <label>Select existing tool panel section:</label>\n                ')
        # SOURCE LINE 130
        __M_writer(unicode(tool_panel_section_select_field.get_html()))
        __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n                    Choose an existing section in your tool panel to contain the installed tools (optional).  \n                </div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="select_tool_panel_section_button" value="Install"/>\n                <div class="toolParamHelp" style="clear: both;">\n                    Clicking <b>Install</b> without selecting a tool panel section will load the installed tools into the tool panel outside of any sections.\n                </div>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f9020037e90')._populate(_import_ns, [u'render_readme_section'])
        _mako_get_namespace(context, '__anon_0x7f90200374d0')._populate(_import_ns, [u'render_dependencies_section'])
        _mako_get_namespace(context, '__anon_0x7f9020037cd0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f90200370d0')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 9
        __M_writer(unicode(h.css( "library" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f9020037e90')._populate(_import_ns, [u'render_readme_section'])
        _mako_get_namespace(context, '__anon_0x7f90200374d0')._populate(_import_ns, [u'render_dependencies_section'])
        _mako_get_namespace(context, '__anon_0x7f9020037cd0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7f90200370d0')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        container_javascripts = _import_ns.get('container_javascripts', context.get('container_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(h.js("libs/jquery/jquery.rating", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(container_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


