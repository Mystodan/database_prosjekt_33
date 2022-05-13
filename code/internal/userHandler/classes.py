import random
from flask_mysqldb import MySQL
from constants.rules import rules
from constants.credentials import Hash
AllUsers = []

class auth_user ():
  """class handler for authenticating user Endpoint
  """
  auth_users = []
  auth_token = ""
  auth_password = ""
  auth_hash = "" 
  def getUser(inn_token, inn_password, inn_endpoint):
    for elem in AllUsers :
      if elem[0].lower() == inn_token.lower() and elem[1].lower() == inn_password.lower()  : 
        return inn_token, inn_password, inn_endpoint
    return False
  def getHash (inn_token, inn_password):
    for elem in AllUsers :
      if elem[0].lower() == inn_token.lower() and elem[1].lower() == inn_password.lower()  : 
        return elem[2]
    return False 
  def encr ():
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    encrypt = ""
    for i in range(0,20) :
      encrypt += symbols[random.randint(0,len(symbols)-1)]
    return encrypt
  
  def defineAuthUser(token, password):
    auth_user.auth_token = token
    auth_user.auth_password = password    
    auth_user.auth_hash = auth_user.encr()
    AllUsers.append(( auth_user.auth_token, auth_user.auth_password,auth_user.auth_hash ))
  def setRandomizer():
    rand = random.randint(1,3)
    if rand == 3:
      random.seed(Hash.KEY_SAUCE1)
    elif rand == 2 :
      random.seed(Hash.KEY_SAUCE2)
    else :
      random.seed(Hash.KEY_SAUCE3)
      

class user ():
  """class handler for local user Endpoint
  """
  token = ""
  password = ""
  endpoint = ""
  def checkUser(t,p,e):
    return user.token == t and user.password == p and user.endpoint == e
  def setUser(inn_token="", inn_password="", inn_endpoint=""):
    if auth_user.getUser(inn_token, inn_password, inn_endpoint) == False :
      return False
    else:
      user.token , user.password, user.endpoint= auth_user.getUser(inn_token, inn_password, inn_endpoint)  
  
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
  
class databaseUser():
  """class handler for database user Endpoint
  """
  sql = MySQL()
  token = ""
  password = ""
  endpoint = ""
  def setUser(inn_token, inn_password, inn_endpoint):
    auth_user.defineAuthUser(inn_token, inn_password)
    if rules.SET_HASH_USER :
      databaseUser.token, databaseUser.password, databaseUser.endpoint  = (auth_user.auth_hash,auth_user.auth_hash, inn_endpoint)
    else :
      databaseUser.token, databaseUser.password, databaseUser.endpoint  = (auth_user.auth_token,auth_user.auth_password, inn_endpoint)
    databaseUser.UploadUserToDataBase(databaseUser.sql)
    
  def UploadUserToDataBase(sql) :
    cur = sql.connection.cursor()  
    cur.execute("INSERT INTO `Authentication` (`Auth_token`, `password`, `Endpoint`) VALUES (%s,%s, %s )",((databaseUser.token,databaseUser.password,databaseUser.endpoint)))
    sql.connection.commit()
    
  def FlushAuth(sql):
    databaseUser.sql = sql
    cur = sql.connection.cursor()  
    cur.execute("DELETE `Authentication`.* FROM `Authentication` ")
    sql.connection.commit()
  
  def DefineAllUsers():
    databaseUser.setUser("Customer_rep","admin","customer_rep")
    databaseUser.setUser("Prod_planner","admin","production_planner")
    databaseUser.setUser("Storekeeper","admin","storekeeper")
    databaseUser.setUser("Public","","public")
    databaseUser.setUser("Transporter","","transporter")
    databaseUser.setUser("Customer","","customer")

