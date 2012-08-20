#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException



class BaseProductFactory(object):
    '''
    Factory for supported products
    '''
    @classmethod
    def get(self, project):
        '''
        Get the project class by project
        returns projectClass.
        '''
        projectClass = None
        if project == 'sam':
            projectClass = SamProduct()
        if project == 'headpin':
            projectClass = HeadpinProduct()
        if project == 'katello':
            projectClass = KatelloProduct()
        if project == 'aeolus':
            projectClass = AeolusProduct()

        return projectClass

class BaseProduct(object):
    '''
    Base class for all Products
    '''
    def __init__(self):
        '''
        Default values for all products; likely won't be used
        as we focus on the differences.
        '''
        pass

class SamProduct(BaseProduct):
    '''
    Elements that are specific to SAM.
    '''
    #_page_title = 'Subscription Asset Manager - Subscription Management'
    #_logo_locator = (By.XPATH, '//img[contains(@src, 'rh-logo.png')]')
    #_footer = 'Subscription Asset Manager Version:'
    
class HeadpinProduct(BaseProduct):
    '''
    Elements specific to Headpin.
    '''
    #_page_title = 'Headpin - Open Source Subscription Management'
    #_logo_locator = (By.XPATH, '//img[contains(@src, 'logo.png')]')
    
class KatelloProduct(BaseProduct):
    '''
    Elements specific to Katello
    '''
    # we are using separate locator files

    #_page_title = 'Katello - Open Source Systems Management'
    #_logo_locator = (By.XPATH, '//img[contains(@src, 'logo.png')]')

class AeolusProduct(BaseProduct):
    '''
    Elements specific to Aeolus
    '''
    # we are using separate locator files

    #_page_title = ''
    #_logo_locator = (By.XPATH, '//img[contains(@src, 'logo.png')]')

class Page(object):
    '''
    Base class for all Pages
    '''

    def __init__(self, testsetup):
        '''
        Constructor
        '''
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.katello_url = testsetup.katello_url
        self.aeolus_url = testsetup.aeolus_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout
        self.project = testsetup.project
        self.org = testsetup.org

###
# from headpin.auto
# not yet used in this project
###
    def click(self, *locator):
        '''
        Executes a Left Mouse Click on locator.
        '''
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_displayed())
        click_locator = self.selenium.find_element(*locator)
        ActionChains(self.selenium).move_to_element(click_locator).\
            click().perform()
        
    def click_and_wait(self, *locator):
        self.click(*locator)
        self.jquery_wait()
    
    def send_characters(self, text, *locator):
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_enabled())
        input_locator = self.selenium.find_element(*locator)
        for c in text:
            input_locator.send_keys(c)
            
    def send_text(self, text, *locator):
        '''
        Sends text to locator, one character at a time.
        '''
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_enabled())
        input_locator = self.selenium.find_element(*locator)
        input_locator.send_keys(text)



###

    @property
    def is_the_current_page(self):
        if self._page_title:
            WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)

        Assert.equal(self.selenium.title, self._page_title,
            'Expected page title: %s. Actual page title: %s' % (self._page_title, self.selenium.title))
        return True

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except NoSuchElementException, ElementNotVisibleException:
            return False

    def get_url_current_page(self):
        return(self.selenium.current_url)
