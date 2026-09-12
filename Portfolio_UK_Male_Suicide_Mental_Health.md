# Every 1.8 Hours, a Man Dies by Suicide in the UK
### A 25-Year Data Analysis — The Silent Burden

**Project Type:** Data Analytics — Portfolio Piece  
**Focus Region:** United Kingdom (England, Wales, Scotland, Northern Ireland)  
**Topic:** Mental Health — Suicide Among Men  
**Analyst:** Kudzanayi Shepherd Mhlanga  
**Role:** Senior Vehicle Engineer — Go Ahead London, Sutton Bus Garage  
**Location:** Sutton, London  
**Date:** July 2026

---

## 1. Project Overview

In the United Kingdom, male suicide remains one of the most significant yet underreported public health challenges. Men account for approximately **75% of all suicide deaths** in the UK — a figure that has been consistent since the mid-1990s. Despite this, mental health services and awareness campaigns have historically failed to engage men effectively. This portfolio project analyses UK-wide data on male suicide rates, trends, geographic disparities, and risk factors, with the aim of producing professional-grade visualisations and insights.

This project is part of my transition into Data Analytics and demonstrates my ability to source, clean, analyse, and communicate real-world health data.

---

## 2. Problem Statement

Suicide is the **leading cause of death for men under 50 in the UK**. The male suicide rate in England and Wales reached its highest point this century in 2024, at 17.6 per 100,000 — yet male mental health remains chronically underfunded and under-discussed. Men are far less likely than women to seek help, and cultural barriers around masculinity perpetuate a "suffer in silence" norm.

**Key Questions This Project Will Answer:**
- How have male suicide rates trended across the UK from 2000–2024?
- Which age group of men faces the greatest risk?
- How do rates differ between England, Wales, Scotland, and Northern Ireland?
- Which regions within England have the highest rates?
- What is the relationship between deprivation and male suicide?
- How do methods of suicide differ by age group among men?
- How does the UK compare internationally?

---

## 3. Key Statistics (United Kingdom)

| Metric | Statistic | Source |
|--------|-----------|--------|
| Male suicide rate — England & Wales (2024) | 17.6 per 100,000 | ONS |
| Male suicide rate — England & Wales (2023) | 17.4 per 100,000 | ONS |
| Male suicide rate — England & Wales (2000) | 17.2 per 100,000 | ONS |
| Male share of all UK suicides | ~75% | ONS / Samaritans |
| Highest risk age group (males) | 50–54 years (27.5/100,000) | ONS 2024 |
| Suicide leading cause of death | Men under 50 | ONS |
| Highest regional rate | North East England (21.4/100,000) | ONS 2022–24 avg |
| Lowest regional rate | London | ONS |
| Scotland male suicides (2024) | 518 deaths (19.3/100,000) | Public Health Scotland |
| Wales male rate (2024) | 25.0 per 100,000 | ONS / CPRMB |
| Wales male rate (2023) | 22.0 per 100,000 | ONS / CPRMB |
| Northern Ireland (2023) | 171 suicides at 20.9/100,000 | NISRA |

> **Note:** Wales saw a dramatic rise from 2023 to 2024 — an additional 41 male deaths, pushing it to the highest rate of all UK nations.

---

## 4. Risk Factors

### 4.1 Demographics
- **Age:** Men aged 50–54 are the highest-risk group (27.5/100,000). Suicide remains the #1 cause of death for men under 50.
- **Geography:** North East England, Wales, and Scotland consistently have higher rates than London and the South East.
- **Deprivation:** Men in the most deprived 10% of areas have significantly higher rates than those in the least deprived.

### 4.2 Mental Health
- Depression is the most prevalent mental health condition among men who die by suicide
- Men are less likely to be diagnosed with depression — partly because male depression often presents differently (anger, substance use, risk-taking) rather than sadness
- Men are significantly less likely to access NHS talking therapies than women
- PTSD, anxiety, and psychosis are significant co-factors

### 4.3 Social & Economic
- Unemployment and job insecurity (particularly post-redundancy)
- Divorce and family breakdown — men lose child contact at higher rates
- Loneliness and social isolation
- Substance use (alcohol especially prevalent in Northern England and Scotland)
- Housing instability and homelessness
- Rural geography — especially relevant for agricultural communities

### 4.4 Cultural Factors
- Traditional British masculine norms ("keep calm and carry on")
- Stigma around mental health help-seeking
- Men make fewer GP visits and are less likely to disclose mental distress
- Workplace cultures in manual industries (construction, manufacturing) that discourage vulnerability

