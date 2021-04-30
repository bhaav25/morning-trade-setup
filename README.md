# morning-trade-setup

Notes:
This script uses a select chrome profile, so that is why line 29 and line 30 exist in app.py.
They should be commented out if the default chrome profile is to be used.

Run the app.py file and you will be prompted with "Enter stock(s):"
1) Enter 1 or more stocks separated by a space and hit ENTER
2) A chrome window will open launching the sites for each stock entered:

'https://finviz.com/quote.ashx?t=' + <THE_STOCK>

'https://www.nasdaq.com/market-activity/stocks/' + <THE_STOCK> + '/sec-filings'

'https://stocktwits.com/symbol/' + <THE_STOCK>

