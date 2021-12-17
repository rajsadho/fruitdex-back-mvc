import os, tempfile, pytest, logging
from App.main import create_app, init_db

from App.controllers import (
    create_users
)

# https://stackoverflow.com/questions/4673373/logging-within-pytest-testshttps://stackoverflow.com/questions/4673373/logging-within-pytest-tests

LOGGER = logging.getLogger(__name__)


# fixetures are used to setup state in the app before the test
# This fixture creates an empty database for the test and deletes it after the test
@pytest.fixture
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///temp.db'})
    init_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/temp.db')

# This fixture depends on create_users which is tested in test #5 test_create_user
@pytest.fixture
def users_in_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///temp.db'})
    init_db(app)
    create_users([
        {
            'username':'bob',
            'email':'bob@mail.com',
            'password':'bobpass'
        },
        {
            'username':'Jane',
            'email':'jane@mail.com',
            'password':'janepass'
        },
        {
            'username':'rick',
            'email':'rick@mail.com',
            'password':'rickpass'
        }
    ])
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/temp.db')