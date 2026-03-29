# 🌾 Crop Yield Predictor. A Simple Tool to Help Farmers

This is a project that uses machine learning to predict how much a crop will yield. It is based on things that affect farming like how much it rains and the temperature. I built this project using Python and some other tools. It is really useful for places like Madhya Pradesh where farmers can make decisions with the right information.

---

## 📌 What This Project Does

Farmers often have a time guessing how much their crops will yield. This tool looks at things like how much it rains the temperature, the quality of the soil and how much fertilizer is used. Then it uses models to predict what the yield will be. It can also tell if a farm is likely to have a yield and suggest things to do to make it better.

---

## 🗂️ Project Structure

```
crop-yield-predictor/
│
├── crop_yield_predictor.py      # The main script that does everything
├── crop_yield_predictor.pkl     # A saved model that we can use again
├── README.md                    # The file you are reading now
├── STATEMENT.md                 # Why I started this project
└── PROJECT_REPORT.md            # A report on how the project went
```

---

## ⚙️ Setup & Installation

First you need to have Python 3.8 or newer on your computer. Then you need to install some tools:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

To run the project you just need to do:

```bash
python crop_yield_predictor.py
```

This will do a few things:

- Create some fake farm data
- Train a few models to predict yields
- Show how well the models work
- Predict the yield for a farm in Madhya Pradesh
- Save the best model so we can use it again

---

## 🌱 Input Features

Here are the things we look at to predict the yield:

- Rainfall in millimeters
- The average temperature
- How good the soil is
- How much fertilizer is used
- How much pesticide is used
- How many hours of irrigation per week
- What the yield was last year
- What kind of crop it is

We use these to predict the **Crop Yield in quintals per hectare**

---

## 🤖 Models Trained

We trained a few models to see which one works best:

- A linear regression model
- A decision tree model that is easy to understand
- A random forest model that is really good at predicting yields

---

## 📊 Sample Output

Here is how well the models did:

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | 4.xx | 5.xx | 0.xx |
| Decision Tree | 3.xx | 4.xx | 0.xx |
| Random Forest | 2.xx | 3.xx | 0.xx |

```
=== Farmer Prediction Example (Madhya Pradesh) ===
Predicted Crop Yield: 34.2 quintals per hectare
This means the farmer can expect a yield.
```

---

## 💾 Reusing the Saved Model

You can use the saved model like this:

```python
import joblib
import pandas as pd

model = joblib.load('crop_yield_predictor.pkl')

farm = pd.DataFrame({
    'Rainfall_mm': [900],
    'Avg_Temperature_C': [27.0],
    'Soil_Fertility_Score': [7.5],
    'Fertilizer_Used_kg_per_hectare': [200],
    'Pesticide_Used_kg_per_hectare': [9],
    'Irrigation_Hours_per_week': [20],
    'Previous_Year_Yield': [35],
    'Crop_Type_Code': [2]
})

print(model.predict(farm)[0])
```

---

## 📍 Real-World Application

This project is based on farming conditions in Madhya Pradesh. We used numbers for things like rainfall and temperature.

---

## 🔮 Future Improvements

We can make this project by:

- Adding real data from government databases
- Including things like crop diseases and market prices
- Making a simple web page to use the model
- Adding more explanations for the models predictions

---

## 📄 License

This project is, for research purposes only.
