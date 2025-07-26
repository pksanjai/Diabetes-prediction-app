import numpy as np
import pickle
import streamlit as st
from fpdf import FPDF
import tempfile

# Load the trained model
try:
    loaded_model = pickle.load(open('trained_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please upload 'trained_model.sav' in the app directory.")
    st.stop()

# Function to make prediction
def diabetes_prediction(input_data):
    input_array = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_array)
    return '🟢 The person is **not diabetic**.' if prediction[0] == 0 else '🔴 The person **is diabetic**.'

# Function to create PDF result
def generate_pdf(data_dict, result_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="🩺 Diabetes Prediction Result", ln=True, align='C')
    pdf.ln(10)
    for key, value in data_dict.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt=f"Result: {result_text}", ln=True)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name

# Main UI
def main():
    st.set_page_config(page_title="Diabetes Predictor", layout="centered", page_icon="💉")

    st.markdown("<h1 style='text-align: center;'>💉 Diabetes Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enter patient details below to check for diabetes.</p>", unsafe_allow_html=True)
    st.markdown("---")

    labels = [
        '🤰 Number of Pregnancies', '🍬 Glucose Level', '💓 Blood Pressure',
        '🧬 Skin Thickness', '💉 Insulin Level', '⚖️ BMI',
        '🧪 Diabetes Pedigree Function', '🎂 Age'
    ]

    # Center inputs in the page using columns
    col_spacer_left, col_main, col_spacer_right = st.columns([1, 2, 1])
    with col_main:
        inputs = []
        for label in labels:
            inputs.append(st.text_input(label))

        if st.button("🚀 Predict Diabetes Status"):
            try:
                numeric_inputs = [float(i) for i in inputs]
                result = diabetes_prediction(numeric_inputs)
                st.success(result)
                st.balloons()

                # Prepare data for PDF
                clean_labels = [
                    'Pregnancies', 'Glucose', 'Blood Pressure',
                    'Skin Thickness', 'Insulin', 'BMI', 'DPF', 'Age'
                ]
                data_dict = dict(zip(clean_labels, inputs))
                pdf_path = generate_pdf(data_dict, result)

                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📄 Download Result as PDF",
                        data=f,
                        file_name="diabetes_result.pdf",
                        mime="application/pdf"
                    )
            except ValueError:
                st.error("⚠️ Please ensure all fields are filled with **valid numbers**.")

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center;'>✅ Made with ❤️ using Streamlit | "
        "<a href='https://github.com/pksanjai/Diabetes-prediction-app' target='_blank'>GitHub Repo</a></div>",
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
