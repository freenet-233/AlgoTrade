from time import sleep

from longport.openapi import QuoteContext, SubType, PushQuote

from longport_openapi.core.account_config import AccountConfig


def on_quote(symbol: str, quote: PushQuote):
    print(symbol, quote)


ctx = QuoteContext(AccountConfig.accountConfig)
ctx.set_on_quote(on_quote)

symbols = ["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"]
ctx.subscribe(symbols, [SubType.Quote], True)
sleep(30)