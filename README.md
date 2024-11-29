# Student Learning Style Prediction App

## Overview
The **Student Learning Style Prediction App** is a web-based tool built using **Streamlit** that predicts a student's learning style (Visual, Auditory, or Kinesthetic) based on their study habits. It uses a **Random Forest Classifier** trained on a synthetic dataset to make predictions. This project is a demonstration of machine learning applications in educational contexts.

---

## Features
- **Input Form**:
  - Time spent watching videos (in minutes).
  - Time spent solving quizzes (in minutes).
  - Test score percentage.
- **Real-Time Predictions**:
  - Predicts one of three learning styles: Visual, Auditory, or Kinesthetic.
- **Interactive UI**:
  - Easy-to-use interface built with Streamlit.

---

## Dataset
The dataset used for training is synthetic and contains the following features:
- `time_video`: Time spent on videos (in minutes).
- `time_quiz`: Time spent on quizzes (in minutes).
- `score`: Test score (percentage).
- `learning_style`: The target variable derived based on conditions:
  - **Visual**: Score > 80% and time spent on videos > 120 minutes.
  - **Auditory**: Score > 60% and time spent on quizzes > 60 minutes.
  - **Kinesthetic**: All other cases.

The dataset is created programmatically using `numpy` and `pandas`.

---

## Installation and Setup
Follow these steps to set up and run the app locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/student-learning-style-app.git
    cd student-learning-style-app
    ```

2. **Install dependencies**:
    Make sure you have Python 3.7+ installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

4. Open the app in your browser (default: `http://localhost:8501`).

---

## How It Works
1. **Input Data**: The user provides values for time spent on videos, quizzes, and test score.
2. **Prediction**: The trained **Random Forest Classifier** uses the input to predict the most likely learning style.
3. **Output**: The app displays the predicted learning style instantly.

---

## Requirements
- Python 3.7 or higher
- Libraries:
  - `streamlit`
  - `pandas`
  - `numpy`
  - `scikit-learn`

Install these dependencies using:
```bash
pip install -r requirements.txt
