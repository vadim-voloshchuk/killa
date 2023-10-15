import joblib
import xgboost as xgb
from data_collector import collect_all_data
import pandas as pd
from sklearn.preprocessing import LabelEncoder

loaded_model = joblib.load('xgboost_model_reg.pkl')

def get_estimate(locality = 'Таганрог',coords=""):
    if coords:
        city = 'Таганрог'
    else:
        print('mew')
        city = locality
    X = get_normal_dataset(city)
    print(X.info())
    y_pred = loaded_model.predict(X)
    return {"positive objects":X['positive_count'].to_numpy()[0],
    "negative objects":X['negative_count'].to_numpy()[0],
    "criterion 1":X['green_zone'].to_numpy()[0],
    "criterion 2":X['negative_count'].to_numpy()[0],
    "criterion 3":X['max_negative'].to_numpy()[0],
    "criterion 4":X['max_positive'].to_numpy()[0],
    "overall assessment":y_pred[0],
    "recommendations":["Фитнес-клуб","Стадион","Рынок","Велодорожка","Парки"]}

def get_normal_dataset(city):
    raw_data = collect_all_data([city])
    raw_data.drop(columns=['average_distance', 'country', 'region','bad_dist_count', 'city'], inplace=True)
    raw_data.dropna(inplace=True)
    
    label_encoder = LabelEncoder()

    raw_data['max_negative'] = label_encoder.fit_transform(raw_data['max_negative']).astype(int)
    raw_data['max_main'] = label_encoder.fit_transform(raw_data['max_main']).astype(int)
    raw_data['max_positive'] = label_encoder.fit_transform(raw_data['max_positive']).astype(int)
    raw_data['place'] = label_encoder.fit_transform(raw_data['place']).astype(int)
    raw_data['population'] = raw_data['population'].astype(int)
    raw_data['main_city_count'] = raw_data['main_city_count'].astype(int)
    raw_data['negative_count'] = raw_data['negative_count'].astype(int)
    raw_data['positive_count'] = raw_data['positive_count'].astype(int)




    return raw_data

if __name__ == "__main__":
    print(get_estimate('Таганрог'))
