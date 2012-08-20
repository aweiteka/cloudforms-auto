#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.page import Page
from pages.page import BaseProductFactory

class Base(Page):
    '''
    Base class for global project specific functions
    '''
    @property
    def page_title(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def baseurl(self):
        # clean this up -- base_url vs baseurl?
        # used for appending view string for direct nav
        return self.base_url + '/'

    def go_to_home_page(self):
        # from --baseurl= arg
        self.selenium.get(self.base_url)

    def go_to_katello(self):
        # from --katello_url= arg
        self.selenium.get(self.katello_url)

    def go_to_aeolus(self):
        # from --aeolus_url= arg
        self.selenium.get(self.aeolus_url)

    def go_to_url(self, url):
        # pass in url
        self.selenium.get(url)

    def click_by_text(self, css_tag, name):
        # when "link" is a javascript span tag or similar
        _text_locator = (By.XPATH, "//%s[text() = '%s']" % (css_tag, name))
        self.selenium.find_element(*_text_locator).click()

