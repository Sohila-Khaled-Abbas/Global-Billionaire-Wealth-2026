<div align="center">

# ⚡ Global Billionaire Wealth to GDP (2026)

### *High-Performance Macroeconomic Analytics & Capital Concentration Intelligence*

<p align="center">
  <a href="powerbi/Global_Billionaire_Wealth_2026.pbip">
    <img src="https://img.shields.io/badge/Power%20BI-PBIP%20Developer%20Mode-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI Developer Mode" />
  </a>
  <a href="powerbi/Global_Billionaire_Wealth_2026.SemanticModel/">
    <img src="https://img.shields.io/badge/Semantic%20Model-TMDL%20Tabular-0078D4?style=for-the-badge&logo=microsoft&logoColor=white" alt="TMDL Semantic Model" />
  </a>
  <a href="docs/business_questions.md">
    <img src="https://img.shields.io/badge/DAX-Dimensional%20Analytics-005A9E?style=for-the-badge&logo=analogue&logoColor=white" alt="DAX Analytics" />
  </a>
  <a href=".github/workflows/ci.yml">
    <img src="https://img.shields.io/badge/CI-Automated%20Audit%20Passing-10B981?style=for-the-badge&logo=githubactions&logoColor=white" alt="CI Status" />
  </a>
  <a href="https://www.kaggle.com/datasets/kanchana1990/global-billionaire-wealth-to-gdp-2026/data">
    <img src="https://img.shields.io/badge/Kaggle-Dataset%20kanchana1990-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Dataset" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-6366F1?style=for-the-badge" alt="MIT License" />
  </a>
</p>

<p align="center">
  <b>An enterprise-grade Power BI dimensional model (PBIP / TMDL) evaluating $19.64 Trillion in private wealth across 3,384 fortunes and 80 sovereign economies.</b>
</p>

</div>

---

## ⚡ At a Glance

<div align="center">

| 💰 Cumulative Wealth | 👥 Total Fortunes | 🌍 Sovereign States | 🚀 Self-Made Ratio | 💻 Dominant Sector | 🏛️ Top Sovereign Concentration |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$19.64T** | **3,384** | **80** | **66.6%** | **Technology ($4.75T)** | **USA (29.0% GDP)** |

</div>

```
Global Capital Distribution by Top 5 Economic Powers
────────────────────────────────────────────────────────────────────────────────
🇺🇸 United States │ ████████████████████████████████████████  $8.34T  (978 Titans)
🇨🇳 China         │ ██████████                                $2.13T  (528 Titans)
🇮🇳 India         │ █████                                     $0.99T  (225 Titans)
🇩🇪 Germany       │ █████                                     $0.99T  (212 Titans)
🇷🇺 Russia        │ ███                                       $0.65T  (149 Titans)
────────────────────────────────────────────────────────────────────────────────
```

---

## 🧭 Navigation

