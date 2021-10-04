"""
This python app takes the current Moscow time and
displays it on the browser window.
"""

from datetime import datetime

import pytz
from flask import Flask

simple_app = Flask(__name__)


@simple_app.route("/")
def home():
    """
    using pytz to take the Moscow current time
    and saving it at variable "time_zone"

    :return:
        returns html page with the current moscow time
    """
    time_zone = pytz.timezone("Europe/Moscow")
    # formatting taken time to HH:MM:SS
    moscow_now = datetime.now(time_zone).strftime("%H:%M:%S")
    with open("my-visits.txt", "a") as file:
        file.write('\n'+moscow_now)
    return """<h1 style='text-align:center'>Moscow Time</h1>
    <h1 style='text-align:center'>{}</h1>""".format(
        str(moscow_now)
    )


if __name__ == "__main__":
    simple_app.run(host = "0.0.0.0")
