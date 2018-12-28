from selenium import webdriver

driver = webdriver.Firefox()
journal_url = "http://www.rondonopolis.mt.gov.br/diario-oficial/"
driver.get(journal_url)
pdf_links = driver.find_elements_by_css_selector("table a")
for link in pdf_links:
    print(link.get_attribute("href"))
driver.close()