---

## 5. Trends Over Time

- Male suicide rate in England & Wales has remained stubbornly high since 2000
- The 2024 rate (17.6) is nearly identical to the 2000 rate (17.2) — **no meaningful improvement in 25 years**
- The all-time peak in the data was **2013 at 18.7 per 100,000** — driven by austerity and the aftermath of the global financial crisis
- 2019 saw a sharp pre-COVID rise (+6.8% to 17.3), followed by a COVID-era dip in 2020–2021
- The post-COVID rebound was sharp: 2022 saw +7.6% in a single year, the steepest rise in the dataset
- Wales has seen the most alarming recent increase (+14% from 2023 to 2024)
- Scotland's 2024 rate (19.3) is above the England & Wales rate — Northern nations consistently higher

---

## 6. Geographic Analysis (England by Region)

| Region | Rate (per 100,000) | Notes |
|--------|-------------------|-------|
| North East | 21.4 | Highest in England · 2022–24 average |
| North West | High | Second highest consistently |
| Yorkshire & Humber | Above average | Former industrial heartland |
| East Midlands | Average | |
| West Midlands | Average | |
| East of England | Below average | |
| South West | Below average | Rural-urban mix |
| South East | Below average | |
| London | Lowest | Dense urban services, diverse population |

---

## 7. Proposed Analysis Plan

### Phase 1: Data Collection & Cleaning
- Download ONS "Suicides in England and Wales" reference tables (Excel)
- Download Public Health Scotland data on male suicide
- Download NISRA data for Northern Ireland
- Download deprivation indices (IMD 2019/2023) for correlation analysis
- Merge and clean all datasets using Python or Excel

### Phase 2: Exploratory Data Analysis (EDA)
- Time series: male vs female rate over 2000–2024
- Regional breakdown: heatmap/choropleth of England + devolved nations
- Age breakdown: bar chart showing rate by 5-year age bands
- Deprivation correlation: scatter plot — deprivation score vs suicide rate
- Method breakdown: visualise method distribution across age groups
- Nations comparison: England vs Wales vs Scotland vs Northern Ireland

### Phase 3: Dashboard
- Build an interactive dashboard (Power BI preferred — NHS sector-relevant)
- Filters: nation, region, year, age group
- KPI summary: current year deaths, rate per 100k, year-on-year change, highest-risk group

### Phase 4: Report & Presentation
- Written report (1,500–2,000 words) contextualising findings
- Slide deck suitable for NHS or public health audience
- Portfolio-ready: hosted on GitHub or personal website

---

## 8. Datasets

### Primary Datasets

| Dataset | Description | URL | Format |
|---------|-------------|-----|--------|
| ONS — Suicides in England and Wales (2024 registrations) | Annual bulletin + reference tables, by sex, age, region, method | https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/suicidesintheunitedkingdomreferencetables | Excel (.xlsx) |
| ONS — Suicides bulletin (2024) | Full statistical bulletin narrative | https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/suicidesintheunitedkingdom/2024registrations | Web / PDF |
| ONS — Mental Health data list | All ONS published mental health datasets | https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/mentalhealth/datalist?filter=datasets | Multiple |
| Public Health Scotland — Suicide Data | Scotland-specific suicide statistics | https://www.publichealthscotland.scot/publications/deaths-by-suicide-in-scotland/ | Excel / PDF |
| NISRA — Northern Ireland Suicide Statistics | NI-specific data by sex and age | https://www.nisra.gov.uk/statistics/cause-death/suicide | Excel |
| Samaritans — Suicide Facts and Figures | UK-wide annual statistical report | https://www.samaritans.org/about-samaritans/research-policy/suicide-facts-and-figures/latest-suicide-data/ | PDF |
| Zero Suicide Alliance — Data Map | Interactive UK map with 100+ indicators | https://www.zerosuicidealliance.com/suicide-data-map | Interactive / CSV |
| ONS — Index of Multiple Deprivation | Deprivation scores by LSOA/MSOA | https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019 | CSV / Excel |
| House of Commons Library — Suicide Statistics | Parliamentary research briefing with compiled stats | https://commonslibrary.parliament.uk/research-briefings/cbp-7749/ | PDF |

### Supplementary Datasets