- [Executive Summary](#-executive-summary)
- [Dimensional Semantic Model & Schema](#-dimensional-semantic-model--schema)
- [Data Pipeline & Normalization Architecture](#-data-pipeline--normalization-architecture)
- [Power Query Engineering & QA Audit Framework](#-power-query-engineering--qa-audit-framework)
- [Macroeconomic Concentration Framework](#-macroeconomic-concentration-framework)
- [DAX Measure Intelligence](#-dax-measure-intelligence)
- [Repository Map](#-repository-map)
- [Quickstart & Reproduction](#-quickstart--reproduction)
- [Documentation Suite](#-documentation-suite)
- [Data Source & Attribution](#-data-source--attribution)

---

## 🎯 Executive Summary

The **Global Billionaire Wealth to GDP (2026)** analytics suite provides an executive-ready, data-engineered exploration into ultra-high-net-worth capital concentration. By marrying individual net worth figures from Forbes Real-Time disclosures with macroeconomic output metrics from the World Bank, the model measures national financial exposure, industrial hegemony, and the velocity of wealth generation.

> [!NOTE]
> **Macroeconomic Lens**: Comparing total billionaire wealth (a cumulative capital *stock*) against annual nominal GDP (an annual economic *flow*) establishes a standardized yardstick to quantify oligarchic concentration, tax jurisdiction migration, and national wealth inequality.

### 💡 High-Impact Takeaways

1. **The American Wealth Hegemony**: The United States accounts for **42.5%** of all global billionaire net worth ($8.34 Trillion across 978 individuals), equivalent to **29.0%** of total US GDP.
2. **The Tech Value Engine**: Technology generates **$4.75 Trillion** across 468 individuals—averaging **$10.16 Billion** per billionaire, eclipsing all traditional sectors in compounding velocity.
3. **The Self-Made Paradigm**: **66.6%** of worldwide billionaires built their fortunes from scratch. In China, that number reaches an extraordinary **97.2%**, contrasting starkly with legacy family dynasties in Germany (**26.9%** self-made) and France (**46.3%** self-made).
4. **Sovereign Outliers**: Jurisdictions offering citizenship-by-investment or financial safe-havens show wealth-to-GDP ratios exceeding 100%: **St. Kitts & Nevis (860.7%)**, **Eswatini (362.6%)**, **Cyprus (148.7%)**, **Belize (114.8%)**, and **Hong Kong SAR (103.9%)**.

---

## 🏛️ Dimensional Semantic Model & Schema

The Power BI Semantic Model implements a star/snowflake dimensional model authored in TMDL. The architecture separates clean descriptive dimensions (`DimCountry`, `DimIndustry`) from granular individual and national facts (`FactBillionaire`, `FactCountrySnapshot`).

<div align="center">

### 📊 Relational Entity-Relationship Diagram (ERD)

<p align="center">
  <img src="assets/erd-diagram.png" alt="Relational Semantic Model ERD" width="820" />
</p>

### 📐 High-Level Dimensional Architecture

<p align="center">
  <img src="assets/datamodeling-diagram.png" alt="Dimensional Modeling Overview" width="550" />
</p>

</div>

### 🧩 Table Catalog & Cardinality

| Table Name | Role | Primary Key | Foreign Keys | Record Count | Description |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`DimCountry`** | Dimension | `iso3` | — | 80 | Standardized sovereign countries and territories (`iso3`, `country`, `wb_country_name`). |
| **`DimIndustry`** | Dimension | `industry` | — | 18 | Standardized global economic industry classifications. |
| **`FactBillionaire`** | Fact | `rank` | `iso3`, `industry` | 3,384 | Granular micro fortunes with age, gender, state, city, net worth, source of wealth, and self-made flag. |
| **`FactCountrySnapshot`** | Fact | `iso3` | `iso3` (1:1 Both) | 80 | Macroeconomic sovereign metrics: GDP, population, total wealth, mean/median wealth, and wealth tiers. |
| **`_Measures`** | Measure Home | — | — | — | Centralized repository for all DAX measures (`Billionaire Count`, `Total Wealth USD`). |

---

## ⚙️ Data Pipeline & Normalization Architecture

To ensure high data integrity and prevent many-to-many Cartesian explosion, the data pipeline implements dedicated normalization bridges:

<div align="center">

### 🔀 Multi-Industry Parsing & Normalization Pipeline

<p align="center">
  <img src="assets/industry-diagram.png" alt="Industry Bridge & Normalization Flow" width="380" />
</p>

### 🛡️ Country Key & Referential Integrity Verification

<p align="center">
  <img src="assets/relationships-diagram.png" alt="Country Key ISO3 Validation Flow" width="650" />
</p>

</div>

---

## 🔍 Power Query Engineering & QA Audit Framework

The Power BI project incorporates a structured Power Query ETL pipeline organized into 7 query groups:

- **`00_Parameters & Functions`**: Centralized configuration (`p_DataFolderPath`, `p_SnapshotDate`) and re-usable text standardization functions (`fn_StandardizeCountry`, `fn_ParseIndustries`).
- **`01_Source`**: Parameterized raw CSV connectors (`src_BillionaireIndividual`, `src_BillionaireCountry`).
- **`02_Staging`**: Type-coerced and validated staging queries (`stg_BillionaireIndividual`, `stg_BillionaireCountry`).
- **`03_Transformations`**: Industry bridge table generation (`int_BillionaireIndustryBridge`, `int_IndustryLookup`).
- **`04_DataModel`**: Production dimension and fact tables (`DimCountry`, `DimIndustry`, `FactBillionaire`, `FactCountrySnapshot`).
- **`05_QA & Reconciliation`**: 17 automated audit queries verifying key uniqueness, zero orphaned foreign keys, rank consistency, and balance sheet reconciliation ($19.64 Trillion exact match).
- **`99_Archive`**: Legacy and staging archive tables.

---

## 🌐 Macroeconomic Concentration Framework

Sovereign states are categorized across five distinct wealth-to-GDP tiers, illustrating contrasting economic models and fiscal exposure:

<div align="center">

| Tier Classification | Wealth-to-GDP % | Sovereign Count | Representative Jurisdictions | Economic Characteristics |
| :--- | :---: | :---: | :--- | :--- |
| 🚨 **Extreme** | $\ge 40\%$ | 9 | St. Kitts & Nevis (860.7%), Cyprus (148.7%), HK (103.9%), Israel (42.4%) | Capital sanctuaries, financial hubs, and citizenship-by-investment states. |
| 🔥 **Very High** | $20\%\text{ to }<40\%$ | 12 | United States (29.0%), Russia (30.1%), India (25.3%), Germany (21.0%) | Major industrial superpowers with massive domestic billionaire conglomerates. |
| ⚡ **High** | $10\%\text{ to }<20\%$ | 21 | China (11.4%), France (18.7%), Canada (19.8%), Brazil (12.1%) | Diversified large economies with balanced corporate distributions. |
| 🌿 **Moderate** | $3\%\text{ to }<10\%$ | 29 | United Kingdom (7.3%), Japan (5.4%), South Korea (8.7%), Turkey (8.4%) | Advanced OECD economies with distributed corporate equity ownership. |
| 💧 **Low** | $< 3\%$ | 9 | Netherlands (2.9%), Saudi Arabia (2.1%), Poland (1.6%), South Africa (1.9%) | Resource economies with sovereign wealth funds or emerging corporate sectors. |

</div>

---

## 🧠 DAX Measure Intelligence

Key analytical formulas implemented in the semantic layer:

### 1. Total Filtered Billionaire Count
```dax
Billionaire Count = 
COUNTROWS(FactBillionaire)
```

### 2. Cumulative Billionaire Net Worth ($ USD)
```dax
Total Billionaire Wealth USD = 
SUM(FactBillionaire[net_worth_usd])
```

### 3. Weighted Wealth-to-GDP Concentration Ratio
```dax
Billionaire Wealth to GDP % = 
VAR TotalWealthUSD = SUM(FactCountrySnapshot[total_wealth_usd])
VAR NationalGDP = AVERAGE(FactCountrySnapshot[gdp_usd])
RETURN
    DIVIDE(TotalWealthUSD, NationalGDP, 0) * 100
```

### 4. Self-Made Entrepreneurial Share
```dax
Self-Made Ratio % = 
VAR TotalCount = COUNTROWS(FactBillionaire)
VAR SelfMadeCount = 
    CALCULATE(
        COUNTROWS(FactBillionaire),
        FactBillionaire[self_made] = TRUE()
    )
RETURN
    DIVIDE(SelfMadeCount, TotalCount, 0) * 100
```

### 5. Per-Capita Billionaire Density
```dax
Billionaires Per Million Pop = 
VAR TotalBillionaires = SUM(FactCountrySnapshot[billionaire_count])
VAR TotalPopulation = AVERAGE(FactCountrySnapshot[population])
RETURN
    DIVIDE(TotalBillionaires, (TotalPopulation / 1000000), 0)
```

---

## 📂 Repository Map

```
Global-Billionaire-Wealth-2026/
├── .github/                                # GitHub automation & templates
│   ├── ISSUE_TEMPLATE/                     # Structured issue templates
│   │   ├── bug_report.md                   # Bug reporting form
│   │   ├── config.yml                      # Template links configuration
│   │   ├── data_inquiry.md                 # Methodology inquiries
│   │   └── feature_request.md              # New feature proposals
│   ├── workflows/                          # GitHub Actions CI
│   │   └── ci.yml                          # Automated data integrity & model test
│   └── pull_request_template.md            # PR review checklist
├── assets/                                 # Architectural & schema diagram renders
│   ├── datamodeling-diagram.png            # Dimensional model layout (Dim -> Fact)
│   ├── erd-diagram.png                     # Full semantic entity-relationship diagram
│   ├── industry-diagram.png                # Industry normalization bridge flow
│   ├── mermaid-diagram.png                 # Canonical ERD schema capture
│   └── relationships-diagram.png           # Country key validation & reconciliation
├── data/                                   # Data assets
│   └── raw/                                # Raw immutable datasets
│       ├── billionaire_country_aggregate_2026.csv  # 80 countries aggregate data
│       └── billionaire_individual_2026.csv         # 3,384 individuals data
├── docs/                                   # Deep documentation suite
│   ├── business_questions.md               # 8+ macroeconomic research questions
│   ├── data_dictionary.md                  # Complete dimensional schema dictionary
│   ├── data_quality_log.md                 # Audit logs & Power Query QA checks
│   └── methodology_and_limitations.md      # Valuation & macro limitations
├── exports/                                # Presentation exports & captures
│   ├── published_assets/                   # PDF/PPT deck outputs
│   ├── report_screenshots/                 # Power BI canvas captures
│   └── README.md                           # Exports folder manifest & guidelines
├── powerbi/                                # Power BI Project (PBIP Developer Mode)
│   ├── Global_Billionaire_Wealth_2026.pbip # Main project launchpad
│   ├── Global_Billionaire_Wealth_2026.Report/       # Visual page definitions & layout
│   └── Global_Billionaire_Wealth_2026.SemanticModel/ # TMDL tabular model & schemas
│       └── definition/
│           ├── tables/                     # DimCountry, DimIndustry, FactBillionaire, etc.
│           ├── database.tmdl
│           ├── expressions.tmdl            # Staging, QA & transformation M-queries
│           ├── model.tmdl                  # Query groups & model metadata
│           └── relationships.tmdl          # Star-schema relationships
├── scripts/                                # Automation & validation scripts
│   └── validate_data.py                    # Cross-platform data & PBIP integrity suite
├── .gitattributes                          # Git LF normalization & TMDL rules
├── .gitignore                              # PBIP, Python, and OS ignore rules
├── CONTRIBUTING.md                         # Contribution guide & DAX standards
├── CODE_OF_CONDUCT.md                      # Community code of conduct
├── requirements-dev.txt                    # CI & Python test dependencies
├── README.md                               # Project homepage
└── SECURITY.md                             # Security & vulnerability reporting
```

---

## 🚀 Quickstart & Reproduction

### Prerequisites
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (PBIP Developer Mode enabled)
- [Git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/) (optional, for validation tests)

### 3-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Global-Billionaire-Wealth-2026.git
cd Global-Billionaire-Wealth-2026

# 2. Run data integrity & semantic model validation
python scripts/validate_data.py

# 3. Launch Power BI Developer Project
# Open 'powerbi/Global_Billionaire_Wealth_2026.pbip' in Power BI Desktop
```

---

## 📖 Documentation Suite

Deep-dive documentation available in [`docs/`](docs/):

| Resource | Scope & Purpose |
| :--- | :--- |
| 📘 [Data Dictionary](docs/data_dictionary.md) | Full dimensional schema dictionary (`DimCountry`, `DimIndustry`, `FactBillionaire`, `FactCountrySnapshot`). |
| ❓ [Business Questions](docs/business_questions.md) | Detailed analysis of 8 core macroeconomic research questions with DAX formulations. |
| 🛡️ [Data Quality Log](docs/data_quality_log.md) | Audit logs, Power Query QA queries, fallen billionaire handling, and outlier registry. |
| 🔬 [Methodology & Limitations](docs/methodology_and_limitations.md) | Economic stock vs. flow analysis, residency distortions, and valuation constraints. |

---

## 📜 Data Source & Attribution

- **Raw Data Source**: [Kaggle: Global Billionaire Wealth to GDP (2026)](https://www.kaggle.com/datasets/kanchana1990/global-billionaire-wealth-to-gdp-2026/data) curated by **kanchana1990**.
- **Wealth Disclosures**: Forbes Real-Time Billionaires Index (April 2026).
- **Macroeconomic Indicators**: The World Bank Group (World Development Indicators: Nominal GDP in USD & National Population).

> [!NOTE]
> **Macroeconomic Vintage & Reference Years**: Country-level GDP and population values use the most recent available source data incorporated into the April 10, 2026 analytical snapshot. GDP reference years vary by country. Liechtenstein has a 2022 GDP observation and is retained as a documented historical-vintage exception pending source-level verification. Original source values are preserved to maintain reproducibility.

---

<div align="center">

**Built with Power BI Developer Mode (PBIP) • Tabular Model Definition Language (TMDL)**

*Crafted for Data Analysts, BI Engineers, and Macroeconomists.*

</div>
