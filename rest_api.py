import pandas as pd
from sklearn.externals import joblib
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    df = pd.DataFrame(json_, index=[0], columns=columns)
    df = df[columns]

    # если есть пропуски в запросе, заполняем медианой
    nan_cols = df.columns[df.isnull().values[0]]
    if nan_cols.any():
        source = pd.read_csv('winequality-white.csv', sep=';')
        for col in nan_cols:
            if col == 'color':
                df.loc[0, col] = 'white'
                continue
            df.loc[0, col] = source[col].median()

    map_ = {'red': 0, 'white': 1}
    df['color'] = df['color'].map(map_)
    df[logs] = df[logs].applymap(np.log)
    df[sqrts] = df[sqrts].applymap(np.sqrt)

    X = df.values.reshape(1, -1)
    X_scaled = scaler.transform(X)

    predict = np.round(model.predict(X_scaled)).astype(np.int8)[0]
    return jsonify({'prediction': '{}'.format(predict)})


if __name__ == '__main__':
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
               'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
               'pH', 'sulphates', 'alcohol', 'color'
               ]

    logs = ['residual sugar', 'free sulfur dioxide', 'sulphates', 'chlorides', 'fixed acidity',
            'volatile acidity']
    sqrts = ['citric acid']

    scaler = joblib.load('scaler')
    model = joblib.load('model')

    dict_pred = {'fixed acidity': 11.2,
                 'volatile acidity': 0.28,
                 'citric acid': 0.56,
                 'residual sugar': 1.9,
                 'chlorides': 0.075,
                 'free sulfur dioxide': 17,
                 'total sulfur dioxide': 60,
                 'density': 0.998,
                 'pH': 3.16,
                 'sulphates': 0.58,
                 'alcohol': 9.8,
                 'color': 'red'
                 }
    app.run(port=9999)
