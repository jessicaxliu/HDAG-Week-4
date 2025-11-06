import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


st.title("HDAG Week 4 HW: Housing for Tina")
st.write("Hi there! Have you ever been interested in housing data? You're in the right place.")

st.header("Housing Prices and Year Built")
st.write("Average price of houses built in rural, suburban, and urban areas, year built starting in 1950.")
df = pd.read_csv("Affordable_Housing_by_Town_2011-2022_copy.csv", encoding='latin1')
df2 = pd.read_csv("housing_price_dataset_copy.csv", encoding = "latin1")
neighborhood_year_prices = df2.groupby(['YearBuilt', 'Neighborhood'])['Price'].mean().unstack()
st.line_chart(neighborhood_year_prices)

st.write("As you can see, prices fluctuate from year to year but don't follow a consistent trend.")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

variables = ['SquareFeet', 'Bathrooms', 'Bedrooms']
house_train, house_test = train_test_split(df2, test_size=0.2, random_state = 2025)
x_train, x_test = house_train[variables], house_test[variables]
y_train, y_test = house_train['Price'], house_test['Price']

multi_linreg = LinearRegression().fit(x_train, y_train)
coefficients = pd.DataFrame(zip(multi_linreg.feature_names_in_, multi_linreg.coef_), columns=['Variable', 'Coefficient'])
multi_r2_train = multi_linreg.score(x_train, y_train)
multi_r2_test = multi_linreg.score(x_test, y_test)
multi_mse_train = mean_squared_error(multi_linreg.predict(x_train), y_train)
multi_mse_test = mean_squared_error(multi_linreg.predict(x_test), y_test)

pd.DataFrame(zip([multi_r2_train],
                 [multi_r2_test],
                 [multi_mse_train],
                 [multi_mse_test]),
             columns=['Train R2', 'Test R2', 'Train MSE', 'Test MSE'],
             index=['multi'])

st.header("Distribution of Home Characteristics")
st.write("Understand the distribution of square feet and price in the housing price dataset.")

fig, ax = plt.subplots()
ax.hist(df2['Price'], bins=50, color = '#ad9aefff', edgecolor = '#4d217aff')
ax.set_xlabel('Price')
ax.set_ylabel('Frequency')
ax.set_title('Frequency Distribution of House Prices')
st.pyplot(fig)
st.write("House prices follow a normal distribution!")

fig, ax = plt.subplots()
ax.hist(df2['SquareFeet'], bins=50, color = '#b3c3ceff', edgecolor = '#374957ff')
ax.set_xlabel('Square Feet')
ax.set_ylabel('Frequency')
ax.set_xlim(500, 3500)
ax.set_title('Frequency Distribution of Square Feet')
st.pyplot(fig)
st.write("House size follows a uniform distribution!")

st.header("Predict the Price of A House")
st.write("You can predict the price of a house using a multivariable linear regression model that takes in three factors: size, number of bedrooms, and number of bathrooms.")
st.write("**Instructions**: input your desired characteristics, using sliders as needed.")


sqfeet = st.number_input("Number of Square Feet:", 750)

bathrooms = st.slider("Number of Bathrooms", 1, 5, 1)

bedrooms = st.slider("Number of Bedrooms:", 2, 5, 1)

bathrooms = int(bathrooms)
bedrooms = int(bedrooms)


calcPrice = multi_linreg.intercept_ + coefficients['Coefficient'][0] * sqfeet + coefficients['Coefficient'][1] * bathrooms + coefficients['Coefficient'][2] * bedrooms

# Display user inputs dynamically
st.write(f"Your estimated house price is: **${calcPrice:.2f}**.")

