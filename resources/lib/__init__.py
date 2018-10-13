# -*- coding: utf-8 -*-

'''
    License summary below, for more details please read license.txt file

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import time
from tulip import control
from tulip.init import params

content = params.get('content_type')
action = params.get('action')
url = params.get('url')
image = params.get('image')
title = params.get('title')
name = params.get('name')
query = params.get('query')
plot = params.get('plot')
genre = params.get('genre')


def refresh_access():

    if control.setting('refresh.token') and control.setting('auto.refresh') == 'true':

        if float(control.setting('expiration.stamp')) < time.time():

            from resources.lib.modules.reddit import get_tokens
            get_tokens(refresh=True)


def first_time_prompt():

    if control.setting('first.time') == 'true':

        from resources.lib.modules.tools import welcome_message
        welcome_message()
        control.setSetting('first.time', 'false')
