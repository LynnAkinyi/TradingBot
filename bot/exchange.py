import ccxt
from decimal import Decimal
from typing import Optional

class ExchangeClient:
    SUPPORTED_EXCHANGES = {
        'BINANCE': 'binance',
        'COINBASE': 'coinbasepro',
        'KRAKEN': 'kraken'
    }

    def __init__(self, exchange_id: str, api_key: str, api_secret: str):
        try:
            # Validate and get correct exchange id
            exchange_id = self.SUPPORTED_EXCHANGES.get(exchange_id.upper())
            if not exchange_id:
                raise ValueError(f"Unsupported exchange. Must be one of {list(self.SUPPORTED_EXCHANGES.keys())}")

            # Initialize exchange
            self.exchange = getattr(ccxt, exchange_id)({
                'apiKey': api_key,
                'secret': api_secret,
                'enableRateLimit': True
            })
            
            # Test connection
            self.exchange.load_markets()
            
        except Exception as e:
            raise ConnectionError(f"Failed to initialize exchange: {str(e)}")

    def get_balance(self, symbol: str) -> Decimal:
        try:
            balance = self.exchange.fetch_balance()
            return Decimal(str(balance[symbol]['free']))
        except Exception as e:
            raise ValueError(f"Failed to get balance for {symbol}: {str(e)}")

    def get_ticker(self, symbol: str) -> dict:
        try:
            return self.exchange.fetch_ticker(symbol)
        except Exception as e:
            raise ValueError(f"Failed to get ticker for {symbol}: {str(e)}")

    def create_order(self, symbol: str, order_type: str, side: str, 
                    amount: Decimal, price: Optional[Decimal] = None) -> dict:
        try:
            return self.exchange.create_order(
                symbol=symbol,
                type=order_type,
                side=side,
                amount=float(amount),
                price=float(price) if price else None
            )
        except Exception as e:
            raise ValueError(f"Failed to create order: {str(e)}")

    def get_supported_pairs(self) -> list:
        try:
            markets = self.exchange.load_markets()
            return list(markets.keys())
        except Exception as e:
            raise ValueError(f"Failed to get supported pairs: {str(e)}")