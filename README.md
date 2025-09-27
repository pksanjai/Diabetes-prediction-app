# Diabetes Prediction Web App using Streamlit

A **web-based diabetes prediction application** built using **Python**, **Streamlit**, and **machine learning (Random Forest model)**. The app allows users to enter patient health details and predicts whether the patient is diabetic or not. It also generates a downloadable PDF report.

---

## Project Overview

The Diabetes Prediction App is designed to provide a quick and interactive way to assess diabetes risk based on patient input. It leverages a pre-trained ML model (`trained_model.sav`) to make predictions.

Key features include:

* Predict diabetes using 8 patient health metrics.
* Interactive and user-friendly Streamlit interface.
* Generates a PDF report with patient details and prediction result.
* Visual feedback: balloons for non-diabetic, snow for diabetic.

---

## How It Works

1. **Input Collection**

   * User enters health metrics such as:

     * Number of pregnancies
     * Glucose level
     * Blood pressure
     * Skin thickness
     * Insulin level
     * BMI
     * Diabetes pedigree function
     * Age

2. **Model Prediction**

   * Input is converted into a NumPy array.
   * The pre-trained ML model (Random Forest) predicts diabetic status.
   * Returns either **Diabetic** or **Not Diabetic**.

3. **Output & Visualization**

   * Prediction result displayed on the web page.
   * Fun visual feedback with Streamlit animations.

4. **PDF Report Generation**

   * Uses `FPDF` to generate a professional report.
   * Includes all input details and the prediction.
   * User can download the report as `diabetes_report.pdf`.

---

## Technical Details

* **Language & Libraries:**

  * Python, NumPy, Pickle, Streamlit, FPDF, tempfile
* **Machine Learning:**

  * Random Forest Classifier (pre-trained model saved as `trained_model.sav`)
* **Web Interface:**

  * Streamlit for interactive UI and easy deployment.
* **PDF Generation:**

  * FPDF library to create downloadable reports.

---

## How to Explain in a Technical Interview

1. **Problem Statement**

   * "The goal is to build a web application that predicts diabetes risk using machine learning and provides a downloadable report."

2. **Input & Features**

   * Explain the 8 input metrics and why they are relevant to diabetes prediction.

3. **Machine Learning Model**

   * Pre-trained Random Forest Classifier used for predictions.
   * Input data is converted into the correct shape for model inference.

4. **App Workflow**

   * User enters data -> data is validated -> model predicts -> result is displayed -> PDF report is generated.

5. **Frontend & Interactivity**

   * Built with Streamlit for ease of use.
   * Visual feedback using `balloons()` and `snow()`.
   * Download button allows the user to save a PDF report.

6. **Error Handling**

   * Checks for missing or invalid input and displays warnings.
   * Stops execution if the model file is missing.

7. **Challenges & Learning**

   * Integrating ML model with a web interface.
   * Handling user input validation.
   * PDF report generation dynamically based on input.

8. **Future Enhancements**

   * Add more ML models for comparison.
   * Include graphs in PDF report.
   * Deploy as a cloud application for remote access.

---

This project demonstrates **full-stack ML integration**, **data validation**, **interactive UI**, and **report generation**, all of which are strong points to discuss in technical interviews.
