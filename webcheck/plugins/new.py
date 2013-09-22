
# new.py - plugin to list recently modified pages
#
# Copyright (C) 1998, 1999 Albert Hopkins (marduk)
# Copyright (C) 2002 Mike W. Meyer
# Copyright (C) 2005, 2006, 2011, 2013 Arthur de Jong
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#
# The files produced as output from the software do not automatically fall
# under the copyright of the software, unless explicitly stated otherwise.

"""Present a list of recently modified pages."""

__title__ = "what's new"
__author__ = 'Arthur de Jong'
__outputfile__ = 'new.html'

import time

from webcheck import config
from webcheck.db import Session, Link
from webcheck.output import render


SECS_PER_DAY = 60 * 60 * 24


def generate(crawler):
    """Output the list of recently modified pages."""
    session = Session()
    newtime = time.time() - SECS_PER_DAY * config.REPORT_WHATSNEW_URL_AGE
    links = session.query(Link).filter_by(is_page=True, is_internal=True)
    links = links.filter(Link.mtime > newtime).order_by(Link.mtime.desc())
    render(__outputfile__, crawler=crawler, title=__title__,
           links=links, now=time.time(), SECS_PER_DAY=SECS_PER_DAY)
    session.close()
