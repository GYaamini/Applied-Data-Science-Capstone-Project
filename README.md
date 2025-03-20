---

# **SpaceX Rocket Landing Prediction**

## **Project Overview**
This project aims to predict the likelihood of a successful landing for SpaceX's Falcon 9 rockets. By analyzing factors like launch site, payload, and weather conditions, we use machine learning models to optimize launch costs and improve mission planning.

---

## **Problem Statement**
SpaceX saves millions by reusing rocket stages, but predicting whether the first stage will land successfully is a complex task. This model uses public launch data to predict landing success, ultimately reducing launch costs and enhancing SpaceX's operations.

---
## **Contents**
1. [Data Collection and Wrangling](https://github.com/GYaamini/Applied-Data-Science-Capstone-Project/tree/main/Module1)
2. [Data Visualization](https://github.com/GYaamini/Applied-Data-Science-Capstone-Project/tree/main/Module2)
3. [Interactive Analysis](https://github.com/GYaamini/Applied-Data-Science-Capstone-Project/tree/main/Module3)
4. [Predictive Analysis](https://github.com/GYaamini/Applied-Data-Science-Capstone-Project/tree/main/Module4)

---

## **Data Collection**
Data was gathered from SpaceX’s public API, which includes details about past launches such as payload, launch site, weather conditions, and landing results and through web-scrapping Wikipidea page.

---

## **Data Wrangling**
The dataset was cleaned and preprocessed by handling missing values, encoding categorical features, and extracting relevant features like payload weight and launch date.

---

## **Modeling and Evaluation**
Various models, including **Logistic Regression**, **SVM**, **Decision Tree** and **KNN**, were evaluated using **Grid-Search cross-validation**. The best-performing model achieved **83% accuracy** and **0.89 F1-score**.

---

## **Results & Insights**
**KSC LC 39A** launch site which is situated in the **East coast of Florida at Merritt Island** is the one with most successful launches and it has launched rockets with variable payload from  **2000Kg to 15000Kg heavy payload** with positive success rate.

Rockets launched to **GEO**, **SSO** orbits has the highest success rate however, **ISS** and **SSO** are the ones delivering positive success rate consistently over the years and **VLEO** has joined the lineup in the recent years with promising success.

**FT** and **B4 boosters** are the ones with higher success rate over the variable payload scale and B4 is the only one which has succeeded in the launch with heavy payload.

**Logistic Regression**, **SVM**, and **KNN** proved to be equally the most effective models, with key features like **payload weight**, **launch site**, and **weather conditions** driving predictions. This model can reliably predict whether a rocket’s first stage will land.

---

## **Technologies Used**
- **Python**
- **pandas**, **numpy** (Data Processing)
- **scikit-learn** (Machine Learning)
- **matplotlib**, **seaborn** (Visualization)
- **Plotly, folium** (Interactive Visualizations & Mapping)

---
