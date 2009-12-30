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
This module implements the trigger of "ctrl+b".
"""

shortcut = "ctrl+b"
sticky = False

import tf.app

class Strong(object):

    def activate(self):
        """
        If has selection - surround selected text with <strong></strong>.
        Else - create tag.
        """
        
        self.document_manager = tf.app.document_manager
        buffer = self.document_manager.get_active_view().buffer
        
        if buffer.get_has_selection():
            start, end = buffer.get_selection_bounds()
            text = buffer.get_text(start, end)
            buffer.delete(start, end)
            buffer.insert_at_cursor("<strong>" + text + "</strong>")
        else:
            insert_mark = buffer.get_insert()
            buffer.insert_at_cursor("<strong></strong>")
            insert_iter = buffer.get_iter_at_mark(insert_mark)
            insert_iter.backward_chars(9)
            buffer.place_cursor(insert_iter)

        return True

