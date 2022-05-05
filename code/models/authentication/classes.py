from constants.REST import  constants

class user ():
  token = ""
  password = ""
  endpoint = ""
  def checkUser(t,p,e):
    return user.token == t and user.password == p and user.endpoint == e
  def setUser(inn_token="", inn_password="", inn_endpoint=""):
    user.token = inn_token
    user.password = inn_password
    user.endpoint = inn_endpoint
  def Json():
    if user.password != "":
      return {
      "auth_token":user.token,
      "password":user.password,
      "endpoint":user.endpoint
      }
    else :
      return {
      "auth_token":user.token,
      "endpoint":user.endpoint
      }

