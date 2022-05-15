import unittest
import requests
from public_test_body import publictestbody as ptb

class Test_Constants(object):
# Default URL
  URL = "http://127.0.0.1:5000"
# Endpoints 
 # Authentication
  URL_AUTH = URL+"/login"
  
  AUTH_CORRECT = [
    {
      "auth_token":"storekeeper",
      "password":"admin"
    },
    {
      "auth_token":"storekeeper",
      "password":"admin"
    },
    { 
      "auth_token":"customer"
    }              
  ]
  AUTH_INCORRECT = [
    {
      "auth_token":"bababoyy",
      "password":"not a real pass"
    },
    { 
    }              
  ]
  AUTH_CORRECT_BODY = [
  b'Signed in as :storekeeper',
  b'Already signed in as storekeeper',
  b'Signed in as :customer'   
  ]
  AUTH_INCORRECT_BODY = [
  b'Invalid Token or Password',
  b'Invalid request body'   
  ]
  AUTH_CORRECT_CODES = [200,208,200]
  AUTH_INCORRECT_CODES =[406,400]

  # Public
  URL_PUBLIC = URL+"/get_model"
  
 
  PUBLIC_CORRECT = [
    {  
    "model": "active",  
    "length": "152"
    },
    {  
    "model": "active",  
    "length": "142"
    },
    {  
    "model": "active",  
    "length": "143"
    }           
  ]
  PUBLIC_CORRECT_BODY = [
    ptb.PUBLIC["specific1"],
    ptb.PUBLIC["specific2"],
    b'0\n'

  ]


class Test_API(unittest.TestCase):
  
  def testAll(self):
    self.test_authentication()
    self.test_public()
    
  def test_authentication(self):
    count = 0
    want = Test_Constants
    i = 0
    for curr in Test_Constants.AUTH_CORRECT : 
      response = requests.post(want.URL_AUTH, json=curr)
      self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
      self.assertEqual(response.status_code,want.AUTH_CORRECT_CODES[i])
      self.assertEqual(response.content,  (want.AUTH_CORRECT_BODY[i]))
    
      i=i+1
      
    count +=i
    i = 0
    for curr in Test_Constants.AUTH_INCORRECT : 
      response = requests.post(want.URL_AUTH, json=curr)
      self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
      self.assertEqual(response.status_code,want.AUTH_INCORRECT_CODES[i])
      self.assertEqual(response.content,  (want.AUTH_INCORRECT_BODY[i]))
      
      i=i+1
    count +=i
    print("All Authentication tests[",count,"] passed!")

  def test_public(self):
    want = Test_Constants
    i = 0
    count = 0
    for curr in Test_Constants.PUBLIC_CORRECT : 
      response = requests.get(want.URL_PUBLIC, json = curr)
      self.assertEqual(response.headers["Content-Type"],"application/json")
      self.assertEqual(response.status_code,200)
      self.assertEqual(response.content,  (want.PUBLIC_CORRECT_BODY[i]))
      i=i+1
    count +=i
    print("All Public endpoint tests[",count,"] passed!")
    
    
      
      
      
      
      
      
test = Test_API()
test.testAll()

