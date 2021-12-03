from django.test import LiveServerTestCase  
from selenium import webdriver
import time
#for keyboard key-pressing:
from selenium.webdriver.common.keys import Keys
#added for headless approach.
from selenium.webdriver.chrome.options import Options

#eg1
#note that each class defined, will be executed automatically without the need of main()
#Classes here are kinda treated like a function I guess(own)......
class Hosttest(LiveServerTestCase):
    
    def testhomepage(self):
        #---begin of headless setting for firefox-----
        options = webdriver.FirefoxOptions()
        options.headless= True
        driver=webdriver.Firefox(options=options) 
        #---end of headless setting -----
        # below are for testing with browser, so if we want headless, we need to commmet it out!!!
        # driver = webdriver.Chrome(executable_path="./chromedriver")

        driver.get(self.live_server_url)
        time.sleep(5)
        assert "Hello, world!" in driver.title


#eg2
class LoginFormTest(LiveServerTestCase):

    def testform(self):
        #----mod for headless approach-------
        options=Options()
        options.headless=True
        #----end of mod-----
        driver = webdriver.Chrome(chrome_options=options)
        #need to do string concat here as get() method only take single argument of string type   
        driver.get(('%s%s' % (self.live_server_url, '/accounts/login/')))
        #you need this for headless , as it goes too fast!!
        time.sleep(1)
        
        #identifying/greping the field
        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(1)

        submit = driver.find_element_by_id('submit')

        #sending value to the field variable define above. 
        user_name.send_keys('admin')
        user_password.send_keys('admin')

        #hitting ENTER key on the submit button. 
        submit.send_keys(Keys.RETURN)

        #post-auth, checking if the string 'admin' present in the webpage. 
        print(driver.page_source)
        assert 'User: admin' in driver.page_source

