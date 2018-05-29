from flask import Flask, request
from redis import Redis
from datetime import datetime
from datetime import date
import os

# Initialize stuff
app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

# main route /hello/John {GET;PUT}
@app.route('/hello/<username>', methods = ['GET', 'PUT'])
def hello(username=None):
    try:
        if request.method == 'GET':
            dateOfBirth = redis.get(username)
            msg = str.format("Hello {}! You do not exist in our database! Sry..", username)

            if dateOfBirth:
                diff = get_date_diff(dateOfBirth)
                msg = str.format("Hello {}! Your birthday is in {} days", username, diff)
                if diff == 0:
                    msg = str.format("Hello {}! Happy birthday!", username)
            return msg

        elif request.method == 'PUT':
            if request.json:
                dateOfBirth = request.json.get("dateOfBirth")
                if not check_date_format(dateOfBirth):
                    return "Please check date format!", 400
                redis.set(username, dateOfBirth)
                return '', 201
            return "No JSON data received!", 400
    except Exception as e:
        return 'Ahh, Something bad happened..', 500

# Sanitizing date of birth
def check_date_format(dateOfBirth):
    try:
        datetime.strptime(dateOfBirth, '%Y-%m-%d')
        return True
    except ValueError:
        return True

# get the number of days until the next anniversary
def get_date_diff(dateOfBirth):
    try:
        date_now = datetime.now()
        new_user_date = str(date_now.year) + str(dateOfBirth)[6:12]
        new_user_date = datetime.strptime(new_user_date, '%Y-%m-%d')

        if new_user_date < date_now:
            new_user_date = new_user_date.replace(year=new_user_date.year + 1)
            return (new_user_date - date_now).days
        return (new_user_date - date_now).days
    except ValueError:
        return -1

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)