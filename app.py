from flask import Flask, render_template
import pandas as pd
import joblib
import sklearn.ensemble
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score
from form import PredictForm





model = joblib.load('model.pkl')


data = pd.read_csv('data.csv')

house_type = data['house_type'].unique().tolist()
house_choice = [(x, x) for x in house_type]

city = data['city'].unique().tolist()
city_choice = [(x, x) for x in city]





def predict_price(city, sale_date, months_listed, bedrooms, house_type, area):

    
    input_data = pd.DataFrame({

        'city': [city],
        'sale_date': [sale_date],
        'months_listed': [months_listed],
        'bedrooms': [bedrooms],
        'house_type': [house_type],
        'area': [area]
    })


    predicted_price = model.predict(input_data)

    return predicted_price[0]


app =  Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
@app.route('/', methods=['GET', 'POST'])
def home():
    formatted_price = 0

    form = PredictForm()
    form.house_type.choices = house_choice
    form.city.choices = city_choice

    if form.validate_on_submit():
        city = form.city.data
        sale_date = pd.to_datetime(form.sale_date.data)
        months_listed = float(form.months_listed.data)
        bedrooms = int(form.bedrooms.data)
        house_type = form.house_type.data
        area = form.area.data
        predicted_price = int(predict_price(city, sale_date, months_listed, bedrooms, house_type, area))
        
        
        
        str_price = str(predicted_price)
        if len(str_price) == 5:
           
            formatted_price = f"{str_price[:2]},{str_price[2:]}"
        elif len(str_price) == 6:
           
            formatted_price = f"{str_price[:3]},{str_price[3:]}"
        else:
      
            formatted_price = str_price
     



    return render_template('index.html', predicted_price=formatted_price, form=form)

if "__main__" == __name__:
    app.run(debug=True)