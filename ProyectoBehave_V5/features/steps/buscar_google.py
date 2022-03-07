from behave import *
from selenium import webdriver
import unittest
from pages.google_page import *

@given('el usuario está en la página de Google')
def step_impl(context):
  context.driver = webdriver.Chrome('/Users/ppando/Proyectos/ProyectoBehave_V4/drivers/chromedriver')
  context.driver.get('https://www.google.com/')

@when('el usuario ingresa {palabra} y pulsa tecla enter')
def step_impl(context, palabra):
  GooglePage(context.driver).buscar(palabra)

@then("el usuario debería ver en el título de la página '{palabra} - Buscar con Google'")
def step_impl(context, palabra):
	assert palabra + ' - Buscar con Google', GooglePage(context.driver).get_title()

@when('el usuario escribe AFIP y pulsa tecla enter')
def step_impl(context):
  GooglePage(context.driver).buscar('AFIP')

@when('el usuario pulsa el boton Imagen')
def step_impl(context):
  GooglePage(context.driver).click_link_imagenes

@then("el usuario debería ver en el título de la página 'AFIP - Búsqueda de Google'")
def step_impl(context):
  assert 'AFIP - Búsqueda de Google', GooglePage(context.driver).get_title()
