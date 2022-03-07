from selenium.webdriver.common.by import By

class GooglePage:
  def __init__(self, driver):
    self.driver = driver
    self.cuadro_ingreso = (By.NAME,'q')
    self.link_imagenes = (By.LINK_TEXT,'Imágenes')
  
  def buscar(self, palabra):
    cuadro = self.driver.find_element(*self.cuadro_ingreso)
    cuadro.send_keys(palabra)
    cuadro.submit()

  def click_link_imagenes(self):
    self.driver.find_element(*self.link_imagenes).click()
  
  def get_title(self):
    return self.driver.title
