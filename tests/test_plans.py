import allure
import pytest


class TestPlans:

    @allure.feature("Тарифы")
    @allure.story("Получение информации о тарифах")
    @pytest.mark.parametrize("account_id", [535])
    def test_get_plans(self, api_client, account_id):
        plans = api_client.get_plans(account_id)
        assert plans, "Список тарифов пуст"
        for plan in plans:
            with (allure.step(f"Проверка тарифа с ID={plan.id}")):
                with allure.step("Проверка наличия и корректности поля id"):
                    assert hasattr(plan,"id") and plan.id > 0, \
                        "Поле 'id' отсутствует или содержит некорректное значение"

                with allure.step("Проверка наличия и непустого поля name"):
                    assert hasattr(plan, "name") and plan.name != "", "Поле 'name' отсутствует или пустое"

                with allure.step("Проверка наличия поля description"):
                    assert hasattr(plan, "description"), "Поле 'description' отсутствует"

                with allure.step("Проверка данных о предоплате: сумма неотрицательная"):
                    assert plan.booking_guarantee_sum >= 0, "'booking_guarantee_sum' - сумма отрицательная"

                with allure.step("Проверка данных о предоплате: единица измерения корректна"):
                    assert plan.booking_guarantee_unit in {"percentage", "absolute"}, \
                        f"Поле 'booking_guarantee_unit' имеет некорректное значение: {plan.booking_guarantee_unit}"

                with allure.step("Проверка правил отмены: cancellation_rules корректного типа"):
                    assert hasattr(plan,"cancellation_rules"), \
                        "Поле 'cancellation_rules' отсутствует"

                with allure.step("Проверка правил отмены: срок отмены не пуст"):
                    assert plan.cancellation_deadline != "", \
                        "Поле 'cancellation_deadline' отсутствует или пустое"

    @allure.feature("Тарифы")
    @allure.story("Обработка запроса с невалидными данными")
    @pytest.mark.parametrize("account_id, expected_status", [
        ("Invalid account_id", 500),
        ("", 406),
    ])
    def test_get_plans_invalid(self, api_client, account_id, expected_status):
        response = api_client.get_plans_raw(account_id)
        assert response.status_code == expected_status, \
                        f"Ожидаемый статус {expected_status}, полученный {response.status_code}: {response.text}"




