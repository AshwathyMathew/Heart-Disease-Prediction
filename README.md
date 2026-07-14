Heart Disease Prediction Using Machine Learning

Abstract

Heart disease is one of the leading causes of death worldwide, making early diagnosis and timely treatment essential for improving patient outcomes. However, identifying heart disease based on multiple clinical factors can be challenging, as symptoms often vary among individuals and may not always be recognized at an early stage. With the increasing availability of healthcare data, machine learning techniques provide an effective approach for analyzing patient information and assisting medical professionals in predicting the likelihood of heart disease more accurately and efficiently.

The motivation behind this project is to develop an intelligent heart disease prediction system that can support healthcare professionals by providing accurate and timely predictions based on patient medical data. Such a system can help identify individuals who are at a higher risk of developing heart disease, enabling early medical intervention and better treatment planning. By comparing the performance of multiple machine learning algorithms, the project aims to determine the most suitable model for heart disease prediction.

This project proposes a machine learning-based heart disease prediction system using five classification algorithms: K-Nearest Neighbors (KNN), Naïve Bayes, Decision Tree, Random Forest, and Support Vector Machine (SVM). The dataset undergoes preprocessing to handle missing values, prepare the data, and improve model performance before being divided into training and testing datasets. Each algorithm is trained and evaluated using classification accuracy as the primary performance metric. The experimental results show that Random Forest achieved the highest prediction accuracy of 85.25%, followed by Naïve Bayes with 83.61%, SVM with 78.69%, Decision Tree with 73.77%, and KNN with 65.57%. These results indicate that the Random Forest algorithm provides the most reliable performance for predicting heart disease among the evaluated models.

The main objectives of this project are to develop an automated heart disease prediction system using machine learning techniques, compare the performance of multiple classification algorithms, identify the most accurate model for disease prediction, and demonstrate the effectiveness of machine learning in supporting healthcare decision-making. The proposed system can serve as a valuable decision-support tool for medical professionals by providing reliable predictions that contribute to early diagnosis, improved patient care, and better clinical outcomes.


# Module Description

### Module 1: Dataset Import

Imports the heart disease dataset containing patient medical information and the corresponding disease status.

### Module 2: Data Preprocessing

Cleans the dataset by handling missing values, removing unnecessary data, and preparing the medical features for analysis.

### Module 3: Feature Selection

Selects important health-related attributes such as age, blood pressure, cholesterol, heart rate, chest pain type, and other clinical factors.

### Module 4: Train-Test Split

Divides the dataset into training and testing sets. The training data is used to build the models, while the testing data is used to evaluate their performance.

### Module 5: Machine Learning Model Development

Develops five machine learning classification models:

* K-Nearest Neighbors
* Naïve Bayes
* Decision Tree
* Random Forest
* Support Vector Machine

### Module 6: Model Training

Trains each algorithm using the prepared training dataset to identify patterns related to the presence or absence of heart disease.

### Module 7: Heart Disease Prediction

Uses the trained models to predict whether a patient is likely to have heart disease based on the entered medical information.

### Module 8: Performance Evaluation

Evaluates and compares the algorithms using classification accuracy. Random Forest achieved the highest accuracy of **85.25%**, followed by Naïve Bayes at **83.61%**, SVM at **78.69%**, Decision Tree at **73.77%**, and KNN at **65.57%**.

### Module 9: Comparative Analysis

Compares the performance of all five algorithms and identifies Random Forest as the most effective model for this dataset.

### Module 10: User Prediction Interface

Provides a simple interface where users can enter patient health details and receive the predicted heart disease result. The system is intended to support preliminary risk assessment and not replace professional medical diagnosis.


<img width="330" height="137" alt="Screenshot 2026-07-13 at 8 43 40 PM" src="https://github.com/user-attachments/assets/b34bcd7d-b28b-4a11-ac21-bdce46518cd8" />




<img width="303" height="218" alt="image" src="https://github.com/user-attachments/assets/f512e9d6-258d-4ba5-9f7c-079cf0c81654" />
