import pytest
from datetime import datetime
from protocol import valid_request

@pytest.fixture
def initial_action():
   return 'test'

@pytest.fixture
def initial_time():
   return datetime.now().timestamp()


@pytest.fixture
def initial_request(initial_action,initial_time):
   return {
       'action':initial_action,
       'time': initial_time     
      }

def test_action_valid_requests(initial_request):
   chek = valid_request(initial_request)
   assert chek == True
   
