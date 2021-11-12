import os, tempfile, pytest, logging
from App.main import create_app, db

from App.controllers import ( 
    get_all_users_json, 
    create_users, 
    get_user_by_fname ,
    create_user
)

# https://stackoverflow.com/questions/4673373/logging-within-pytest-testshttps://stackoverflow.com/questions/4673373/logging-within-pytest-tests

LOGGER = logging.getLogger(__name__)


# fixetures are used to setup state in the app before the test
# This fixture creates an empty database for the test
@pytest.fixture
def client():
    # this fixture starts up the app, is needed for testing routes
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path})
    db.create_all(app=app)
    yield app.test_client()
    os.close(db_fd)
    os.unlink(db_path)

# This fixture depends on create_users which is tested in test #5 test_create_user
# @pytest.fixture
# def insert_user_data():
#     db_fd, db_path = tempfile.mkstemp()
#     app = create_app({'TESTING': True, 'DATABASE': db_path})
#     db.create_all(app=app)
#     create_users([
#         {
#             'first_name':'Bob',
#             'last_name':'Smith',
#             'email':'bob@mail.com',
#             'password':'bobpass'
#         },
#         {
#             'first_name':'Jame',
#             'last_name':'Smith',
#             'email':'jane@mail.com',
#             'password':'janepass'
#         },
#         {
#             'first_name':'Rick',
#             'last_name':'Smith',
#             'email':'rick@mail.com',
#             'password':'rickpass'
#         }
#     ])
#     yield app.test_client()
#     os.close(db_fd)
#     os.unlink(db_path)

'''
   Unit Tests
'''

# This is a unit test because there are no side effects
# Test 1: Checks if api/lol route returns 'lol'
def test_hello(client):
    response = client.get('/api/lol')
    assert b'lol' in response.data

# Test 2: api/users should return an empty array when there are no users
def test_no_users(client):
    response = client.get('/api/users')
    print(response.status_code)
    assert b'[]' in response.data

# Test 3: /api/users should return a 200 status code
def test_users_status_code(client):
    response = client.get('/api/users')
    assert response.status_code == 200

# Test 4: get_all_users() controller should return an empty array when there are no users
def test_get_all_empty_users(client):
    users = get_all_users_json()
    # user logger to print messages in tests
    LOGGER.info(users)
    assert users == []

# Test 5: /api/users view should return json data of user inserted in insert_user_data fixture
# def test_user_route(insert_user_data):
#     response = insert_user_data.get('/api/users')
#     # this route returns an array of json objects
#     userobj = response.get_json()[0]
#     LOGGER.info(userobj)
#     checks = True
#     if userobj.first_name != user['first_name'] or userobj.last_name != user['last_name'] or userobj.email != user['email'] or not userobj.check_password(user['password']):
#         checks = False
#     assert checks


'''
   Integration Tests  
'''
# This is an integration test because it has side effects in the database
# Test 5: create_user controller should create a user record with the values given to it
def test_create_user():
    create_user('rob', 'smith', 'rob@mail.com', 'bobpass')
    userobj = get_user_by_fname('rob')

    checks = False
    if userobj.first_name != 'rob' or userobj.last_name != 'smith' or userobj.email != 'bob@mail.com' or not userobj.check_password('bobpass'):
        checks = False
    assert checks    


# Test 6: create_users controller should create user objects and store them with the values given to it
# def test_create_users():
#     user_data = [
#         {
#             'first_name':'Bob',
#             'last_name':'Smith',
#             'email':'bob@mail.com',
#             'password':'bobpass'
#         },
#         {
#             'first_name':'Jame',
#             'last_name':'Smith',
#             'email':'jane@mail.com',
#             'password':'janepass'
#         },
#         {
#             'first_name':'Rick',
#             'last_name':'Smith',
#             'email':'rick@mail.com',
#             'password':'rickpass'
#         }
#     ]

#     create_users(user_data)

#     savedusers = []
#     checks = True

#     for user in user_data:
#         userobj = get_user_by_fname(user['first_name'])
#         if userobj.first_name != user['first_name'] or userobj.last_name != user['last_name'] or userobj.email != user['email'] or not userobj.check_password(user['password']):
#             checks = False

#     assert checks    