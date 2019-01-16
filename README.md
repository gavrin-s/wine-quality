# wine-quality
1. EDA.ipynb - eda датасета
2. Preprocessing and model selection.ipynb - предобработка датасета и выбор модели
3. work with catboost.ipynb - эксперименты с catboost
4. Evaluation of results.ipynb - оценка результатов и подведение итогов
5. rest_api.py - файл для запуска сервера с api
6. endpoint request.ipynb - тетрадка для endpoint запросов (разрешены пропуски)

Для запуска rest api необходимо запустить rest_api.py (например из консоли python3 rest_api.py). Через тетрадку endpoint request.ipynb выполняются запросы post запросы к серверу.

Для запуска докера нужно выполнить "docker build -t wine ." и затем "docker run -p 9999:9999 wine"

winequality-red.csv, winequality-white.csv - файлы с данными
model, scaler - файл с обученой моделью и "нормализатором".


P.S. Вроде всё работает, но если нет, а считаете что должно, пишите сюда gavrin_s@mail.ru.
