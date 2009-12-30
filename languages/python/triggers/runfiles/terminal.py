# -*- coding: utf-8 -*-

#######################################################################
# Copyright © 2007-2008 Yuri Malheiros.
# Copyright © 2009 TextFlow Team.
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

import gtk
import vte

"""
This module implements a class responsible for create a window
with a terminal and turn possible to execute programs in this terminal.
"""

class RunTerminal(object):
    def __init__(self):
        """
        Constructor.
        """
        self.window = gtk.Window()
        self.window.set_title("Running Python Script")
        
        self.terminal = vte.Terminal()
        
        self.window.add(self.terminal)
        self.window.show_all()
        self.__apply_preferences()
        
        self.terminal.connect("child-exited", self.child_exited)
        self.window.connect("delete-event", lambda *x: self.window.destroy())
        
    #################### Public Methods ####################
    
    def run(self, *command):
        """
        Run a command in terminal window
        
        @param *command: first parameter is the command and
                         the next ones are the first command arguments.
        @type *command: Strings.
        """
        pid = self.terminal.fork_command(command[0], command)
    
    
    #################### Private Methods ####################    
            
    def __apply_preferences(self):
        """
        Set terminal font, size and colors.
        """
        self.terminal.set_font_from_string("Bitstream Vera Sans Mono 12")
        self.terminal.set_color_foreground(gtk.gdk.color_parse('#444444'))
        self.terminal.set_color_background(gtk.gdk.color_parse('#ffffff'))
        self.terminal.set_color_cursor(gtk.gdk.color_parse('#444444'))
        self.terminal.set_cursor_shape(vte.CURSOR_SHAPE_UNDERLINE)
        self.terminal.set_size(30, 19)
        
        
    #################### Callbacks ####################

    def child_exited(self, widget):
        self.terminal.connect("key-press-event", self.key_press)
    
    def key_press(self, widget, event):
        exit_values = (gtk.keysyms.Escape, gtk.keysyms.Return)
        exit_ctrl_values = (gtk.keysyms.c, gtk.keysyms.d)
        
        if event.state & gtk.gdk.CONTROL_MASK and event.keyval in exit_ctrl_values:
            self.window.destroy()
        elif event.keyval in exit_values:
            self.window.destroy()