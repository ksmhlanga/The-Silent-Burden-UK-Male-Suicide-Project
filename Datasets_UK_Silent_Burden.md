# Datasets Reference — UK Project
## The Silent Burden: Understanding Male Suicide in the United Kingdom

**Project:** Portfolio Data Analytics Project
**Analyst:** Kudzanayi Shepherd Mhlanga — Senior Vehicle Engineer, Go Ahead London
**Date:** June 2026

---

## HOW TO USE THIS FILE

Work through the checklist at the bottom. Download each file, save it to your `01_Raw_Data/` folder, and note the download date. ONS data is updated annually — always record when you downloaded it.

---

## PRIMARY DATASETS

---

### 1. ONS — Suicides in England and Wales: Reference Tables ⭐ START HERE

**What it is:** The single most important UK dataset. Annual Excel file with suicide deaths broken down by sex, age group, region, method, and year. This is your backbone dataset.

**URL:** https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/suicidesintheunitedkingdomreferencetables

**How to download:**
1. Visit the URL
2. Click the most recent Excel file (e.g. `suicidesintheukdatasets2024.xlsx`)
3. Save to `01_Raw_Data/`

**Format:** Excel (.xlsx) — multiple tabs
**Coverage:** England & Wales, 2001–2024
**Key tabs to use:**
- Table 1: Deaths and rates by sex and age group (your main analysis table)
- Table 2: Methods of suicide by sex
- Table 3: Rates by region of usual residence
- Table 4: Age-specific rates over time

**Data limitations to note:**
- Figures are based on date of *registration*, not date of death (can lag by months)
- Coroner verdicts of "undetermined intent" are excluded — real figures may be higher
- England & Wales only — Scotland and Northern Ireland are separate

---

### 2. ONS — Suicides in England and Wales: Statistical Bulletin (2024)

**What it is:** The full narrative bulletin that accompanies the reference tables. Includes charts, commentary, and ONS analysis. Essential reading for contextualising your own findings.

**URL:** https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/suicidesintheunitedkingdom/2024registrations

**Format:** Web page + downloadable PDF
**Use for:** Background reading, citations, understanding what ONS considers significant trends

---

### 3. Public Health Scotland — Deaths by Suicide in Scotland

**What it is:** Scotland's equivalent of the ONS tables. Annual statistics on suicide deaths by sex, age group, and NHS health board. Essential for the UK nations comparison.

**URL:** https://www.publichealthscotland.scot/publications/deaths-by-suicide-in-scotland/

**Format:** Excel + PDF report
**Coverage:** Scotland by year, sex, age, and health board

**Data note:** Scotland uses slightly different registration rules to England & Wales. Flag this clearly when comparing nations in your dashboard.

---

### 4. NISRA — Northern Ireland Suicide Statistics

**What it is:** Northern Ireland Statistics and Research Agency data on suicide deaths by sex, age, and area. Required for a full UK picture.

**URL:** https://www.nisra.gov.uk/statistics/cause-death/suicide

**Format:** Excel + PDF
**Coverage:** Northern Ireland by year and sex

**Personal relevance:** Northern Ireland has a rate of 20.9 per 100,000 — above the England average. Worth a dedicated callout in your regional analysis.

---

### 5. Samaritans — Suicide Facts and Figures (Annual Report)

**What it is:** Samaritans' own annual analysis of UK-wide suicide data. Well-written, widely cited, and goes beyond raw ONS numbers to provide context on risk factors, trends, and demographic patterns.

**URL:** https://www.samaritans.org/about-samaritans/research-policy/suicide-facts-and-figures/latest-suicide-data/

**Format:** PDF download (free)
**Use for:** Citations in your written report, background on risk factors, and context for your Act 2 narration

---

### 6. Zero Suicide Alliance — UK Suicide Data Map

**What it is:** Interactive map with over 100 indicators covering suicide rates, risk factors, mental health wellbeing, and service availability across England. Data is exportable.

**URL:** https://www.zerosuicidealliance.com/suicide-data-map

**Format:** Interactive web tool + CSV export
**Use for:** Local authority level analysis, linking deprivation to rates, regional drill-down

---

### 7. English Indices of Multiple Deprivation (IMD 2019)

**What it is:** Official government deprivation scores for every small area (LSOA) in England. The primary dataset for your deprivation vs suicide rate correlation analysis and predictive model.

**URL:** https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019

**How to download:**
1. Visit the URL
2. Download "File 7: all ranks, deciles and scores for the indices of deprivation"
3. This is the main analysis file

**Format:** CSV / Excel
**Key field:** `Index of Multiple Deprivation (IMD) Score` — match to local authority suicide rates by area code

---

