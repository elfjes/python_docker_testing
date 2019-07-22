import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

pytest_plugins = ["docker_compose"]


@pytest.fixture
def session(function_scoped_containers):
    request_session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    request_session.mount('http://', HTTPAdapter(max_retries=retries))

    service = function_scoped_containers["tests_web_1"].network_info[0]

    api_url = "http://%s:%s/" % (service.hostname, service.host_port)
    assert request_session.get(api_url)
    return request_session, api_url


def test_hello_world(session):
    session, base_url = session
    assert session.get(base_url).text == 'Hello, World!'
