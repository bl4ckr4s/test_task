import allure
import requests
from requests import Response

from api.endpoints import Endpoints
from api.models import AccountMeta, PlanModel, RoomType


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.endpoints = Endpoints()

    def get(self, url: str, params: dict = None) -> Response:
        with allure.step(f"Отправляем GET-запрос {url}, c параметрами: {params}"):
            response = requests.get(url, params=params)
            allure.attach(response.request.url, name="Request URL", attachment_type=allure.attachment_type.URI_LIST)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
            try:
                body = response.json()
                allure.attach(response.text, name="Response JSON", attachment_type=allure.attachment_type.JSON)
            except ValueError:
                allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.TEXT)

        return response

    def get_account_info(self, uid: str) -> AccountMeta:
        url = self.endpoints.get_account_info(self.base_url)
        response = self.get(url, params={"uid": uid})
        assert response.status_code == 200, \
            f"Ожидаемый статус 200, полученный {response.status_code}: {response.text}"

        return AccountMeta(**response.json()["account"])

    def get_account_info_raw(self, uid: str) -> Response:
        url = self.endpoints.get_account_info(self.base_url)
        return self.get(url, params={"uid": uid})

    def get_plans(self, account_id: int) -> list[PlanModel]:
        url = self.endpoints.get_plans(self.base_url)
        response = self.get(url, {"account_id": account_id})
        assert response.status_code == 200, \
                f"Ожидаемый статус 200, полученный {response.status_code}: {response.text}"
        items = response.json().get("plans", [])
        return [PlanModel(**item) for item in items]

    def get_plans_raw(self, account_id) -> Response:
        url = self.endpoints.get_plans(self.base_url)
        return self.get(url, {"account_id": account_id})

    def get_room_types(self, account_id: int, address_included: bool = False) -> list[RoomType]:
        url = self.endpoints.get_room_types(self.base_url)
        response = self.get(url, {"account_id": account_id, "address_included": address_included})

        assert response.status_code == 200, \
                f"Ожидаемый статус 200, полученный {response.status_code}: {response.text}"
        rooms = response.json().get("rooms", [])

        return [RoomType(**room) for room in rooms]

    def get_room_types_raw(self, account_id, address_included: bool = False) -> Response:
        url = self.endpoints.get_room_types(self.base_url)
        return self.get(url, {"account_id": account_id, "address_included": address_included})
