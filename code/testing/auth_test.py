import unittest
import requests


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



class Test_API(unittest.TestCase):
  TestClear = True
  def testAll(self):
    Test_API.test_authentication(self)
    
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


    
    
      
      
      
      
      
      
test = Test_API()
test.testAll()

