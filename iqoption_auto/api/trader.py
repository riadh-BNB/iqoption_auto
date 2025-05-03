from iqoption_auto.api.client import IQClient


class IQTrader:
    def __init__(self, client: IQClient):
        if not client.is_connected():
            raise Exception("Client must be connected before creating a trader.")
        self.client = client

    def get_balance(self) -> float:
        balance = self.client.connection.get_balance()
        print(f"Current balance: {balance}")
        return balance

    def place_trade(self, asset: str, amount: float, direction: str, duration: int = 1) -> dict:
        print(f"Placing trade: {asset}, {amount}, {direction}, {duration}")
        check, trade_id = self.client.connection.buy(
            amount=amount,
            ACT=asset,
            ACTION=direction,
            expirations_time=duration
        )
        if check:
            print(f"Trade successful, ID: {trade_id}")
            return {"success": True, "trade_id": trade_id}
        else:
            print("Trade failed.")
            return {"success": False, "trade_id": None}
