from flask import Flask
import redis


app = Flask(__name__)

cache = redis.Redis(host="redis", port=6379)


@app.route("/")
def hello_world():
    value = cache.incr("test")
    return f"test={value}"
