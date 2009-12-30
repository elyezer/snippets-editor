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
This module implements the trigger of "Return".
"""

shortcut = unichr(65293) #Return
sticky = False

import re
import tf.app

class AutoIndent(object):
    
    def activate(self):
        """
        Auto indent.
        """
        
        self.document_manager = tf.app.document_manager
        document = self.document_manager.get_active_document()
        view = document.view
        buffer = document.buffer
        
        if view.get_auto_indent() and not buffer.get_has_selection():
            
            insert_mark = buffer.get_insert()
            insert_iter = buffer.get_iter_at_mark(insert_mark)
            
            begin, end = document.get_line_iters()
            text = buffer.get_text(begin, end)
            
            if self.__verify_auto_indent(text) and insert_iter.ends_line():
                # Indentation stuff
                pref_manager = tf.app.preferences_manager
                spaces = pref_manager.get_value("indentation/use_spaces")
                tab_width = view.get_tab_width()
                
                indent = document.get_indentation(insert_iter)
                
                buffer.insert_at_cursor("\n" + indent)
                
                if spaces:
                    buffer.insert_at_cursor(" " * tab_width)
                else:
                    buffer.insert_at_cursor("\t")
                return True
            else:
                return False
        else:
            return False

    
    def __verify_auto_indent(self, text):
        """
        Verify if the next line must be indented.
        
        @param text: Line text.
        @type text: A String.
        """
        reserved_words = "def|class|elif|else|except|for|if|try|while"
        regex = re.compile("^\s*(" + reserved_words + ").*:\s*$")
        match = regex.search(text)
        
        if match != None:
            return True
        else:
            return False
