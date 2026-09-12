# Every 1.8 Hours, a Man Dies by Suicide in the UK
## A 25-Year Data Analysis — The Silent Burden

An independent data analytics project examining 25 years of UK male suicide data (2000–2024), with a focus on race, ethnicity, age, geography, and access to mental health services. Built on official government data from ONS, NHS Digital, NISRA, and Public Health Scotland.

**Live dashboard:** [silent-burden-uk.vercel.app](https://silent-burden-uk.vercel.app)

---

## What this project is about

Men account for roughly 75% of all suicides in the UK — a figure that has barely changed in thirty years. In 2024, the male suicide rate in England and Wales reached 17.6 per 100,000, the highest recorded this century. In Wales alone, the rate jumped 14% in a single year.

This project asks why that is, and what the data tells us about who is most at risk and why they are least likely to receive help before it is too late.

The analysis covers the full 24-year trend from 2000 to 2024, four-nation comparisons, age-group breakdowns, and a detailed look at what happens to ethnic minority men specifically. Black men are detained under the Mental Health Act at four times the rate of White British men, yet reach recovery in NHS Talking Therapies (IAPT) at less than half the rate. That gap does not happen by accident. This project tries to explain it with data.

---

## What is in this repo

**`silent_burden_uk_dashboard.html`** — The main output. An interactive analytics dashboard with seven sections: Overview, Race & Ethnicity, Nations & Regions, Age Analysis, Trends 2000–2024, Risk Factors, and Methodology. Open it locally in any browser, or visit the live version linked above.

**`The_Silent_Burden_UK_Findings_Report.pdf`** — A structured PDF summary of the key findings, suitable for sharing with colleagues or attaching to an email.

**`The_Silent_Burden_UK_Presentation.pptx`** — A slide deck version of the core findings, designed for public health, policy, or NHS audiences.

**`The_Silent_Burden_UK_Project_Writeup.docx`** — A full academic research paper with abstract, literature review, methodology, analysis, policy recommendations, and references.

**`01_uk_data_collection.ipynb` / `02_uk_data_cleaning.ipynb` / `03_uk_eda_insights.ipynb`** — The full data pipeline showing how data was collected from government sources, cleaned, standardised, and explored.

---

## Data sources

All figures come from official published sources:

| Source | Organisation | Coverage |
|--------|-------------|---------|
| Suicides Reference Tables | Office for National Statistics | England & Wales, 2000–2024 |
| Deaths by Suicide | Public Health Scotland | Scotland, 2000–2024 |
| Suicide Statistics | NISRA | Northern Ireland, 2000–2024 |
| NHS Talking Therapies (IAPT) | NHS Digital | 2017–2023, by ethnicity |
| Mental Health Act Statistics | NHS Digital | 2010–2023, by ethnicity |
| Annual Statistical Report | Samaritans | 2023 |
| Index of Multiple Deprivation | MHCLG / ONS | England, 2019 |

Where ONS records ethnicity as "not stated" (around 18% of male suicide deaths), this is flagged as a limitation. The real minority male suicide rate is almost certainly higher than any figure in this project.

---

## A note on the numbers

The dashboard reports two kinds of figure, and they are labelled differently on purpose:

- **Official statistics** — suicide rates, IAPT recovery rates, and Mental Health Act detention rates come directly from the published sources in the table above.
- **Analyst-constructed indices** — the 1–10 risk-factor scores are my own synthesis of the literature, used to compare the *relative* weight of risk factors between groups. They are not published statistics and are labelled as such in the dashboard.

Regional figures are age-standardised rates per 100,000 for males, from `data/ons_regions.csv`. The North East has the highest rate (21.4) and the East of England the lowest (12.8); London sits mid-table at 16.8.

## Key findings

- The UK male suicide rate reached **17.6 per 100,000** in 2024 — the highest this century
- Men account for **75%** of all UK suicides. This ratio has not improved in 30 years
- Wales recorded a **+14% year-on-year increase** in 2024, reaching 25.0 per 100,000
- The peak risk age group is **50–54 years** (27.5 per 100,000 for males)
- Black men are detained under the Mental Health Act at **4× the rate** of White British men
- Black men reach recovery in NHS Talking Therapies at **32%** vs 65% for White British men
- Gypsy, Roma and Traveller men have a life expectancy gap of **10–12 years** below the national average
- The North East of England has a rate **27% higher** than London

---

## How to use the dashboard

Download `silent_burden_uk_dashboard.html` and open it in any modern browser. No server or internet connection required once downloaded (Chart.js loads from CDN on first open).

Use the sidebar icons to switch between sections. The right-hand panel updates with supporting context, statistics, and crisis helpline numbers for each section.

---

## About the analyst

This project was built by **Kudzanayi Shepherd Mhlanga**, a Senior Vehicle Engineer at Go Ahead London, a Data Science enthusiast. Originally from Harare, Zimbabwe. Based in London, UK.

The project is personal as much as it is analytical. The data here represents people, not abstractions. That is why this topic was chosen.

Contact: ksmhlanga@gmail.com | GitHub: [ksmhlanga](https://github.com/ksmhlanga)

---

*If you are struggling, please reach out.*
*Samaritans: 116 123 (free, 24/7) · CALM: 0800 58 58 58 (5pm–midnight) · Text Shout: 85258*