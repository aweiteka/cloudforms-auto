#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from base import Base
from page import Page
from locators_katello import *

# needed for locally defined locators
from selenium.webdriver.common.by import By

import time

class Katello(Base):

    @property
    def header_text(self):
        return self.selenium.find_element(*header_locator).text

    def login(self, user, password):
        '''
        login
        '''
        # consider using send_characters if reliability is an issue
        self.send_text(user, *username_text_field)
        self.send_text(password, *password_text_field)
        self.selenium.find_element(*login_locator).click()

    def select_org(self, org):
        '''
        select organization
        '''
        # org drop-down not expanding
        self.selenium.find_element(*org_switcher_locator).click()
        self.click_by_text('a', org)

    def create_system_template(self, name, desc):
        '''
        create system template, name and description
        '''
        self.selenium.find_element(*new_template).click()
        self.send_text(name, *system_template_name)
        self.send_text(desc, *system_template_description)
        self.selenium.find_element(*template_save).click()

    def remove_element(self):
        '''
        click remove button
        '''
        self.selenium.find_element(*remove_template).click()
        self.click_by_text('span', 'Yes')

