 from flask import Flask
 from redis import Redis

# app =Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1> Hello Docker! </h1>'
# if __name__ == '__main__':
#     app.run(debug=True)



@app = Flask(__name__)
redis_client = Redis(host="redis_service", port=6379)


@app.route('/')
def index():
    return '<h1> Hello, Docker! </h1>'
    hits = redis_client.incr('hits')
    return f'<h1> Hello, Docker! </h1><br> This page called {hits} times'

if __name__ == '__main__':
    app.run(debug=True)
