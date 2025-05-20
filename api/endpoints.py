class Endpoints:
    @staticmethod
    def get_account_info(host: str):
        return f"{host}/v1/api/accounts"

    @staticmethod
    def get_room_types(host: str):
        return f"{host}/v1/api/roomtypes"

    @staticmethod
    def get_plans(host: str):
        return f"{host}/v1/api/plans"
