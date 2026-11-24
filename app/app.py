"""Small Flask service used by the CI practical work."""

from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def index():
    """Return basic service information."""
    return jsonify(service="devops-ci-app", student="Gabdushov Erlan")


@app.get("/health")
def health():
    """Return the service health status."""
    return jsonify(status="unhealthy")
