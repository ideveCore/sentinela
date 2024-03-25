# application.py
#
# Copyright 2024 Ideve Core
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio
from .utils import Utils
from .window import create_main_window
from .actions import application_actions
from .define import APP_ID

application = Adw.Application.new(
  application_id     = APP_ID,
  flags              = Gio.ApplicationFlags.DEFAULT_FLAGS,
)

def startup(application: Adw.Application):
  application.utils = Utils(application)
  application_actions(application)

def activate(application: Adw.Application):
  create_main_window(application).present()

application.connect('startup', lambda user_data: startup(user_data))
application.connect('activate', lambda user_data: activate(user_data))
