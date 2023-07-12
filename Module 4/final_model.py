import streamlit as st
import pickle
st.header("Iris Petal Identification")

# Load the saved model from the file
@st.cache_data
def load_model():
    with open('knn_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

model = load_model()

left,right = st.columns(2)
left.markdown("### Lentgh")
right.markdown("### Width")

sepal_l = left.number_input("Sepal",help="Enter value in cm",key=1)
petal_l = left.number_input("Petal",help="Enter value in cm",key=2)

sepal_w = right.number_input("Sepal",help="Enter value in cm",key=3)
petal_w = right.number_input("Petal",help="Enter value in cm",key=4)


def predict(model_input,model):
    prediction = model.predict_proba([model_input])
    prediction = [round(i,2) for i in prediction]
    
    st.session_state['output'] =  [['setosa', 'versicolor', 'virginica'],
               *prediction]

st.button("Predict",on_click=predict,args=[[sepal_l,
                                            sepal_w,
                                            petal_l,
                                            petal_w],
                                            model])
if 'output' in st.session_state:
    st.write(st.session_state.output)