### 8. NHS Talking Therapies — IAPT Statistics

**What it is:** NHS data on access to psychological therapies (IAPT) broken down by demographic group. Critical for the access gap analysis — showing how few men use available services.

**URL:** https://digital.nhs.uk/data-and-information/publications/statistical/psychological-therapies-report-on-the-use-of-iapt-services

**Format:** Excel + PDF
**Key metrics:** Referral rates by sex, age, ethnicity; completion rates; waiting times

---

## SUPPLEMENTARY DATASETS

| Dataset | What It Adds | URL |
|---------|-------------|-----|
| House of Commons Library — Suicide Statistics | Cross-UK compiled stats, policy context | https://commonslibrary.parliament.uk/research-briefings/cbp-7749/ |
| ONS — Mental Health Datasets List | Index of all ONS mental health data | https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/mentalhealth/datalist?filter=datasets |
| Men's Health Forum — Key Data | Compiled UK men's mental health statistics | https://www.menshealthforum.org.uk/key-data-mental-health |
| CPRMB — Male Suicide Rates 2025 | Analysis of rising male rates in E&W | https://menandboys.org.uk/male-suicide-combined-rates25/ |
| Statista — Suicide Rate by Gender E&W | Historical gender comparison (2000–2024) | https://www.statista.com/statistics/282203/suicide-rate-in-the-united-kingdom-uk-since-2000-by-gender/ |
| ONS — Self-Harm & Suicide by Sexual Orientation | LGBTQ+ disaggregated data | https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/mentalhealth/bulletins/selfharmandsuicidebysexualorientationenglandandwales/march2021todecember2023 |
| Tough to Talk — 2024 Deep Dive | Narrative analysis of 2024 trends | https://www.toughtotalk.com/post/england-wales-suicide-trends-a-2024-deep-dive |

---

## PREDICTIVE MODEL FEATURE DATASETS

For Phase 6 — these feed your machine learning model alongside the ONS suicide rates:

| Feature | Dataset | URL |
|---------|---------|-----|
| Deprivation score | IMD 2019 (Dataset 7 above) | gov.uk/...deprivation-2019 |
| Unemployment rate by LA | ONS Labour Market Statistics | https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment |
| GP mental health referral rate | NHS IAPT Statistics (Dataset 8 above) | digital.nhs.uk |
| Alcohol-related hospital admissions | NHS NCDR / LSOA alcohol data | https://fingertips.phe.org.uk/ |
| Rural/urban classification | ONS Rural-Urban Classification | https://www.ons.gov.uk/methodology/geography/geographicalproducts/ruralurbanclassifications |

---

## RECOMMENDED FOLDER STRUCTURE

```
The Silent Burden - UK Male Suicide Project/
├── 01_Raw_Data/
│   ├── ONS_suicides_reference_tables_2024.xlsx       ← Download first
│   ├── PHS_scotland_suicides_2024.xlsx
│   ├── NISRA_NI_suicides_2024.xlsx
│   ├── Samaritans_annual_report_2024.pdf
│   ├── IMD_2019_deprivation_file7.csv
│   ├── NHS_IAPT_statistics_2024.xlsx
│   └── ZSA_data_map_export.csv
├── 02_Cleaned_Data/
│   ├── uk_male_suicide_cleaned.csv
│   └── uk_deprivation_merged.csv
├── 03_Analysis/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_predictive_model.ipynb
├── 04_Visualisations/
├── 05_Dashboard/
│   └── silent_burden_dashboard.pbix
├── 06_Streamlit_App/
│   ├── app.py
│   └── pages/
└── 07_Report/
    └── findings_report.pdf
```

---

## DOWNLOAD CHECKLIST

### Must Have (project cannot proceed without these)
- [ ] ONS Reference Tables Excel file — `01_Raw_Data/`
- [ ] IMD 2019 File 7 (deprivation) — `01_Raw_Data/`
- [ ] Public Health Scotland annual report — `01_Raw_Data/`
- [ ] NISRA Northern Ireland data — `01_Raw_Data/`

### Should Have (strengthens analysis significantly)
- [ ] Samaritans annual report PDF — `01_Raw_Data/`
- [ ] NHS IAPT Statistics — `01_Raw_Data/`
- [ ] Zero Suicide Alliance data export — `01_Raw_Data/`

### Nice to Have (for supplementary context)
- [ ] House of Commons Library briefing PDF
- [ ] ONS rural-urban classification
- [ ] ONS unemployment by local authority

---

*Datasets reference — The Silent Burden (UK)*
*June 2026 | Kudzanayi Shepherd Mhlanga | Senior Vehicle Engineer, Go Ahead London*
*Always record the date you downloaded each file — ONS data updates annually*
