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

shortcut = 'ctrl+' + unichr(65293) #Ctrl+Return
sticky = False

import tf.app

class Br(object):
    
    def activate(self):
        """
        Auto indent.
        """
        self.document_manager = tf.app.document_manager
        self.view = self.document_manager.get_active_view()
        self.buffer = self.view.buffer
        self.buffer.insert_at_cursor("<br />")
        
        return True
        
        
