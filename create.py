# 프로그래머스 문제 번호, 문제 제목, url, 언어타입에 맞춰 자동으로 생성하기 위한 파일
import os
import requests
from bs4 import BeautifulSoup

commentsByType = {"py": "#", "sql": "--"}# 언어 별 주석

lv = input("lv을 입력해 주세요. :")
url = input("url을 입력해 주세요. :")

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

problemType = soup.select('a.btn-tab.nav-link.active')[0].text.lstrip().rstrip().split('.')[1]# 언어 타입
title = soup.select("#tab > li")[0].text.lstrip().rstrip()# 문제 제목

startIdx = int(url.rfind("lessons") + 8)# lessons 문자열 길이 + / 길이
endIdx = int(url.rfind("?language="))# 언어 설정 문자열이 있는 url일 경우

if endIdx != -1:
    problemNum = url[startIdx: endIdx]
else:
    problemNum = url[startIdx:]

file_path = f'lv{lv}/{problemNum}.{problemType}'# 문제 레벨에 따라 다른 경로 문제 타입의 파일을 생성

if os.path.isfile(file_path):
    print(f"{file_path}가 이미 존재 합니다.")
else:
    with open(file_path, 'a') as file:
        # 주석 내용을 파일에 작성
        file.write(f'{commentsByType[problemType]} {title}\n')
        file.write(f'{commentsByType[problemType]} {url}\n')
    print("파일 생성 완료")