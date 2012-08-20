#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.katello_page import Katello
import time

class TestKatello():

    @pytest.mark.demo
    def test_login_and_nav(self, mozwebqa):
        '''
        Login and navigate to random pages
        '''
        workflow = ['sync_plans', 'systems', 'system_templates', 'roles']
        page = Katello(mozwebqa)
        page.go_to_home_page()
        page.login('admin', 'admin')
        #page.select_org(' redhat ')
        for view in workflow:
            page.go_to_url(page.baseurl + view)
        time.sleep(1)
