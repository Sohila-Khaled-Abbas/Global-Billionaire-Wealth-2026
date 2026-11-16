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
    <img src="https://img.shields.io/badge/DAX-Advanced%20Analytics-005A9E?style=for-the-badge&logo=analogue&logoColor=white" alt="DAX Analytics" />
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
  <b>A modern business intelligence and macro-financial model dissecting $19.64 Trillion in private capital across 3,384 fortunes and 80 sovereign economies.</b>
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
- [System Architecture & Data Flow](#-system-architecture--data-flow)
- [Relational Data Model (ERD)](#-relational-data-model-erd)
- [Macro Concentration Landscape](#-macro-concentration-landscape)
- [Capital Origin Dynamics](#-capital-origin-dynamics)
- [DAX Measure Intelligence](#-dax-measure-intelligence)
- [Repository Map](#-repository-map)
- [Quickstart & Reproduction](#-quickstart--reproduction)
- [Data Governance & Documentation](#-data-governance--documentation)
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

## 🏗️ System Architecture & Data Flow

A streamlined, modern data pipeline transforming raw source dumps into interactive Power BI artifacts:

```mermaid
flowchart TD
    classDef sourceStyle fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#F8FAFC,rx:8,ry:8;
    classDef storageStyle fill:#0F172A,stroke:#F59E0B,stroke-width:2px,color:#F8FAFC,rx:8,ry:8;
    classDef engineStyle fill:#1E1E38,stroke:#10B981,stroke-width:2px,color:#F8FAFC,rx:8,ry:8;
    classDef semanticStyle fill:#2A1B4E,stroke:#A855F7,stroke-width:2px,color:#F8FAFC,rx:8,ry:8;
    classDef presentationStyle fill:#3B1124,stroke:#F43F5E,stroke-width:2px,color:#F8FAFC,rx:8,ry:8;

    subgraph S1["🌐 1. Ingestion Layer"]
        A1["📦 Kaggle Raw Dataset<br/>kanchana1990/global-billionaire-wealth-2026"]:::sourceStyle
        A2["⚡ Forbes Real-Time Index<br/>Net Worth • Industry • Demographics"]:::sourceStyle
        A3["🏛️ World Bank Indicators<br/>Nominal GDP • Population"]:::sourceStyle
    end

    subgraph S2["💾 2. Raw Data Assets"]
        B1[("📄 billionaire_individual_2026.csv<br/>3,384 Records • 25 Columns")]:::storageStyle
        B2[("📄 billionaire_country_aggregate_2026.csv<br/>80 Jurisdictions • 23 Columns")]:::storageStyle
    end

    subgraph S3["⚙️ 3. Power Query & M Engine"]
        C1["🧹 Type Casting & Normalization<br/>Int64, Double, Boolean, Text"]:::engineStyle
        C2["🔍 Edge Case Treatment<br/>Zero-Net-Worth Fallen Billionaires"]:::engineStyle
    end

    subgraph S4["🧠 4. Semantic Layer (TMDL / PBIP)"]
        D1["📊 Country Aggregate Dimension (1)"]:::semanticStyle
        D2["👥 Individual Billionaire Fact (*)"]:::semanticStyle
        D3["📐 High-Performance DAX Measures<br/>Wealth-to-GDP • Density • Oligarchy Index"]:::semanticStyle
    end

    subgraph S5["📊 5. Analytical Visual Canvas"]
        E1["🗺️ Geographic Exposure Maps"]:::presentationStyle
        E2["🌲 Sector Dominance Treemaps"]:::presentationStyle
        E3["⚖️ Self-Made vs. Inherited Quadrants"]:::presentationStyle
        E4["📈 Demographic Age & Gender Matrix"]:::presentationStyle
    end

    A1 --> B1
    A2 --> B1
    A3 --> B2
    B1 --> C1
    B2 --> C1
    C1 --> D1
    C1 --> D2
    C2 --> D1
    C2 --> D2
    D1 -->|"1 to Many: country"| D2
    D1 --> D3
    D2 --> D3
    D3 --> E1
    D3 --> E2
    D3 --> E3
    D3 --> E4
```

---

## 🧩 Relational Data Model (ERD)

The Power BI Semantic Model enforces a clean, high-performance dimensional schema connected via a single-column 1-to-Many (`1..*`) relationship on the `country` key.

```mermaid
erDiagram
    billionaire_country_aggregate_2026 ||--o{ billionaire_individual_2026 : "country"

    billionaire_country_aggregate_2026 {
        int country_wealth_rank PK "Global wealth rank"
        string country FK "Country common name"
        string iso3 "ISO 3166-1 alpha-3 code"
        string wb_country_name "Standardized World Bank name"
        int billionaire_count "Total resident billionaires"
        double total_wealth_usd_m "Aggregate wealth in USD Millions"
        int64 total_wealth_usd "Aggregate wealth in absolute USD"
        double mean_wealth_usd_m "Mean net worth in USD Millions"
        double median_wealth_usd_m "Median net worth in USD Millions"
        double max_wealth_usd_m "Top billionaire net worth in USD Millions"
        string top_billionaire "Wealthiest resident individual"
        string dominant_industry_by_wealth "Leading industry sector"
        int self_made_count "Count of self-made individuals"
        double self_made_ratio_pct "Self-made proportion percentage"
        double mean_age "Average age of billionaires"
        double country_wealth_gdp_pct "Total wealth as percent of national GDP"
        double billionaires_per_million_pop "Billionaire density per million residents"
        string wealth_concentration_tier "Macro exposure classification"
        double gdp_per_billionaire_bn "National GDP per billionaire in USD Billions"
        double sector_dominance_score "Primary sector concentration score"
        double gdp_usd "Annual nominal GDP in USD"
        int64 population "Total national population"
        int gdp_year "GDP reference baseline year"
    }

    billionaire_individual_2026 {
        int rank PK "Global individual wealth rank"
        string person_name "Full name of billionaire or family"
        string gender "Gender classification"
        float age "Age in years"
        string country FK "Primary economic country"
        string iso3 "ISO 3166-1 alpha-3 code"
        string wb_country_name "Standardized World Bank name"
        string state "State or province"
        string city "City of primary residence"
        double net_worth_usd_m "Net worth in USD Millions"
        int64 net_worth_usd "Net worth in absolute USD"
        string source_of_wealth "Primary company or asset origin"
        string industries "Reported industry sector"
        string primary_industry "Standardized industry category"
        boolean self_made "Self-made or Inherited flag"
        double wealth_gdp_ratio_pct "Individual net worth as percent of GDP"
        double wealth_per_citizen_usd "Per-capita equivalent dividend"
        double wealth_country_share_pct "Share of national billionaire wealth"
        double sector_dominance_score "Sector dominance benchmark"
        double gdp_usd "Country GDP in USD"
        int64 population "Country population"
        int gdp_year "GDP reference year"
        string forbes_uri "Forbes profile slug identifier"
        string scrape_timestamp "Data capture timestamp"
        float birth_year "Inferred year of birth"
    }
```

---

## 🌐 Macro Concentration Landscape

Sovereign states are categorized across five distinct wealth-to-GDP tiers, illustrating contrasting economic models and fiscal exposure:

```mermaid
flowchart LR
    classDef extreme fill:#450A0A,stroke:#EF4444,stroke-width:2px,color:#FEE2E2,rx:8,ry:8;
    classDef veryHigh fill:#431407,stroke:#F97316,stroke-width:2px,color:#FFEDD5,rx:8,ry:8;
    classDef high fill:#362B05,stroke:#EAB308,stroke-width:2px,color:#FEF9C3,rx:8,ry:8;
    classDef moderate fill:#064E3B,stroke:#10B981,stroke-width:2px,color:#D1FAE5,rx:8,ry:8;
    classDef low fill:#0C4A6E,stroke:#0EA5E9,stroke-width:2px,color:#E0F2FE,rx:8,ry:8;

    T1["🚨 Extreme Tier<br/>40% or more of GDP<br/>9 Jurisdictions<br/>St. Kitts, Cyprus, HK, Israel"]:::extreme
    T2["🔥 Very High Tier<br/>20% to 40% of GDP<br/>12 Nations<br/>USA, Russia, India, Germany"]:::veryHigh
    T3["⚡ High Tier<br/>10% to 20% of GDP<br/>21 Nations<br/>China, France, Canada, Brazil"]:::high
    T4["🌿 Moderate Tier<br/>3% to 10% of GDP<br/>29 Nations<br/>UK, Japan, South Korea, Turkey"]:::moderate
    T5["💧 Low Tier<br/>Under 3% of GDP<br/>9 Nations<br/>Netherlands, Saudi Arabia, Poland"]:::low

    T1 --> T2 --> T3 --> T4 --> T5
```

---

## 🧬 Capital Origin Dynamics

```mermaid
flowchart TD
    classDef selfMadeStyle fill:#064E3B,stroke:#10B981,stroke-width:2px,color:#ECFDF5,rx:8,ry:8;
    classDef inheritedStyle fill:#3B0764,stroke:#C084FC,stroke-width:2px,color:#FAF5FF,rx:8,ry:8;
    classDef rootStyle fill:#0F172A,stroke:#64748B,stroke-width:2px,color:#F8FAFC,rx:8,ry:8;

    R["🌍 3,384 Global Fortunes: $19.64 Trillion"]:::rootStyle
    
    R --> S["🚀 Self-Made Fortunes<br/>66.6% Share • 2,255 Billionaires<br/>Tech Founders & Industrialists"]:::selfMadeStyle
    R --> I["🏛️ Inherited Fortunes<br/>33.4% Share • 1,129 Billionaires<br/>Multi-Generational Wealth Dynasties"]:::inheritedStyle

    S --> SC["🇨🇳 China: 97.2% Self-Made<br/>🇷🇺 Russia: 94.0% Self-Made<br/>🇺🇸 USA: 72.2% Self-Made"]:::selfMadeStyle
    I --> IC["🇩🇪 Germany: 73.1% Inherited<br/>🇪🇸 Spain: 75.0% Inherited<br/>🇫🇷 France: 53.7% Inherited"]:::inheritedStyle
```

---

## 🧠 DAX Measure Intelligence

Key analytical formulas implemented in the semantic layer:

### 1. Cumulative Billionaire Net Worth ($M)
```dax
Total Billionaire Wealth ($M) = 
SUM(billionaire_individual_2026[net_worth_usd_m])
```

### 2. Weighted Wealth-to-GDP Concentration Ratio
```dax
Billionaire Wealth to GDP % = 
VAR TotalWealthUSD = SUM(billionaire_country_aggregate_2026[total_wealth_usd])
VAR NationalGDP = AVERAGE(billionaire_country_aggregate_2026[gdp_usd])
RETURN
    DIVIDE(TotalWealthUSD, NationalGDP, 0) * 100
```

### 3. Self-Made Entrepreneurial Share
```dax
Self-Made Ratio % = 
VAR TotalCount = COUNTROWS(billionaire_individual_2026)
VAR SelfMadeCount = 
    CALCULATE(
        COUNTROWS(billionaire_individual_2026),
        billionaire_individual_2026[self_made] = TRUE()
    )
RETURN
    DIVIDE(SelfMadeCount, TotalCount, 0) * 100
```

### 4. Per-Capita Billionaire Density
```dax
Billionaires Per Million Pop = 
VAR TotalBillionaires = SUM(billionaire_country_aggregate_2026[billionaire_count])
VAR TotalPopulation = AVERAGE(billionaire_country_aggregate_2026[population])
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
│   ├── workflows/                          # GitHub Actions workflows
│   │   └── ci.yml                          # Data integrity & PBIP validation
│   └── pull_request_template.md            # PR review checklist
├── assets/                                 # Visual media & architecture renders
│   └── mermaid-diagram.png                 # Exported diagram image
├── data/                                   # Data assets
│   └── raw/                                # Raw immutable datasets
│       ├── billionaire_country_aggregate_2026.csv  # 80 countries aggregate data
│       └── billionaire_individual_2026.csv         # 3,384 individuals data
├── docs/                                   # Deep documentation suite
│   ├── business_questions.md               # 8+ macroeconomic research questions
│   ├── data_dictionary.md                  # Complete 48-field data dictionary
│   ├── data_quality_log.md                 # Validation audit & anomaly log
│   └── methodology_and_limitations.md      # Valuation & macro limitations
├── exports/                                # Presentation exports & captures
│   ├── published_assets/                   # PDF/PPT deck outputs
│   └── report_screenshots/                 # Power BI canvas captures
├── powerbi/                                # Power BI Project (PBIP Developer Mode)
│   ├── Global_Billionaire_Wealth_2026.pbip # Main project launchpad
│   ├── Global_Billionaire_Wealth_2026.Report/       # Visual page definitions & JSON
│   └── Global_Billionaire_Wealth_2026.SemanticModel/ # TMDL tabular model & schemas
├── scripts/                                # Automation & validation scripts
│   └── validate_data.py                    # Cross-platform data integrity test
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

# 2. Run data integrity & schema validation
python scripts/validate_data.py

# 3. Launch Power BI Developer Project
# Open 'powerbi/Global_Billionaire_Wealth_2026.pbip' in Power BI Desktop
```

---

## 📖 Data Governance & Documentation

Deep-dive documentation available in [`docs/`](docs/):

| Resource | Scope & Purpose |
| :--- | :--- |
| 📘 [Data Dictionary](docs/data_dictionary.md) | Full 48-column schema definitions, data types, null rules, and tier descriptions. |
| ❓ [Business Questions](docs/business_questions.md) | Detailed analysis of 8 core macroeconomic research questions with DAX formulations. |
| 🛡️ [Data Quality Log](docs/data_quality_log.md) | Audit logs, reconciliation verification, fallen billionaire handling, and outlier registry. |
| 🔬 [Methodology & Limitations](docs/methodology_and_limitations.md) | Economic stock vs. flow analysis, residency distortions, and valuation constraints. |

---

## 📜 Data Source & Attribution

- **Raw Data Source**: [Kaggle: Global Billionaire Wealth to GDP (2026)](https://www.kaggle.com/datasets/kanchana1990/global-billionaire-wealth-to-gdp-2026/data) curated by **kanchana1990**.
- **Wealth Disclosures**: Forbes Real-Time Billionaires Index (April 2026).
- **Macroeconomic Indicators**: The World Bank Group (World Development Indicators: Nominal GDP in USD & National Population).

---

<div align="center">

**Built with Power BI Developer Mode (PBIP) • Tabular Model Definition Language (TMDL)**

*Crafted for Data Analysts, BI Engineers, and Macroeconomists.*

</div>
