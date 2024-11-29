import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Function to create a synthetic dataset
def create_synthetic_data():
    np.random.seed(42)
    num_samples = 200
    time_video = np.random.randint(30, 180, size=num_samples)  # time spent on videos (minutes)
    time_quiz = np.random.randint(10, 120, size=num_samples)  # time spent on quizzes (minutes)
    score = np.random.randint(50, 100, size=num_samples)  # test score

    # Define learning styles based on certain conditions
    learning_styles = []
    for i in range(num_samples):
        if score[i] > 80 and time_video[i] > 120:
            learning_styles.append('Visual')
        elif score[i] > 60 and time_quiz[i] > 60:
            learning_styles.append('Auditory')
        else:
            learning_styles.append('Kinesthetic')

    # Create DataFrame
    data = pd.DataFrame({
        'time_video': time_video,
        'time_quiz': time_quiz,
        'score': score,
        'learning_style': learning_styles
    })

    return data
# Load the synthetic dataset
data = create_synthetic_data()

# Split dataset into features and target variable
X = data[['time_video', 'time_quiz', 'score']]
y = data['learning_style']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Streamlit app UI
st.title("Student Learning Style Prediction")
st.write("This app predicts a student's learning style (Visual, Auditory, Kinesthetic) based on their study behavior.")

# Input fields for user to enter data
time_video = st.number_input("Time spent on videos (minutes)", min_value=0, max_value=500, value=120)
time_quiz = st.number_input("Time spent on quizzes (minutes)", min_value=0, max_value=500, value=30)
score = st.number_input("Score (%)", min_value=0, max_value=100, value=85)

# Button to predict learning style
if st.button("Predict Learning Style"):
    # Predict using the trained model
    prediction = model.predict([[time_video, time_quiz, score]])
    
    # Display the prediction
    st.write(f"The predicted learning style is: **{prediction[0]}**")

