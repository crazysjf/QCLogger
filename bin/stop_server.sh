ps axuww | grep 'uwsgi.*QCLogger' | awk '{print $2}' | xargs kill -9