# -*- coding: utf-8 -*-

from flask import Flask

import get_main_topics

app = Flask(__name__)

@app.route("/")
def topics():
    labels = get_main_topics.main_topics()
    return labels.head(10).to_json(orient='values')

if __name__ == '__main__':
    app.run(debug=True)