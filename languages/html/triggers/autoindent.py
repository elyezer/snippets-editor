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
        self.view = self.document_manager.get_active_view()
        self.buffer = self.view.buffer
        
        if self.buffer.get_has_selection():
            return False
        
        if (self.view.get_auto_indent()):
            
            insert_mark = self.buffer.get_insert()
            insert_iter = self.buffer.get_iter_at_mark(insert_mark)
            
            tag = self.__get_previous_tag(insert_mark)

            if self.__verify_auto_indent(tag):
                
                # Indentation stuff
                pref_manager = tf.app.preferences_manager
                spaces = pref_manager.get_value("indentation/use_spaces")
                tab_width = pref_manager.get_value("indentation/tab_width")
                indent = self.view.get_indentation(insert_iter)
                
                next_tag = self.__get_next_tag(self.buffer.get_insert())
                
                if next_tag != None:
                    self.buffer.insert_at_cursor("\n")
                    
                self.buffer.insert_at_cursor("\n")
                self.buffer.insert_at_cursor(indent)
                
            #    insert_mark = self.buffer.get_insert()
                insert_iter = self.buffer.get_iter_at_mark(insert_mark)
                
                if next_tag != None:
                    insert_iter.backward_line()
                    
                    self.buffer.place_cursor(insert_iter)
                    self.buffer.insert_at_cursor(indent)
                
                if spaces:
                    self.buffer.insert_at_cursor(" " * tab_width)
                else:
                    self.buffer.insert_at_cursor("\t")
            
                return True
            else:
                return False
        else:
            return False
    
    def __get_previous_tag(self, insert_mark):
        end_iter = self.buffer.get_iter_at_mark(insert_mark)
        
        while end_iter.backward_char():
            char = end_iter.get_char() 
            if char == ">":
                end_iter.forward_char()
                begin_iter = end_iter.copy()
                
                while begin_iter.backward_char():
                    if begin_iter.get_char() == "<":
                        return self.buffer.get_text(begin_iter, end_iter)
                        
                break
                
            elif char in (" ", '\t'):
                continue
            else:
                break
        
        return None
        
        
    def __get_next_tag(self, insert_mark):
        begin_iter = self.buffer.get_iter_at_mark(insert_mark)
        
        while True:
            char = begin_iter.get_char()
            if char == "<":
                end_iter = begin_iter.copy()
                
                while end_iter.forward_char():
                    char = end_iter.get_char()
                    if char == ">":
                        end_iter.forward_char()
                        return self.buffer.get_text(begin_iter, end_iter)
                        
                break
                
            elif char in (" ", '\t'):
                continue
            else:
                break
        
            begin_iter.forward_char()
            
        return None
    
        
    def __verify_auto_indent(self, tag):
        if tag == None:
            return False
        
        tag = tag.strip()    
        #regex = re.compile("^<[^/].*[^/]>$")
        regex = re.compile("^<[^/]+>$")
        match = regex.search(tag)
        
        if match != None:
            return True
        else:
            return False
