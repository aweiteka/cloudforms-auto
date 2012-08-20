#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.aeolus_page import Aeolus
import time

class TestAeolus():

    @pytest.mark.demo
    def test_login_and_nav(self, mozwebqa):
        '''
        Login and nav to random pages
        '''
        workflow = ['users', 'providers', 'permissions', 'pool_families', 'logout']
        page = Aeolus(mozwebqa)
        page.go_to_home_page()
        page.login('admin', 'password')
        #Assert.equal(page.page_title, 'Aeolus Conductor')
        for view in workflow:
            page.go_to_url(page.baseurl + view)
        time.sleep(1)
