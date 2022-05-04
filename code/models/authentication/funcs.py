from flask import request
def contains (want, list):
  if want in list :
    return True
  return False

def HandleAuthentication(cur):
  hasPasw = False
  data = request.get_json()
  if contains(",",request.get_data(as_text=True)  ) :
    hasPasw=True
  token = data['auth_token']
  password = ""
        
  if hasPasw :
    password = data['password']
        
  sql = 'SELECT * FROM `authentication` WHERE `authentication`.`Auth_Token` = "'+token+'" AND `authentication`.`password` ="'+password+'"'
  return cur.execute(sql), password