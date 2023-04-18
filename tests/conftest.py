from typing import Generator

import pytest
from requests_toolbelt.sessions import BaseUrlSession


@pytest.fixture(scope="function")
def session() -> Generator[BaseUrlSession, None, None]:
    session = BaseUrlSession(base_url="https://helloacm.com/api/")
    yield session
