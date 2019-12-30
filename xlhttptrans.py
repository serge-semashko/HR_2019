import os, sys
import requests 
import openpyxl as xl
from openpyxl import load_workbook 
from openpyxl import Workbook
from datetime import datetime
import time
workbook_path = 'G:/home/JINR/HR_2019/nica2019.xlsx'
wb = xl.load_workbook(workbook_path)
first_sheet = wb.worksheets[0]
t1 = time.time()
for i in range(2):
    rus_text = '  7.4.1.7 Разработка  ubuntu рабочих чертежей трекера для диаметра камеры MPD 64 мм и технологической оснастки для её изготовления'
    token = 'trnsl.1.1.20191225T214637Z.70e877a967974c76.65880b0aa066226a077346596774c28736fabd41'
    #url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    url_trans = 'https://192.168.1.2:8082/trans'
    trans_option = {'key':'token', 'lang':'ru-en', 'text': 'rus_text'}
    webRequest = requests.get(url_trans, params = trans_option)
    print(webRequest.text)
    webRequest = ''
    
t2 = time.time()
print(str((t2-t1)/50))


