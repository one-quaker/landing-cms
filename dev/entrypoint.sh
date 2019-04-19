#!/bin/bash

MPY_FP="$ENV_PYTHON_BIN manage.py"

while [ "true" ]; do
    /bin/sleep 1
    if [[ $1 == "gunicorn" ]]; then
        $MPY_FP migrate && $ENV_BIN_ROOT/gunicorn $2.wsgi:application --name $2 --workers 2 --bind=0.0.0.0:8000 --reload --log-level=debug --log-file=-
    elif [[ $1 == "dev" ]]; then
        $MPY_FP runserver 0.0.0.0:8000
    else
        /bin/sleep 5; echo "Entrypoint is empty"
    fi
done
