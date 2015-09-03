# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1433361600.3771391
_template_filename=u'templates/webapps/tool_shed/repository/common.mako'
_template_uri=u'/webapps/tool_shed/repository/common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_tool_dependency_successful_installation', 'render_tool_dependency', 'render_not_tested', 'render_missing_test_component', 'render_folder', 'render_tool', 'render_clone_str', 'render_test_environment', 'container_javascripts', 'render_readme', 'render_tool_dependency_installation_error', 'render_repository_dependency', 'render_repository_successful_installation', 'render_datatype', 'render_failed_test', 'common_javascripts', 'render_valid_data_manager', 'render_repository_installation_error', 'render_invalid_repository_dependency', 'render_invalid_tool', 'render_workflow', 'render_repository_type_select_field', 'render_passed_test', 'render_repository_items', 'render_invalid_data_manager', 'render_sharable_str', 'render_table_wrap_style', 'render_invalid_tool_dependency']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 76
        __M_writer(u'\n\n')
        # SOURCE LINE 163
        __M_writer(u'\n\n')
        # SOURCE LINE 206
        __M_writer(u'         \n            \n')
        # SOURCE LINE 214
        __M_writer(u'\n\n')
        # SOURCE LINE 222
        __M_writer(u'\n\n')
        # SOURCE LINE 421
        __M_writer(u'\n\n')
        # SOURCE LINE 445
        __M_writer(u'\n\n')
        # SOURCE LINE 471
        __M_writer(u'\n\n')
        # SOURCE LINE 493
        __M_writer(u'\n\n')
        # SOURCE LINE 512
        __M_writer(u'\n\n')
        # SOURCE LINE 535
        __M_writer(u'\n\n')
        # SOURCE LINE 566
        __M_writer(u'\n\n')
        # SOURCE LINE 590
        __M_writer(u'\n\n')
        # SOURCE LINE 609
        __M_writer(u'\n\n')
        # SOURCE LINE 681
        __M_writer(u'\n\n')
        # SOURCE LINE 696
        __M_writer(u'\n\n')
        # SOURCE LINE 727
        __M_writer(u'\n\n')
        # SOURCE LINE 757
        __M_writer(u'\n\n')
        # SOURCE LINE 791
        __M_writer(u'\n\n')
        # SOURCE LINE 822
        __M_writer(u'\n\n')
        # SOURCE LINE 843
        __M_writer(u'\n\n')
        # SOURCE LINE 866
        __M_writer(u'\n\n')
        # SOURCE LINE 915
        __M_writer(u'\n\n')
        # SOURCE LINE 971
        __M_writer(u'\n\n')
        # SOURCE LINE 998
        __M_writer(u'\n\n')
        # SOURCE LINE 1021
        __M_writer(u'\n\n')
        # SOURCE LINE 1063
        __M_writer(u'\n\n')
        # SOURCE LINE 1233
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 729
        __M_writer(u'\n    ')
        # SOURCE LINE 730

        encoded_id = trans.security.encode_id( successful_installation.id )
            
        
        # SOURCE LINE 732
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 734
        if parent is not None:
            # SOURCE LINE 735
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 737
        __M_writer(u'        id="libraryItem-rtdsi-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 738
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        # SOURCE LINE 744
        __M_writer(filters.html_escape(unicode(successful_installation.name )))
        __M_writer(u'</td>\n                    <td>')
        # SOURCE LINE 745
        __M_writer(filters.html_escape(unicode(successful_installation.type )))
        __M_writer(u'</td>\n                    <td>')
        # SOURCE LINE 746
        __M_writer(filters.html_escape(unicode(successful_installation.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Installation directory</th></tr>\n                <tr><td colspan="3">')
        # SOURCE LINE 749
        __M_writer(filters.html_escape(unicode(successful_installation.installation_directory )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 753

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 756
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 917
        __M_writer(u'\n    ')
        # SOURCE LINE 918

        from galaxy.util import string_as_bool
        encoded_id = trans.security.encode_id( tool_dependency.id )
        is_missing = tool_dependency.installation_status not in [ 'Installed' ]
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 926
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 928
        if parent is not None:
            # SOURCE LINE 929
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 931
        __M_writer(u'        id="libraryItem-rtd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 932
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        # SOURCE LINE 933
        if row_is_header:
            # SOURCE LINE 934
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
            # SOURCE LINE 935
        elif trans.webapp.name == 'galaxy' and tool_dependency.tool_dependency_id:
            # SOURCE LINE 936
            if tool_dependency.repository_id and tool_dependency.installation_status in [ trans.install_model.ToolDependency.installation_status.INSTALLED ]:
                # SOURCE LINE 937
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_dependency', id=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                # SOURCE LINE 938
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n                    </a>\n')
                # SOURCE LINE 940
            elif tool_dependency.installation_status not in [ trans.install_model.ToolDependency.installation_status.UNINSTALLED ]:
                # SOURCE LINE 941
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository_tool_dependencies', tool_dependency_ids=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                # SOURCE LINE 942
                __M_writer(unicode(tool_dependency.name))
                __M_writer(u'\n                    </a>\n')
                # SOURCE LINE 944
            else:
                # SOURCE LINE 945
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 947
        else:
            # SOURCE LINE 948
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 950
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 951
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n            ')
        # SOURCE LINE 952

        if tool_dependency.version:
            version_str = tool_dependency.version
        else:
            version_str = ''
                    
        
        # SOURCE LINE 957
        __M_writer(u'\n            ')
        # SOURCE LINE 958
        __M_writer(filters.html_escape(unicode(version_str )))
        __M_writer(u'\n        </')
        # SOURCE LINE 959
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 960
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool_dependency.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 961
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        # SOURCE LINE 962
        if trans.webapp.name == 'galaxy':
            # SOURCE LINE 963
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.installation_status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 965
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 967

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 970
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_not_tested(context,not_tested,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 824
        __M_writer(u'\n    ')
        # SOURCE LINE 825

        encoded_id = trans.security.encode_id( not_tested.id )
            
        
        # SOURCE LINE 827
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 829
        if parent is not None:
            # SOURCE LINE 830
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 832
        __M_writer(u'        id="libraryItem-rnt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 833
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td>')
        # SOURCE LINE 835
        __M_writer(filters.html_escape(unicode(not_tested.reason )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 839

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 842
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 568
        __M_writer(u'\n    ')
        # SOURCE LINE 569

        encoded_id = trans.security.encode_id( missing_test_component.id )
            
        
        # SOURCE LINE 571
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 573
        if parent is not None:
            # SOURCE LINE 574
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 576
        __M_writer(u'        id="libraryItem-rmtc-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 577
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        # SOURCE LINE 579
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        # SOURCE LINE 580
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool guid:</b> ')
        # SOURCE LINE 581
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_guid )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Missing components:</b> <br/>')
        # SOURCE LINE 582
        __M_writer(filters.html_escape(unicode(missing_test_component.missing_components )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 586

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 589
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_folder(context,folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        def render_tool_dependency_successful_installation(successful_installation,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_tool_dependency_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        enumerate = context.get('enumerate', UNDEFINED)
        def render_tool_dependency(tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_not_tested(not_tested,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_not_tested(context,not_tested,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_missing_test_component(missing_test_component,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        def render_tool(tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_test_environment(test_environment,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_test_environment(context,test_environment,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_datatype(datatype,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_tool_dependency_installation_error(installation_error,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_tool_dependency_installation_error(context,installation_error,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_repository_dependency(repository_dependency,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_repository_successful_installation(successful_installation,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
            return render_render_repository_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header,is_current_repository,render_repository_actions_for)
        def render_readme(readme,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_readme(context,readme,pad,parent,row_counter,render_repository_actions_for)
        def render_failed_test(failed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_failed_test(context,failed_test,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_valid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_repository_installation_error(installation_error,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
            return render_render_repository_installation_error(context,installation_error,pad,parent,row_counter,row_is_header,is_current_repository,render_repository_actions_for)
        def render_invalid_repository_dependency(invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for)
        def render_invalid_tool(invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid,render_repository_actions_for)
        def render_workflow(workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        h = context.get('h', UNDEFINED)
        def render_passed_test(passed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_passed_test(context,passed_test,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        str = context.get('str', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        def render_invalid_tool_dependency(invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for)
        __M_writer = context.writer()
        # SOURCE LINE 224
        __M_writer(u'\n    ')
        # SOURCE LINE 225

        encoded_id = trans.security.encode_id( folder.id )
        
        if is_root_folder:
            pad = folder_pad
            expander = h.url_for("/static/images/silk/resultset_bottom.png")
            folder_img = h.url_for("/static/images/silk/folder_page.png")
        else:
            pad = folder_pad + 20
            expander = h.url_for("/static/images/silk/resultset_next.png")
            folder_img = h.url_for("/static/images/silk/folder.png")
        my_row = None
            
        
        # SOURCE LINE 237
        __M_writer(u'\n')
        # SOURCE LINE 238
        if not is_root_folder:
            # SOURCE LINE 239
            __M_writer(u'        ')

            if parent is None:
                bg_str = 'bgcolor="#D8D8D8"'
            else:
                bg_str = ''
                    
            
            # SOURCE LINE 244
            __M_writer(u'\n        <tr id="folder-')
            # SOURCE LINE 245
            __M_writer(unicode(encoded_id))
            __M_writer(u'" ')
            __M_writer(unicode(bg_str))
            __M_writer(u' class="folderRow libraryOrFolderRow"\n')
            # SOURCE LINE 246
            if parent is not None:
                # SOURCE LINE 247
                __M_writer(u'                parent="')
                __M_writer(unicode(parent))
                __M_writer(u'"\n                style="display: none;"\n')
                pass
            # SOURCE LINE 250
            __M_writer(u'            >\n            ')
            # SOURCE LINE 251

            col_span_str = ''
            folder_label = str( folder.label )
            if folder.datatypes:
                col_span_str = 'colspan="4"'
            elif folder.label == 'Missing tool dependencies':
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these missing dependencies</i>" % folder_label
                col_span_str = 'colspan="5"'
            elif folder.label in [ 'Installed repository dependencies', 'Repository dependencies', 'Missing repository dependencies' ]:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                elif folder.label not in [ 'Installed repository dependencies' ] and folder.parent.label not in [ 'Installation errors' ]:
                    folder_label = "%s<i> - installation of these additional repositories is required</i>" % folder_label
                if trans.webapp.name == 'galaxy':
                    col_span_str = 'colspan="4"'
            elif folder.label == 'Invalid repository dependencies':
                folder_label = "%s<i> - click the repository dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Invalid tool dependencies':
                folder_label = "%s<i> - click the tool dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Valid tools':
                col_span_str = 'colspan="3"'
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to preview the tool and use the pop-up menu to inspect all metadata</i>" % folder_label
            elif folder.invalid_tools:
                if trans.webapp.name == 'tool_shed':
                    folder_label = "%s<i> - click the tool config file name to see why the tool is invalid</i>" % folder_label
            elif folder.tool_dependencies:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these dependencies</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.workflows:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to view an SVG image of the workflow</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.valid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="3"'
            elif folder.invalid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="2"'
                        
            
            # SOURCE LINE 302
            __M_writer(u'\n            <td ')
            # SOURCE LINE 303
            __M_writer(unicode(col_span_str))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(folder_pad))
            __M_writer(u'px;">\n                <span class="expandLink folder-')
            # SOURCE LINE 304
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                    <div style="float: left; margin-left: 2px;" class="expandLink folder-')
            # SOURCE LINE 305
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                        <a class="folder-')
            # SOURCE LINE 306
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click" href="javascript:void(0);">\n                            ')
            # SOURCE LINE 307
            __M_writer(unicode(folder_label))
            __M_writer(u'\n                        </a>\n                    </div>\n                </span>\n            </td>\n        </tr>\n        ')
            # SOURCE LINE 313

            my_row = row_counter.count
            row_counter.increment()  
                    
            
            # SOURCE LINE 316
            __M_writer(u'\n')
            pass
        # SOURCE LINE 318
        for sub_folder in folder.folders:
            # SOURCE LINE 319
            __M_writer(u'        ')
            __M_writer(unicode(render_folder( sub_folder, pad, parent=my_row, row_counter=row_counter, is_root_folder=False, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 321
        for readme in folder.readme_files:
            # SOURCE LINE 322
            __M_writer(u'        ')
            __M_writer(unicode(render_readme( readme, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 324
        for invalid_repository_dependency in folder.invalid_repository_dependencies:
            # SOURCE LINE 325
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_repository_dependency( invalid_repository_dependency, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 327
        for index, repository_dependency in enumerate( folder.repository_dependencies ):
            # SOURCE LINE 328
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            # SOURCE LINE 329
            __M_writer(unicode(render_repository_dependency( repository_dependency, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 331
        for invalid_tool_dependency in folder.invalid_tool_dependencies:
            # SOURCE LINE 332
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool_dependency( invalid_tool_dependency, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 334
        for index, tool_dependency in enumerate( folder.tool_dependencies ):
            # SOURCE LINE 335
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            # SOURCE LINE 336
            __M_writer(unicode(render_tool_dependency( tool_dependency, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 338
        if folder.valid_tools:
            # SOURCE LINE 339
            for index, tool in enumerate( folder.valid_tools ):
                # SOURCE LINE 340
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 341
                __M_writer(unicode(render_tool( tool, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 344
        for invalid_tool in folder.invalid_tools:
            # SOURCE LINE 345
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool( invalid_tool, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 347
        if folder.workflows:
            # SOURCE LINE 348
            for index, workflow in enumerate( folder.workflows ):
                # SOURCE LINE 349
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 350
                __M_writer(unicode(render_workflow( workflow, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 353
        if folder.datatypes:
            # SOURCE LINE 354
            for index, datatype in enumerate( folder.datatypes ):
                # SOURCE LINE 355
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 356
                __M_writer(unicode(render_datatype( datatype, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 359
        if folder.valid_data_managers:
            # SOURCE LINE 360
            for index, data_manager in enumerate( folder.valid_data_managers ):
                # SOURCE LINE 361
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 362
                __M_writer(unicode(render_valid_data_manager( data_manager, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 365
        if folder.invalid_data_managers:
            # SOURCE LINE 366
            for index, data_manager in enumerate( folder.invalid_data_managers ):
                # SOURCE LINE 367
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                # SOURCE LINE 368
                __M_writer(unicode(render_invalid_data_manager( data_manager, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 371
        if folder.test_environments:
            # SOURCE LINE 372
            for test_environment in folder.test_environments:
                # SOURCE LINE 373
                __M_writer(u'            ')
                __M_writer(unicode(render_test_environment( test_environment, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 376
        if folder.failed_tests:
            # SOURCE LINE 377
            for failed_test in folder.failed_tests:
                # SOURCE LINE 378
                __M_writer(u'            ')
                __M_writer(unicode(render_failed_test( failed_test, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 381
        if folder.not_tested:
            # SOURCE LINE 382
            for not_tested in folder.not_tested:
                # SOURCE LINE 383
                __M_writer(u'            ')
                __M_writer(unicode(render_not_tested( not_tested, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 386
        if folder.passed_tests:
            # SOURCE LINE 387
            for passed_test in folder.passed_tests:
                # SOURCE LINE 388
                __M_writer(u'            ')
                __M_writer(unicode(render_passed_test( passed_test, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 391
        if folder.missing_test_components:
            # SOURCE LINE 392
            for missing_test_component in folder.missing_test_components:
                # SOURCE LINE 393
                __M_writer(u'            ')
                __M_writer(unicode(render_missing_test_component( missing_test_component, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 396
        if folder.tool_dependency_installation_errors:
            # SOURCE LINE 397
            for tool_dependency_installation_error in folder.tool_dependency_installation_errors:
                # SOURCE LINE 398
                __M_writer(u'            ')
                __M_writer(unicode(render_tool_dependency_installation_error( tool_dependency_installation_error, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 401
        if folder.tool_dependency_successful_installations:
            # SOURCE LINE 402
            for tool_dependency_successful_installation in folder.tool_dependency_successful_installations:
                # SOURCE LINE 403
                __M_writer(u'            ')
                __M_writer(unicode(render_tool_dependency_successful_installation( tool_dependency_successful_installation, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 406
        if folder.repository_installation_errors:
            # SOURCE LINE 407
            for repository_installation_error in folder.repository_installation_errors:
                # SOURCE LINE 408
                __M_writer(u'            ')
                __M_writer(unicode(render_repository_installation_error( repository_installation_error, pad, my_row, row_counter, is_current_repository=False, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 411
        if folder.current_repository_installation_errors:
            # SOURCE LINE 412
            for repository_installation_error in folder.current_repository_installation_errors:
                # SOURCE LINE 413
                __M_writer(u'            ')
                __M_writer(unicode(render_repository_installation_error( repository_installation_error, pad, my_row, row_counter, is_current_repository=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 416
        if folder.repository_successful_installations:
            # SOURCE LINE 417
            for repository_successful_installation in folder.repository_successful_installations:
                # SOURCE LINE 418
                __M_writer(u'            ')
                __M_writer(unicode(render_repository_successful_installation( repository_successful_installation, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 868
        __M_writer(u'\n    ')
        # SOURCE LINE 869

        encoded_id = trans.security.encode_id( tool.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 875
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 877
        if parent is not None:
            # SOURCE LINE 878
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 880
        __M_writer(u'        id="libraryItem-rt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        # SOURCE LINE 881
        if row_is_header:
            # SOURCE LINE 882
            __M_writer(u'            <th style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">')
            __M_writer(filters.html_escape(unicode(tool.name )))
            __M_writer(u'</th>\n')
            # SOURCE LINE 883
        else:
            # SOURCE LINE 884
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            # SOURCE LINE 885
            if tool.repository_id:
                # SOURCE LINE 886
                if trans.webapp.name == 'tool_shed':
                    # SOURCE LINE 887
                    __M_writer(u'                        <div style="float:left;" class="menubutton split popup" id="tool-')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="view-info" href="')
                    # SOURCE LINE 888
                    __M_writer(unicode(h.url_for( controller='repository', action='display_tool', repository_id=trans.security.encode_id( tool.repository_id ), tool_config=tool.tool_config, changeset_revision=tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'</a>\n                        </div>\n                        <div popupmenu="tool-')
                    # SOURCE LINE 890
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="action-button" href="')
                    # SOURCE LINE 891
                    __M_writer(unicode(h.url_for( controller='repository', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">View tool metadata</a>\n                        </div>\n')
                    # SOURCE LINE 893
                elif trans.webapp.name == 'galaxy':
                    # SOURCE LINE 894
                    if tool.repository_installation_status == trans.install_model.ToolShedRepository.installation_status.INSTALLED:
                        # SOURCE LINE 895
                        __M_writer(u'                            <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id )))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 896
                    else:
                        # SOURCE LINE 897
                        __M_writer(u'                            ')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'\n')
                        pass
                    # SOURCE LINE 899
                else:
                    # SOURCE LINE 900
                    __M_writer(u'                        ')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 902
            else:
                # SOURCE LINE 903
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool.name )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 905
            __M_writer(u'            </td>\n')
            pass
        # SOURCE LINE 907
        __M_writer(u'        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.description )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 908
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        # SOURCE LINE 910
        __M_writer(u'    </tr>\n    ')
        # SOURCE LINE 911

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 914
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_clone_str(context,repository):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 216
        __M_writer(u'\n    ')
        # SOURCE LINE 217

        from tool_shed.util.common_util import generate_clone_url_for_repository_in_tool_shed
        clone_str = generate_clone_url_for_repository_in_tool_shed( trans.user, repository )
            
        
        # SOURCE LINE 220
        __M_writer(u'\n    hg clone <a href="')
        # SOURCE LINE 221
        __M_writer(unicode(clone_str))
        __M_writer(u'">')
        __M_writer(unicode(clone_str))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_test_environment(context,test_environment,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 973
        __M_writer(u'\n    ')
        # SOURCE LINE 974
        encoded_id = trans.security.encode_id( test_environment.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 976
        if parent is not None:
            # SOURCE LINE 977
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 979
        __M_writer(u'        id="libraryItem-rte-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 980
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table class="grid" id="test_environment">\n                <tr><td><b>Time tested:</b> ')
        # SOURCE LINE 982
        __M_writer(filters.html_escape(unicode(test_environment.time_tested )))
        __M_writer(u'</td></tr>\n                <tr><td><b>System:</b> ')
        # SOURCE LINE 983
        __M_writer(filters.html_escape(unicode(test_environment.system )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Architecture:</b> ')
        # SOURCE LINE 984
        __M_writer(filters.html_escape(unicode(test_environment.architecture )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Python version:</b> ')
        # SOURCE LINE 985
        __M_writer(filters.html_escape(unicode(test_environment.python_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy revision:</b> ')
        # SOURCE LINE 986
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy database version:</b> ')
        # SOURCE LINE 987
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed revision:</b> ')
        # SOURCE LINE 988
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed database version:</b> ')
        # SOURCE LINE 989
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed mercurial version:</b> ')
        # SOURCE LINE 990
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_mercurial_version )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 994

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 997
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container_javascripts(context):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 78
        __M_writer(u'\n    <script type="text/javascript">\n        var init_dependencies = function() {\n            var storage_id = "library-expand-state-')
        # SOURCE LINE 81
        __M_writer(unicode(trans.security.encode_id(10000)))
        __M_writer(u'";\n            var restore_folder_state = function() {\n                var state = $.jStorage.get(storage_id);\n                if (state) {\n                    for (var id in state) {\n                        if (state[id] === true) {\n                            var row = $("#" + id),\n                                index = row.parent().children().index(row);\n                            row.addClass("expanded").show();\n                            row.siblings().filter("tr[parent=\'" + index + "\']").show();\n                        }\n                    }\n                }\n            };\n            var save_folder_state = function() {\n                var state = {};\n                $("tr.folderRow").each( function() {\n                    var folder = $(this);\n                    state[folder.attr("id")] = folder.hasClass("expanded");\n                });\n                $.jStorage.set(storage_id, state);\n            };\n            $(".container-table").each(function() {\n                //var container_id = this.id.split( "-" )[0];\n                //alert( container_id );\n                var child_of_parent_cache = {};\n                // Recursively fill in children and descendants of each row\n                var process_row = function(q, parents) {\n                    // Find my index\n                    var parent = q.parent(),\n                        this_level = child_of_parent_cache[parent] || (child_of_parent_cache[parent] = parent.children());\n                    var index = this_level.index(q);\n                    // Find my immediate children\n                    var children = $(par_child_dict[index]);\n                    // Recursively handle them\n                    var descendants = children;\n                    children.each( function() {\n                        child_descendants = process_row( $(this), parents.add(q) );\n                        descendants = descendants.add(child_descendants);\n                    });\n                    // Set up expand / hide link\n                    var expand_fn = function() {\n                        if ( q.hasClass("expanded") ) {\n                            descendants.hide();\n                            descendants.removeClass("expanded");\n                            q.removeClass("expanded");\n                        } else {\n                            children.show();\n                            q.addClass("expanded");\n                        }\n                        save_folder_state();\n                    };\n                    $("." + q.attr("id") + "-click").click(expand_fn);\n                    // return descendants for use by parent\n                    return descendants;\n                }\n                // Initialize dict[parent_id] = rows_which_have_that_parent_id_as_parent_attr\n                var par_child_dict = {},\n                    no_parent = [];\n                $(this).find("tbody tr").each( function() {\n                    if ( $(this).attr("parent")) {\n                        var parent = $(this).attr("parent");\n                        if (par_child_dict[parent] !== undefined) {\n                            par_child_dict[parent].push(this);\n                        } else {\n                            par_child_dict[parent] = [this];\n                        }\n                    } else {\n                        no_parent.push(this);\n                    }                        \n                });\n                $(no_parent).each( function() {\n                    descendants = process_row( $(this), $([]) );\n                    descendants.hide();\n               });\n            });\n            restore_folder_state();\n        };\n        $(function() {\n            init_dependencies();\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_readme(context,readme,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 592
        __M_writer(u'\n    ')
        # SOURCE LINE 593
        encoded_id = trans.security.encode_id( readme.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 595
        if parent is not None:
            # SOURCE LINE 596
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'" \n')
            pass
        # SOURCE LINE 598
        __M_writer(u'        id="libraryItem-rr-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 599
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="readme_files">\n                <tr><td>')
        # SOURCE LINE 601
        __M_writer(unicode( readme.text ))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 605

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 608
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 698
        __M_writer(u'\n    ')
        # SOURCE LINE 699

        from galaxy.util import unicodify
        encoded_id = trans.security.encode_id( installation_error.id )
            
        
        # SOURCE LINE 702
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 704
        if parent is not None:
            # SOURCE LINE 705
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 707
        __M_writer(u'        id="libraryItem-rtdie-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 708
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        # SOURCE LINE 714
        __M_writer(filters.html_escape(unicode(installation_error.name )))
        __M_writer(u'</td>\n                    <td>')
        # SOURCE LINE 715
        __M_writer(filters.html_escape(unicode(installation_error.type )))
        __M_writer(u'</td>\n                    <td>')
        # SOURCE LINE 716
        __M_writer(filters.html_escape(unicode(installation_error.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Error</th></tr>\n                <tr><td colspan="3">')
        # SOURCE LINE 719
        __M_writer(filters.html_escape(unicode(unicodify( installation_error.error_message ) )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 723

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 726
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 611
        __M_writer(u'\n    ')
        # SOURCE LINE 612

        from galaxy.util import asbool
        from tool_shed.util.shed_util_common import get_repository_by_name_and_owner
        encoded_id = trans.security.encode_id( repository_dependency.id )
        if trans.webapp.name == 'galaxy':
            if repository_dependency.tool_shed_repository_id:
                encoded_required_repository_id = trans.security.encode_id( repository_dependency.tool_shed_repository_id )
            else:
                encoded_required_repository_id = None
            if repository_dependency.installation_status:
                installation_status = str( repository_dependency.installation_status )
            else:
                installation_status = None
        repository_name = str( repository_dependency.repository_name )
        repository_owner = str( repository_dependency.repository_owner )
        changeset_revision = str( repository_dependency.changeset_revision )
        if asbool( str( repository_dependency.prior_installation_required ) ):
            prior_installation_required_str = " <i>(prior install required)</i>"
        else:
            prior_installation_required_str = ""
        if trans.webapp.name == 'galaxy':
            if row_is_header:
                cell_type = 'th'
            else:
                cell_type = 'td'
            rd = None
        else:
            # We're in the tool shed.
            cell_type = 'td'
            rd = get_repository_by_name_and_owner( trans.app, repository_name, repository_owner )
            
        
        # SOURCE LINE 642
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 644
        if parent is not None:
            # SOURCE LINE 645
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 647
        __M_writer(u'        id="libraryItem-rrd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        # SOURCE LINE 648
        if trans.webapp.name == 'galaxy':
            # SOURCE LINE 649
            __M_writer(u'            <')
            __M_writer(unicode(cell_type))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            # SOURCE LINE 650
            if row_is_header:
                # SOURCE LINE 651
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'\n')
                # SOURCE LINE 652
            elif encoded_required_repository_id:
                # SOURCE LINE 653
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=encoded_required_repository_id )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</a>\n')
                # SOURCE LINE 654
            else:
                # SOURCE LINE 655
                __M_writer(u'                   ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u' \n')
                pass
            # SOURCE LINE 657
            __M_writer(u'            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            # SOURCE LINE 658
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            # SOURCE LINE 659
            __M_writer(filters.html_escape(unicode(changeset_revision )))
            __M_writer(u'\n            </')
            # SOURCE LINE 660
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            # SOURCE LINE 661
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            # SOURCE LINE 662
            __M_writer(filters.html_escape(unicode(repository_owner )))
            __M_writer(u'\n            </')
            # SOURCE LINE 663
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            # SOURCE LINE 664
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            # SOURCE LINE 665
            __M_writer(unicode(installation_status))
            __M_writer(u'\n            </')
            # SOURCE LINE 666
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n')
            # SOURCE LINE 667
        else:
            # SOURCE LINE 668
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            # SOURCE LINE 669
            if render_repository_actions_for == 'tool_shed' and rd:
                # SOURCE LINE 670
                __M_writer(u'                    <a class="view-info" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='view_or_manage_repository', id=trans.security.encode_id( rd.id ), changeset_revision=changeset_revision )))
                __M_writer(u'">Repository <b>')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</b> revision <b>')
                __M_writer(filters.html_escape(unicode(changeset_revision )))
                __M_writer(u'</b> owned by <b>')
                __M_writer(filters.html_escape(unicode(repository_owner )))
                __M_writer(u'</b></a>')
                __M_writer(unicode(prior_installation_required_str))
                __M_writer(u'\n')
                # SOURCE LINE 671
            else:
                # SOURCE LINE 672
                __M_writer(u'                    Repository <b>')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</b> revision <b>')
                __M_writer(filters.html_escape(unicode(changeset_revision )))
                __M_writer(u'</b> owned by <b>')
                __M_writer(filters.html_escape(unicode(repository_owner )))
                __M_writer(u'</b>')
                __M_writer(unicode(prior_installation_required_str))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 674
            __M_writer(u'            </td>\n')
            pass
        # SOURCE LINE 676
        __M_writer(u'    </tr>\n    ')
        # SOURCE LINE 677

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 680
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 793
        __M_writer(u'\n    ')
        # SOURCE LINE 794

        encoded_id = trans.security.encode_id( successful_installation.id )
            
        
        # SOURCE LINE 796
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 798
        if parent is not None:
            # SOURCE LINE 799
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 801
        __M_writer(u'        id="libraryItem-rrsi-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 802
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n')
        # SOURCE LINE 804
        if not is_current_repository:
            # SOURCE LINE 805
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            # SOURCE LINE 809
            __M_writer(filters.html_escape(unicode(successful_installation.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 810
            __M_writer(filters.html_escape(unicode(successful_installation.name )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 811
            __M_writer(filters.html_escape(unicode(successful_installation.owner )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 812
            __M_writer(filters.html_escape(unicode(successful_installation.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
            pass
        # SOURCE LINE 815
        __M_writer(u'            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 818

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 821
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 423
        __M_writer(u'\n    ')
        # SOURCE LINE 424

        encoded_id = trans.security.encode_id( datatype.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 430
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 432
        if parent is not None:
            # SOURCE LINE 433
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 435
        __M_writer(u'        id="libraryItem-rd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 436
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(datatype.extension )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 437
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 438
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.mimetype )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 439
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.subclass )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 441

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 444
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_failed_test(context,failed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 447
        __M_writer(u'\n    ')
        # SOURCE LINE 448
 
        from tool_shed.util.basic_util import to_html_string
        encoded_id = trans.security.encode_id( failed_test.id )
            
        
        # SOURCE LINE 451
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 453
        if parent is not None:
            # SOURCE LINE 454
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 456
        __M_writer(u'        id="libraryItem-rft-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 457
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        # SOURCE LINE 459
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        # SOURCE LINE 460
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        # SOURCE LINE 461
        __M_writer(filters.html_escape(unicode(failed_test.test_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Stderr:</b> <br/>')
        # SOURCE LINE 462
        __M_writer(unicode( to_html_string( failed_test.stderr ) ))
        __M_writer(u'</td></tr>\n                <tr><td><b>Traceback:</b> <br/>')
        # SOURCE LINE 463
        __M_writer(unicode( to_html_string( failed_test.traceback ) ))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 467

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 470
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_common_javascripts(context,repository):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("#tree").ajaxComplete(function(event, XMLHttpRequest, ajaxOptions) {\n                _log("debug", "ajaxComplete: %o", this); // dom element listening\n            });\n            // --- Initialize sample trees\n            $("#tree").dynatree({\n                title: "')
        # SOURCE LINE 9
        __M_writer(unicode(repository.name))
        __M_writer(u'",\n                rootVisible: true,\n                minExpandLevel: 0, // 1: root node is not collapsible\n                persist: false,\n                checkbox: true,\n                selectMode: 3,\n                onPostInit: function(isReloading, isError) {\n                    //alert("reloading: "+isReloading+", error:"+isError);\n                    logMsg("onPostInit(%o, %o) - %o", isReloading, isError, this);\n                    // Re-fire onActivate, so the text is updated\n                    this.reactivate();\n                }, \n                fx: { height: "toggle", duration: 200 },\n                // initAjax is hard to fake, so we pass the children as object array:\n                initAjax: {url: "')
        # SOURCE LINE 23
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'",\n                           dataType: "json", \n                           data: { folder_path: "')
        # SOURCE LINE 25
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'" },\n                },\n                onLazyRead: function(dtnode){\n                    dtnode.appendAjax({\n                        url: "')
        # SOURCE LINE 29
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'", \n                        dataType: "json",\n                        data: { folder_path: dtnode.data.key },\n                    });\n                },\n                onSelect: function(select, dtnode) {\n                    // Display list of selected nodes\n                    var selNodes = dtnode.tree.getSelectedNodes();\n                    // convert to title/key array\n                    var selKeys = $.map(selNodes, function(node) {\n                        return node.data.key;\n                    });\n                    if (document.forms["select_files_to_delete"]) {\n                        // The following is used only ~/templates/webapps/tool_shed/repository/browse_repository.mako.\n                        document.select_files_to_delete.selected_files_to_delete.value = selKeys.join(",");\n                    }\n                    // The following is used only in ~/templates/webapps/tool_shed/repository/upload.mako.\n                    if (document.forms["upload_form"]) {\n                        document.upload_form.upload_point.value = selKeys.slice(-1);\n                    }\n                },\n                onActivate: function(dtnode) {\n                    var cell = $("#file_contents");\n                    var selected_value;\n                     if (dtnode.data.key == \'root\') {\n                        selected_value = "')
        # SOURCE LINE 54
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'/";\n                    } else {\n                        selected_value = dtnode.data.key;\n                    };\n                    if (selected_value.charAt(selected_value.length-1) != \'/\') {\n                        // Make ajax call\n                        $.ajax( {\n                            type: "POST",\n                            url: "')
        # SOURCE LINE 62
        __M_writer(unicode(h.url_for( controller='repository', action='get_file_contents' )))
        __M_writer(u'",\n                            dataType: "json",\n                            data: { file_path: selected_value },\n                            success : function ( data ) {\n                                cell.html( \'<label>\'+data+\'</label>\' )\n                            }\n                        });\n                    } else {\n                        cell.html( \'\' );\n                    };\n                },\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1000
        __M_writer(u'\n    ')
        # SOURCE LINE 1001

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 1007
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 1009
        if parent is not None:
            # SOURCE LINE 1010
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 1012
        __M_writer(u'        id="libraryItem-rvdm-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 1013
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.name )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1014
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1015
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.data_tables )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 1017

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 1020
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 759
        __M_writer(u'\n    ')
        # SOURCE LINE 760

        from galaxy.util import unicodify
        encoded_id = trans.security.encode_id( installation_error.id )
            
        
        # SOURCE LINE 763
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 765
        if parent is not None:
            # SOURCE LINE 766
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 768
        __M_writer(u'        id="libraryItem-rrie-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 769
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n')
        # SOURCE LINE 771
        if not is_current_repository:
            # SOURCE LINE 772
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            # SOURCE LINE 776
            __M_writer(filters.html_escape(unicode(installation_error.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 777
            __M_writer(filters.html_escape(unicode(installation_error.name )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 778
            __M_writer(filters.html_escape(unicode(installation_error.owner )))
            __M_writer(u'</td>\n                        <td>')
            # SOURCE LINE 779
            __M_writer(filters.html_escape(unicode(installation_error.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
            pass
        # SOURCE LINE 782
        __M_writer(u'                <tr><th>Error</th></tr>\n                <tr><td colspan="4">')
        # SOURCE LINE 783
        __M_writer(filters.html_escape(unicode(unicodify( installation_error.error_message ) )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 787

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 790
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 495
        __M_writer(u'\n    ')
        # SOURCE LINE 496

        encoded_id = trans.security.encode_id( invalid_repository_dependency.id )
            
        
        # SOURCE LINE 498
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 500
        if parent is not None:
            # SOURCE LINE 501
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 503
        __M_writer(u'        id="libraryItem-rird-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 504
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            ')
        # SOURCE LINE 505
        __M_writer(filters.html_escape(unicode( invalid_repository_dependency.error )))
        __M_writer(u'\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 508

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 511
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 514
        __M_writer(u'\n    ')
        # SOURCE LINE 515
        encoded_id = trans.security.encode_id( invalid_tool.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 517
        if parent is not None:
            # SOURCE LINE 518
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 520
        __M_writer(u'        id="libraryItem-rit-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 521
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        # SOURCE LINE 522
        if trans.webapp.name == 'tool_shed' and invalid_tool.repository_id and invalid_tool.tool_config and invalid_tool.changeset_revision:
            # SOURCE LINE 523
            __M_writer(u'                <a class="view-info" href="')
            __M_writer(unicode(h.url_for( controller='repository', action='load_invalid_tool', repository_id=trans.security.encode_id( invalid_tool.repository_id ), tool_config=invalid_tool.tool_config, changeset_revision=invalid_tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">\n                    ')
            # SOURCE LINE 524
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n                </a>\n')
            # SOURCE LINE 526
        else:
            # SOURCE LINE 527
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 529
        __M_writer(u'        </td>\n    </tr>\n    ')
        # SOURCE LINE 531

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 534
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1023
        __M_writer(u'\n    ')
        # SOURCE LINE 1024

        from tool_shed.util.encoding_util import tool_shed_encode
        encoded_id = trans.security.encode_id( workflow.id )
        encoded_workflow_name = tool_shed_encode( workflow.workflow_name )
        if trans.webapp.name == 'tool_shed':
            encoded_repository_metadata_id = trans.security.encode_id( workflow.repository_metadata_id )
            encoded_repository_id = None
        else:
            encoded_repository_metadata_id = None
            encoded_repository_id = trans.security.encode_id( workflow.repository_id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 1038
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 1040
        if parent is not None:
            # SOURCE LINE 1041
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 1043
        __M_writer(u'        id="libraryItem-rw-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 1044
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        # SOURCE LINE 1045
        if row_is_header:
            # SOURCE LINE 1046
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
            # SOURCE LINE 1047
        elif trans.webapp.name == 'tool_shed' and encoded_repository_metadata_id:
            # SOURCE LINE 1048
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_workflow', workflow_name=encoded_workflow_name, repository_metadata_id=encoded_repository_metadata_id, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
            # SOURCE LINE 1049
        elif trans.webapp.name == 'galaxy' and encoded_repository_id:
            # SOURCE LINE 1050
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_workflow', workflow_name=encoded_workflow_name, repository_id=encoded_repository_id )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
            # SOURCE LINE 1051
        else:
            # SOURCE LINE 1052
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 1054
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1055
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.steps )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1056
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.format_version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 1057
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.annotation )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 1059

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 1062
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_type_select_field(context,repository_type_select_field,render_help=True):
    context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 165
        __M_writer(u'\n    <div class="form-row">\n        <label>Repository type:</label>\n        ')
        # SOURCE LINE 168

        from tool_shed.repository_types import util
        options = repository_type_select_field.options
        repository_types = []
        for option_tup in options:
            repository_types.append( option_tup[ 1 ] )
        render_as_text = len( options ) == 1
        if render_as_text:
            repository_type = options[ 0 ][ 0 ]
                
        
        # SOURCE LINE 177
        __M_writer(u'\n')
        # SOURCE LINE 178
        if render_as_text:
            # SOURCE LINE 179
            __M_writer(u'            ')
            __M_writer(filters.html_escape(unicode(repository_type )))
            __M_writer(u'\n')
            # SOURCE LINE 180
            if render_help:
                # SOURCE LINE 181
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    This repository\'s type cannot be changed because its contents are valid only for its current type or it has been cloned.\n                </div>\n')
                pass
            # SOURCE LINE 185
        else:
            # SOURCE LINE 186
            __M_writer(u'            ')
            __M_writer(unicode(repository_type_select_field.get_html()))
            __M_writer(u'\n')
            # SOURCE LINE 187
            if render_help:
                # SOURCE LINE 188
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    Select the repository type based on the following criteria.\n                    <ul>\n')
                # SOURCE LINE 191
                if util.UNRESTRICTED in repository_types:
                    # SOURCE LINE 192
                    __M_writer(u'                            <li><b>Unrestricted</b> - contents can be any set of valid Galaxy utilities or files\n')
                    pass
                # SOURCE LINE 194
                if util.REPOSITORY_SUITE_DEFINITION in repository_types:
                    # SOURCE LINE 195
                    __M_writer(u'                            <li><b>Repository suite definition</b> - contents will always be restricted to one file named repository_dependencies.xml\n')
                    pass
                # SOURCE LINE 197
                if util.TOOL_DEPENDENCY_DEFINITION in repository_types:
                    # SOURCE LINE 198
                    __M_writer(u'                            <li><b>Tool dependency definition</b> - contents will always be restricted to one file named tool_dependencies.xml\n')
                    pass
                # SOURCE LINE 200
                __M_writer(u'                    </ul>\n                </div>\n')
                pass
            pass
        # SOURCE LINE 204
        __M_writer(u'        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_passed_test(context,passed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 845
        __M_writer(u'\n    ')
        # SOURCE LINE 846

        encoded_id = trans.security.encode_id( passed_test.id )
            
        
        # SOURCE LINE 848
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 850
        if parent is not None:
            # SOURCE LINE 851
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 853
        __M_writer(u'        id="libraryItem-rpt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 854
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        # SOURCE LINE 856
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        # SOURCE LINE 857
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        # SOURCE LINE 858
        __M_writer(filters.html_escape(unicode(passed_test.test_id )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 862

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 865
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_items(context,metadata,containers_dict,can_set_metadata=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        def render_table_wrap_style(table_id):
            return render_render_table_wrap_style(context,table_id)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        __M_writer = context.writer()
        # SOURCE LINE 1065
        __M_writer(u'\n    ')
        # SOURCE LINE 1066

        from tool_shed.util.encoding_util import tool_shed_encode
        
        has_datatypes = metadata and 'datatypes' in metadata
        has_readme_files = metadata and 'readme_files' in metadata
        has_workflows = metadata and 'workflows' in metadata
        
        datatypes_root_folder = containers_dict.get( 'datatypes', None )
        invalid_data_managers_root_folder = containers_dict.get( 'invalid_data_managers', None )
        invalid_repository_dependencies_root_folder = containers_dict.get( 'invalid_repository_dependencies', None )
        invalid_tool_dependencies_root_folder = containers_dict.get( 'invalid_tool_dependencies', None )
        invalid_tools_root_folder = containers_dict.get( 'invalid_tools', None )
        missing_repository_dependencies_root_folder = containers_dict.get( 'missing_repository_dependencies', None )
        missing_tool_dependencies_root_folder = containers_dict.get( 'missing_tool_dependencies', None )
        readme_files_root_folder = containers_dict.get( 'readme_files', None )
        repository_dependencies_root_folder = containers_dict.get( 'repository_dependencies', None )
        test_environment_root_folder = containers_dict.get( 'test_environment', None )
        tool_dependencies_root_folder = containers_dict.get( 'tool_dependencies', None )
        tool_test_results_root_folder = containers_dict.get( 'tool_test_results', None )
        valid_data_managers_root_folder = containers_dict.get( 'valid_data_managers', None )
        valid_tools_root_folder = containers_dict.get( 'valid_tools', None )
        workflows_root_folder = containers_dict.get( 'workflows', None )
        
        has_contents = datatypes_root_folder or invalid_tools_root_folder or valid_tools_root_folder or workflows_root_folder
        has_dependencies = \
            invalid_repository_dependencies_root_folder or \
            invalid_tool_dependencies_root_folder or \
            missing_repository_dependencies_root_folder or \
            repository_dependencies_root_folder or \
            tool_dependencies_root_folder or \
            missing_tool_dependencies_root_folder
        
        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
            
        
        # SOURCE LINE 1105
        __M_writer(u'\n')
        # SOURCE LINE 1106
        if readme_files_root_folder:
            # SOURCE LINE 1107
            __M_writer(u'        ')
            __M_writer(unicode(render_table_wrap_style( "readme_files" )))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Repository README files - may contain important installation or license information</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            # SOURCE LINE 1113
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="readme_files">\n                    ')
            # SOURCE LINE 1115
            __M_writer(unicode(render_folder( readme_files_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
            pass
        # SOURCE LINE 1120
        if has_dependencies:
            # SOURCE LINE 1121
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Dependencies of this repository</div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 1124
            if invalid_repository_dependencies_root_folder:
                # SOURCE LINE 1125
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1126
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_repository_dependencies">\n                        ')
                # SOURCE LINE 1128
                __M_writer(unicode(render_folder( invalid_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1131
            if missing_repository_dependencies_root_folder:
                # SOURCE LINE 1132
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1133
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_repository_dependencies">\n                        ')
                # SOURCE LINE 1135
                __M_writer(unicode(render_folder( missing_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1138
            if repository_dependencies_root_folder:
                # SOURCE LINE 1139
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1140
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="repository_dependencies">\n                        ')
                # SOURCE LINE 1142
                __M_writer(unicode(render_folder( repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1145
            if invalid_tool_dependencies_root_folder:
                # SOURCE LINE 1146
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1147
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tool_dependencies">\n                        ')
                # SOURCE LINE 1149
                __M_writer(unicode(render_folder( invalid_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1152
            if tool_dependencies_root_folder:
                # SOURCE LINE 1153
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1154
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="tool_dependencies">\n                        ')
                # SOURCE LINE 1156
                __M_writer(unicode(render_folder( tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1159
            if missing_tool_dependencies_root_folder:
                # SOURCE LINE 1160
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1161
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_tool_dependencies">\n                        ')
                # SOURCE LINE 1163
                __M_writer(unicode(render_folder( missing_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1166
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 1169
        if has_contents:
            # SOURCE LINE 1170
            __M_writer(u'        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Contents of this repository</div>\n            <div class="toolFormBody">\n')
            # SOURCE LINE 1174
            if valid_tools_root_folder:
                # SOURCE LINE 1175
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1176
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_tools">\n                        ')
                # SOURCE LINE 1178
                __M_writer(unicode(render_folder( valid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1181
            if invalid_tools_root_folder:
                # SOURCE LINE 1182
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1183
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tools">\n                        ')
                # SOURCE LINE 1185
                __M_writer(unicode(render_folder( invalid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1188
            if valid_data_managers_root_folder:
                # SOURCE LINE 1189
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1190
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_data_managers">\n                        ')
                # SOURCE LINE 1192
                __M_writer(unicode(render_folder( valid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1195
            if invalid_data_managers_root_folder:
                # SOURCE LINE 1196
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1197
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_data_managers">\n                        ')
                # SOURCE LINE 1199
                __M_writer(unicode(render_folder( invalid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1202
            if workflows_root_folder:
                # SOURCE LINE 1203
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1204
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="workflows">\n                        ')
                # SOURCE LINE 1206
                __M_writer(unicode(render_folder( workflows_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1209
            if datatypes_root_folder:
                # SOURCE LINE 1210
                __M_writer(u'                    <p/>\n                    ')
                # SOURCE LINE 1211
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="datatypes">\n                        ')
                # SOURCE LINE 1213
                __M_writer(unicode(render_folder( datatypes_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
                pass
            # SOURCE LINE 1216
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 1219
        if tool_test_results_root_folder:
            # SOURCE LINE 1220
            __M_writer(u'        ')
            __M_writer(unicode(render_table_wrap_style( "test_environment" )))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Automated tool test results</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            # SOURCE LINE 1226
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="test_environment">\n                    ')
            # SOURCE LINE 1228
            __M_writer(unicode(render_folder( tool_test_results_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 473
        __M_writer(u'\n    ')
        # SOURCE LINE 474

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        # SOURCE LINE 480
        __M_writer(u'\n    <tr class="datasetRow"\n')
        # SOURCE LINE 482
        if parent is not None:
            # SOURCE LINE 483
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 485
        __M_writer(u'        id="libraryItem-ridm-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        # SOURCE LINE 486
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.index )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        # SOURCE LINE 487
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.error )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')
        # SOURCE LINE 489

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 492
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_sharable_str(context,repository,changeset_revision=None):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 208
        __M_writer(u'\n    ')
        # SOURCE LINE 209

        from tool_shed.util.shed_util_common import generate_sharable_link_for_repository_in_tool_shed
        sharable_link = generate_sharable_link_for_repository_in_tool_shed( repository, changeset_revision=changeset_revision )
            
        
        # SOURCE LINE 212
        __M_writer(u'\n    ')
        # SOURCE LINE 213
        __M_writer(unicode(sharable_link))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_table_wrap_style(context,table_id):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 683
        __M_writer(u'\n    <style type="text/css">\n        table.')
        # SOURCE LINE 685
        __M_writer(unicode(table_id))
        __M_writer(u'{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px; \n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n        ul{ list-style-type: disc;\n            padding-left: 20px; }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 537
        __M_writer(u'\n    ')
        # SOURCE LINE 538

        encoded_id = trans.security.encode_id( invalid_tool_dependency.id )
            
        
        # SOURCE LINE 540
        __M_writer(u'\n    <style type="text/css">\n        #invalid_td_table{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px; \n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n    </style>\n    <tr class="datasetRow"\n')
        # SOURCE LINE 552
        if parent is not None:
            # SOURCE LINE 553
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 555
        __M_writer(u'        id="libraryItem-ritd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        # SOURCE LINE 556
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="invalid_td_table">\n                <tr><td>')
        # SOURCE LINE 558
        __M_writer(filters.html_escape(unicode( invalid_tool_dependency.error )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')
        # SOURCE LINE 562

        my_row = row_counter.count
        row_counter.increment()
            
        
        # SOURCE LINE 565
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


