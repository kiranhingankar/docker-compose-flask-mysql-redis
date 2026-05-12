from flask import Flask
import mysql.connector
import redis
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database=os.environ.get("MYSQL_DB")
        )

        redis_client = redis.Redis(
            host=os.environ.get("REDIS_HOST"),
            port=6379
        )

        redis_client.set("message", "Docker Compose is working!")
        msg = redis_client.get("message").decode("utf-8")

        return f"MySQL + Redis Connected Successfully! Message: {msg}"

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
