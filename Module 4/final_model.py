import streamlit as st
import pickle
st.header("Iris Petal Identification")

# Load the saved model from the file
@st.cache
def load_model():
    with open('knn_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

left,right = st.columns(2)
left.markdown("### Lentgh")
right.markdown("### Width")

sepal_l = left.number_input("Sepal",help="Enter value in cm")
petal_l = left.number_input("Petal",help="Enter value in cm")

sepal_w = right.number_input("Sepal",help="Enter value in cm")
petal_w = right.number_input("Petal",help="Enter value in cm")


def predict(model_input,model):
    prediction = model.predict_proba([model_input])
    prediction = [round(i,2) for i in prediction]
    
    return [['setosa', 'versicolor', 'virginica'],
               *prediction]

