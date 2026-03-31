import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

np.random.seed(42)

print("Generating synthetic crop yield dataset...\n")

n_samples = 400

data = {
    'Rainfall_mm': np.random.uniform(400, 1200, n_samples),
    'Avg_Temperature_C': np.random.uniform(22, 35, n_samples),
    'Soil_Fertility_Score': np.random.uniform(4, 9, n_samples),
    'Fertilizer_Used_kg_per_hectare': np.random.uniform(50, 250, n_samples),
    'Pesticide_Used_kg_per_hectare': np.random.uniform(2, 15, n_samples),
    'Irrigation_Hours_per_week': np.random.uniform(5, 25, n_samples),
    'Previous_Year_Yield': np.random.uniform(15, 45, n_samples),
    'Crop_Type_Code': np.random.randint(0, 5, n_samples)
}

df = pd.DataFrame(data)

df['Crop_Yield_quintal_per_hectare'] = (
    0.35 * df['Rainfall_mm'] / 50 +
    0.25 * df['Soil_Fertility_Score'] * 4 +
    0.20 * df['Fertilizer_Used_kg_per_hectare'] / 10 +
    0.10 * df['Irrigation_Hours_per_week'] +
    0.10 * df['Previous_Year_Yield'] -
    0.05 * df['Avg_Temperature_C'] * 0.8 +
    np.random.normal(0, 6, n_samples)
)

df['Crop_Yield_quintal_per_hectare'] = df['Crop_Yield_quintal_per_hectare'].clip(10, 60).round(1)

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe().round(2))

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Feature Correlation Heatmap - Crop Yield Prediction')
plt.tight_layout()
plt.show()

print("\nTraining Machine Learning models...\n")

X = df.drop('Crop_Yield_quintal_per_hectare', axis=1)
y = df['Crop_Yield_quintal_per_hectare']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42, max_depth=6),
    "Random Forest": RandomForestRegressor(n_estimators=150, random_state=42)
}

results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        'Model': name,
        'MAE': round(mae, 2),
        'RMSE': round(rmse, 2),
        'R2 Score': round(r2, 4)
    })

results_df = pd.DataFrame(results)
print("Model Performance Comparison:")
print(results_df.to_string(index=False))

best_model = models["Random Forest"]
print("\nBest performing model selected: Random Forest")

print("\n=== Farmer Prediction Example (Madhya Pradesh Conditions) ===")

new_farm = pd.DataFrame({
    'Rainfall_mm': [850],
    'Avg_Temperature_C': [28.5],
    'Soil_Fertility_Score': [7.2],
    'Fertilizer_Used_kg_per_hectare': [180],
    'Pesticide_Used_kg_per_hectare': [8],
    'Irrigation_Hours_per_week': [18],
    'Previous_Year_Yield': [32],
    'Crop_Type_Code': [1]
})

predicted_yield = best_model.predict(new_farm)[0]

print(f"Predicted Crop Yield: {predicted_yield:.1f} quintals per hectare")

if predicted_yield < 25:
    print("Low yield expected. Consider increasing irrigation or fertilizer application.")
else:
    print("Good yield is expected under the current conditions.")

joblib.dump(best_model, 'crop_yield_predictor.pkl')
print("\nModel saved successfully as 'crop_yield_predictor.pkl'")
print("You can load it anytime with: joblib.load('crop_yield_predictor.pkl')")
