from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
class MainTripAD:
    def __init__(self):
        self.requests = __import__('requests')
        self.pandas = __import__('pandas')
        self.json = __import__('json')
        self.time = __import__('time')
        self.os = __import__('os')
        self.tripAd_url = 'https://www.tripadvisor.com.ph'
    def test(self,name=''):
        return print(name)
    def setup(self):
        main_os = self.os.getcwd()
        setup_list = {
            'mainFolder':['main','bin','logs'],
            'subFolder1':[['saved_bulk','saved_solo'],['deleted'],['user_saved','user_actions'] ],
            'subFolder2':[['hotel','restaurant','tourist_establishment']],
            'subFolder3':[['website']],
            'subFolder4':[['region']],
            'subFolder5':[['city']],
            'subFolder6':[['metadata','reviews']]
            }
        dir_deep = [i[-1] for i in setup_list.keys() if i[-1].isnumeric()==True]
        '''
        for i,x in enumerate(setup_list['mainFolder']):
            os_main = main_os+'\\'+x
            try:
                self.os.mkdir(os_main)
            except FileExistsError:
                pass
            self.os.chdir(os_main)
            for j in dir_deep:
                for z in setup_list['subFolder'+j][i]:
                    self.os.mkdir(os_main+'\\'+z)
        '''
        return dir_deep
            
            
    def setSelenium(self):
        options=Options()
        options.add_argument('start-maximized')
        options.add_argument('--headless')
        driver=webdriver.Firefox(options=options,executable_path=r'Y:\geckodriver.exe')
        return driver


