import pytest
from sqlbag import temporary_database
from testcontainers.postgres import PostgresContainer
from sqlbag import S, create_database
import random
import string

pg_container = PostgresContainer("postgres:14.1")

def pytest_sessionstart(session):
    pg_container.start()
    with S(pg_container.get_connection_url()) as s:
        s.execute('create role postgres;')

def pytest_sessionfinish(session, exitstatus):
    if pg_container.get_wrapped_container():
        pg_container.stop()

@pytest.fixture()
def db():
    db_url = pg_container.get_connection_url()
    parts = db_url.rsplit('/', 1)
    random_letters = [random.choice(string.ascii_lowercase) for _ in range(10)]
    random_letters = "".join(random_letters)
    db_url = parts[0] + '/' + random_letters

    create_database(db_url)
    return db_url


def pytest_addoption(parser):
    parser.addoption(
        "--timescale", action="store_true", help="Test with Timescale extension"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "timescale: mark timescale specific tests")


def pytest_collection_modifyitems(config, items):
    skip_timescale = pytest.mark.skip(reason="need --timescale option to run")
    if not config.getoption("--timescale", default=False):
        # no option given in cli: skip the timescale tests
        for item in items:
            if "timescale" in item.keywords:
                item.add_marker(skip_timescale)
