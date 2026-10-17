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
