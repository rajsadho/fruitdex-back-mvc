import os, stat, tempfile, pytest, logging, json
from App.main import create_app, init_db

from App.controllers import ( 
    get_all_users_json, 
    create_users, 
    get_user_by_username ,
    create_user
)

# https://stackoverflow.com/questions/4673373/logging-within-pytest-testshttps://stackoverflow.com/questions/4673373/logging-within-pytest-tests

LOGGER = logging.getLogger(__name__)


# fixetures are used to setup state in the app before the test
# This fixture creates an empty database for the test and deletes it after the test
@pytest.fixture
def empty_db():
    
    if not os.path.exists(os.getcwd()+'/App/temp.db'):
        os.umask(0)
        with open(os.open(os.getcwd()+'/App/temp.db', os.O_CREAT | os.O_WRONLY, 0o777), 'w'): pass
    
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///temp.db'})
    init_db(app)
    yield app.test_client()
    LOGGER.info(os.getcwd())
    os.chmod(os.getcwd()+'/App/temp.db', stat.S_IRWXO)
    os.remove(os.getcwd()+'/App/temp.db')

# This fixture depends on create_users which is tested in test #5 test_create_user
@pytest.fixture
def users_in_db():
    
    if not os.path.exists(os.getcwd()+'/App/temp.db'):
        os.umask(0)
        with open(os.open(os.getcwd()+'/App/temp.db', os.O_CREAT | os.O_WRONLY, 0o777), 'w'): pass
    
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
    os.chmod(os.getcwd()+'/App/temp.db', stat.S_IRWXO)
    os.remove(os.getcwd()+'/App/temp.db')

'''
   Unit Tests
'''

# This is a unit test because there are no side effects
# Test 1: Checks if api/lol route returns 'lol'
# def test_root(empty_db):
#     response = empty_db.get('/')
#     LOGGER.info("This thing on?")
#     LOGGER.info(os.getcwd())
#     LOGGER.info(os.path.isfile(os.getcwd()+'/App/temp.db'))
#     assert response.status_code == 200

# Test 2: api/users should return an empty array when there are no users
# def test_no_users(empty_db):
#     response = empty_db.get('/api/users')
#     print(response.status_code)
#     assert b'[]' in response.data

# Test 3: /api/users should return a 200 status code
# def test_users_status_code(empty_db):
#     response = empty_db.get('/api/users')
#     assert response.status_code == 200

# Test 4: get_all_users() controller should return an empty array when there are no users
# def test_get_all_empty_users():
#     users = get_all_users_json()
    # user logger to print messages in tests
    # LOGGER.info(users)
    # assert users == []

# Test 5: /api/users view should return json data of user inserted in insert_user_data fixture
def test_user_route(users_in_db):
    response = users_in_db.get('/api/users')
    # this route returns an array of json objects
    userobj = response.get_json()
    # LOGGER.info(userobj)
    userjson = {
        "users":[
            {
                "email":"bob@mail.com",
                "id":1,     
                "username":"bob"
            },
            {
                "email":"jane@mail.com",
                "id":2,      
                "username":"Jane"
            },
            {
                "email":"rick@mail.com",
                "id":3,       
                "username":"rick"
            }
        ]
    }

    # you can use encode() method instead of b
    assert userjson['users'] == response.json['users']


'''
   Integration Tests  
'''
# This is an integration test because it has side effects in the database
# Test 5: create_user controller should create a user record with the values given to it
# def test_create_user(empty_db):
#     create_user('rob', 'smith', 'rob@mail.com', 'bobpass')
#     userobj = get_user_by_fname('rob')

#     checks = False
#     if userobj.first_name != 'rob' or userobj.last_name != 'smith' or userobj.email != 'bob@mail.com' or not userobj.check_password('bobpass'):
#         checks = False
#     assert checks    


# Test 6: create_users controller should create user objects and store them with the values given to it
# def test_create_users(client):
    # user_data = [
    #     {
    #         'first_name':'Bob',
    #         'last_name':'Smith',
    #         'email':'bob@mail.com',
    #         'password':'bobpass'
    #     },
    #     {
    #         'first_name':'Jame',
    #         'last_name':'Smith',
    #         'email':'jane@mail.com',
    #         'password':'janepass'
    #     },
    #     {
    #         'first_name':'Rick',
    #         'last_name':'Smith',
    #         'email':'rick@mail.com',
    #         'password':'rickpass'
    #     }
    # ]

    # create_users(user_data)

    # savedusers = []
    # checks = True

    # for user in user_data:
    #     userobj = get_user_by_fname(user['first_name'])
    #     if userobj.first_name != user['first_name'] or userobj.last_name != user['last_name'] or userobj.email != user['email'] or not userobj.check_password(user['password']):
    #         checks = False

    # assert checks