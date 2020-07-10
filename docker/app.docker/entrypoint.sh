#!/bin/sh
cd /app/user_service
if [ -f "/flags/db_exists.flag" ]
then
	echo "DB alredy exists."
else
	echo "DB NOT exists."
	python ./init_db.py
	touch /flags/db_exists.flag
fi

export FLASK_APP=app.py
flask run -h 0.0.0.0
