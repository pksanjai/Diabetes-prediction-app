import numpy as np
import pickle
import streamlit as st
from fpdf import FPDF
import tempfile

# Load model
try:
    model = pickle.load(open('trained_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please upload 'trained_model.sav' to the same folder.")
    st.stop()

# Prediction function
def predict_diabetes(data):
    array = np.array(data, dtype=float).reshape(1, -1)
    result = model.predict(array)[0]
    return '🟢 Not Diabetic' if result == 0 else '🔴 Diabetic'

# PDF generator
def create_pdf(details, prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="🩺 Diabetes Test Report", ln=True, align='C')
    pdf.ln(10)
    for k, v in details.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt=f"Prediction Result: {prediction}", ln=True)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp.name)
    return tmp.name

# UI Setup
def main():
    st.set_page_config("Diabetes Predictor", page_icon="💉", layout="centered")

    # Light/dark mode styling
    st.markdown("""
        <style>
            h1, h2, h3, h4, p {
                text-align: center !important;
            }
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                max-width: 700px;
                margin: auto;
            }
            .stTextInput>div>div>input {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>💉 Diabetes Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<p>Know your health risk using machine learning!</p>", unsafe_allow_html=True)
    st.divider()

    st.image("https://cdn.pixabay.com/photo/2017/08/06/11/45/blood-2595152_960_720.jpg",
             use_container_width=True, caption="🩸 Early detection can save lives!")

    st.markdown("### 🔢 Enter Patient Details Below")

    # Input fields
    input_labels = [
        ("🤰 Number of Pregnancies", "preg"),
        ("🍬 Glucose Level", "glucose"),
        ("💓 Blood Pressure", "bp"),
        ("🧬 Skin Thickness", "skin"),
        ("💉 Insulin Level", "insulin"),
        ("⚖️ BMI (Body Mass Index)", "bmi"),
        ("🧪 Diabetes Pedigree Function", "dpf"),
        ("🎂 Age", "age"),
    ]

    inputs = {}
    for label, key in input_labels:
        inputs[key] = st.text_input(label)

    # Prediction
if st.button("🚀 Run Prediction"):
    try:
        input_values = []
        data_dict = {}

        # Sanitize and validate inputs
        for (label, key) in input_labels:
            val = inputs[key].strip()
            if val == "":
                raise ValueError("Empty input")
            float_val = float(val)
            input_values.append(float_val)
            data_dict[label] = val

        # Run prediction
        prediction = predict_diabetes(input_values)
        st.success(f"✅ Prediction: **{prediction}**")

        # Celebration animation
        st.balloons() if "Not" in prediction else st.snow()

        # Create and show PDF download button
        pdf_file = create_pdf(data_dict, prediction)
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📄 Download Report (PDF)",
                data=f,
                file_name="diabetes_report.pdf",
                mime="application/pdf"
            )

    except ValueError:
        st.warning("⚠️ Please fill all fields with valid numbers.")

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center;'>Built with ❤️ using Streamlit | "
        "<a href='https://github.com/pksanjai/Diabetes-prediction-app' target='_blank'>GitHub Repo</a></div>",
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
