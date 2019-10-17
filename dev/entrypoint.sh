#!/bin/bash

MPY_FP="$ENV_PYTHON_BIN manage.py"

while [ "true" ]; do
    if [[ $DEBUG == "1" ]]; then
        echo "Developer mode"
        echo "$MPY_FP runserver 0.0.0.0:8000"
    else
        echo "Production mode"
        $MPY_FP migrate && $ENV_BIN_ROOT/gunicorn $2.wsgi:application --name $2 --workers 2 --bind=0.0.0.0:8000 --reload --log-level=debug --log-file=-
    fi
    /bin/sleep 10
done