| Dataset | Description | URL |
|---------|-------------|-----|
| Men's Health Forum — Key Data | Compiled UK men's mental health statistics | https://www.menshealthforum.org.uk/key-data-mental-health |
| Men's Counselling Service — Statistics Guide | Key men's mental health statistics UK | https://menscounsellingservice.com/resources/key-mens-mental-health-statistics-a-guide-to-the-data/ |
| CPRMB — Male Suicide Combined Rates 2025 | Analysis of rising male suicide rates in England & Wales | https://menandboys.org.uk/male-suicide-combined-rates25/ |
| ScienceDirect — Regional Disparities Study | Academic paper on changing UK suicide trends | https://www.sciencedirect.com/science/article/pii/S0033350624004906 |
| Tough to Talk — 2024 Deep Dive | Analysis of England & Wales trends | https://www.toughtotalk.com/post/england-wales-suicide-trends-a-2024-deep-dive |
| Statista — Suicide Rate by Gender (E&W) | Historical gender comparison data | https://www.statista.com/statistics/282203/suicide-rate-in-the-united-kingdom-uk-since-2000-by-gender/ |
| ONS — Self-Harm & Suicide by Sexual Orientation | LGBTQ+ suicide data | https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/mentalhealth/bulletins/selfharmandsuicidebysexualorientationenglandandwales/march2021todecember2023 |

---

## 9. Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python (Pandas, Matplotlib, Seaborn) | Data cleaning, EDA, and chart generation |
| Chart.js (JavaScript) | Interactive dashboard visualisations |
| HTML / CSS | Custom dashboard UI (responsive, dark theme) |
| Jupyter Notebook | Analysis documentation and pipeline |
| GitHub + Vercel | Portfolio hosting, version control, auto-deployment |
| python-docx / python-pptx | Word report and PowerPoint generation |
| Power BI | Considered for NHS relevance; Chart.js chosen for live web deployment |

> **Portfolio Note:** The final dashboard is deployed as a live web application at [the-silent-burden.vercel.app](https://the-silent-burden.vercel.app), using Chart.js for interactive visualisations. Power BI is widely used across the NHS and remains relevant for that sector.

---

## 10. Deliverables

- [x] Cleaned, merged UK dataset (7 CSVs: ONS, NHS Digital, NISRA, Samaritans, IMD)
- [x] EDA notebooks with visualisations (3 Jupyter notebooks + generate_charts.py)
- [x] Regional rate comparison (England regions + four nations)
- [x] Time-series trend chart (2000–2024, male vs female) — in interactive dashboard
- [x] Deprivation correlation scatter plot (IMD score vs male suicide rate by region)
- [x] Age breakdown bar chart — with peak group highlighted (50–54)
- [x] Interactive dashboard (Chart.js, 9 tabs, deployed live on Vercel)
- [x] Written findings report (PDF — The_Silent_Burden_UK_Findings_Report.pdf)
- [x] Presentation slide deck (NHS / public health audience — .pptx)
- [x] GitHub repository with full documentation (README, methodology tab, data sources)
- [x] International comparison (21 countries, WHO data)
- [x] Methods & Means analysis (by age group, safe-messaging compliant)
- [x] Race & Ethnicity deep-dive (IAPT funnel, MHA detention, culturally specific barriers)

---

## 11. Personal Relevance & Context

This project holds personal relevance as someone based in Sutton, London, working as a Senior Vehicle Engineer with Go Ahead London — a bus company whose drivers, engineers, and operational staff reflect many of the demographics most affected by this crisis. The transport sector employs large numbers of men in physically and mentally demanding roles, often with shift patterns, job insecurity, and limited access to mental health support. Understanding this crisis is directly relevant to the people I work alongside every day.

Presenting this analysis through a data analytics lens is also a direct demonstration of skills applicable to NHS data roles — the kind of evidence-based analysis that informs policy, service design, and mental health funding decisions.

---

## 12. Key Sources & References

- [ONS — Suicides in England and Wales 2024](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/suicidesintheunitedkingdom/2024registrations)
- [ONS — Suicides Dataset Reference Tables](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/suicidesintheunitedkingdomreferencetables)
- [Samaritans — Latest Suicide Data](https://www.samaritans.org/about-samaritans/research-policy/suicide-facts-and-figures/latest-suicide-data/)
- [CPRMB — Male Suicide Combined Rates Highest This Century](https://menandboys.org.uk/male-suicide-combined-rates25/)
- [Zero Suicide Alliance — UK Suicide Data Map](https://www.zerosuicidealliance.com/suicide-data-map)
- [House of Commons Library — Suicide Statistics](https://commonslibrary.parliament.uk/research-briefings/cbp-7749/)
- [Men's Health Forum — Key Data Mental Health](https://www.menshealthforum.org.uk/key-data-mental-health)
- [ScienceDirect — Regional Disparities in UK Suicide]