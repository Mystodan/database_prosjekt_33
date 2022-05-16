from flask import Flask
from constants.credentials import Credentials as credentials
from constants.REST import error
from internal.userHandler.classes import databaseUser
class setupInstance ():
  def init(inn):
    return Flask(inn)
  
  def configureApp(app , credentials):
    """Configures Flask with current Credentials

    Args:
        app (Flask): current Flask application

    Returns:
        app(Flask): configured Flask application
    """
    app.config['MYSQL_HOST']= credentials.DB_HOST
    app.config['MYSQL_USER']= credentials.DB_USER
    app.config['MYSQL_PASSWORD']= credentials.DB_PASSWORD
    app.config['MYSQL_DB']= credentials.DB_NAME
    return app
  
  def checkAndPreprocessConnection(app,sql):
    try: # Checks for database connection and handles previous values
      with app.app_context():
        print(error.DataBase_Found)
        databaseUser    .FlushAuth(sql)     # removes any leftover user if any
        databaseUser    .DefineAllUsers()   # Adds all users
    except: # No database found
      print(error.No_DataBase_Found)
      exit()

  def setListener(app, compare):
    if compare == '__main__':
      app.run(debug=True)

  
    
  