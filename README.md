# Student Learning Style Prediction

This project is designed to predict a student's preferred learning style based on their responses to a set of questions. The application utilizes machine learning techniques to analyze input data and classify students into categories such as visual, auditory, or kinesthetic learners.

## Features
- **User Input**: Collects responses from users via a web interface.
- **Machine Learning Model**: Predicts learning styles based on input data.
- **Interactive Application**: Built using a lightweight framework for ease of use.
- **Customizable**: Easily adaptable to include additional learning styles or parameters.

## Libraries Used
The following libraries are used in this project:

- **Streamlit**: For creating the interactive web application.
- **scikit-learn**: For building and deploying the machine learning model.
- **pandas**: For handling input and structured data.
- **numpy**: For numerical computations.

## Requirements
To run the project, you need the following dependencies:

```bash
flask
scikit-learn
pandas
numpy
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/alphacrypto246/Student-Learning-Style-Prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Student-Learning-Style-Prediction
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```
3. Input the required data and receive the predicted learning style.

## File Structure
- `app.py`: The main script for running the Flask application.
- `model.pkl`: Pre-trained machine learning model for predictions.
- `templates/`: Directory containing HTML templates for the web interface.
- `static/`: Directory for static files like CSS and JavaScript.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## Dataset
The application requires a dataset of student responses and their corresponding learning styles for training and evaluation. The dataset should include:
- Input features (e.g., questionnaire responses).
- Target labels (e.g., visual, auditory, kinesthetic).

## Results
The application provides accurate predictions of learning styles based on user input. It can help educators tailor their teaching strategies to suit individual student needs.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to the developers of the libraries used in this project and the open-source community for providing resources to build machine learning applications.

---

Feel free to raise issues or feature requests via the [Issues](https://github.com/alphacrypto246/Student-Learning-Style-Prediction/issues) tab.
