"""
The Silent Burden — UK Male Suicide Project
Chart Generator  |  Analyst: Kudzanayi Shepherd Mhlanga

Reads from ./data/clean/ and ./data/ and writes 8 PNG charts to ./data/charts/
Usage:  python generate_charts.py
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CLEAN  = "./data/clean"
RAW    = "./data"
CHARTS = "./data/charts"
os.makedirs(CHARTS, exist_ok=True)

# Palette
TEAL  = "#00b4d8"
CORAL = "#e63946"
GREY  = "#6c757d"
DARK  = "#1a1a2e"
GOLD  = "#ffd166"
GREEN = "#06d6a0"

def save(fig, name):
    path = os.path.join(CHARTS, name)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  OK  {name}")


# ══════════════════════════════════════════════════════════════════════════════
# 1  HEADLINE TRENDS  (England & Wales, 2000–2024)
# ══════════════════════════════════════════════════════════════════════════════
def chart01():
    df = pd.read_csv(f"{CLEAN}/ons_ew_annual_clean.csv")
    df = df[df["year"].between(2000, 2024)]

    fig, ax = plt.subplots(figsize=(12, 6), facecolor=DARK)
    ax.set_facecolor(DARK)

    ax.plot(df["year"], df["male_rate"],   color=TEAL,  lw=2.5, label="Male rate")
    ax.plot(df["year"], df["female_rate"], color=CORAL, lw=2.0, linestyle="--", label="Female rate")

    periods = [
        (2000, 2007, "#1a1a2e", 0.40, "Pre-crisis"),
        (2008, 2013, "#2d1b1b", 0.50, "Fin. crisis + austerity"),
        (2014, 2019, "#1a2d1b", 0.40, "Recovery period"),
        (2020, 2021, "#2d2d1b", 0.60, "COVID-19"),
        (2022, 2024, "#2d1b2d", 0.50, "Post-COVID rise"),
    ]
    for start, end, col, alpha, label in periods:
        ax.axvspan(start, end, color=col, alpha=alpha)

    # Annotate peak
    peak_row = df.loc[df["male_rate"].idxmax()]
    ax.annotate(
        f"Peak {int(peak_row['year'])}\n{peak_row['male_rate']:.1f}",
        xy=(peak_row["year"], peak_row["male_rate"]),
        xytext=(peak_row["year"] - 4, peak_row["male_rate"] + 0.9),
        color=GOLD, fontsize=8,
        arrowprops=dict(arrowstyle="->", color=GOLD)
    )
    # Annotate 2024
    val_2024 = df.loc[df["year"] == 2024, "male_rate"].values[0]
    ax.annotate(
        f"2024: {val_2024:.1f}",
        xy=(2024, val_2024), xytext=(2019, val_2024 + 0.8),
        color=TEAL, fontsize=8,
        arrowprops=dict(arrowstyle="->", color=TEAL)
    )

    ax.set_xlabel("Year", color="white")
    ax.set_ylabel("Rate per 100,000", color="white")
    ax.set_title("UK Male vs Female Suicide Rate  2000–2024", color="white", fontsize=14, pad=12)
    ax.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax.spines.values()]
    ax.legend(facecolor="#222", labelcolor="white", fontsize=9)
    ax.grid(color="#333", linestyle="--", linewidth=0.5)

    save(fig, "01_headline_trends.png")


# ══════════════════════════════════════════════════════════════════════════════
# 2  AGE GROUP BREAKDOWN
# ══════════════════════════════════════════════════════════════════════════════
def chart02():
    df = pd.read_csv(f"{CLEAN}/age_analysis_clean.csv")
    df = df.sort_values("male_rate", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 7), facecolor=DARK)
    ax.set_facecolor(DARK)

    bar_colors = [CORAL if row["is_peak"] == True or str(row["is_peak"]) == "True"
                  else GOLD if row["abs_risk_flag"] == "Very High"
                  else TEAL
                  for _, row in df.iterrows()]

    bars = ax.barh(df["age_group"], df["male_rate"], color=bar_colors, alpha=0.85)
    for bar in bars:
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():.1f}", va="center", color="white", fontsize=9)

    ax.set_xlabel("Rate per 100,000", color="white")
    ax.set_title("Male Suicide Rate by Age Group — England & Wales 2024", color="white",
                 fontsize=13, pad=10)
    ax.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax.spines.values()]
    ax.grid(axis="x", color="#333", linestyle="--", linewidth=0.5)

    patches = [
        mpatches.Patch(color=CORAL, label="Peak age group (50–54)"),
        mpatches.Patch(color=GOLD,  label="Very High risk"),
        mpatches.Patch(color=TEAL,  label="Other age groups"),
    ]
    ax.legend(handles=patches, facecolor="#222", labelcolor="white", fontsize=9)
    save(fig, "02_age_groups.png")


# ══════════════════════════════════════════════════════════════════════════════
# 3  REGIONAL BREAKDOWN (England)
# ══════════════════════════════════════════════════════════════════════════════
def chart03():
    df = pd.read_csv(f"{CLEAN}/regions_imd_clean.csv")
    df = df.sort_values("male_rate", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 7), facecolor=DARK)
    ax.set_facecolor(DARK)

    max_r = df["male_rate"].max()
    min_r = df["male_rate"].min()
    colors = [CORAL if r == max_r else GREEN if r == min_r else TEAL
              for r in df["male_rate"]]

    bars = ax.barh(df["region"], df["male_rate"], color=colors, alpha=0.85)
    for bar in bars:
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():.1f}", va="center", color="white", fontsize=9)

    ax.set_xlabel("Rate per 100,000", color="white")
    ax.set_title("Male Suicide Rate by English Region — 2022/23 avg", color="white",
                 fontsize=13, pad=10)
    ax.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax.spines.values()]
    ax.grid(axis="x", color="#333", linestyle="--", linewidth=0.5)

    patches = [
        mpatches.Patch(color=CORAL,  label="Highest"),
        mpatches.Patch(color=GREEN,  label="Lowest"),
        mpatches.Patch(color=TEAL,   label="Other regions"),
    ]
    ax.legend(handles=patches, facecolor="#222", labelcolor="white", fontsize=9)
    save(fig, "03_regional_breakdown.png")


# ══════════════════════════════════════════════════════════════════════════════
# 4  UK NATIONS COMPARISON  (latest year per nation)
# ══════════════════════════════════════════════════════════════════════════════
def chart04():
    df = pd.read_csv(f"{CLEAN}/four_nations_clean.csv")
    latest = df.groupby("nation").last().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6), facecolor=DARK)
    ax.set_facecolor(DARK)

    x = np.arange(len(latest))
    w = 0.35

    ax.bar(x - w/2, latest["male_rate"],   w, label="Male",   color=TEAL,  alpha=0.85)
    ax.bar(x + w/2, latest["female_rate"], w, label="Female", color=CORAL, alpha=0.85)

    for i, (m, f) in enumerate(zip(latest["male_rate"], latest["female_rate"])):
        ax.text(i - w/2, m + 0.3, f"{m:.1f}", ha="center", color="white", fontsize=9)
        ax.text(i + w/2, f + 0.3, f"{f:.1f}", ha="center", color="white", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(latest["nation"], color="white", fontsize=9)
    ax.set_ylabel("Rate per 100,000", color="white")
    ax.set_title("Suicide Rate by UK Nation & Sex — Latest Available Year", color="white",
                 fontsize=13, pad=10)
    ax.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax.spines.values()]
    ax.legend(facecolor="#222", labelcolor="white")
    ax.grid(axis="y", color="#333", linestyle="--", linewidth=0.5)
    save(fig, "04_nations_comparison.png")


# ══════════════════════════════════════════════════════════════════════════════
# 5  DEPRIVATION CORRELATION (scatter — regions)
# ══════════════════════════════════════════════════════════════════════════════
def chart05():
    df = pd.read_csv(f"{CLEAN}/regions_imd_clean.csv")

    fig, ax = plt.subplots(figsize=(10, 7), facecolor=DARK)
    ax.set_facecolor(DARK)

    ax.scatter(df["avg_imd_score"], df["male_rate"], color=TEAL, s=80, alpha=0.85,
               edgecolors="#444", linewidths=0.5)

    for _, row in df.iterrows():
        ax.annotate(row["region"], (row["avg_imd_score"], row["male_rate"]),
                    textcoords="offset points", xytext=(5, 3),
                    color="white", fontsize=7)

    z = np.polyfit(df["avg_imd_score"], df["male_rate"], 1)
    p = np.poly1d(z)
    xs = np.linspace(df["avg_imd_score"].min(), df["avg_imd_score"].max(), 200)
    ax.plot(xs, p(xs), color=CORAL, lw=2, linestyle="--", label="Trend")

    corr = df["avg_imd_score"].corr(df["male_rate"])
    ax.set_xlabel("IMD Score (higher = more deprived)", color="white")
    ax.set_ylabel("Male Suicide Rate per 100,000", color="white")
    ax.set_title(f"Deprivation vs Male Suicide Rate by Region  (r = {corr:.2f})",
                 color="white", fontsize=13, pad=10)
    ax.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax.spines.values()]
    ax.legend(facecolor="#222", labelcolor="white")
    ax.grid(color="#333", linestyle="--", linewidth=0.5)
    save(fig, "05_deprivation_correlation.png")


# ══════════════════════════════════════════════════════════════════════════════
# 6  RISK FACTORS RADAR  (Samaritans general male scores)
# ══════════════════════════════════════════════════════════════════════════════
def chart06():
    df = pd.read_csv(f"{RAW}/samaritans_risk.csv")
    # Use top-8 factors for readability
    df = df.nlargest(8, "general_male_score")
    categories = df["risk_factor"].tolist()
    values = (df["general_male_score"] / 10).tolist()   # normalise to 0–10
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)] + [0]
    values = values + [values[0]]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), facecolor=DARK)
    ax.set_facecolor(DARK)
    fig.patch.set_facecolor(DARK)

    ax.plot(angles, values, color=TEAL, linewidth=2)
    ax.fill(angles, values, color=TEAL, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color="white", size=9)
    ax.set_yticklabels([])
    ax.spines["polar"].set_color("#444")
    ax.grid(color="#444")
    ax.set_title("Male Suicide Risk Factor Intensity\n(Samaritans 2024, top 8 factors)",
                 color="white", fontsize=13, pad=25, y=1.08)
    save(fig, "06_risk_radar.png")


# ══════════════════════════════════════════════════════════════════════════════
# 7  NHS TALKING THERAPIES (IAPT) — ethnicity access & recovery
# ══════════════════════════════════════════════════════════════════════════════
def chart07():
    df = pd.read_csv(f"{CLEAN}/iapt_ethnicity_clean.csv")

    fig, ax1 = plt.subplots(figsize=(12, 7), facecolor=DARK)
    ax1.set_facecolor(DARK)
    ax2 = ax1.twinx()
    ax2.set_facecolor(DARK)

    x = np.arange(len(df))
    w = 0.3

    ax1.bar(x - w, df["referral_index"],       w, color=TEAL,  alpha=0.75,
            label="Referral index (WB=100)")
    ax1.bar(x,     df["treatment_start_index"], w, color=GOLD,  alpha=0.75,
            label="Treatment start index")
    ax2.plot(x,    df["recovery_index"],        color=CORAL, marker="o", lw=2.5,
             label="Recovery index (WB=100)")

    ax1.set_xticks(x)
    ax1.set_xticklabels(df["ethnic_group"], rotation=30, ha="right", color="white", fontsize=8)
    ax1.set_ylabel("Index (White British = 100)", color="white")
    ax2.set_ylabel("Recovery Index", color="white")
    ax1.set_title("NHS Talking Therapies — Access & Recovery by Ethnicity (2022/23)",
                  color="white", fontsize=13, pad=10)
    ax1.tick_params(colors="white")
    ax2.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax1.spines.values()]
    [s.set_edgecolor("#444") for s in ax2.spines.values()]

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, facecolor="#222", labelcolor="white", fontsize=8)
    ax1.grid(axis="y", color="#333", linestyle="--", linewidth=0.5)
    save(fig, "07_iapt_access.png")


# ══════════════════════════════════════════════════════════════════════════════
# 8  SAMARITANS RISK FACTORS (horizontal bar — all factors, general male score)
# ══════════════════════════════════════════════════════════════════════════════
def chart08():
    df = pd.read_csv(f"{RAW}/samaritans_risk.csv")
    df = df.sort_values("general_male_score", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 8), facecolor=DARK)
    ax.set_facecolor(DARK)

    colors = [CORAL if s >= 85 else GOLD if s >= 70 else TEAL
              for s in df["general_male_score"]]
    bars = ax.barh(df["risk_factor"], df["general_male_score"], color=colors, alpha=0.85)

    for bar in bars:
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width()}", va="center", color="white", fontsize=9)

    ax.set_xlabel("Risk Score (0–100)", color="white")
    ax.set_title("Male Suicide Risk Factor Scores — Samaritans 2024", color="white",
                 fontsize=13, pad=10)
    ax.tick_params(colors="white")
    [s.set_edgecolor("#444") for s in ax.spines.values()]
    ax.grid(axis="x", color="#333", linestyle="--", linewidth=0.5)

    patches = [
        mpatches.Patch(color=CORAL, label="Critical risk (≥85)"),
        mpatches.Patch(color=GOLD,  label="High risk (70–84)"),
        mpatches.Patch(color=TEAL,  label="Moderate risk (<70)"),
    ]
    ax.legend(handles=patches, facecolor="#222", labelcolor="white", fontsize=9)
    save(fig, "08_samaritans_risk.png")


# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("The Silent Burden — Chart Generator")
    print("=" * 45)
    steps = [
        ("01 Headline Trends",          chart01),
        ("02 Age Groups",               chart02),
        ("03 Regional Breakdown",       chart03),
        ("04 Nations Comparison",       chart04),
        ("05 Deprivation Correlation",  chart05),
        ("06 Risk Factor Radar",        chart06),
        ("07 IAPT Access",              chart07),
        ("08 Samaritans Risk Scores",   chart08),
    ]
    errors = []
    for label, fn in steps:
        print(f"\n{label}")
        try:
            fn()
        except Exception as e:
            import traceback
            print(f"  ERR  {e}")
            traceback.print_exc()
            errors.append((label, str(e)))

    print("\n" + "=" * 45)
    if errors:
        print(f"Done — {len(errors)} error(s):")
        for lbl, err in errors:
            print(f"  {lbl}: {err}")
    else:
        print(f"All 8 charts saved to {CHARTS}/")
