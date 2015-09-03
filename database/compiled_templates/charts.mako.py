# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1435172960.7153871
_template_filename='config/plugins/visualizations/charts/templates/charts.mako'
_template_uri='charts.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        config = context.get('config', UNDEFINED)
        visualization_name = context.get('visualization_name', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        visualization_id = context.get('visualization_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        root        = h.url_for( "/" )
        app_root    = root + "plugins/visualizations/charts/static/"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['app_root','root'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 4
        __M_writer(u'\n\n\n<!DOCTYPE HTML>\n<html>\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        <title>')
        # SOURCE LINE 11
        __M_writer(unicode(hda.name))
        __M_writer(u' | ')
        __M_writer(unicode(visualization_name))
        __M_writer(u'</title>\n\n')
        # SOURCE LINE 14
        __M_writer(u'        ')
        __M_writer(unicode(h.js( 'libs/jquery/jquery',
                'libs/bootstrap',
                'libs/require',
                'libs/underscore',
                'libs/backbone/backbone',
                'libs/d3')))
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'        ')
        __M_writer(unicode(h.css( 'base' )))
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'        ')
        __M_writer(unicode(h.javascript_link( app_root + "plugins/crossfilter/crossfilter.js" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'        ')
        __M_writer(unicode(h.javascript_link( app_root + "plugins/canvg/rgbcolor.js" )))
        __M_writer(u'\n        ')
        # SOURCE LINE 29
        __M_writer(unicode(h.javascript_link( app_root + "plugins/canvg/canvg.js" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'        ')
        __M_writer(unicode(h.stylesheet_link( app_root + "plugins/nvd3/nv.d3.css" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'        ')
        __M_writer(unicode(h.stylesheet_link( app_root + "plugins/jqplot/jquery.jqplot.css" )))
        __M_writer(u'\n        ')
        # SOURCE LINE 36
        __M_writer(unicode(h.javascript_link( app_root + "plugins/jqplot/jquery.jqplot.js" )))
        __M_writer(u'\n        ')
        # SOURCE LINE 37
        __M_writer(unicode(h.javascript_link( app_root + "plugins/jqplot/jquery.jqplot.plugins.js" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'        ')
        __M_writer(unicode(h.javascript_link( app_root + "build-app.js" )))
        __M_writer(u'\n        \n')
        # SOURCE LINE 43
        __M_writer(u'        ')
        __M_writer(unicode(h.stylesheet_link( app_root + "app.css" )))
        __M_writer(u'\n    </head>\n\n    <body>\n        <script type="text/javascript">\n            // get configuration\n            var config = {\n                root     : \'')
        # SOURCE LINE 50
        __M_writer(unicode(root))
        __M_writer(u"',\n                app_root : '")
        # SOURCE LINE 51
        __M_writer(unicode(app_root))
        __M_writer(u'\'\n            };\n            \n            // link galaxy\n            var Galaxy = Galaxy || parent.Galaxy;\n\n            // console protection\n            window.console = window.console || {\n                log     : function(){},\n                debug   : function(){},\n                info    : function(){},\n                warn    : function(){},\n                error   : function(){},\n                assert  : function(){}\n            };\n\n            // configure require\n            require.config({\n                baseUrl: config.root + "static/scripts/",\n                paths: {\n                    "plugin"        : "')
        # SOURCE LINE 71
        __M_writer(unicode(app_root))
        __M_writer(u'",\n                    "d3"            : "libs/d3"\n                },\n                shim: {\n                    "libs/underscore": { exports: "_" },\n                    "libs/backbone/backbone": { exports: "Backbone" },\n                    "d3": { exports: "d3"}\n\n                }\n            });\n\n            // application\n            var app = null;\n            $(function() {   \n                // request application script\n                require([\'plugin/app\'], function(App) {\n                    // load options\n                    var options = {\n                        id      : ')
        # SOURCE LINE 89
        __M_writer(unicode(h.dumps( visualization_id )))
        __M_writer(u' || undefined,\n                        config  : ')
        # SOURCE LINE 90
        __M_writer(unicode(h.dumps( config )))
        __M_writer(u"\n                    }\n                    \n                    // create application\n                    app = new App(options);\n                    \n                    // add to body\n                    $('body').append(app.$el);\n                });\n            });\n\n        </script>\n    </body>\n</html>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


