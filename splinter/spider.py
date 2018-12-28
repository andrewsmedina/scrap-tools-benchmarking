from splinter import Browser

journal_url = "http://www.rondonopolis.mt.gov.br/diario-oficial/"
with Browser() as browser:
    browser.visit(journal_url)
    pdf_links = browser.find_by_css("table a")
    for link in pdf_links:
        print(link["href"])