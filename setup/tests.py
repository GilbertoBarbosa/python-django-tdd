from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('/home/python/python-django-tdd/chromedriver')

    def tearDown(self):
        self.browser.quit()

    #def test_para_verificar_se_a_janela_do_browser_esta_ok(self):
    #    self.browser.get('https://www.alura.com.br')

    def test_abre_janela_do_chrome(self):
        self.browser.get(self.live_server_url)

    def test_deu_ruim(self):
        """Teste de exemplo de erro"""
        self.fail('Teste falhou - deu ruim mesmo')
        