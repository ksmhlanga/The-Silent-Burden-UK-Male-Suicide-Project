# Power BI + Streamlit Integration Guide
## Male Suicide Analytics Projects — UK & USA
### Mirroring the London Safety Analysis Project Structure

**By:** Kudzanayi Shepherd Mhlanga
**Date:** June 2026

---

## WHY INTEGRATE POWER BI WITH STREAMLIT?

Power BI is the gold standard for NHS, public sector, and enterprise dashboards in the UK — exactly the audience for your UK project. However, Power BI dashboards require a Microsoft licence to view publicly. Streamlit solves this by creating a **free, publicly accessible web app** that anyone can open in a browser without logging in.

The approach mirrors the *london-safety-analysis* project:
- **Power BI** → for professional/employer presentations and internal use
- **Streamlit** → for the public-facing portfolio version, shared via URL

Both pull from the same cleaned data files — so you build the data once, and present it twice.

---

## ARCHITECTURE OVERVIEW

```
Cleaned Data (CSV)
        │
        ├──→  Power BI Desktop (.pbix)
        │         └──→ Published to Power BI Service (internal/employer use)
        │
        └──→  Streamlit App (Python)
                  └──→ Deployed to Streamlit Cloud (public URL, shareable)
```

---

## PART 1: SETTING UP THE STREAMLIT APP

### 1.1 Install Streamlit

```bash
pip install streamlit pandas plotly folium streamlit-folium scikit-learn
```

### 1.2 Folder Structure

```
silent-burden-uk/          (or silent-crisis-usa/)
├── app.py                 # Main entry point
├── pages/
│   ├── 01_Overview.py
│   ├── 02_Age_Analysis.py
│   ├── 03_Regional_Map.py
│   ├── 04_Risk_Factors.py
│   ├── 05_Predictive_Model.py
│   └── 06_Resources.py
├── data/
│   ├── uk_suicide_cleaned.csv   (or usa_suicide_cleaned.csv)
│   ├── deprivation_data.csv
│   └── model_outputs.csv
├── models/
│   └── risk_model.pkl           # Trained scikit-learn model
├── assets/
│   └── logo.png
└── requirements.txt
```

---

## PART 2: CORE APP CODE

### 2.1 app.py — Main Entry Point

```python
import streamlit as st

st.set_page_config(
    page_title="The Silent Burden — UK Male Suicide Analysis",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("The Silent Burden")
st.subheader("Understanding Male Suicide in the United Kingdom")

st.markdown("""
This dashboard presents data analysis of male suicide rates in the United Kingdom,
drawn from ONS, Samaritans, and NHS sources (2000–2024).

**If you are struggling, please contact Samaritans: 116 123 — free, any time.**
""")

# Navigation handled automatically by /pages/ folder structure
```

---

### 2.2 pages/01_Overview.py — Summary Statistics

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Overview")
st.markdown("Key statistics on male suicide in the United Kingdom.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/uk_suicide_cleaned.csv")

df = load_data()

# KPI cards
col1, col2, col3, col4 = st.columns(4)

latest_year = df["year"].max()
latest_data = df[df["year"] == latest_year]

with col1:
    st.metric(
        label="Male Suicide Rate (per 100k)",
        value=f"{latest_data['male_rate'].values[0]:.1f}",
        delta=f"{latest_data['male_rate'].values[0] - df[df['year']==latest_year-1]['male_rate'].values[0]:.1f} vs prior year"
    )

with col2:
    st.metric(
        label="Total Male Deaths",
        value=f"{int(latest_data['male_deaths'].values[0]):,}"
    )

with col3:
    st.metric(
        label="Male Share of All Suicides",
        value="~75%"
    )

with col4:
    st.metric(
        label="Data Year",
        value=str(latest_year)
    )

st.divider()

