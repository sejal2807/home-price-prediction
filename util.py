import json
import pickle
import numpy as np

def get_location_names():
    with open ("artifacts/columns.json",'r') as f:
        data_columns = json.load(f)['data_columns']
        global len_of_columns
        len_of_columns = len(data_columns)
        data_columns = data_columns[3:]
    return data_columns

def load_save_artifacts():
    model_pickle = "artifacts/banglore_home_prices_model.pickle"
    with open(model_pickle, 'rb') as f:
        model=pickle.load(f)
    return model

def get_estimated_price(location,sqft,bhk,bath):
    model = load_save_artifacts()
    try:
        loc_index = get_location_names().index(location.lower())
    except:
        loc_index=-1
    x =np.zeros(len_of_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]




if __name__ == "__main__":
    data_columns = get_location_names()

    print(data_columns)
    print(get_estimated_price('1st phase jp nagar', 1000, 2, 2))