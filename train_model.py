
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Change this to your actual CSV filename
CSV_FILE = r"c:\Users\Other\Downloads\archive (4)\311_Service_Requests_from_2010_to_Present.csv"

print("Loading dataset...")
df = pd.read_csv(
    CSV_FILE,
    usecols=["Complaint Type", "Descriptor"],
    nrows=50000,
    low_memory=True
)

# Use the available complaint fields
df["Complaint Type"] = df["Complaint Type"].fillna("").astype(str)

if "Descriptor" in df.columns:
    df["Descriptor"] = df["Descriptor"].fillna("").astype(str)
    df["text"] = (
        df["Complaint Type"] + " " + df["Descriptor"]
    )
else:
    df["text"] = df["Complaint Type"]

df = df[
    (df["text"].str.strip() != "")
    & (df["Complaint Type"].str.strip() != "")
]

# Keep common categories so training is more manageable
common_types = df["Complaint Type"].value_counts()
common_types = common_types[common_types >= 20].index

df = df[df["Complaint Type"].isin(common_types)]

# Limit training size to keep the first run manageable
df = df.sample(
    n=min(50000, len(df)),
    random_state=42
)

X = df["text"]
y = df["Complaint Type"]

if y.nunique() < 2:
    raise ValueError("The dataset needs at least two complaint categories.")

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=20000,
        ngram_range=(1, 2),
        stop_words="english"
    )),
    ("classifier", LogisticRegression(
        max_iter=300,
        class_weight="balanced"
    ))
])

print("Training AI model...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Test accuracy: {accuracy:.2%}")

joblib.dump(model, "complaint_model.joblib")
print("Saved model as complaint_model.joblib")
print("Training completed!")
