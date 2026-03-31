# Problem Statement

## Project **Crop Yield Prediction Using Machine Learning**

---

## Domain

Agriculture | Predictive Analytics | Rural Technology

---

## Background

Agriculture is very important for Indias economy. It supports half of the people who work and adds a lot to the countrys money.. Many farmers in states like Madhya Pradesh, Uttar Pradesh and Maharashtra make big decisions. They decide what to grow how money to spend and when to harvest. They mostly use their experience and old ways to make these decisions.

The uncertainty of how much crop will grow leads to problems. These problems include spending much money on things needed for farming selling crops at low prices, unstable food supply and in bad cases financial troubles for farming families. As weather patterns change and costs of things needed for farming go up the room for mistakes gets smaller every year.

There is a need for tools that are easy to use and based on data. These tools can help farmers and government officials make decisions before the crop is planted.

---

## Problem Definition

> **Can we make a model that accurately guesses how much crop will grow (in quintals per hectare) using farm inputs that we can measure. So that farmers can plan better and government bodies can give out resources efficiently?**

---

## Objectives

1. Find out which factors affect how much crop grows in an area
2.. Test many models that predict numbers to find the most accurate one
3. Create a tool that can be used again to predict crop growth using farm data
4. Give results. Not just a number, but a suggestion based on how much crop will grow

---

## Scope

This project is about:

* **context:** Parameters are made to reflect conditions typical of central Indian states, especially Madhya Pradesh
* **Crop variety:** Five types of crops are represented via a category variable
* **Synthetic data:** A dataset of 400 records is created with realistic value ranges and a defined formula for crop growth with added noise to simulate real-world variability
* **Models evaluated:** Linear Regression, Decision Tree Regressor and Random Forest Regressor

This project does **not** cover:

* Using real-time satellite or IoT sensor data
* Predicting market prices. Analyzing supply chains
* Detecting diseases or identifying pests

---

## Why This Matters

In Madhya Pradesh, soybean and wheat growth vary a lot depending on irrigation access and soil quality. A tool like this. Even trained on made-up data. Shows a proof of concept that when connected to data could:

* Help state agricultural departments decide where to give subsidies
* Enable banks and cooperatives to make decisions about crop loans
* Give farmers a simple way to check their seasonal plan

---

## Approach

The project follows a standard pipeline for supervised learning:

1. **Data Generation**. Simulate farm data with known relationships between inputs and crop growth
2. **Exploratory Analysis**. Understand how features are connected using a heatmap
3. **Model Training**. Train three regression models on 75% of the data
4. **Evaluation**. Compare models using MAE, RMSE and R² Score on the remaining 25%
5. **Prediction**. Apply the model to a new farm profile and interpret the result
6. **Deployment**. Save the trained model using joblib for future use

---

## Expected Outcome

A trained Random Forest model that can predict crop growth with accuracy along, with a reusable `.pkl` file that can be integrated into a larger agricultural advisory system or web application.
