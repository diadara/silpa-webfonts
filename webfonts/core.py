#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import fonts


class Webfonts:
    def __init__(self):
        self.available_fonts = fonts.fonts

    def get_fonts_list(self, languages=None):
        result = []
        if languages is None or languages == []:
            result = [dict([i]) for i in self.available_fonts.items()]
        else:
            for language in languages:
                try:
                    for font in self.available_fonts:
                        if self.available_fonts[font]['Language'] == language:
                            result.append({font: self.available_fonts[font]})
                except KeyError:
                    pass
        return result

    def get_module_name(self):
        return "Webfonts"

    def get_info(self):
        return "Indic Webfonts"


def getInstance():
    return Webfonts()
