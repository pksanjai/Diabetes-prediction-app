import numpy as np
import pickle
import streamlit as st
import io

# Load the trained model
try:
    loaded_model = pickle.load(open('trained_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please upload 'trained_model.sav' in the app directory.")
    st.stop()

# Prediction function
def diabetes_prediction(input_data):
    input_array = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_array)
    return '🟢 The person is **not diabetic**.' if prediction[0] == 0 else '🔴 The person **is diabetic**.'

# Main UI
def main():
    st.set_page_config(page_title="Diabetes Predictor", layout="wide", page_icon="💉")
    st.title('💉 Diabetes Prediction Web App')
    st.markdown("#### Predict whether a person is diabetic based on medical inputs.")

    st.markdown("---")

    with st.sidebar:
        st.header("📋 User Input Features")
        st.info("Enter the following values:")

        pregnancies = st.text_input('🤰 Number of Pregnancies', '0')
        glucose = st.text_input('🍬 Glucose Level', '100')
        bloodPressure = st.text_input('💓 Blood Pressure (mm Hg)', '70')
        skinThickness = st.text_input('🧬 Skin Thickness (mm)', '20')
        insulin = st.text_input('💉 Insulin Level', '80')
        bmi = st.text_input('⚖️ BMI Value', '25.0')
        dpf = st.text_input('🧪 Diabetes Pedigree Function', '0.5')
        age = st.text_input('🎂 Age', '33')

    # Validate numeric inputs
    inputs = [pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, dpf, age]
    try:
        numeric_inputs = [float(i) for i in inputs]
    except ValueError:
        st.warning("⚠️ Please make sure all fields are filled with valid **numbers**.")
        return

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Predict Diabetes Status"):
            result = diabetes_prediction(numeric_inputs)
            st.success(result)
            st.balloons()

            # Download button for result
            result_text = f"""
📋 Diabetes Prediction Result
-----------------------------
Pregnancies: {pregnancies}
Glucose: {glucose}
Blood Pressure: {bloodPressure}
Skin Thickness: {skinThickness}
Insulin: {insulin}
BMI: {bmi}
Diabetes Pedigree Function: {dpf}
Age: {age}

Result: {result}
            """.strip()

            st.download_button(
                label="📄 Download Your Result",
                data=result_text,
                file_name="diabetes_result.txt",
                mime="text/plain"
            )

    st.markdown("---")
    st.markdown("✅ Developed with Streamlit | [GitHub Repo](https://github.com/pksanjai/Diabetes-prediction-app)")

if __name__ == '__main__':
    main()
