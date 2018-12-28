import time

import pandas as pd
from sklearn.externals import joblib
import numpy as np
from flask import Flask, jsonify, request
import redis
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/predict', methods=['POST'])
def predict():
    count = get_hit_count()

    json_ = request.json
    df = pd.DataFrame(json_, index=[0], columns=columns)
    df = df[columns]

    nan_cols = df.columns[df.isnull().values[0]]
    if nan_cols.any():
        for col in nan_cols:
            if col == 'color':
                df.loc[0, col] = 'white'
                continue
            df.loc[0, col] = filler[col]

    map_ = {'red': 0, 'white': 1}
    df['color'] = df['color'].map(map_)
    df[logs] = df[logs].applymap(np.log)
    df[sqrts] = df[sqrts].applymap(np.sqrt)

    X = df.values.reshape(1, -1)
    X_scaled = scaler.transform(X)

    prediction = np.round(model.predict(X_scaled)).astype(np.int8)[0]
    return jsonify({"prediction": '{}'.format(prediction),
                    "count": "{}".format(count)})


if __name__ == '__main__':
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
               'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
               'pH', 'sulphates', 'alcohol', 'color'
               ]

    logs = ['residual sugar', 'free sulfur dioxide', 'sulphates', 'chlorides', 'fixed acidity',
            'volatile acidity']
    sqrts = ['citric acid']

    filler = {'fixed acidity': 7.0, 'volatile acidity': 0.29,
              'citric acid': 0.31, 'residual sugar': 3.0,
              'chlorides': 0.047, 'free sulfur dioxide': 29.0,
              'total sulfur dioxide': 118.0, 'density': 0.99488,
              'pH': 3.21, 'sulphates': 0.51,
              'alcohol': 10.3, 'quality': 6.0}

    scaler = joblib.load('scaler')
    model = joblib.load('model')

    app.run(port=9999, host="0.0.0.0")
