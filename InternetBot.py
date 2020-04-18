import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

# Options not to display the browser while running the program (headless mode)
# Uncomment the following lines if you want to use headless mode for Chrome Browser.
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'


class InternetBot:

    FACEBOOK_CONNEXION = 'https://www.facebook.com/'
    INSTAGRAM_CONNEXION = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

    DEFAULT_BROWSER = 'Firefox'

    def __init__(self, browser = DEFAULT_BROWSER):
        self.useBrowser(browser)
        self.wait = WebDriverWait(self.driver, 10)

    def useBrowser(self, browser):
        browser = browser.lower()
        browser = browser.capitalize()

        if browser == 'Chrome':
            # Uncomment this line and replace the absolute path if you want to use headless mode for Chrome Browser.
            #self.driver = webdriver.Chrome(executable_path=r"your_absolute_path_to_chromedriver.exe", chrome_options=chrome_options)
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else :
            #self.driver = eval(webdriver + '.' + browser + '()')
            self.driver = getattr(webdriver, browser)

    def closeBrowser(self):
        self.driver.close()

    def connectOn(self, site, usernameElementSelector='', username='', passwordElementSelector='', password='', formElement=''):
        if site == 'facebook':
            self.goTo(self.FACEBOOK_CONNEXION)
            self.fillElement("//input[@id='email' and @name='email']", username)
            self.fillElement("//input[@id='pass' and @name='pass']", password)
            self.submitForm("//*[@id='login_form']")

        elif site == 'instagram':
            self.goTo(self.INSTAGRAM_CONNEXION)
            self.fillElement("//input[@name='username']", username)
            self.fillElement("//input[@name='password']", password)
            self.submitForm("/html/body/div[1]/section/main/div/article/div/div[1]/div/form")

        else :
            self.goTo(site)
            self.fillElement(usernameElementSelector, username)
            self.fillElement(passwordElementSelector, password)
            self.submitForm(formElement)

    def getDynamicElement(self, condition, method, elementSelector):
        dynamicElement = None
        try:
            dynamicElement = self.wait.until((getattr(EC, condition)((getattr(By, method), elementSelector))))
            return dynamicElement
        except TimeoutException:
            print('Exception Timeout')
            return None
        except ElementNotVisibleException:
            print('Exception Element Not Visible')
            return None
        except NoSuchElementException:
            print('Exception No Suche Element Exception')
            return None
        except:
            print('Exception non attrapée')

    def goTo(self, url):
        self.driver.get(url)

    def fillElement(self, elementSelector, text, method='XPATH', condition='visibility_of_element_located'):
        element = None
        while(element is None):
            element = self.getDynamicElement(condition, method, elementSelector)

        element.send_keys(text)

    def clickElement(self, elementSelector, method='XPATH', condition='element_to_be_clickable'):
        element = None
        while(element is None):
            element = self.getDynamicElement(condition, method, elementSelector)

        element.click()

    def hoverElement(self, elementSelector, method='XPATH', condition='visibility_of_element_located'):
        element = None
        while(element is None):
            element = self.getDynamicElement(condition, method, elementSelector)

        ActionChains(self.driver).move_to_element(element).perform()

    def submitForm(self, formElementSelector, method='XPATH', condition='element_to_be_clickable'):
        formElement = None
        while(formElement is None):
            formElement = self.getDynamicElement(condition, method, formElementSelector)

        formElement.submit()

    #def putData(self, data):
        #if isinstance(data, collections.Sequence):
