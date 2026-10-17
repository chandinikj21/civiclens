# CiviclensAI
AI-powered community complaint analysis, issue clustering, and explainable priority recommendations.
Demo Video

Watch our CivicLens AI solution demonstration:

▶ Watch the CivicLens AI Demo on Youtube [https://youtu.be/bWC8lZ5fr5E]

This video presents our solution for transforming community complaints into organized insights to help identify recurring civic issues and prioritize problems that need attention.

Project: CivicLens AI — From Community Complaints to Actionable Solutions
Event: IBM Z Datathon 2026
Track: Track 3 — Wildcard


# CivicLens AI
### From Community Complaints to Actionable Solutions

**IBM Z Datathon 2026 | Track 3 — Wildcard**

##  Project Overview

CivicLens AI is an AI-powered community intelligence platform designed to transform scattered citizen complaints into organized, evidence-based insights and actionable priorities.

Community issues such as water shortages, garbage accumulation, damaged roads, broken streetlights, and drainage problems are often reported through different channels. Similar complaints can remain disconnected, making it difficult to understand the scale of a problem and determine which issues need attention first.

CivicLens AI uses artificial intelligence and data analytics to classify complaints, identify similar reports, group related issues, calculate explainable priority scores, and recommend appropriate next steps through an interactive dashboard.

##  Problem Statement

Community complaints are often scattered across multiple channels, making recurring problems difficult to identify and urgent issues difficult to prioritize. There is a need for an intelligent system that consolidates related reports, evaluates community impact, and helps decision-makers prioritize problems transparently.

##  Our Solution

CivicLens AI converts individual citizen reports into consolidated community issue records. It analyzes complaint text, identifies potentially related reports, evaluates issue severity and recency, and presents prioritized issues through an interactive dashboard.

The system provides explanations for its recommendations and supports human review and resolution tracking, helping communities and administrators make more informed decisions.

##  Key Features

- **Smart Complaint Analysis:** Categorizes citizen reports using AI.
- **Intelligent Duplicate Detection:** Identifies similar complaints and groups related reports.
- **Explainable Priority Scoring:** Explains why an issue may require attention first.
- **Community Intelligence Dashboard:** Displays issue categories, trends, and unresolved problems.
- **Location-Based Visualization:** Shows where reported issues occur.
- **Action Recommendations:** Suggests appropriate next steps for review and intervention.
- **Resolution Tracking:** Tracks issues from reporting through review to resolution.

##  Technology Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Sentence Transformers
- Streamlit
- SQLite
- Plotly
- Folium

*The final technology list will be updated to reflect the components actually implemented in the prototype.*

##  How It Works

1. Citizens submit complaints with descriptions and available location details.
2. The system analyzes the complaint and identifies its category.
3. AI compares the report with existing complaints to identify potential duplicates.
4. Related reports are grouped into a consolidated issue record.
5. A priority score is calculated using defined factors such as severity, report volume, recency, and estimated impact.
6. The dashboard displays issue clusters, priority explanations, and recommended next actions.
7. An administrator reviews the recommendations and updates the issue status.

##  Expected Social Impact

- Improve visibility of recurring community problems.
- Reduce the manual effort involved in organizing complaints.
- Support transparent, data-driven prioritization.
- Help administrators monitor unresolved issues.
- Encourage citizen participation and accountability.

##  Problem Definition Video

Watch our 30-second problem-awareness video:

**YouTube:** [Add your actual YouTube video link here]

##  Evaluation

The prototype will be evaluated using test complaints and human-reviewed examples. Evaluation measures may include complaint classification performance, duplicate-grouping accuracy, priority-ranking quality, and correct handling of uncertain reports.

Simulated data and estimated impacts will be clearly identified.

##  Future Scope

- Multilingual complaint analysis, including Kannada.
- Voice-based complaint submission.
- Integration with verified civic-reporting systems.
- Improved geospatial analysis and issue trend detection.
- Deployment on an IBM platform if required by the datathon rules.

## Team

**Project Name:** CivicLens AI  
**Event:** IBM Z Datathon 2026  
**Track:** Track 3 — Wildcard

Add your team members' names and responsibilities here.

## Disclaimer

CivicLens AI is a decision-support prototype. AI-generated groupings and priority scores require validation and human review. The prototype does not independently verify complaints, contact authorities, or guarantee that an issue has been resolved.
# CivicLens AI

CivicLens AI explores NYC 311 complaints and suggests complaint categories.

## Get the 311 dataset

The NYC 311 CSV is over GitHub's 100 MB file limit, so it is intentionally not
stored in this repository. Download it from the official
[NYC Open Data 311 Service Requests dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9),
then choose **Export** and download the data as a CSV.

To use the app, run it locally and upload the downloaded CSV when prompted.
The app reads up to the first 100,000 rows.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```
