"""
Project 2: Data Classification Using AI
DecodeLabs - AI Internship (Batch 2026)

Goal: Build a basic classification model using the Iris dataset.
Pipeline: Load data -> Scale features -> Train/Test split ->
          Train KNN model -> Predict -> Evaluate (Confusion Matrix, F1 Score)
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score
import pandas as pd


# STEP 1: INPUT - Load and understand the dataset
iris = load_iris()
X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(y, iris.target_names)

print("=" * 55)
print("STEP 1: DATASET OVERVIEW")
print("=" * 55)
print(f"Samples: {X.shape[0]} | Features: {X.shape[1]} | Classes: {len(iris.target_names)}")
print(f"Classes: {list(iris.target_names)}")
print("\nFirst 5 rows:")
print(df.head())
print("\nClass distribution:")
print(df["species"].value_counts())


# STEP 2: PROCESS - Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 55)
print("STEP 2: TRAIN-TEST SPLIT")
print("=" * 55)
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples:  {X_test.shape[0]}")


# STEP 2b: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# STEP 3: Apply a simple classification algorithm (KNN)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)


# STEP 4: OUTPUT - Evaluate the model
print("\n" + "=" * 55)
print("STEP 3: MODEL EVALUATION")
print("=" * 55)

accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average="weighted")

print(f"Accuracy Score: {accuracy:.2%}")
print(f"F1 Score (weighted): {f1:.2f}")

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, predictions)
cm_df = pd.DataFrame(cm, index=iris.target_names, columns=iris.target_names)
print(cm_df)

print("\nDetailed Classification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))


# STEP 5: Predict on a brand-new, unseen flower sample
print("=" * 55)
print("STEP 4: PREDICTION ON NEW DATA")
print("=" * 55)

new_flower = [[5.0, 3.4, 1.5, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
predicted_class = model.predict(new_flower_scaled)

print(f"New sample: {new_flower[0]}")
print(f"Predicted species: {iris.target_names[predicted_class[0]]}")
