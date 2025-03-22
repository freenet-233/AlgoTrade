# 获取标的 k 线
from longport.openapi import QuoteContext, Period, AdjustType

from longport_openapi.core.account_config import AccountConfig

ctx = QuoteContext(AccountConfig.accountConfig)

resp = ctx.candlesticks("TSLA.US", Period.Day, 10, AdjustType.NoAdjust)
print(resp)