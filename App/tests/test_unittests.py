import os, tempfile, pytest, logging
from App.main import create_app, init_db

LOGGER = logging.getLogger(__name__)

from App.controllers import ( 
    get_all_users_json, 
    create_users, 
    get_user_by_username ,
    create_user
)

from App.tests.fixtures import (
    empty_db,
    users_in_db
)

'''
   Unit Tests
'''

# This is a unit test because there are no side effects
# Test 1: Checks if api/lol route returns 'lol'
def test_root(empty_db):
    response = empty_db.get('/')
    assert response.status_code == 200

# Test 2: api/users should return an empty array when there are no users
def test_no_users(empty_db):
    response = empty_db.get('/api/users')
    print(response.status_code)
    assert b'[]' in response.data

# Test 3: /api/users should return a 200 status code
def test_users_status_code(empty_db):
    response = empty_db.get('/api/users')
    assert response.status_code == 200

# Test 4: get_all_users() controller should return an empty array when there are no users
def test_get_all_empty_users():
    users = get_all_users_json()
    # user logger to print messages in tests
    # LOGGER.info(users)
    assert users == []

# Test 5: /api/users view should return json data of user inserted in insert_user_data fixture
def test_user_route(users_in_db):
    response = users_in_db.get('/api/users')
    # this route returns an array of json objects
    userobj = response.get_json()[0]
    # LOGGER.info(userobj)
    userjson = """[
        {
            email: "bob@mail.com",
            first_name: "Bob",
            id: 1,
            last_name: "Smith"
        },
        {
            email: "jane@mail.com",
            first_name: "Jame",
            id: 2,
            last_name: "Smith"
        },
        {
            email: "rick@mail.com",
            first_name: "Rick",
            id: 3,
            last_name: "Smith"
        }
    ]"""

    # you can use encode() method instead of b
    assert userjson.endcode() in response.data

