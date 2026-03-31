# Crop Yield Prediction Using Machine Learning: A Practical Tool for Farmers

## Crop Yield Predictor – A Simple Tool to Help Farmers

I come from a place where farming is not just an occupation — it is survival. In Madhya Pradesh, I have watched farmers wake up before sunrise, tend to their fields all day, and still go to sleep unsure whether the season will treat them well. They rely on experience, intuition, and a lot of hope. I always felt that was unfair.

So I built this. Not a fancy app, not something that requires a computer science degree — just a straightforward Python program that takes a few details about a farm and tells you, as clearly as possible, how much yield you can expect. If something looks off, it tells you that too.

It is my way of trying to put useful technology in the hands of the people who actually need it.

---

## What This Project Does

I want to be honest about what this tool is and what it is not. It does not connect to satellites or pull live weather data. What it does is take eight simple inputs about farming conditions and use machine learning to estimate how much a crop is likely to yield — in quintals per hectare.

Here is what happens when you run it:

1. It generates a dataset of 400 farm records based on realistic conditions in Madhya Pradesh — rainfall, temperature, soil quality, and so on.
2. It trains three different models on that data: Linear Regression, Decision Tree, and Random Forest.
3. It compares all three and picks the one that performs best — which turns out to be Random Forest almost every time.
4. It then runs a real prediction for a sample farmer in Madhya Pradesh and tells you the expected yield.
5. If that yield is below 25 quintals per hectare, the tool flags it and nudges you to look at things like irrigation or fertilizer use.

It is not magic. But it is a genuine, data-backed estimate — and that alone can help a farmer make a smarter call.

---

## Project Structure

```
crop-yield-predictor/
│
├── crop_yield_predictor.py   # Main program — run this
├── crop_yield_predictor.pkl  # The trained model, saved and ready to use
├── README.md                 # Documentation
├── STATEMENT.md              # Motivation
└── PROJECT_REPORT.md         # Report on project
```

---

## Setup & Installation

Nothing complicated here. You need Python 3.8 or above. Once you have that, open your terminal and install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

Then just run the main file:

```bash
python crop_yield_predictor.py
```

The program takes care of everything from there. It will create the farm data, train the models, print out how each model performed, make a yield prediction for a Madhya Pradesh farm, and save the best model to your folder — all in one go. You do not need to configure anything or touch any settings.

---

## Input Features

These are the eight things the model considers when making a prediction. I chose these because they are the factors that actually matter most in real farming — not abstract variables, but things a farmer deals with every single season.

- **Rainfall (mm)** — Total rainfall the farm received
- **Average Temperature (C)** — Seasonal average temperature
- **Soil Fertility Score** — Rated from 4 to 9 based on soil health
- **Fertilizer Used (kg per hectare)** — How much fertilizer went into the soil
- **Pesticide Used (kg per hectare)** — Pesticide quantity applied
- **Irrigation Hours per Week** — How many hours per week the crops were watered
- **Previous Year's Yield** — What the farm produced last season — this one matters more than people expect
- **Crop Type** — Different crops respond differently, so this is encoded as a number from 0 to 4

**Target:** Crop yield in quintals per hectare

---

## Models Trained

I did not want to build something that just works on paper. So instead of picking one model and hoping for the best, I trained all three and compared them honestly.

| Model             | MAE  | RMSE | R² Score |
|-------------------|------|------|----------|
| Linear Regression | 4.xx | 5.xx | 0.xx     |
| Decision Tree     | 3.xx | 4.xx | 0.xx     |
| Random Forest     | 2.xx | 3.xx | 0.xx     |

Random Forest consistently comes out ahead. It does not assume that everything has a neat linear relationship — because in farming, it rarely does. Soil quality, rainfall, and temperature interact in messy ways, and Random Forest handles that much better than the other two.

---

## Sample Output

When you run the program for a typical Madhya Pradesh farm, here is what you will see:

**Farmer Prediction Example (Madhya Pradesh):**

```
Predicted Crop Yield: 34.2 quintals per hectare
Good yield is expected under the current conditions.
```

And if conditions look unfavorable and the prediction drops below 25 quintals, the program does not just go quiet — it tells you to look into your irrigation schedule or fertilizer application. Small changes at the right time can make a real difference.

---

## Reusing the Saved Model

After the program runs once, the trained model gets saved as a `.pkl` file. You do not have to retrain it every time. Just load it up and feed in your farm's numbers directly:

```python
import joblib, pandas as pd

# Load the pre-trained model
model = joblib.load('crop_yield_predictor.pkl')

# Enter your farm's details
farm = pd.DataFrame({
    'Rainfall_mm': [850],
    'Avg_Temperature_C': [28.5],
    'Soil_Fertility_Score': [7.2],
    'Fertilizer_Used_kg_per_hectare': [180],
    'Pesticide_Used_kg_per_hectare': [8],
    'Irrigation_Hours_per_week': [18],
    'Previous_Year_Yield': [32],
    'Crop_Type_Code': [1]
})

# Get the predicted yield
print(model.predict(farm)[0])
```

Just swap in the actual numbers from your farm and it will give you a prediction within seconds.

---

## Real-World Application

Every number in this project — the rainfall range, the temperature values, the soil scores — was chosen to reflect conditions that are realistic for Madhya Pradesh. This is not a generic global model. It was built with a specific place and specific people in mind.

That said, the underlying structure is flexible. If you have agricultural data from another region, you can swap it in and the model will learn from that instead. The code does not care where the data comes from — it just needs honest inputs.

---

## Future Improvements

I know this is not a finished product. There is a lot more I want to do with it when time and resources allow:

- Bring in real data from government agricultural records instead of using synthetic samples
- Add crop disease patterns and pest data, because those can wipe out a season no matter how good everything else looks
- Pull in market price trends so the prediction is not just about yield but about whether that yield is actually worth something
- Build a simple web interface — because asking farmers to run Python scripts is not realistic
- Add proper model explanations so a farmer understands not just the number but what is driving it

---

*This project started as a college assignment. But the problem it tries to solve is real, and the people it is meant for are real. I hope it becomes something genuinely useful someday.*
