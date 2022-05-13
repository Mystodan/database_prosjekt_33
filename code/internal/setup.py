import sys
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from constants.credentials import Credentials as credentials

class setupInstance ():
  def init(inn):
    return Flask(inn)
  
  def configureApp(app):
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

  def setListener(app, compare):
    if compare == '__main__':
      app.run(debug=True)

  
    
  