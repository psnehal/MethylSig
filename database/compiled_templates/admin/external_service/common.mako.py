# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1434727147.2879879
_template_filename=u'templates/admin/external_service/common.mako'
_template_uri=u'/admin/external_service/common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_external_service']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_external_service(context,external_service):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <div class="toolForm">\n        <div class="toolFormTitle">External service</div>\n        <div class="form-row">\n            <label>Name:</label>\n            ')
        # SOURCE LINE 6
        __M_writer(unicode(external_service.name))
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'            <div style="clear: both"></div>\n        </div>\n        <div class="form-row">\n            <label>Description:</label>\n            ')
        # SOURCE LINE 12
        __M_writer(unicode(external_service.description))
        __M_writer(u'\n            <div style="clear: both"></div>\n        </div>\n        <div class="form-row">\n            <label>Version:</label>\n            ')
        # SOURCE LINE 17
        __M_writer(unicode(external_service.version))
        __M_writer(u'\n            <div style="clear: both"></div>\n        </div>\n        <div class="form-row">\n            <label>External service type:</label>\n')
        # SOURCE LINE 22
        if trans.app.external_service_types.all_external_service_types.has_key( external_service.external_service_type_id ):
            # SOURCE LINE 23
            __M_writer(u'                ')
            __M_writer(unicode(trans.app.external_service_types.all_external_service_types[ external_service.external_service_type_id ].name))
            __M_writer(u'\n')
            # SOURCE LINE 24
        else:
            # SOURCE LINE 25
            __M_writer(u'                ')
            __M_writer(unicode('Error loading external_service type: %s' % external_service.external_service_type_id))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 27
        __M_writer(u'            <div style="clear: both"></div>\n        </div>\n')
        # SOURCE LINE 29
        if external_service.external_service_type_id != 'none':
            # SOURCE LINE 30
            for field_index, field in enumerate( external_service.form_definition.fields ):
                # SOURCE LINE 31
                __M_writer(u'                ')
 
                field_value = external_service.form_values.content.get( field['name'], '' )
                if field[ 'type' ] == 'PasswordField':
                    field_value = '*' * len( field_value )
                                
                
                # SOURCE LINE 35
                __M_writer(u'\n                <div class="form-row">\n                    <label>')
                # SOURCE LINE 37
                __M_writer(unicode(field[ 'label' ]))
                __M_writer(u':</label>\n                    ')
                # SOURCE LINE 38
                __M_writer(unicode(field_value))
                __M_writer(u'\n                </div>\n')
                pass
            # SOURCE LINE 41
        else:
            # SOURCE LINE 42
            __M_writer(u'            <div class="form-row">\n                External service information is not set, click the <b>Edit external service</b> button to set it.\n            </div>\n')
            pass
        # SOURCE LINE 46
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


