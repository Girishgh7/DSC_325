import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import joblib


df=pd.read_csv('Political_Bias.csv')



# Fill missing text values with empty string
df["Text"].fillna("", inplace=True)

# Combine Title and Text for better feature extraction
df["Combined"] = df["Title"] + " " + df["Text"]

# Encode target labels (using this insted of maping)
label_encoder = LabelEncoder()
df["Bias_encoded"] = label_encoder.fit_transform(df["Bias"])

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    df["Combined"], df["Bias_encoded"], test_size=0.2, random_state=42
)

# Define pipeline with CountVectorizer and Logistic Regression
pipeline = Pipeline([
    ("vectorizer", CountVectorizer(stop_words="english", ngram_range=(1,2))),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
pipeline.fit(X_train, y_train)

# Save the trained model and label encoder
joblib.dump(pipeline, "bias_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

# Check model accuracy
accuracy = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")
