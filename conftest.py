import pytest

from api.client import ApiClient

BASE_URL = "https://public-api.reservationsteps.ru"
UID = "d7494710-8c8c-4c4c-bba4-f71caf96fece"

@pytest.fixture(scope="function")
def api_client():
    return ApiClient(BASE_URL)

@pytest.fixture(scope="function")
def uid():
    return UID

