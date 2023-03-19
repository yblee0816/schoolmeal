from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os 

options = webdriver.ChromeOptions()# 옵션 생성
options.add_argument("headless")# 창 숨기는 옵션 추가

print("본 프로그램은 Chrome 브라우저에서만 작동되는 프로그램입니다.")
while(1):
    cmd = 'mode 60,29'
    os.system(cmd)

    print("이번주의 급식만 확인 가능합니다.")
    print("확인하고 싶은 급식의 요일을 ↓ 칸에 입력하세요 예)화,수,금")
    day=input()

    driver = webdriver.Chrome(options=options)
    driver.get("https://kmit-h.goeujb.kr/kmit-h/ad/fm/foodmenu/selectFoodMenuView.do?mi=2771")

    cmd='mode 30,16'
    os.system(cmd)

    if day=="월":
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/thead/tr/th[3]").text)
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[2]/div/p[2]").text)
        print("\n")
    elif day=="화":
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/thead/tr/th[4]").text)
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[3]/div/p[2]").text)
        print("\n")
    elif day=="수":
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/thead/tr/th[5]").text)
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[4]/div/p[2]").text)
        print("\n")
    elif day=="목":
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/thead/tr/th[6]").text)
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[5]/div/p[2]").text)
        print("\n")
    elif day=="금":
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/thead/tr/th[7]").text)
        print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[6]/div/p[2]").text)
        print("\n")
    elif day=="토" and "일":
        print("토요일 일요일은 급식이 없다 멍청아")
    else:
        print("요일을 제대로 입력해주세요. 예) 월,수,금")
    
    keep_question=input("다른 요일의 급식을\n확인하시겠습니까? y/n: ")
    if keep_question=='y':
        continue
    elif keep_question=='n':
        print("\n사용해주셔서 감사합니다.")
        exit()
    












#day=input() int로 받을시에는 selenium이 인식불가능.












