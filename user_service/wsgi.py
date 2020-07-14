"""WSGI wrapper"""
import sys
print('!!!', sys.path)
from app import app as application

if __name__ == "__main__":
    application.run()
