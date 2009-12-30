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
This module implements the trigger of ">".
"""

shortcut = ">"
sticky = False

import tf.app
from HTMLParser import HTMLParser, HTMLParseError

class AutoCloseTag(object):
    
    def activate(self):
        """
        Auto indent.
        """
        self.document_manager = tf.app.document_manager
        self.view = self.document_manager.get_active_view()
        self.buffer = self.view.buffer
        self.buffer.insert_at_cursor(">")
        text = self.view.get_text()
        
        insert_mark = self.buffer.get_insert()
        insert_iter = self.buffer.get_iter_at_mark(insert_mark)
        line_number = insert_iter.get_line()
        
        tag_name = self.__get_typed_name(insert_iter)
        
        parser = Parser()
        
        try:
            parser.feed(text)
        except HTMLParseError:
            return True
                        
        
        if len(parser.stack) > 0:
            
            tag = self.__get_tag(parser.stack, line_number)
            
            if tag != None:
                if tag[0] == tag_name:
                    cursor_mark = self.buffer.create_mark("cursor", insert_iter, True)
                    self.buffer.insert_at_cursor("</" + tag[0] + ">")
                    new_cursor_iter = self.buffer.get_iter_at_mark(cursor_mark)
                    self.buffer.place_cursor(new_cursor_iter)
        
        return True
        
    def __get_tag(self, parser_stack, line_number):
        """
        Get the correct tag according cursor position and the parser stack.
        
        @param parser_stack: The stack with opened and not closed tags.
        @type parser_stack: A List.
        
        @param line_number: The current line number.
        @type line_number: A Int.
        """
        
        for tag in reversed(parser_stack):
            if tag[1] <= line_number + 1:
                return tag
        
        return None
        
    def __get_typed_name(self, insert_iter):
        """
        Get the tag name before insert cursor without '<' and '>'
        
        @param insert_iter: the iter of insert cursor
        @type insert_iter: TextIter.
        """
        
        end_iter = insert_iter.copy()
        
        while end_iter.backward_char():
            char = end_iter.get_char()

            if char == ">":
                start_iter = end_iter.copy()
                
                while start_iter.backward_char():
                    char = start_iter.get_char()
                    
                    if char == "<":
                        start_iter.forward_char()
                        #end_iter.backward_char()
                        text = self.buffer.get_text(start_iter, end_iter)
                        text = text.strip()
                        text = text.split(" ")[0]
                        return text
                
                return None
        
        return None
        
    
class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        self.stack.append((tag, self.getpos()[0]))
        
    def handle_endtag(self, tag):
        stack_len = len(self.stack)
        for i in xrange(stack_len):
            #if i[0] == tag:
            if self.stack[stack_len-i-1][0] == tag:
                self.stack.pop(stack_len-i-1)
                #self.stack.pop()
                return
    
    def get_stack_top(self):
        return self.stack[-1]
