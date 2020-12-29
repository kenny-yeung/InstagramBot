from selenium import webdriver
from time import sleep
import os

class InstagramBot:
    def __init__(self, username, password): 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")

        #Location of chrome driver
        self.driver = webdriver.Chrome(os.path.join('directory of chrome drive'),options=chrome_options)
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(3)
        user = driver.find_element_by_name('username')
        user.send_keys(self.username)

        passw = driver.find_element_by_name('password')
        passw.send_keys(self.password)

        login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button') #css selector of the login in button
        login.click()
        sleep(3)

    def search(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag)

    def like(self, number):
        driver = self.driver
        #driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        post = driver.find_element_by_class_name('v1Nh3') #class name of each post in the explore page
        post.click()
        sleep(2)

        i = 1
        while i <= number:
            sleep(3)
            article = driver.find_element_by_class_name('fr66n')
            like_check = article.find_element_by_tag_name('svg')
            like_check = like_check.get_attribute('aria-label')
            if(like_check == "Like"):
                article.click() #class name of the heart button
                i += 1
            sleep(2)
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() #class name of the 'next' arrow button

        driver.get('https://www.instagram.com')



gram = InstagramBot('Your Login', 'Your Password')
gram.login()
sleep(1)
gram.search('Search in explorer tab i.e basketball')
gram.like(100)

