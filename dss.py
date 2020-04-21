import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from time import sleep

dss_url = "https://www.employment.gov.sk/sk/centralny-register-poskytovatelov-socialnych-sluzieb/?page={}" \
          "&searchBean.kraj=" \
		  "&searchBean.druhSluzby=zariadenie+pre+seniorov" \
		  "&searchBean.forma=pobytov%C3%A1+-+ro%C4%8Dn%C3%A1" \
		  "&searchBean.typPoskytovatela=" \
		  "&btnSubmit=Vybra%C5%A5"

driver = webdriver.Firefox(executable_path='/home/marek/Desktop/del/dss/geckodriver')

for page_id in range (1, 62):
	driver.get(dss_url.format(page_id))


	page_content = driver.page_source

	soup = BeautifulSoup(page_content, 'html.parser')


	content = soup.select("#content")[0]
	table = content.find_all("table")[1]
	table_body = table.find_all("tbody")[0]
	tr_elements = table_body.find_all("tr", ["even", "odd"])
	tr_elements_detail = table_body.find_all("tr", ["detail_line"])

	for i in range(len(tr_elements)):
		m = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", str(tr_elements_detail[i]))
		if m:
			print(m[0].strip())
	sleep(1)

driver.close()
