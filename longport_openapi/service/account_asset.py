from longport.openapi import TradeContext

from longport_openapi.core.account_config import AccountConfig

ctx = TradeContext(AccountConfig.accountConfig)

resp = ctx.account_balance()
print(resp)