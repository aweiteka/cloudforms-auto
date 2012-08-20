# CloudForms integration automated test framework

The focus of this test framework is on product integration testing as opposed to comprehensive UI verification. The tests are generally user workflows. See the [CloudForms QE Integration Test Plan](https://docspace.corp.redhat.com/docs/DOC-112731).

This project is derived from Eric Sammons [headpin.auto](https://github.com/eanxgeek/headpin.auto) test framework, which in turn is based on the work of Mozilla's Web QA team. In an effort to learn and extend headpin.auto much of the code was left out. If this project is adopted then extensive work of headpin.auto should be incorporated.

Learn about the [pytest-mozwebqa plugin](https://github.com/davehunt/pytest-mozwebqa), view the [mozwebqa-test-template]() or consult the [mozwebqa-test-template wiki](https://github.com/mozilla/mozwebqa-test-templates/wiki).

## Installation and Dependencies
1. Clone this repository
        git clone https://github.com/aweiteka/cloudforms-auto.git
2. Run the pip installer
        pip install -r requirements.txt

### Requirements
* py (?)
* pytest
* pytest-mozwebqa
* PyYAML
* requests (?)
* Selenium Webdriver
* UnittestZero

### Optional
* Firefox Firebug plugin for web page inspection
* Selenium IDE Firefox plugin may be handy if you're new to Selenium. You can record navigation and see what tags it uses. Usually the element tags are not specific enough so it is of limited value.
* Check out [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) for parsing page content
        easy_install beautifulsoup4

## Executing Tests
### Basic usage
    py.test --driver=firefox --baseurl=https://<FQDN>/conductor|katello/ -q testdir/path/my_test_file.py

### Options
* `--driver=firefox` Allows tests to be run without a separate Selenium server running.
* `--baseurl=...` Used when only one product is under test, i.e. katello or aeolus. FIXME: trailing slash required?
* `--katello_url=...|--aeolus_url=...` Required when two products are under test.
* `-m <marker>` For running tests tagged with py.test markers. See [py.test documentation](http://pytest.org/latest/example/markers.html).
* `--product=katello|aeolus|combined` Specify product for test customization.

For complete options see the [pytest-mozwebqa project](https://github.com/davehunt/pytest-mozwebqa).

## Development Notes

### About the files
Derived from [mozwebqa-test-templates wiki](https://github.com/mozilla/mozwebqa-test-templates/wiki/File-glossary).

`/pages/page.py` This python file contains setup methods that we want to use throughout the page objects. By inheritance these methods are accessible in other page objects. It is important not to include locators or site specific functions in this file. Generally the functions in this file are common across our projects and don't change often.

`/pages/base.py` In base.py we place page object functions that are global across the whole site. For example if your website has a header or footer you can place references to these inside this class and they will be inherited by page objects.

`/pages/page_object.py` This is a page object file that represents a page on the website. When testing workflows there may not be a separate page for each link. Rather a "page" may be the katello project. All actions and actions that exist on this page should be contained in this page object. It inherits the base.py class and inturn all of the methods that base.py has access to.

/pages/__init__.py This empty py file signifies to python that the files inside this folder are python classes. Now they can be access from within other python classes using the folder name as a path, for example import pages.page_object

`/tests/test_file.py` Test code goes here. Consider using py.test metadata markers to tag tests, e.g. `@pytest.mark.katello_workflow` and run as `-m katello_workflow`

`credentials.yaml` Store the credentials to log into the site with. The mozwebqa plugin will parse this file and make the values available inside the tests.

`conftest.py` Specify command-line options.

`mozwebqa.cfg` Save your typing fingers, use this file. The mozwebqa plugin will read the parameters in this file and automatically add them onto the py.test command line. It is handy for parameters that are constant like --browsername=firefox

`README.md` A README file typical of software, here we explain the contents of the repository and how one might get started using the software.

`requirements.txt` Python does not compile with external packages and as such you will need to download them. We have listed the required packages in requirements.txt. Running sudo pip install -r requirements.txt (Mac/Linux) will automatically download and install the packages in this file. We recommend 'pinning' the packages to a specific version, for example pytest==2.1.3. This decreases the chance that a change to py.test will affect your test suite.

### Selenium
If you're new to Selenium read about the [Webdriver API](http://seleniumhq.org/docs/03_webdriver.html). You'll need the Firefox Firebug plugin to learn about page markup. Right-click on any component of a web site and select "Inspect Element." 

### Interactive Test Development
Developing Selenium tests is tricky and requires some trial and error. Launching a whole test just to see if your last code edit works takes a long time. A quicker way is to use the interactive Python shell (or even better, [IPython](http://ipython.org/) for auto-complete) to start an interactive webdriver session.
    $ python
    >>> from selenium import webdriver
    >>> url = 'https://myUrl/aeolus'
    >>> driver = webdriver.Firefox()
    >>> driver.get(url)
A Firefox browser window should open to the URL. You can now interact with the new  browser window (login, nav to page you're working on, inspect elements). Then try a locator and see if it works. 
    >>> driver.find_elements_by_css_selector('li#promotions')
    >>> [<selenium.webdriver.remote.webelement.WebElement at 0x1a42e50>] # valid
Once your selector code is valid you can add to your code and keep going!

### TODO
* Port data-driven model over from headpin.auto.

### Notes
* The `*_variable` is used with Selenium tags since number of items passed vary.
* Use CSS selectors over XPath if at all possible.
* Consider tagging tests with [py.test metadata markers](http://pytest.org/latest/example/markers.html).
* I understand mozwebqa requires each test to be specified with a destructive/nondestructive decorator but I have not verified. For example, mark a class or method with `@pytest.mark.destructive`.
* Some tests use direct navigation to known views. For example, instead of clicking menu item "Content Management > System Templates" it may be appropriate to go to URL "./katello/system_templates". If the UI navigation is being tested then menu clicking is required, but for workflow tests if is acceptable to go to the URL directly.
* Style guide, anyone? [Mozilla QA](https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide)
