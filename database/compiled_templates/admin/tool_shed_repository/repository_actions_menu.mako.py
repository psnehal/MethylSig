# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1433363697.2492311
_template_filename=u'templates/admin/tool_shed_repository/repository_actions_menu.mako'
_template_uri=u'/admin/tool_shed_repository/repository_actions_menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_galaxy_repository_actions']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_galaxy_repository_actions(context,repository=None):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        workflow_name = context.get('workflow_name', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4

        from tool_shed.util.encoding_util import tool_shed_encode
        in_error_state = repository.in_error_state
        tool_dependency_ids = [ trans.security.encode_id( td.id ) for td in repository.tool_dependencies ]
        if repository.status in [ trans.install_model.ToolShedRepository.installation_status.DEACTIVATED,
                                  trans.install_model.ToolShedRepository.installation_status.ERROR,
                                  trans.install_model.ToolShedRepository.installation_status.INSTALLED ]:
            can_administer = True
        else:
            can_administer = False
            
        
        # SOURCE LINE 14
        __M_writer(u'\n    <br/><br/>\n    <ul class="manage-table-actions">\n        <li><a class="action-button" id="repository-')
        # SOURCE LINE 17
        __M_writer(unicode(repository.id))
        __M_writer(u'-popup" class="menubutton">Repository Actions</a></li>\n        <div popupmenu="repository-')
        # SOURCE LINE 18
        __M_writer(unicode(repository.id))
        __M_writer(u'-popup">\n')
        # SOURCE LINE 19
        if workflow_name:
            # SOURCE LINE 20
            __M_writer(u'                <li><a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='import_workflow', workflow_name=tool_shed_encode( workflow_name ), repository_id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Import workflow to Galaxy</a></li>\n')
            pass
        # SOURCE LINE 22
        if repository.can_reinstall_or_activate:
            # SOURCE LINE 23
            __M_writer(u'                <a class="action-button" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_repositories', operation='activate or reinstall', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Activate or reinstall repository</a>\n')
            pass
        # SOURCE LINE 25
        if in_error_state:
            # SOURCE LINE 26
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='reset_to_install', id=trans.security.encode_id( repository.id ), reset_repository=True )))
            __M_writer(u'">Reset to install</a>\n')
            # SOURCE LINE 27
        elif repository.can_install:
            # SOURCE LINE 28
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=trans.security.encode_id( repository.id ), operation='install' )))
            __M_writer(u'">Install</a>\n')
            # SOURCE LINE 29
        elif can_administer:
            # SOURCE LINE 30
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Manage repository</a>\n                <a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 31
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Browse repository files</a>\n                <a class="action-button" target="galaxy_main" href="')
            # SOURCE LINE 32
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='check_for_updates', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Get repository updates</a>\n')
            # SOURCE LINE 33
            if repository.can_reset_metadata:
                # SOURCE LINE 34
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='reset_repository_metadata', id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Reset repository metadata</a>\n')
                pass
            # SOURCE LINE 36
            if repository.includes_tools:
                # SOURCE LINE 37
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='set_tool_versions', id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Set tool versions</a>\n')
                pass
            # SOURCE LINE 39
            if tool_dependency_ids:
                # SOURCE LINE 40
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository_tool_dependencies', tool_dependency_ids=tool_dependency_ids, repository_id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Manage tool dependencies</a>\n')
                pass
            # SOURCE LINE 42
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='deactivate_or_uninstall_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Deactivate or uninstall repository</a>\n')
            pass
        # SOURCE LINE 44
        __M_writer(u'            <a class="action-button" target="galaxy_main" href="')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='repair_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'">Repair repository</a>\n        </div>\n    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


