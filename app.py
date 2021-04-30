from selenium import webdriver
import sys

# opening tabs
def open_tabs(stock):
    global driver, window_original

    finviz = 'https://finviz.com/quote.ashx?t=' + stock
    stocktwits = 'https://stocktwits.com/symbol/' + stock
    sec_filings = 'https://www.nasdaq.com/market-activity/stocks/' + stock + '/sec-filings'
    driver.execute_script("window.open('%s', '_blank')" % finviz)
    driver.execute_script("window.open('%s', '_blank')" % sec_filings)
    driver.execute_script("window.open('%s', '_blank')" % stocktwits)

# loop prompt until program is closed
def maintask():
    while True:
        try:
            symbols = input("Enter stock(s): ")
            stocks = symbols.split(' ')
            for stock in stocks:
                open_tabs(stock)
        except KeyboardInterrupt:
            print("\nExiting program...")
            sys.exit()

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument("--user-data-dir=C:\\User Data")
options.add_argument("profile-directory=Profile 3")
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe', options=options)
driver.minimize_window()
window_original = driver.window_handles[0]
driver.get('https://www.marketwatch.com/')

maintask()