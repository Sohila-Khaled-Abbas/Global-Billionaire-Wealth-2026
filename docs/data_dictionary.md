# Data Dictionary: Global Billionaire Wealth to GDP (2026)

This document provides complete field-level definitions, data types, primary/foreign keys, validation constraints, and business rules for the Power BI Semantic Model and data pipeline.

---

## 🏛️ Semantic Model Architecture Overview

The analytical model implements a Kimball-style dimensional architecture (Star/Snowflake schema) engineered in Power BI Desktop Developer Mode (`.pbip` / TMDL):

```
                     ┌──────────────────┐
                     │    DimCountry    │
                     │  (80 Countries)  │
                     └────────┬─────────┘
                              │
                    1 : *     │     1 : 1 (Both)
            ┌─────────────────┴─────────────────┐
            ▼                                   ▼
   ┌─────────────────┐                ┌───────────────────┐
   │ FactBillionaire │                │FactCountrySnapshot│
   │ (3,384 Records) │                │   (80 Records)    │
   └────────▲────────┘                └───────────────────┘
            │
            │ * : 1
   ┌────────┴────────┐
   │   DimIndustry   │
   │ (18 Industries) │
   └─────────────────┘
```

---

## 1. Dimension Tables

### A. `DimCountry` (Country Dimension)
- **Primary Grain**: One row per sovereign nation or economic territory.
- **Record Count**: 80 records.
- **Primary Key**: `iso3`

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `iso3` | String (3 chars) | Text | No (PK) | Standard ISO 3166-1 alpha-3 uppercase country identifier. Joins to `FactBillionaire.iso3` and `FactCountrySnapshot.iso3`. |
| `country` | String | Text | No | Standardized common country name (e.g., `United States`, `China`, `Germany`). |
| `wb_country_name` | String | Text | No | Official nation name aligned with World Bank national accounts nomenclature. |

---

### B. `DimIndustry` (Industry Dimension)
- **Primary Grain**: One row per standardized economic sector.
- **Record Count**: 18 industries.
- **Primary Key**: `industry`

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `industry` | String | Text | No (PK) | Standardized primary industrial sector (e.g., `Technology`, `Finance & Investments`, `Fashion & Retail`). Joins to `FactBillionaire.industry`. |

---

## 2. Fact Tables

### A. `FactBillionaire` (Billionaire Fact)
- **Primary Grain**: One row per billionaire individual or family entity.
- **Record Count**: 3,384 records.
- **Foreign Keys**: `iso3` (to `DimCountry`), `industry` (to `DimIndustry`).

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `rank` | Int64 | Whole Number | No | Global wealth rank (1 = richest individual, Elon Musk). |
| `person_name` | String | Text | No | Full legal or publicly recognized name of the billionaire or family group. |
| `gender` | String (1 char) | Text | No | Gender code: `M` (Male, 2,910 records), `F` (Female, 474 records). |
| `age` | Int64 | Whole Number | Yes (48 nulls) | Current age in years. Blank for private individuals with undisclosed birthdates. |
| `birth_year` | Int64 | Whole Number | Yes (48 nulls) | Inferred year of birth (`2026 - age`). |
| `iso3` | String (Hidden) | Text | No (FK) | Foreign key joining to `DimCountry.iso3`. |
| `state` | String | Text | Yes (1,842 nulls) | Administrative state or province (predominantly US and Canadian entries). |
| `city` | String | Text | Yes (49 nulls) | City of primary residence or operational headquarters. |
| `net_worth_usd` | Decimal (Fixed) | Currency | No | Total estimated net worth in absolute US Dollars (USD). |
| `source_of_wealth` | String | Text | No | Primary business, company, or venture originating the fortune (e.g., `Tesla, SpaceX`, `Google`). |
| `industry` | String (Hidden) | Text | No (FK) | Foreign key joining to `DimIndustry.industry`. |
| `self_made` | Boolean | True/False | No | Entrepreneurial classification: `TRUE` = self-made founder/creator; `FALSE` = inherited/dynastic. |
| `snapshot_date` | DateTime (Date) | Date | No | Reference date of the snapshot (`p_SnapshotDate`). |
| `forbes_uri` | String (Hidden) | Text | No | Unique slug identifier for the billionaire's Forbes profile page. |
| `scrape_timestamp` | DateTimeZone (Hidden) | Date/Time/Zone | No | Exact UTC timestamp of data retrieval (`2026-04-10 21:32 UTC`). |

