import re

import allure
import pytest


class TestRoomTypes:

    @allure.feature("Категории номеров")
    @allure.story("Получение информации о категориях номеров")
    @pytest.mark.parametrize("account_id, address_included", [
        (535, False),
        (535, True),
    ])
    def test_get_roomtypes(self, api_client, account_id, address_included):
        with allure.step("Отправка запроса на получение категорий номеров"):
            rooms = api_client.get_room_types(account_id, address_included)

        with allure.step("Проверка, что список категорий не пуст"):
            assert rooms, "Список категорий пуст"

        for room in rooms:
            with allure.step(f"Проверка RoomType для ID={room.id}"):
                with allure.step("Проверка наличия и корректности поля id"):
                    assert hasattr(room, "id") and room.id > 0, \
                        f"Поле 'id' отсутствует или некорректно"

                with allure.step("Проверка наличия и непустого поля name"):
                    assert hasattr(room, "name") and room.name != "", \
                        f"Поле 'name' отсутствует или пустое"

                with allure.step("Проверка наличия поля description"):
                    assert hasattr(room, "description"), "Поле 'description' отсутствует"

                with allure.step("Проверка данных о вместимости: adults"):
                    assert room.adults >= 0, f"Некорректное значение adults: {room.adults}"

                with allure.step("Проверка данных о вместимости: children"):
                    assert room.children >= 0, f"Некорректное значение children: {room.children}"

                if room.photos is not None:
                    with allure.step("Проверка списка фотографий на корректность"):
                        assert isinstance(room.photos, list) and room.photos, "Фотографии должны быть непустым списком"
                        for photo in room.photos:
                            with allure.step(f"Проверка URL фотографии '{photo.get('url')}'"):
                                url = photo.get("url")
                                assert isinstance(url, str) and url.startswith("http"), \
                                    f"URL фотографии должен быть валидным: {url}"

                with allure.step("Проверка локализации названия на русском"):
                    if room.name_ru != '':
                        assert re.search('[а-яА-ЯёЁ]', room.name_ru), \
                            f"Поле name_ru '{room.name_ru}' не содержит кириллических символов"

                with allure.step("Проверка локализации названия на английском"):
                    if room.name_en != '':
                        assert re.search('[a-zA-Z]', room.name_en), \
                            f"Поле name_en '{room.name_en}' не содержит английских символов"

    @allure.feature("Категории номеров")
    @allure.story("Обработка запроса с невалидными данными")
    @pytest.mark.parametrize("account_id, expected_status", [
        ("Invalid account_id", 500),
        ("", 406),
    ])
    def test_get_roomtypes_invalid(self, api_client, account_id, expected_status):
        response = api_client.get_room_types_raw(account_id)
        assert response.status_code == expected_status, \
            f"Ожидаемый статус {expected_status}, полученный {response.status_code}: {response.text}"


