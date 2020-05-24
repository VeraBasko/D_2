import sentry_sdk
import os
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://615e9144b90f4db3bde501864352c1eb@o397304.ingest.sentry.io/5251658",
    integrations=[BottleIntegration()]
)
app = Bottle()

@app.route('/fail')
def index():
    raise RuntimeError("There is an error!")
    return

@app.route('/success')
def index():
    return

app.run(host='localhost', port=8080)

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)