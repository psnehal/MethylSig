# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1434727147.2770729
_template_filename='templates/admin/external_service/create_external_service.mako'
_template_uri='/admin/external_service/create_external_service.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x7fd2f0197110', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fd2f0197110')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x7fd2f0197e90', context._clean_inheritance_tokens(), templateuri=u'/admin/external_service/common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fd2f0197e90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fd2f0197110')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fd2f0197e90')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        widgets = _import_ns.get('widgets', context.get('widgets', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        if message:
            # SOURCE LINE 6
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'\n<form name="create_external_service" action="')
        # SOURCE LINE 9
        __M_writer(unicode(h.url_for( controller='external_service', action='create_external_service' )))
        __M_writer(u'" method="post">\n    <div class="toolForm">\n        <div class="toolFormTitle">New external service</div>\n')
        # SOURCE LINE 12
        if widgets:
            # SOURCE LINE 13
            for i, field in enumerate( widgets ):
                # SOURCE LINE 14
                __M_writer(u'                <div class="form-row">\n                    <label>')
                # SOURCE LINE 15
                __M_writer(unicode(field['label']))
                __M_writer(u':</label>\n                    ')
                # SOURCE LINE 16
                __M_writer(unicode(field['widget'].get_html()))
                __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        ')
                # SOURCE LINE 18
                __M_writer(unicode(field['helptext']))
                __M_writer(u'\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            pass
        # SOURCE LINE 24
        __M_writer(u'    </div>\n    <div class="form-row">\n        <input type="submit" name="create_external_service_button" value="Save"/>\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


