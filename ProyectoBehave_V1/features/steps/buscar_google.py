from behave import *
from selenium import webdriver
import unittest

@given('el usuario está en la página de Google')
def step_impl(context):
  context.driver = webdriver.Chrome('/Users/ppando/Proyectos/ProyectoBehave_V1/drivers/chromedriver')
  context.driver.get('https://www.google.com/')

@when('el usuario ingresa AFIP y pulsa tecla enter')
def step_impl(context):
  cuadro_ingreso = context.driver.find_element_by_name('q')
  cuadro_ingreso.send_keys('AFIP')
  cuadro_ingreso.submit()

@then("el usuario debería ver en el título de la página 'AFIP - Buscar con Google'")
def step_impl(context):
	assert 'AFIP - Buscar con Google', context.driver.title