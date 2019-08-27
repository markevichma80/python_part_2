import pytest
from datetime import datetime
from serverdate.controlers import date_control

@pytest.fixture
def initial_action():
   return 'test'
@pytest.fixture
def initial_code():
   return 200

@pytest.fixture
def initial_request(initial_action,initial_code):
   return {
       'action':initial_action,
       'time': datetime.now().timestamp(),       
       'code':initial_code
   }

def test_action_make_response(initial_request,initial_code,initial_action):
   actual_date = date_control(initial_request)
   assert actual_date.get('action') == initial_action
   
def test_code_make_response(initial_request,initial_code,initial_action):
   actual_code = date_control(initial_request)
   assert actual_code.get('code') == initial_code

