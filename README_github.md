# 🔵 The Silent Burden — UK Male Suicide, Race & Mental Health

**A data analytics portfolio project by Kudzanayi Shepherd Mhlanga**  
📊 [Live Dashboard](https://silent-burden-uk.vercel.app) · 🌐 [Portfolio](https://datascienceportfol.io/ksmhlanga) · 💻 [GitHub](https://github.com/ksmhlanga/UK_Silent_Crisis_Project)

---

## Overview

Every 2 hours, a man dies by suicide in the UK. **75% of all suicides are male** — a ratio that has not changed in 30 years. Yet within that statistic lies a deeper, less-visible crisis: the men whose pain is hidden by culture, silenced by stigma, and missed by systems that were never designed for them.

This project analyses UK male suicide data from 2000 to 2024 with a specific focus on **ethnic minority men** — the group most underserved by existing mental health services, most underrepresented in official statistics, and most exposed to compounding structural risk factors.

---

## Key Findings

| Finding | Statistic |
|---------|-----------|
| UK male suicide rate (2024) | **17.6 per 100,000** — highest this century |
| Male share of all suicides | **75%** — unchanged since the mid-1990s |
| Wales 2024 rate | **25.0** — up +14% in a single year |
| Scotland 2024 rate | **19.3** — 518 deaths |
| Northern Ireland 2024 rate | **20.9** — significantly above UK average |
| Peak risk age group | **50–54** at 27.5 per 100,000 |
| Black men: MHA detention | **4× the rate** of White British men |
| Minority men: therapy completion | **~50% of** the White British completion rate |
| GRT men: life expectancy gap | **10–12 years** below national average |

---

## Project Structure

```
The Silent Burden - UK Male Suicide Project/
│
├── 📓 Notebooks
│   ├── 01_uk_data_collection.ipynb     # Data sources, URLs, raw dataset creation
│   ├── 02_uk_data_cleaning.ipynb       # Cleaning, merging, derived columns, export
│   └── 03_uk_eda_insights.ipynb        # EDA, visualisations, key findings
│
├── 📊 Dashboard
│   └── silent_burden_uk_dashboard.html # Interactive HTML dashboard (Chart.js)
│
├── 📁 data/
│   ├── ons_ew_annual.csv               # ONS England & Wales annual rates 2000–2024
│   ├── ons_age_2024.csv                # Age-specific rates by sex (2024)
│   ├── ons_regions.csv                 # Regional rates for England
│   ├── phs_scotland.csv                # Public Health Scotland annual data
│   ├── nisra_ni.csv                    # NISRA Northern Ireland data
│   ├── iapt_ethnicity.csv              # NHS Talking Therapies access by ethnicity
│   ├── mha_detention.csv               # Mental Health Act detention by ethnicity
│   ├── samaritans_risk.csv             # Risk factor scores (synthesised)
│   ├── imd_deprivation.csv             # Index of Multiple Deprivation correlation
│   └── clean/                          # Cleaned & merged datasets (from Notebook 2)
│       ├── ons_ew_annual_clean.csv
│       ├── four_nations_clean.csv
│       ├── age_analysis_clean.csv
│       ├── ethnicity_composite_clean.csv
│       └── regions_imd_clean.csv
│
├── 📈 charts/                          # Charts exported from Notebook 3
│   ├── 01_headline_trends.png
│   ├── 02_gender_analysis.png
│   ├── 03_nations_comparison.png
│   ├── 04_age_analysis.png
│   ├── 05_covid_rebound.png
│   ├── 06_ethnicity_disparities.png
│   ├── 07_deprivation_correlation.png
│   └── 08_risk_factors.png
│
├── 📄 Documentation
│   ├── UK_Master_Project_Plan_Silent_Burden.md
│   ├── Portfolio_UK_Male_Suicide_Mental_Health.md
│   ├── Datasets_UK_Silent_Burden.md
│   └── UK_Documentary_Script_and_Interview_Guide.md
│
└── vercel.json                         # Vercel deployment config
```

---

## Data Sources

| # | Source | Organisation | URL |
|---|--------|-------------|-----|
| 1 | Suicides in England & Wales — Reference Tables | ONS | [Link](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/suicidesintheunitedkingdomreferencetables) |
| 2 | Deaths by Suicide in Scotland | Public Health Scotland | [Link](https://www.publichealthscotland.scot/publications/deaths-by-suicide-in-scotland/) |
| 3 | Northern Ireland Suicide Statistics | NISRA | [Link](https://www.nisra.gov.uk/statistics/cause-death/suicides) |
| 4 | NHS Talking Therapies Annual Report (IAPT) | NHS Digital | [Link](https://digital.nhs.uk/data-and-information/publications/statistical/psychological-therapies-annual-reports-on-the-use-of-iapt-services) |
| 5 | Mental Health Act Statistics | NHS Digital | [Link](https://digital.nhs.uk/data-and-information/publications/statistical/mental-health-act-statistics-annual-figures) |
| 6 | Annual Statistical Report | Samaritans | [Link](https://www.samaritans.org/about-samaritans/research-policy/suicide-facts-and-figures/) |
| 7 | Index of Multiple Deprivation (IMD) | MHCLG / ONS | [Link](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019) |

---

## Notebooks — What Each One Covers

### 📓 01 — Data Sources & Collection
- Documents all 7 data sources with official URLs
- Explains why each source was chosen and its limitations
- Recreates representative datasets from published official statistics
- Highlights the **critical underreporting problem** for ethnic minority communities
- Exports all raw source datasets to `/data/`

### 🧹 02 — Data Cleaning & Merging
- Loads and audits all 9 raw datasets (missing values, duplicates, outliers)
- Standardises column naming conventions
- Builds the **four-nations combined dataset** (E&W + Scotland + N.Ireland + Wales)
- Handles suppressed ethnicity counts (ONS small-number suppression)
- Creates a **composite ethnicity vulnerability score** from NHS service data
- Merges IMD deprivation scores with regional suicide rates
- Z-score outlier detection on the 24-year annual series
- Exports 5 clean analysis-ready datasets to `/data/clean/`

### 📈 03 — EDA & Insights
- **Headline trends**: 24-year male rate with period shading + YoY change bars
- **Gender gap analysis**: dual-line, gap over time, male % of all deaths
- **Four-nations comparison**: trend lines + 2024 snapshot
- **Age group deep dive**: rate by band + male:female ratio by age
- **Post-COVID rebound**: 2020–2025 focused analysis with 2025 projection
- **Ethnicity disparities**: IAPT access funnel + MHA detention index + composite score
- **Deprivation correlation**: scatter plot + regional correlation (r values)
- **Risk factor analysis**: general vs minority men side-by-side
- **Key findings summary**: printed analytical conclusions

---

## Dashboard

The interactive dashboard is built as a single-file HTML with **Chart.js 4.4.0**. No build tools or dependencies needed — open directly in any browser.

**Tabs:**
1. 📊 Overview — KPI cards, gender comparison, nations, age overview
2. ✊ Race & Ethnicity — the hero tab: group-by-group analysis, IAPT/MHA charts, cultural barriers, evidence-based solutions
3. 🗺 Nations & Regions — four-nations trend + English regional breakdown
4. 👤 Age Analysis — age band rates, race × age compound risk
5. 📈 Trends 2000–2024 — full trend line, YoY change, 2020–2025 focused view
6. ⚠ Risk Factors — deprivation scatter, risk radar, race-specific risk cards
7. 🔬 Methodology — data sources, limitations, portfolio context

---

## Skills Demonstrated

- **Real government data sourcing** — ONS, NHS Digital, NISRA, PHS, MHCLG
- **Multi-source data merging** and longitudinal analysis (24 years)
- **Health equity analysis** — ethnicity × gender × deprivation intersectionality
- **Missing data handling** — ONS small-number suppression, 'not stated' ethnicity coding
- **Statistical analysis** — correlation, z-scores, regression, period classification
- **Data visualisation** — matplotlib dark theme, Chart.js interactive dashboard
- **NHS / public health communication** — policy-relevant framing
- **Jupyter notebook workflow** — collection → cleaning → EDA → insights

---

## Setup & Run

```bash
# Clone the repo
git clone https://github.com/ksmhlanga/UK_Silent_Crisis_Project.git
cd UK_Silent_Crisis_Project

# Install dependencies
pip install pandas numpy matplotlib scipy jupyter

# Run notebooks in order
jupyter notebook 01_uk_data_collection.ipynb
jupyter notebook 02_uk_data_cleaning.ipynb
jupyter notebook 03_uk_eda_insights.ipynb

# Open dashboard in browser
open silent_burden_uk_dashboard.html
```

---

## Crisis Support

If you or someone you know is struggling, please reach out:

| Organisation | Number | Hours |
|-------------|--------|-------|
| **Samaritans** | 116 123 | 24/7, free |
| **CALM** | 0800 58 58 58 | 5pm–midnight |
| **Shout** | Text 85258 | 24/7 text |
| **Black Minds Matter** | blackmindsmatter.co.uk | Free therapy for Black adults |
| **BAATN** | baatn.org.uk | Black & Asian therapy network |
| **Nafsiyat** | nafsiyat.org.uk | Intercultural therapy centre |

---

## About the Analyst

**Kudzanayi Shepherd Mhlanga** — Senior Vehicle Engineer at Go Ahead London, a Data Science enthusiast. Originally from Harare, Zimbabwe. Based in London, UK.

This project is personal as much as it is analytical. As someone who works alongside drivers, engineers, and operational staff — many of them men from minority backgrounds in physically and mentally demanding roles — the data represents people, not numbers.

📧 ksmhlanga@gmail.com · 🌐 [datascienceportfol.io/ksmhlanga](https://datascienceportfol.io/ksmhlanga)

---

*Data covers 2000–2024. Sources: ONS, Public Health Scotland, NISRA, NHS Digital, Samaritans, MHCLG. 2025 figures are provisional projections.*
