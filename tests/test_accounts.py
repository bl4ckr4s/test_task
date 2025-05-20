import allure
import pytest


class TestAccounts:
    @allure.feature("Мета-информация об отеле")
    @allure.story("Получение мета-информации об отеле")
    def test_get_account_info(self, api_client, uid):
        with allure.step("Отправка запроса на получение информации об аккаунте"):
            account = api_client.get_account_info(uid)

        with allure.step("Проверка названия отеля"):
            assert account.name == 'Отель «Вилла Олива» , API', (
                f"Ожидали имя 'Отель «Вилла Олива» , API', полученный '{account.name}'"
            )

        with allure.step("Проверка телефонного номера отеля"):
            assert account.phone == '+799955555', (
                f"Ожидаемый телефон '+799955555', полученный '{account.phone}'"
            )

        with allure.step("Проверка email отеля"):
            assert account.email == 'alena.s@bnovo.ru', (
                f"Ожидаемый email 'alena.s@bnovo.ru', полученный '{account.email}'"
            )

        with allure.step("Проверка адреса отеля"):
            assert account.address == 'Санкт-Петербург, Коломяжский пр-кт, 15, к 2', \
                f"Ожидаемый адрес 'Санкт-Петербург, Коломяжский пр-кт, 15, к 2', полученный '{account.address}'"

        with allure.step("Проверка типа отеля на допустимые значения"):
            assert account.hotel_type in {"hotel", "apartments"}, (
                f"Поле 'hotel_type' имеет недопустимое значение: '{account.hotel_type}'"
            )

    @allure.feature("Мета-информация об отеле")
    @allure.story("Обработка запроса с невалидными данными")
    @pytest.mark.parametrize("uid, expected_status", [
        ("Invalid uid", 404),
        ("", 406),
    ])
    def test_get_account_info_missing_or_invalid_params(self, api_client, uid, expected_status):
        with allure.step(f"Отправка запроса с некорректным uid='{uid}' и ожидание статуса {expected_status}"):
            response = api_client.get_account_info_raw(uid)

        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == expected_status, (
                f"Ожидаемый статус {expected_status}, полученный {response.status_code}: {response.text}"
            )

