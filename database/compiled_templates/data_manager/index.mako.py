# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1433516295.7069139
_template_filename='templates/webapps/galaxy/data_manager/index.mako'
_template_uri='data_manager/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f90200f7f90', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f90200f7f90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f90200f7f90')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        data_managers = _import_ns.get('data_managers', context.get('data_managers', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        view_only = _import_ns.get('view_only', context.get('view_only', UNDEFINED))
        tool_data_tables = _import_ns.get('tool_data_tables', context.get('tool_data_tables', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        if message:
            # SOURCE LINE 7
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 9
        __M_writer(u'\n<h2>Data Manager</h2>\n\n')
        # SOURCE LINE 12
        if view_only:
            # SOURCE LINE 13
            __M_writer(u'    <p>Not implemented</p>\n')
            # SOURCE LINE 14
        elif not data_managers.data_managers:
            # SOURCE LINE 15
            __M_writer(u'    ')
            __M_writer(unicode( render_msg( 'You do not currently have any Data Managers installed. You can install some from a <a href="%s">ToolShed</a>.' % ( h.url_for( controller="admin_toolshed", action="browse_tool_sheds" ) ), "warning" ) ))
            __M_writer(u'\n')
            # SOURCE LINE 16
        else:
            # SOURCE LINE 17
            __M_writer(u'    <p>Choose your data managing option from below. You may install additional Data Managers from a <a href="')
            __M_writer(unicode( h.url_for( controller='admin_toolshed', action='browse_tool_sheds' ) ))
            __M_writer(u'">ToolShed</a>.</p>\n    <ul>\n        <li><h3>Run Data Manager Tools</h3>\n            <div style="margin-left:1em">\n            <ul>\n')
            # SOURCE LINE 22
            for data_manager_id, data_manager in sorted( data_managers.data_managers.iteritems(), key=lambda x:x[1].name ):
                # SOURCE LINE 23
                __M_writer(u'                <li>\n                    <a href="')
                # SOURCE LINE 24
                __M_writer(unicode( h.url_for( controller='tool_runner', action='index', tool_id=data_manager.tool.id ) ))
                __M_writer(u'"><strong>')
                __M_writer(filters.html_escape(unicode( data_manager.name )))
                __M_writer(u'</strong></a> - ')
                __M_writer(filters.html_escape(unicode( data_manager.description )))
                __M_writer(u'\n                </li>\n                <p/>\n')
                pass
            # SOURCE LINE 28
            __M_writer(u'            </ul>\n            </div>\n        </li>\n        <p/>\n        <li><h3>View Data Manager Jobs</h3>\n            <div style="margin-left:1em">\n            <ul>\n')
            # SOURCE LINE 35
            for data_manager_id, data_manager in sorted( data_managers.data_managers.iteritems(), key=lambda x:x[1].name ):
                # SOURCE LINE 36
                __M_writer(u'                    <li>\n                        <a href="')
                # SOURCE LINE 37
                __M_writer(unicode( h.url_for( controller='data_manager', action='manage_data_manager', id=data_manager_id)))
                __M_writer(u'" target="galaxy_main"><strong>')
                __M_writer(filters.html_escape(unicode( data_manager.name )))
                __M_writer(u'</strong></a> - ')
                __M_writer(filters.html_escape(unicode( data_manager.description )))
                __M_writer(u'</a>\n                    </li>\n                    <p/>\n')
                pass
            # SOURCE LINE 41
            __M_writer(u'            </ul>\n            </div>\n        </li>\n        <p/>\n        <p/>\n        <li><h3>View Tool Data Table Entries</h3>\n            <div style="margin-left:1em">\n            <ul>\n                ')
            # SOURCE LINE 49
            managed_table_names = data_managers.managed_data_tables.keys() 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['managed_table_names'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            # SOURCE LINE 50
            for table_name in sorted( tool_data_tables.get_tables().keys() ):
                # SOURCE LINE 51
                __M_writer(u'                    <li>\n                        <a href="')
                # SOURCE LINE 52
                __M_writer(unicode(h.url_for( controller='data_manager', action='manage_data_table', table_name=table_name)))
                __M_writer(u'" target="galaxy_main">\n')
                # SOURCE LINE 53
                if table_name in managed_table_names:
                    # SOURCE LINE 54
                    __M_writer(u'                                </span><strong>')
                    __M_writer(filters.html_escape(unicode( table_name )))
                    __M_writer(u'</strong></a> <span class="fa fa-exchange">\n')
                    # SOURCE LINE 55
                else:
                    # SOURCE LINE 56
                    __M_writer(u'                                ')
                    __M_writer(filters.html_escape(unicode( table_name )))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 58
                __M_writer(u'                    </li>\n                    <p/>\n')
                pass
            # SOURCE LINE 61
            __M_writer(u'            </ul>\n            </div>\n        </li>\n        <p/>\n    </ul>\n    <p/>\n    <br/>\n')
            pass
        # SOURCE LINE 69
        __M_writer(u'\n')
        # SOURCE LINE 70
        __M_writer(unicode(render_msg( 'To find out more information about Data Managers, please visit the <a href="https://wiki.galaxyproject.org/Admin/Tools/DataManagers" target="_blank">wiki.</a>', "info" ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f90200f7f90')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Data Manager')
        return ''
    finally:
        context.caller_stack._pop_frame()


