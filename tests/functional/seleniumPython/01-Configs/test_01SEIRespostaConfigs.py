# Generated by Selenium IDE
# -*- coding: utf-8 -*-
import pytest
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test01SEIRespostaConfigs():
  def setup_method(self, method):
    if ("LOCAL" == os.environ["SELENIUMTEST_MODALIDADE"]):
        self.driver = webdriver.Chrome()
    else:
        self.driver = webdriver.Remote(command_executor=os.environ["SELENIUMTEST_SELENIUMHOST_URL"], desired_capabilities=DesiredCapabilities.CHROME)
        
    if ((not 'maximizar_screen' in os.environ) or os.environ['maximizar_screen'] == 'true'):
        self.driver.maximize_window()
        
    self.driver.implicitly_wait(5)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_00ConfigValidacaoSistema(self):
    self.driver.get(os.environ["SELENIUMTEST_SISTEMA_URL"]+"/sip/login.php?sigla_orgao_sistema="+os.environ["SELENIUMTEST_SISTEMA_ORGAO"]+"&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()=\"Administração\"]")))
    self.driver.find_element(By.XPATH, "//*[text()=\"Administração\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()=\"Módulo de Resposta - Gov.br\"]")))
    self.driver.find_element(By.XPATH, "//*[text()=\"Módulo de Resposta - Gov.br\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Parâmetros de Configuração")))
    self.driver.find_element(By.LINK_TEXT, "Parâmetros de Configuração").click()
    self.driver.find_element(By.NAME, "sbmSalvar").click()
    assert self.driver.switch_to.alert.text == "Selecione o Sistema."
    self.driver.switch_to.alert.accept()
  
  def test_01ConfigValidacaoDocumento(self):
    self.driver.get(os.environ["SELENIUMTEST_SISTEMA_URL"]+"/sip/login.php?sigla_orgao_sistema="+os.environ["SELENIUMTEST_SISTEMA_ORGAO"]+"&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()=\"Administração\"]")))
    self.driver.find_element(By.XPATH, "//*[text()=\"Administração\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()=\"Módulo de Resposta - Gov.br\"]")))
    self.driver.find_element(By.XPATH, "//*[text()=\"Módulo de Resposta - Gov.br\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Parâmetros de Configuração")))
    self.driver.find_element(By.LINK_TEXT, "Parâmetros de Configuração").click()
    self.driver.find_element(By.ID, "selSistema").click()
    dropdown = self.driver.find_element(By.ID, "selSistema")
    dropdown.find_element(By.XPATH, "//option[. = 'PD_GOV_BR']").click()
    self.driver.find_element(By.NAME, "sbmSalvar").click()
    assert self.driver.switch_to.alert.text == "Selecione o Tipo de Documento."
    self.driver.switch_to.alert.accept()
  
  def test_02ConfigConfirmacao(self):
    self.driver.get(os.environ["SELENIUMTEST_SISTEMA_URL"]+"/sip/login.php?sigla_orgao_sistema="+os.environ["SELENIUMTEST_SISTEMA_ORGAO"]+"&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()=\"Administração\"]")))
    self.driver.find_element(By.XPATH, "//*[text()=\"Administração\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()=\"Módulo de Resposta - Gov.br\"]")))
    self.driver.find_element(By.XPATH, "//*[text()=\"Módulo de Resposta - Gov.br\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Parâmetros de Configuração")))
    self.driver.find_element(By.LINK_TEXT, "Parâmetros de Configuração").click()
    self.driver.find_element(By.ID, "selSistema").click()
    dropdown = self.driver.find_element(By.ID, "selSistema")
    dropdown.find_element(By.XPATH, "//option[. = 'PD_GOV_BR']").click()
    dropdown = self.driver.find_element(By.ID, "selTipoDocumento")
    dropdown.find_element(By.XPATH, "//option[. = 'Resposta pelo Protocolo Digital']").click()
    self.driver.find_element(By.ID, "selTipoDocumento").click()
    self.driver.find_element(By.NAME, "sbmSalvar").click()
    time.sleep(2)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id=\"divInfraMensagens\"]")))
    self.vars["Mapeamento cadastrado com sucesso."] = self.driver.find_element(By.XPATH, "//*[@id=\"divInfraMensagens\"]").text
  
