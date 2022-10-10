from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('/home/python/python-django-tdd/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def tearDown(self):
        self.browser.quit()

    #def test_para_verificar_se_a_janela_do_browser_esta_ok(self):
    #    self.browser.get('https://www.alura.com.br')

    #def test_abre_janela_do_chrome(self):
    #    self.browser.get(self.live_server_url)

    #def test_deu_ruim(self):
    #    """Teste de exemplo de erro"""
    #    self.fail('Teste falhou - deu ruim mesmo')

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando
        """
    
        # Vini, deseja encontrar um novo animal, para adotar.

        # Ele encontra o busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')

        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'),'Exemplo: leão, urso...')

        # Ele pesquisa por leão e clica no botão pesquisar.
        # aguardar 2 segundos
        time.sleep(2)
        # Digitar no input
        buscar_animal_input.send_keys('leão')
        time.sleep(2)
        # Clicar no botão
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()


        # O site exibe 4 características do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um leão.
        
        