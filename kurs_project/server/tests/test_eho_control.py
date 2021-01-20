import pytest
from datetime import datetime
from echo.controlers import echo_controlers

@pytest.fixture
def initial_action():
   return 'test'
@pytest.fixture
def initial_code():
   return 200

@pytest.fixture
def initial_data():
   return 'text'

@pytest.fixture
def initial_request(initial_action,initial_code, initial_data):
   return {
       'action':initial_action,
       'time': datetime.now().timestamp(),       
       'code': initial_code,
       'data': initial_data
   }

def test_action_make_response(initial_request,initial_code,initial_action):
   actual_date = echo_controlers(initial_request)
   assert actual_date.get('action') == initial_action
   
def test_code_make_response(initial_request,initial_code,initial_action):
   actual_code = echo_controlers(initial_request)
   assert actual_code.get('code') == initial_code

def test_data_make_response(initial_request,initial_code,initial_data):
   actual_data = echo_controlers(initial_request)
   assert actual_data.get('data') == initial_data
