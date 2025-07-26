import numpy as np
import pickle
import streamlit as st
from fpdf import FPDF
import tempfile

# Load trained model
try:
    model = pickle.load(open('trained_model.sav', 'rb'))
except FileNotFoundError:
    st.error("❌ Model file not found. Please upload 'trained_model.sav' in the same folder.")
    st.stop()

# Prediction function
def predict_diabetes(data):
    array = np.array(data, dtype=float).reshape(1, -1)
    result = model.predict(array)[0]
    return '🟢 Not Diabetic' if result == 0 else '🔴 Diabetic'

# Generate PDF report
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

# Main Streamlit App
def main():
    st.set_page_config("Diabetes Predictor", page_icon="💉", layout="centered")

    st.markdown("<h1 style='text-align:center;'>💉 Diabetes Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Know your health risk using Machine Learning!</p>", unsafe_allow_html=True)
    st.divider()

    st.image("https://retinalscreenings.com/wp-content/uploads/2021/11/diabetes-awarenss-month-scaled.jpg",  use_container_width=True, caption="Early detection can save lives!")

    st.markdown("### 🔢 Enter Patient Details")

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

    if st.button("🚀 Run Prediction"):
        try:
            input_values = []
            data_dict = {}

            # Validate all fields
            for (label, key) in input_labels:
                val = inputs[key].strip()
                if val == "":
                    raise ValueError("Empty input")
                float_val = float(val)
                input_values.append(float_val)
                data_dict[label] = val

            # Predict
            prediction = predict_diabetes(input_values)
            st.success(f"✅ Prediction: **{prediction}**")

            if "Not" in prediction:
                st.balloons()
            else:
                st.snow()

            # PDF download
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
