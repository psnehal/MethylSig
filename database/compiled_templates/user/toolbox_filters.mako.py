# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1434391208.8490701
_template_filename='templates/user/toolbox_filters.mako'
_template_uri='user/toolbox_filters.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x947d210', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x947d210')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x947d210')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        label_filters = _import_ns.get('label_filters', context.get('label_filters', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        tool_filters = _import_ns.get('tool_filters', context.get('tool_filters', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        section_filters = _import_ns.get('section_filters', context.get('section_filters', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if message:
            # SOURCE LINE 5
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 7
        __M_writer(u'</br>\n</br>\n\n<ul class="manage-table-actions">\n    <li>\n        <a class="action-button"  href="')
        # SOURCE LINE 12
        __M_writer(unicode(h.url_for( controller='user', action='index', cntrller=cntrller )))
        __M_writer(u'">User preferences</a>\n    </li>\n</ul>\n\n')
        # SOURCE LINE 16
        if tool_filters or section_filters or label_filters:
            # SOURCE LINE 17
            __M_writer(u'    <div class="toolForm">\n        <form name="toolbox_filter" id="toolbox_filter" action="')
            # SOURCE LINE 18
            __M_writer(unicode(h.url_for( controller='user', action='edit_toolbox_filters', cntrller=cntrller, user_id=trans.security.encode_id( user.id ) )))
            __M_writer(u'" method="post" >\n')
            # SOURCE LINE 19
            if tool_filters:
                # SOURCE LINE 20
                __M_writer(u'                <div class="toolFormTitle">Edit ToolBox filters :: Tools</div>\n                <div class="toolFormBody">\n')
                # SOURCE LINE 22
                for filter in tool_filters:
                    # SOURCE LINE 23
                    __M_writer(u'                        <div class="form-row">\n                            <div style="float: left; width: 40px; margin-right: 10px;">\n')
                    # SOURCE LINE 25
                    if filter['checked']:
                        # SOURCE LINE 26
                        __M_writer(u'                                    <input type="checkbox" name="t_')
                        __M_writer(unicode(filter['filterpath']))
                        __M_writer(u'" checked="checked">\n')
                        # SOURCE LINE 27
                    else:
                        # SOURCE LINE 28
                        __M_writer(u'                                    <input type="checkbox" name="t_')
                        __M_writer(unicode(filter['filterpath']))
                        __M_writer(u'">\n')
                        pass
                    # SOURCE LINE 30
                    __M_writer(u'                            </div>\n                            <div style="float: left; margin-right: 10px;">\n                                ')
                    # SOURCE LINE 32
                    __M_writer(unicode(filter['short_desc']))
                    __M_writer(u'\n                                <div class="toolParamHelp" style="clear: both;">')
                    # SOURCE LINE 33
                    __M_writer(unicode(filter['desc']))
                    __M_writer(u'</div>\n                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n')
                    pass
                # SOURCE LINE 38
                __M_writer(u'                </div>\n')
                pass
            # SOURCE LINE 40
            __M_writer(u'\n')
            # SOURCE LINE 41
            if section_filters:
                # SOURCE LINE 42
                __M_writer(u'                <div class="toolFormTitle">Edit ToolBox filters :: Sections</div>\n                <div class="toolFormBody">\n')
                # SOURCE LINE 44
                for filter in section_filters:
                    # SOURCE LINE 45
                    __M_writer(u'                        <div class="form-row">\n                            <div style="float: left; width: 40px; margin-right: 10px;">\n')
                    # SOURCE LINE 47
                    if filter['checked']:
                        # SOURCE LINE 48
                        __M_writer(u'                                    <input type="checkbox" name="s_')
                        __M_writer(unicode(filter['filterpath']))
                        __M_writer(u'" checked="checked">\n')
                        # SOURCE LINE 49
                    else:
                        # SOURCE LINE 50
                        __M_writer(u'                                    <input type="checkbox" name="s_')
                        __M_writer(unicode(filter['filterpath']))
                        __M_writer(u'">\n')
                        pass
                    # SOURCE LINE 52
                    __M_writer(u'                            </div>\n                            <div style="float: left; margin-right: 10px;">\n                                ')
                    # SOURCE LINE 54
                    __M_writer(unicode(filter['short_desc']))
                    __M_writer(u'\n                                <div class="toolParamHelp" style="clear: both;">')
                    # SOURCE LINE 55
                    __M_writer(unicode(filter['desc']))
                    __M_writer(u'</div>\n                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n')
                    pass
                # SOURCE LINE 60
                __M_writer(u'                </div>\n')
                pass
            # SOURCE LINE 62
            __M_writer(u'\n')
            # SOURCE LINE 63
            if label_filters:
                # SOURCE LINE 64
                __M_writer(u'                <div class="toolFormTitle">Edit ToolBox filters :: Labels</div>\n                <div class="toolFormBody">\n')
                # SOURCE LINE 66
                for filter in label_filters:
                    # SOURCE LINE 67
                    __M_writer(u'                        <div class="form-row">\n                            <div style="float: left; width: 40px; margin-right: 10px;">\n')
                    # SOURCE LINE 69
                    if filter['checked']:
                        # SOURCE LINE 70
                        __M_writer(u'                                    <input type="checkbox" name="l_')
                        __M_writer(unicode(filter['filterpath']))
                        __M_writer(u'" checked="checked">\n')
                        # SOURCE LINE 71
                    else:
                        # SOURCE LINE 72
                        __M_writer(u'                                    <input type="checkbox" name="l_')
                        __M_writer(unicode(filter['filterpath']))
                        __M_writer(u'">\n')
                        pass
                    # SOURCE LINE 74
                    __M_writer(u'                            </div>\n                            <div style="float: left; margin-right: 10px;">\n                                ')
                    # SOURCE LINE 76
                    __M_writer(unicode(filter['short_desc']))
                    __M_writer(u'\n                                <div class="toolParamHelp" style="clear: both;">')
                    # SOURCE LINE 77
                    __M_writer(unicode(filter['desc']))
                    __M_writer(u'</div>\n                            </div>\n                            <div style="clear: both"></div>\n                        </div>\n')
                    pass
                # SOURCE LINE 82
                __M_writer(u'                </div>\n')
                pass
            # SOURCE LINE 84
            __M_writer(u'            <div class="form-row">\n                <input type="submit" name="edit_toolbox_filter_button" value="Save changes">\n            </div>\n        </form>\n    </div>\n')
            # SOURCE LINE 89
        else:
            # SOURCE LINE 90
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( 'No filter available. Contact you system administrator or check your configuration file.', 'info' )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


