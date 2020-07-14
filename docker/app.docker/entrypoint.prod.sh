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
cd /app
#uwsgi -s /sockets/user_service.sock --manage-script-name --plugin python3 --mount /user_service=user_service:app
uwsgi --ini /app/user_service/wsgi.ini
