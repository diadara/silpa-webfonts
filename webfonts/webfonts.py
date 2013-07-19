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

from flask import Blueprint, render_template, request, url_for, abort, make_response
from fonts import fonts as available_fonts

blueprint = Blueprint('webfonts', __name__,
                      template_folder='templates', static_folder='fonts', static_url_path='/webfonts/static')


@blueprint.route('/webfonts', methods=['GET'])
def serve():
        try:
                req_fonts = request.args.get('font').split('|')
        except AttributeError:
                abort(400)
        match_request = set(req_fonts).intersection(set(available_fonts.keys()))
        if not match_request:
                abort(400)
        else:
                fonts = [{'family': f,
                          'eot': url_for('webfonts.static', _external=True, filename=available_fonts[f]['eot']),
                          'woff': url_for('webfonts.static',  _external=True, filename=available_fonts[f]['woff']),
                          'ttf': url_for('webfonts.static', _external=True, filename=available_fonts[f]['ttf'])
                          } for f in match_request]
                resp = make_response(render_template('webfonts.css', fonts=fonts))
                resp.headers.add('content-type', 'text/css')
                return resp
