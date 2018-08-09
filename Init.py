#
#
# #############################################################################
#       Copyright (c) 2018 Universidad Nacional de Colombia All Rights Reserved.
#
#             This work was made as a development to improve data collection
#       for self-assessment and accreditation processes in the Vicedeanship
#       of academic affairs in the Engineering Faculty of the Universidad
#       Nacional de Colombia and is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International License
#       and MIT Licence.
#
#       by Manuel Embus.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#
#
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
pwd = os.getcwd()
cwd = 'browser = webdriver.Chrome(executable_path=r"'+ pwd +'\chromedriver.exe")'
exec (cwd)
browser.get('http://sara.unal.edu.co/saraweb/webcommon/acceso.jspx');
NameLogin = browser.find_element_by_name('login:usuario')
#NameLogin.send_keys('maguzmanp')
NameLogin.send_keys('mfneirae')
PassLogin = browser.find_element_by_name('login:password')
PassLogin.send_keys('test123' + Keys.RETURN)
time.sleep(5) # Let the user actually see something!
browser.quit()

DraSaChaPiPo2019
