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

# IMPORT SECTION

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import getpass

#INGRESAR USUARIO

#username = input('Ingrese su usuario UNAL:             ')
#password = getpass.getpass('Ingrese la contraseña de su correo:             ')

#APERTURA DEL NAVEGADOR
pwd = os.getcwd()
cwd = 'browser = webdriver.Chrome(executable_path=r"'+ pwd +'\chromedriver.exe")'
exec (cwd)
browser.get('http://sara.unal.edu.co/saraweb/webcommon/acceso.jspx');

#DATOS DE INGRESO

NameLogin = browser.find_element_by_name('login:usuario')
NameLogin.send_keys(username)
PassLogin = browser.find_element_by_name('login:password')
PassLogin.send_keys(password + Keys.RETURN)

#INGRESO AL SARA

time.sleep(1) # Let the user actually see something!
thing = browser.find_element_by_id('popupMopdulo:j_id407:1:j_id411')
thing.click()
time.sleep(2)
thing = browser.find_element_by_id('popupBusqueda_form:j_id425:0:j_id437')
thing.click()
time.sleep(2)
thing = browser.find_element_by_id('formSalir:j_id43:j_id44:j_id652')
Hover = ActionChains(browser).move_to_element(thing)
link = browser.find_element_by_xpath("//span[@class='iceMnuBarItemLabel']").click()
time.sleep(1)
link = browser.find_element_by_xpath("//span[contains(text(),'Consultar Prog. Trab. Acad.')]").click()

# time.sleep(5)
# browser.quit()
