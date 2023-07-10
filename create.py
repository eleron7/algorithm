import os
import requests
from bs4 import BeautifulSoup
#문제 번호가 담긴 파일을 자동으로 생성하기 위한 파일

lv = input("lv을 입력해 주세요. :")
url = input("url을 입력해 주세요. :")
launguageStr = "?language=python3"

startIdx = int(url.rfind("lessons") + 8)#lessons 문자열 길이 + / 길이
endIdx = int(url.rfind(launguageStr))#언어 설정 문자열이 있는 url일 경우

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
data = requests.get(url if endIdx != -1 else url + launguageStr, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select("#tab > li")[0].text.lstrip().rstrip()#문제 제목

if endIdx != -1:
    problemNum = url[startIdx: endIdx]
else:
    problemNum = url[startIdx:]

file_path = f'lv{lv}/{problemNum}.py'#문제 레벨에 따라 다른 경로

if os.path.isfile(file_path):
    print(f"{file_path}가 이미 존재 합니다.")
else:
    with open(file_path, 'a') as file:
        # 주석 내용을 파일에 작성
        file.write(f'# {title}\n')
        file.write(f'# {url}\n')
    print("파일 생성 완료")