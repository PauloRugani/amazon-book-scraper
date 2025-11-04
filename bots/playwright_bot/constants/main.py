class PlaywrightConstants:
    DB_PATH = './bots/playwright_bot/data'
    BOOKS_LIST: str = '[role="listitem"]'
    BOOK_TITLE: str = '[id="productTitle"]'
    BOOK_RATING: str = '//*[@id="averageCustomerReviews"]'
    BOOK_DESCRIPTION: str = '[id="bookDescription_feature_div"]'
    BOOK_CONTRIBUTIONS: str = '[class="contribution"]'
    PAGE_AMOUNT_BOOK: str = '//*[@id="search"]/span/div/h1/div/div[1]/div/div/div[2]/h2/span[1]'
    LIST_AUTHORS: str = '//*[@id="bylineInfo"]/span/a'