# Time series chart
st.subheader("Male vs Female Suicide Rate Over Time (England & Wales)")
fig = px.line(
    df,
    x="year",
    y=["male_rate", "female_rate"],
    labels={"value": "Rate per 100,000", "year": "Year", "variable": "Sex"},
    color_discrete_map={"male_rate": "#1f77b4", "female_rate": "#ff7f0e"},
    title="Suicide Rates by Sex, England & Wales, 2000–2024"
)
fig.update_layout(legend_title_text="Sex")
st.plotly_chart(fig, use_container_width=True)
```

---

### 2.3 pages/03_Regional_Map.py — Choropleth Map

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import requests

st.title("Regional Analysis")
st.markdown("Male suicide rates by region in England, plus Scotland, Wales, and Northern Ireland.")

@st.cache_data
def load_regional_data():
    return pd.read_csv("data/uk_regional_suicide.csv")

df_regional = load_regional_data()

# Year filter
selected_year = st.slider(
    "Select Year",
    min_value=int(df_regional["year"].min()),
    max_value=int(df_regional["year"].max()),
    value=int(df_regional["year"].max())
)

df_filtered = df_regional[df_regional["year"] == selected_year]

# Choropleth map using Plotly and a GeoJSON for UK regions
# Download UK regions GeoJSON from:
# https://raw.githubusercontent.com/thomasvalentine/Choropleth/main/Local_Authority_Districts_(May_2021)_UK_BFE.json

fig = px.choropleth(
    df_filtered,
    geojson="uk_regions.geojson",   # local file
    locations="region_code",
    featureidkey="properties.RGN21CD",
    color="male_rate",
    color_continuous_scale="Reds",
    hover_name="region_name",
    hover_data={"male_rate": ":.1f"},
    labels={"male_rate": "Rate per 100k"},
    title=f"Male Suicide Rate by Region — {selected_year}"
)
fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

# Nations comparison table
st.subheader("UK Nations Comparison")
nations_data = df_filtered[df_filtered["area_type"] == "nation"][["region_name", "male_rate", "male_deaths"]]
st.dataframe(nations_data.rename(columns={
    "region_name": "Nation",
    "male_rate": "Rate per 100,000",
    "male_deaths": "Total Male Deaths"
}), use_container_width=True)
```

---

### 2.4 pages/05_Predictive_Model.py — Risk Predictor

```python
import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title("Predictive Risk Model")
st.markdown("""
This model uses socioeconomic and health data to estimate male suicide risk at a local authority level.

**Model:** Gradient Boosting (XGBoost) | **Features:** Deprivation, unemployment, GP referral rate, rural index
""")

# Load trained model
@st.cache_resource
def load_model():
    with open("models/risk_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.subheader("Explore Risk Factors")
st.markdown("Adjust the sliders to see how changes in key variables affect predicted suicide risk.")

col1, col2 = st.columns(2)

with col1:
    deprivation_score = st.slider("Deprivation Score (IMD — higher = more deprived)", 1, 10, 5)
    unemployment_rate = st.slider("Unemployment Rate (%)", 1.0, 15.0, 5.0, step=0.5)
    gp_referral_rate = st.slider("GP Mental Health Referral Rate (per 1,000)", 1.0, 20.0, 8.0, step=0.5)

with col2:
    rural_index = st.slider("Rural Index (0 = urban, 10 = highly rural)", 0, 10, 3)
    alcohol_rate = st.slider("Alcohol-related hospital admissions (per 100k)", 200, 1000, 500, step=50)

features = np.array([[deprivation_score, unemployment_rate, gp_referral_rate, rural_index, alcohol_rate]])
predicted_rate = model.predict(features)[0]

st.divider()
st.subheader("Predicted Male Suicide Rate")

if predicted_rate < 15:
    risk_level = "🟢 Lower Risk"
    colour = "green"
elif predicted_rate < 20:
    risk_level = "🟡 Moderate Risk"
    colour = "orange"
else:
    risk_level = "🔴 Elevated Risk"
    colour = "red"

st.metric(label=risk_level, value=f"{predicted_rate:.1f} per 100,000")

st.info("""
**Note:** This model is for analytical and educational purposes only.
It identifies statistical patterns, not individual risk.
It is intended to support public health planning discussions.
""")
```

