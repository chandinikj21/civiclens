
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CivicLens AI", layout="wide")

st.title("CivicLens AI")
st.subheader("From Community Complaints to Actionable Solutions")

uploaded_file = st.file_uploader(
    "Upload your NYC 311 CSV file",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload your 311 CSV file to start.")
    st.stop()

df = pd.read_csv(
    uploaded_file,
    low_memory=True,
    nrows=100000
)

# Prepare columns
df["Created Date"] = pd.to_datetime(
    df["Created Date"],
    format="mixed",
    errors="coerce"
)

df["Complaint Type"] = df["Complaint Type"].fillna("Unknown")
df["Status"] = df["Status"].fillna("Unknown")

# Sidebar filters
st.sidebar.header("Filter Complaints")

types = sorted(df["Complaint Type"].unique())
selected_types = st.sidebar.multiselect(
    "Complaint Type", types, default=types[:10]
)

boroughs = sorted(df["Borough"].dropna().unique())
selected_boroughs = st.sidebar.multiselect(
    "Borough", boroughs, default=boroughs
)

filtered = df[
    df["Complaint Type"].isin(selected_types)
]

if selected_boroughs:
    filtered = filtered[
        filtered["Borough"].isin(selected_boroughs)
    ]
else:
    filtered = filtered.iloc[0:0]

# Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Total Complaints", f"{len(filtered):,}")
c2.metric("Complaint Types", filtered["Complaint Type"].nunique())
c3.metric(
    "Open Complaints",
    int(filtered["Status"].astype(str).str.lower()
        .str.contains("open").sum())
)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Most Reported Problems")
    counts = filtered["Complaint Type"].value_counts().head(10)
    if not counts.empty:
        fig = px.bar(
            x=counts.values,
            y=counts.index,
            orientation="h",
            labels={"x": "Complaints", "y": "Complaint Type"},
            title="Top 10 Complaint Types"
        )
        st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Complaint Status")
    status_counts = filtered["Status"].value_counts()
    if not status_counts.empty:
        fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Status Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

st.subheader("Priority Ranking")
st.caption(
    "Suggested ranking based on complaint frequency. "
    "This is a prototype score, not an official urgency assessment."
)

priority = (
    filtered.groupby("Complaint Type")
    .size()
    .reset_index(name="Complaint Count")
    .sort_values("Complaint Count", ascending=False)
)
priority.insert(0, "Rank", range(1, len(priority) + 1))
st.dataframe(priority.head(10), use_container_width=True)

st.subheader("Complaint Locations")

if "Latitude" in filtered.columns and "Longitude" in filtered.columns:
    locations = filtered[["Latitude", "Longitude"]].copy()
    locations["Latitude"] = pd.to_numeric(
        locations["Latitude"], errors="coerce"
    )
    locations["Longitude"] = pd.to_numeric(
        locations["Longitude"], errors="coerce"
    )
    locations = locations.dropna()

    locations = locations[
        locations["Latitude"].between(40, 42)
        & locations["Longitude"].between(-75, -72)
    ].head(5000)

    if not locations.empty:
        st.map(
            locations.rename(
                columns={"Latitude": "latitude",
                         "Longitude": "longitude"}
            )
        )
    else:
        st.info("No valid coordinates found for these filters.")

st.subheader("Complaint Records")
st.dataframe(
    filtered[
        ["Created Date", "Complaint Type", "Borough", "Status"]
    ].head(500),
    use_container_width=True
)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Filtered Complaints",
    data=csv,
    file_name="civiclens_filtered_complaints.csv",
    mime="text/csv"
)



# -------- AI COMPLAINT CATEGORIZATION --------

import joblib

st.divider()
st.header("AI Complaint Categorization")

st.write("Enter a community complaint to predict its category.")

@st.cache_resource
def load_complaint_model():
    return joblib.load("complaint_model.joblib")

try:
    model = load_complaint_model()

    complaint = st.text_area(
        "Describe the problem",
        placeholder="Example: Cars are blocking my driveway"
    )

    if st.button("Predict Category"):
        if complaint.strip():
            probabilities = model.predict_proba([complaint])[0]
            classes = model.classes_

            top_indices = probabilities.argsort()[-3:][::-1]

            st.subheader("Top 3 Suggested Categories")

            for index in top_indices:
                category = classes[index]
                score = probabilities[index]
                st.write(f"**{category}** — {score:.1%}")

            best_score = probabilities[top_indices[0]]

            if best_score < 0.50:
                st.warning(
                    "Low confidence: please review the suggestions."
                )
            else:
                st.info(
                    "Please verify the suggested category before action."
                )
        else:
            st.warning("Please enter a complaint.")

except FileNotFoundError:
    st.error("Model file not found. Run train_model.py first.")
