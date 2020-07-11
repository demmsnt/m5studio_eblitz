#!/bin/sh
cd /app/user_service
pylint --load-plugins pylint_flask_sqlalchemy *.py