---

### B. `FactCountrySnapshot` (Country Macroeconomic Snapshot)
- **Primary Grain**: One row per sovereign nation/territory.
- **Record Count**: 80 records.
- **Key**: `iso3` (1-to-1 bidirectional relationship with `DimCountry.iso3`).

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `iso3` | String | Text | No (FK/PK) | Standard ISO 3166-1 alpha-3 country identifier. |
| `country_wealth_rank` | Int64 | Whole Number | No | Sovereign rank ordered by cumulative billionaire wealth descending (1 = USA). |
| `billionaire_count` | Int64 | Whole Number | No | Total resident billionaire headcount in the country. |
| `total_wealth_usd_m` | Decimal | Currency | No | Cumulative billionaire net worth in Millions of US Dollars ($M). |
| `total_wealth_usd` | Decimal | Currency | No | Cumulative billionaire net worth in absolute US Dollars (USD). |
| `mean_wealth_usd_m` | Double | Decimal Number | No | Arithmetic average wealth per billionaire ($M). |
| `median_wealth_usd_m` | Double | Decimal Number | No | Median wealth per billionaire ($M). |
| `max_wealth_usd_m` | Double | Decimal Number | No | Net worth of the single wealthiest individual in the country ($M). |
| `top_billionaire` | String | Text | No | Name of the nation's wealthiest citizen. |
| `dominant_industry_by_wealth` | String | Text | No | Sector contributing the highest aggregate wealth in the country. |
| `self_made_count` | Int64 | Whole Number | No | Headcount of self-made billionaires in the country. |
| `self_made_ratio_pct` | Double | Decimal Number | No | Percentage of resident billionaires who are self-made (`self_made_count / billionaire_count * 100`). |
| `mean_age` | Double | Decimal Number | No | Average age of resident billionaires. |
| `country_wealth_gdp_pct` | Double | Decimal Number | No | Total billionaire wealth expressed as a percentage of nominal national GDP. |
| `billionaires_per_million_pop` | Double | Decimal Number | No | Billionaire density per million residents (`billionaire_count / (population / 1,000,000)`). |
| `wealth_concentration_tier` | String | Text | No | Macroeconomic tier: `Extreme (≥40%)`, `Very High (20–40%)`, `High (10–20%)`, `Moderate (3–10%)`, `Low (<3%)`. |
| `gdp_per_billionaire_bn` | Double | Decimal Number | No | National economic output per billionaire (GDP / billionaire_count in $B USD). |
| `sector_dominance_score` | Double | Decimal Number | No | Share of national billionaire wealth held in the single leading sector (%). |
| `gdp_usd` | Decimal | Currency | No | Annual nominal GDP in US Dollars from World Bank. |
| `population` | Int64 | Whole Number | No | Total national population from World Bank. |
| `gdp_year` | Int64 | Whole Number | No | Baseline year of national GDP indicator (2023 or 2024). |
| `snapshot_date` | DateTime (Date) | Date | No | Analytical snapshot date (`p_SnapshotDate`). |

---

## 3. Dedicated Measures Table (`_Measures`)

All analytical DAX metrics are centralized in the `_Measures` table:

| Measure Name | DAX Expression | Formatting | Description |
| :--- | :--- | :--- | :--- |
| `Billionaire Count` | `COUNTROWS(FactBillionaire)` | Whole Number (`#,##0`) | Dynamic count of billionaires based on active filter context. |
| `Total Billionaire Wealth USD` | `SUM(FactBillionaire[net_worth_usd])` | Currency (`$#,##0`) | Aggregate net worth across the filtered population in absolute USD. |

---

## 4. Power Query Parameters & Intermediate Tables

- **`p_DataFolderPath`**: Configurable root path for raw CSV files (`data\raw`).
- **`p_SnapshotDate`**: Parameterized date anchor for time-series modeling.
- **`fn_StandardizeCountry`**: Custom M function standardizing text whitespace and capitalization.
- **`fn_ParseIndustries`**: Custom M function splitting delimited industry strings.
- **`int_BillionaireIndustryBridge`**: Normalized bridge table connecting each billionaire to one or more industries (`person_name`, `industry`, `rank`).
- **`int_IndustryLookup`**: Distinct deduped industry catalog feeding `DimIndustry`.
