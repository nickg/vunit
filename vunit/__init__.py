# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014, Lars Asplund lars.anders.asplund@gmail.com

from vunit.ui import VUnit

def generate_all(fun):
    fun._vunit_generate_all = True
    return fun