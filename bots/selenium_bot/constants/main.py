class SeleniumConstants:
    DB_PATH = './bots/selenium_bot/data'
    CHROME_DRIVER_PATH: str = r'bots\selenium_bot\driver\chromedriver.exe'
    BOOKS_LIST: str = "//*[@role='listitem']"
    BOOK_TITLE: str = 'productTitle'
    BOOK_RATING: str = 'acrPopover'
    BOOK_DESCRIPTION: str = 'bookDescription_feature_div'
    BOOK_AUTHOR: str = 'bylineInfo'
    BOOK_CONTRIBUTIONS: str = "contribution"
    PAGE_AMOUNT_BOOK: str = '//*[@id="search"]/span/div/h1/div/div[1]/div/div/div[2]/h2/span[1]'
    LIST_AUTHORS: str = '//*[@id="bylineInfo"]/span/a'