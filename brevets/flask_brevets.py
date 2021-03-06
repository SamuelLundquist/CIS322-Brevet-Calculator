"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import logging
import os

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')

@app.route("/<filepath>")
def found(filepath):
    if ((".." in filepath) or ("//" in filepath) or ("~" in filepath)):
        return flask.render_template('403.html'), 403
    if os.path.isfile("templates/" + filepath):
        return flask.render_template(filepath), 200
    else:
        return flask.render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

@app.errorhandler(403)
def forbidden_request(error):
    app.logger.debug("Forbidden request")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('403.html'), 403


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    date = request.args.get('dt', type=str)
    brev = request.args.get('bv', type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME: These probably aren't the right open and close times
    # and brevets may be longer than 200km
    open_time = acp_times.open_time(km, brev, date)
    close_time = acp_times.close_time(km, brev, date)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(debug=True, port=CONFIG.PORT, host="0.0.0.0")
