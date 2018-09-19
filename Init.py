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

username = input('Ingrese su usuario UNAL:             ')
password = getpass.getpass('Ingrese la contraseña de su correo:             ')
delay = int(input('Ingrese el número en segundos de delay:             '))
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

time.sleep(delay + 1.5)
thing = browser.find_element_by_id('popupMopdulo:j_id407:1:j_id411').click()
time.sleep(delay + 1.5)
thing = browser.find_element_by_id('popupBusqueda_form:j_id425:0:j_id437')
thing.click()
time.sleep(delay + 1.5)
thing = browser.find_element_by_id('formSalir:j_id43:j_id44:j_id652')
time.sleep(delay)
Hover = ActionChains(browser).move_to_element(thing)
link = browser.find_element_by_xpath("//span[@class='iceMnuBarItemLabel']").click()
time.sleep(delay)
link = browser.find_element_by_xpath("//span[contains(text(),'Consultar Prog. Trab. Acad.')]").click()
time.sleep(delay)
link = browser.find_element_by_xpath("//select[@id='listadoJornadaDocente_form:j_id69']/option[text()='PERIODO ACADEMICO 2018 PARA DOCENTES DE PLANTA']").click()
time.sleep(delay)
#link = browser.find_element_by_xpath("//select[@id='listadoJornadaDocente_form:j_id79']/option[text()='Autorizado']").click()
link = browser.find_element_by_xpath("//select[@id='listadoJornadaDocente_form:j_id79']/option[text()='Aprobado']").click()
time.sleep(delay)
link = browser.find_element_by_xpath("//span[@id='listadoJornadaDocente_form:j_id96']").click()
time.sleep(delay + 1)
link = browser.find_element_by_xpath("//a[@id='listadoJornadaDocente_form:j_id97:0.1']").click()

# time.sleep(5)
# browser.quit()
