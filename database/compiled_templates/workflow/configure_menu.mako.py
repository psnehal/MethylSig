# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1433451642.4097149
_template_filename='templates/webapps/galaxy/workflow/configure_menu.mako'
_template_uri='workflow/configure_menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['init', 'center_panel', 'title']


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
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="workflow"
        self.message_box_visible=False
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        ids_in_menu = context.get('ids_in_menu', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        util = context.get('util', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        message = context.get('message', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    <div style="overflow: auto; height: 100%;">\n        <div class="page-container" style="padding: 10px;">\n')
        # SOURCE LINE 17
        if message:
            # SOURCE LINE 18

            try:
                messagetype
            except:
                messagetype = "done"
            
            
            # SOURCE LINE 23
            __M_writer(u'\n<p />\n<div class="')
            # SOURCE LINE 25
            __M_writer(unicode(messagetype))
            __M_writer(u'message">\n    ')
            # SOURCE LINE 26
            __M_writer(unicode(message))
            __M_writer(u'\n</div>\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'\n<form action="')
        # SOURCE LINE 30
        __M_writer(unicode(h.url_for(controller='workflow', action='configure_menu')))
        __M_writer(u'" method="POST">\n\n<table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n    <tr class="header">\n        <th>Name</th>\n        <th>Owner</th>\n        <th># of Steps</th>\n')
        # SOURCE LINE 38
        __M_writer(u'        <th>Show in menu</th>\n    </tr>\n        \n')
        # SOURCE LINE 41
        if workflows:
            # SOURCE LINE 42
            __M_writer(u'\n')
            # SOURCE LINE 43
            for i, workflow in enumerate( workflows ):
                # SOURCE LINE 44
                __M_writer(u'            <tr>\n                <td>\n                    ')
                # SOURCE LINE 46
                __M_writer(unicode(util.unicodify( workflow.name )))
                __M_writer(u'\n                </td>\n                <td>You</td>\n                <td>')
                # SOURCE LINE 49
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n                <td>\n                    <input type="checkbox" name="workflow_ids" value="')
                # SOURCE LINE 51
                __M_writer(unicode(workflow.id))
                __M_writer(u'"\n')
                # SOURCE LINE 52
                if workflow.id in ids_in_menu:
                    # SOURCE LINE 53
                    __M_writer(u'                        checked\n')
                    pass
                # SOURCE LINE 55
                __M_writer(u'                    />\n                </td>\n            </tr>    \n')
                pass
            # SOURCE LINE 59
            __M_writer(u'\n')
            pass
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 62
        if shared_by_others:
            # SOURCE LINE 63
            __M_writer(u'\n')
            # SOURCE LINE 64
            for i, association in enumerate( shared_by_others ):
                # SOURCE LINE 65
                __M_writer(u'            ')
                workflow = association.stored_workflow 
                
                __M_writer(u'\n            <tr>\n                <td>\n                    ')
                # SOURCE LINE 68
                __M_writer(unicode(util.unicodify( workflow.name )))
                __M_writer(u'\n                </td>\n                <td>')
                # SOURCE LINE 70
                __M_writer(unicode(workflow.user.email))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 71
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n                <td>\n                    <input type="checkbox" name="workflow_ids" value="')
                # SOURCE LINE 73
                __M_writer(unicode(workflow.id))
                __M_writer(u'"\n')
                # SOURCE LINE 74
                if workflow.id in ids_in_menu:
                    # SOURCE LINE 75
                    __M_writer(u'                        checked\n')
                    pass
                # SOURCE LINE 77
                __M_writer(u'                    />\n                </td>\n            </tr>    \n')
                pass
            # SOURCE LINE 81
            __M_writer(u'\n')
            pass
        # SOURCE LINE 83
        __M_writer(u'\n')
        # SOURCE LINE 84
        if not workflows and not shared_by_others:
            # SOURCE LINE 85
            __M_writer(u'        <tr>\n            <td colspan="4">You do not have any accessible workflows.</td>\n        </tr>\n')
            pass
        # SOURCE LINE 89
        __M_writer(u'\n</table>\n\n<p />\n<input type="Submit" value="Save" />\n\n</form>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'Configure workflow menu')
        return ''
    finally:
        context.caller_stack._pop_frame()


