#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from base import Base
from page import Page
from locators_aeolus import *
import time

class Aeolus(Base):

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

