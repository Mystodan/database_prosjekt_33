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
  AUTH_INCORRECT_CODES =[406,400]

class Test_API(unittest.TestCase):
  TestClear = True
  def test_authentication(self):
    i = 0
    want = Test_Constants

    for curr in Test_Constants.AUTH_CORRECT : 
      response = requests.post(want.URL_AUTH, json=curr)
      self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
      self.assertEqual(response.status_code,200)
      
    for curr in Test_Constants.AUTH_INCORRECT : 
      response = requests.post(want.URL_AUTH, json=curr)
      self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
      self.assertEqual(response.status_code,want.AUTH_INCORRECT_CODES[i])
      i=i+1
    print("All Authentication tests passed!")


    
    
      
      
      
      
      
      
test = Test_API()
test.test_authentication()

