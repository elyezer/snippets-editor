# -*- coding: utf-8 -*-

#######################################################################
# Copyright © 2007-2009 Yuri Malheiros.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# the Free Software Foundation; version 2 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#######################################################################

"""
This module implements the trigger of "ctrl+/".
"""

shortcut = "ctrl+/"
sticky = False

import tf.app

class CommentLine(object):
    
    def activate(self):
        """
        Comment current or selected lines.
        """
        self.document_manager = tf.app.document_manager
        document = self.document_manager.get_active_document()
        view = self.document_manager.get_active_view()
        buffer = view.buffer
        
        if buffer.get_has_selection():
            pref_manager = self.document_manager.preferences_manager
        
            start_iter, end_iter = buffer.get_selection_bounds()
            start_index = start_iter.get_line()
            end_index = end_iter.get_line()
            
            buffer.begin_user_action()
                       
            # Getting the smaller indentation level
            indent_iter = start_iter.copy()
            temp_size = 0
            smaller_size = 0
            tab_width = pref_manager.get_value("indentation/tab_width") 
            
            # First line
            indent = document.get_indentation(indent_iter)
                
            for i in indent:
                if i == " ":
                    smaller_size += 1
                elif i == "\t":
                    smaller_size += tab_width
                    
            indent_iter.forward_line()

            # Other lines                        
            for line_index in range(start_index+1, end_index+1):
                indent = document.get_indentation(indent_iter)
                
                for i in indent:
                    if i == " ":
                        temp_size += 1
                    elif i == "\t":
                        temp_size += tab_width
                        
                if temp_size < smaller_size:
                    smaller_size = temp_size
                    
                indent_iter.forward_line()
                
                temp_size = 0
                
            # Writing comment characters
            for line_index in range(start_index, end_index+1):
                start_iter = buffer.get_iter_at_line(line_index)
                
                start_iter.forward_chars(smaller_size)
                buffer.insert(start_iter, '#')
                start_iter.forward_line()
            
            buffer.end_user_action()
            
        else:
            # Comment single line
            start_iter, end_iter = document.get_line_iters()
            self.__find_smart_start(start_iter)
            
            buffer.begin_user_action()
            buffer.insert(start_iter, '#')
            buffer.end_user_action()
        
        return True

    def __find_smart_start(self, iterator):
        """
        This method puts a iter at the smart start of it line.
        
        @param iterator: A text iter that will be
        put at the smart start of it line.
        @type iterator: A TextIter object.
        """
        
        while True:
            char = iterator.get_char()
            if char == " " or char == "\t":
                iterator.forward_char()
            else:
                return
        return
