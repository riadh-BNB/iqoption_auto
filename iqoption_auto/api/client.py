from iqoptionapi.stable_api import IQ_Option


class IQClient:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.connection = None

    def connect(self) -> bool:
        try:
            self.connection = IQ_Option(self.email, self.password)
            self.connection.connect()
            if self.connection.check_connect():
                print("Connected to IQ Option successfully.")
                return True
            else:
                print("Failed to connect to IQ Option.")
                return False
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def is_connected(self) -> bool:
        return self.connection is not None and self.connection.check_connect()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from IQ Option.")
