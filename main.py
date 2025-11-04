from playwright.sync_api import sync_playwright

from bots.playwright_bot.main import AmazonBookExtractorPw
from bots.selenium_bot.main import AmazonBookExtractorSel

SEARCH_STRING = 'cura quantica and energia and chakras and reiki and lei da atracao and cura natural'
PAGE_AMOUNT = 1

bot = input('bot[selenium, playwright]: ')

if bot.lower() == 'selenium':
    book_scraper = AmazonBookExtractorSel(SEARCH_STRING, PAGE_AMOUNT)
    book_scraper.run()
elif bot.lower() == 'playwright':
    with sync_playwright() as playwright:
        book_scraper = AmazonBookExtractorPw(playwright, SEARCH_STRING, PAGE_AMOUNT)
        book_scraper.run()
else:
    print('Opção não disponível!')                    
                    