---

## PART 3: REQUIREMENTS.TXT

```
streamlit==1.35.0
pandas==2.2.0
plotly==5.22.0
folium==0.16.0
streamlit-folium==0.20.0
scikit-learn==1.4.0
xgboost==2.0.3
numpy==1.26.4
requests==2.31.0
pickle5==0.0.12
```

---

## PART 4: DEPLOYING TO STREAMLIT CLOUD (FREE)

1. Push your project to GitHub (public repository)
2. Go to **share.streamlit.io** → "New app"
3. Connect your GitHub account
4. Select repository → `app.py` → Deploy
5. Your app gets a permanent public URL:
   `https://[your-username]-silent-burden-uk-app.streamlit.app`
6. Share this URL in your LinkedIn posts, GitHub README, and CV

**Cost:** Free forever on Streamlit Community Cloud for public repositories.

---

## PART 5: LINKING POWER BI TO STREAMLIT DATA

The cleanest approach — keep both tools pointing at the same source:

### Option A: CSV files (simplest)
- Export cleaned data from Python as CSV
- Import the same CSV into Power BI Desktop
- When data updates, refresh both

### Option B: GitHub raw CSV URL (Power BI can live-connect)
1. Upload cleaned CSV to your GitHub repository
2. Get the "raw" URL: `https://raw.githubusercontent.com/[user]/[repo]/main/data/uk_suicide_cleaned.csv`
3. In Power BI: Get Data → Web → paste the raw URL
4. Power BI refreshes from GitHub on demand

This means: **update the CSV once → both Power BI and Streamlit update automatically.**

---

## PART 6: POWER BI SETUP FOR BOTH PROJECTS

### Power BI Dashboard Structure (UK and USA)

**For each project, create a Power BI file (.pbix) with these pages:**

| Tab | Content |
|-----|---------|
| Overview | KPI cards + time series |
| Age Analysis | Bar chart by 5-year age band |
| Regional Map | Choropleth using ArcGIS or Shape map visual |
| Risk Factors | Scatter plots (deprivation vs rate, unemployment vs rate) |
| Predictive Heatmap | Import Streamlit model output as table → display as map |
| Method Breakdown | Firearms vs other (USA); methods by age (UK) |

**Key Power BI settings:**
- Theme: Dark or neutral professional
- Currency/number format: per 100,000 standard
- Enable Q&A visual for employer demos
- Publish to Power BI Service (free with Microsoft account) for online sharing

---

## PART 7: GITHUB README TEMPLATE

```markdown
# The Silent Burden — UK Male Suicide Analysis
> A data analytics + documentary portfolio project

## Live Dashboard
🔗 [Open Streamlit App](https://your-app.streamlit.app)

## Power BI Dashboard
📊 [View on Power BI Service](https://app.powerbi.com/...)
(Or download the .pbix file from /dashboard/)

## Project Structure
- `notebooks/` — data cleaning, EDA, predictive model (Jupyter)
- `data/` — cleaned datasets (ONS, Samaritans)
- `streamlit_app/` — public web application
- `dashboard/` — Power BI file
- `script/` — documentary script
- `report/` — written findings

## Data Sources
- ONS Suicides in England and Wales (2024 registrations)
- Samaritans Annual Statistical Report
- IMD 2019 Deprivation Index
- Public Health Scotland
- NISRA (Northern Ireland)

## Key Findings
[Add after analysis is complete]

## If You Are Struggling
Samaritans: 116 123 — free, any time
CALM: 0800 58 58 58 (5pm–midnight)
Andy's Man Club: andysmanclub.co.uk
```

---

*Power BI + Streamlit Integration Guide*
*June 2026 | Kudzanayi Shepherd Mhlanga*
