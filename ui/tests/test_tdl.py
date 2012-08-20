#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.katello_page import Katello
import time, random
#from pages.locators_katello import *

class TestTDL():

    @pytest.mark.katello_workflow
    def test_create_tdl(self, mozwebqa):
        '''
        Create TDL name and description, remove
        '''
        page = Katello(mozwebqa)
        page.go_to_home_page()
        page.login('admin', 'admin')

        page.go_to_url(page.baseurl + "system_templates")

        template_name = 'My System ' + str(time.time())
        template_description = 'My template description'
        page.create_system_template(template_name, template_description)
        time.sleep(1)
        page.click_by_text('span', template_name)
        time.sleep(1)
        page.remove_element()

        # logout not working due to data-method='POST' requirement?
        #page.go_to_url(page.baseurl + 'logout')
        time.sleep(1)

