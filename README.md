# LapPricer

```markdown
# LapPricer - Laptop Price Predictor 💻💰

LapPricer is a web application designed to predict the price of laptops based on various features. It utilizes a Random Forest machine learning model to provide an estimated price based on user-inputted laptop configurations.

## Getting Started 🚀

### Prerequisites

Make sure you have the required Python libraries installed. You can install them using the following command:

```bash
pip install streamlit pandas numpy scikit-learn
```

### Running the App

1. Clone the repository:

```bash
git clone <repository-url>
cd LapPricer
```

2. Run the application:

```bash
streamlit run app.py
```

3. Open your browser and go to [http://localhost:8501](http://localhost:8501) to access LapPricer.

## Features

- **Predict Laptop Price**: Input laptop configuration details and get an estimated price using a Random Forest model.
- **User-Friendly Interface**: Simple and intuitive user interface for easy interaction.
- **Feedback System**: Users can provide feedback on the predicted price.

## Model and Data 🧠📊

LapPricer uses a Random Forest machine learning model trained on a dataset containing various laptop configurations. The trained model is stored in `pipe.pkl`, and the dataset is in `df.pkl`.

## Input Details

- **Brand and Laptop Type**: Select the brand and type of the laptop.
- **RAM and Weight**: Choose the RAM size and input the weight of the laptop.
- **Touchscreen and IPS**: Indicate if the laptop has a touchscreen and IPS display.
- **Screen Size and Resolution**: Enter the screen size in inches and select the screen resolution.
- **CPU, HDD, SSD, GPU, OS**: Choose the CPU, HDD, SSD, GPU, and OS for the laptop.

## Predicting Price

After providing the necessary details, click on the "Predict Price" button to get the estimated price. The application will display the predicted price based on the input configuration.

## Feedback

Users can provide feedback on the predicted price by selecting "Yes" or "No" in the satisfaction dropdown. This feedback helps improve the prediction accuracy.

## About the Author 👨‍💻

- **Name:** Md Parwez Ansari
- **College:** IIIT Allahabad
- **Enrollment No:** IIT2021113

## Acknowledgments

- LapPricer makes use of the Streamlit library for creating web applications.
- The machine learning model is implemented using the scikit-learn library and specifically employs the Random Forest algorithm.
- The dataset used for training is included in the repository.

---

**Note:** This web app is created for educational purposes.

```
