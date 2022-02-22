import os
import unittest
from selenium import webdriver
from MainPage import MainPage


class MainPageTest(unittest.TestCase):

    def setUp(self):
        os.environ['PATH'] += 'C:/Users/Public/Pasha/Selenium_drivers'
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.agatmedfarm.ru/')
        self.driver.maximize_window()
        self.mainpage = MainPage(self.driver)

    def testheadertext(self):
        self.assertEqual(self.mainpage.getheadertext(), 'ТК АГАТМЕД')

    def testfindtext(self):
        self.assertEqual(('Поиск',
                          'простыня',
                          ['Комплект акушерский стерильный (Гекса)',
                           'Простыня 310х260/200см для проктологических операций (на прямой кишке) '
                           'стерильная Эконом Плюс',
                           'Комплект белья постельного (простыня, пододеяльник, наволочка) стерильный '
                           'Спанбонд 42/Спанлейс 40',
                           'Комплект белья постельного (простыня, пододеяльник, наволочка) стерильный '
                           'Спанбонд 42',
                           'Комплект белья постельного (простыня, пододеяльник, наволочка) стерильный '
                           'Спанбонд 25',
                           'Комплект белья постельного (простыня, пододеяльник, наволочка) нестерильный '
                           'Спанбонд 42/Спанлейс 40',
                           'Комплект белья постельного (простыня, пододеяльник, наволочка) нестерильный '
                           'Спанбонд 42',
                           'Комплект белья постельного (простыня, пододеяльник, наволочка) нестерильный '
                           'Спанбонд 25',
                           'Простыня для нефроскопии 160х300см с отверстием 19х30см, сборным карманом, '
                           'операционной пленкой стерильная Эконом Плюс']), self.mainpage.findtext('простыня'))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
