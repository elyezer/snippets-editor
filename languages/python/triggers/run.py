# -*- coding: utf-8 -*-

#######################################################################
# Copyright © 2007-2009 Yuri Malheiros.
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

"""
This module implements the trigger of "F5".
"""


import tf.app
from tf.languages.python.triggers.runfiles.terminal import RunTerminal

shortcut = unichr(65474) #F5
sticky = False

class Run(object):
    
    def activate(self):
        """
        Execute the current python file.
        """
        self.document_manager = tf.app.document_manager
        document = self.document_manager.get_active_document()
        
        self.terminal = RunTerminal()
        self.terminal.run("python", document.file_uri)
        
        return True
