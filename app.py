import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('trained_model.sav','rb'))

def diabetes_prediction(input_data):
    
    input_array = np.asarray(input_data)
    
    input_reshaped = input_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_reshaped)
    print(prediction)
    
    if(prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
def main():
    
    st.title('Diabetes Prediction App')
    
    pregnancies = st.text_input('Number of Pregnancies')
    glucose = st.text_input('Gulcose Level')
    bloodPressure = st.text_input('Blood Pressure Value')
    skinThickness = st.text_input('Skin Thickness Value')
    insulin = st.text_input('Insulin Level')
    bmi = st.text_input('BMI Value')
    diaprdifun = st.text_input('Diabetes Pedigree Function Value')
    age = st.text_input('Age of the Preson')
    
    diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([pregnancies,glucose,bloodPressure,skinThickness,insulin,bmi,diaprdifun,age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
