# Data Dictionary: Global Billionaire Wealth to GDP (2026)

This document provides complete field-level definitions, data types, primary/foreign keys, validation constraints, and business rules for the Power BI Semantic Model and data pipeline.

---

## 🏛️ Semantic Model Architecture Overview

The analytical model implements an enterprise-grade dimensional architecture (Star/Snowflake schema) engineered in Power BI Desktop Developer Mode (`.pbip` / TMDL):

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
   └─────────────────┘                └───────────────────┘
```

---

## 1. Dimension Tables

### A. `DimCountry` (Country Dimension)
- **Primary Grain**: One row per sovereign nation or economic territory.
- **Record Count**: 80 records.
- **Primary Key**: `iso3`

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `iso3` | String (3 chars) | Text | No (PK) | Standard ISO 3166-1 alpha-3 uppercase country identifier. Joins to `FactBillionaire.iso3` and `FactCountrySnapshot.iso3`. Normalized via `fn_NormalizeISO3`. |
| `country` | String | Text | No | Standardized common country name (e.g., `United States`, `China`, `Germany`). Cleaned via `fn_CleanText`. |
| `wb_country_name` | String | Text | No | Official nation name aligned with World Bank national accounts nomenclature. Cleaned via `fn_CleanText`. |
| `country_display_label` | String | Text | No | Derived composite label for presentation: `[country] & " (" & [iso3] & ")"`. |
| `country_name_alignment` | String | Text | No | Naming alignment diagnostic: `"Same label"`, `"Different source label"`, or `"Missing name"`. |

---

### B. `DimIndustry` (Industry Dimension)
- **Primary Grain**: One row per standardized economic sector.
- **Record Count**: 18 industries.
- **Primary Key**: `industry`

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `industry` | String | Text | No (PK) | Standardized primary industrial sector (e.g., `Technology`, `Finance & Investments`, `Fashion & Retail`). Processed from `int_IndustryLookup` and cleaned via `fn_CleanText`. |

---

## 2. Fact Tables

### A. `FactBillionaire` (Billionaire Fact)
- **Primary Grain**: One row per billionaire individual or family entity.
- **Record Count**: 3,384 records.
- **Foreign Key**: `iso3` (to `DimCountry.iso3`).

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `rank` | Int64 | Whole Number | No | Global wealth rank (1 = richest individual, Elon Musk). |
| `person_name` | String | Text | No | Full legal or publicly recognized name. Cleaned via `fn_CleanText`. |
| `source_of_wealth` | String | Text | No | Primary business, enterprise, or asset origin. Cleaned via `fn_CleanText`. |
| `industry` | String | Text | No | Primary economic industry classification. Cleaned via `fn_CleanText`. |
| `state` | String | Text | Yes (1,842 nulls) | Administrative state or province (predominantly US and Canadian entries). |
| `city` | String | Text | Yes (49 nulls) | City of primary residence or family office base. Cleaned via `fn_CleanText`. |
| `gender` | String (1 char) | Text | No | Gender code: `M` (Male, 2,910 records), `F` (Female, 474 records). |
| `age` | Int64 | Whole Number | Yes (48 nulls) | Current age in years as of the 2026 assessment. Blank for undisclosed birthdates. |
| `age_band` | String | Text | No | Demographic age cohort: `Under 30`, `30–39`, `40–49`, `50–59`, `60–69`, `70–79`, `80+`, or `Not disclosed`. |
| `iso3` | String (Hidden) | Text | No (FK) | Normalized ISO 3166-1 alpha-3 country key joining to `DimCountry.iso3`. |
| `net_worth_usd` | Decimal (Fixed) | Currency | No | Total estimated net worth in absolute US Dollars (USD). |
| `self_made` | Boolean | True/False | No | Entrepreneurial classification: `TRUE` = self-made founder; `FALSE` = inherited/dynastic. |
| `self_made_label` | String | Text | No | User-friendly label: `"Self-made"`, `"Inherited / family wealth"`, or `"Not disclosed"`. |
| `wealth_gdp_ratio_pct` | Double | Decimal Number | Yes (4 nulls) | Individual net worth expressed as a percentage of national nominal GDP. |
| `wealth_per_citizen_usd` | Decimal (Fixed) | Currency | Yes (4 nulls) | Per-capita equivalent dividend if net worth were distributed equally across national population. |
| `wealth_country_share_pct` | Double | Decimal Number | No | Share of national billionaire wealth held by this single individual (%). |
| `wealth_tier` | String | Text | No | Capital concentration tier: `$100B+`, `$50B to under $100B`, `$10B to under $50B`, `$5B to under $10B`, `$1B to under $5B`, `Below $1B`. |
| `wealth_tier_sort` | Int64 | Whole Number | No | Numeric sort order (1 to 6) for `wealth_tier`. |
| `forbes_uri` | String (Hidden) | Text | No | Unique slug identifier for the billionaire's Forbes profile page. |
| `scrape_timestamp` | DateTimeZone (Hidden) | Date/Time/Zone | No | Exact UTC timestamp of data capture (`2026-04-10 21:32 UTC`). |
| `birth_year` | Int64 | Whole Number | Yes (48 nulls) | Inferred year of birth (`2026 - age`). |
| `snapshot_date` | DateTime (Date) | Date | No | Reference date of the analytical snapshot (`p_SnapshotDate`). |

---

### B. `FactCountrySnapshot` (Country Macroeconomic Snapshot)
- **Primary Grain**: One row per sovereign nation/territory.
- **Record Count**: 80 records.
- **Key**: `iso3` (1-to-1 bidirectional relationship with `DimCountry.iso3`).

| Column Name | Storage Type | Power BI Type | Nullable | Description & Business Rules |
| :--- | :--- | :--- | :---: | :--- |
| `iso3` | String | Text | No (FK/PK) | Standard ISO 3166-1 alpha-3 country identifier. Normalized via `fn_NormalizeISO3`. |
| `country_wealth_rank` | Int64 | Whole Number | No | Sovereign rank ordered by cumulative billionaire wealth descending (1 = USA). |
| `billionaire_count` | Int64 | Whole Number | No | Total resident billionaire headcount in the country. |
| `top_billionaire` | String | Text | No | Name of the nation's wealthiest citizen. Cleaned via `fn_CleanText`. |
| `dominant_industry_by_wealth` | String | Text | No | Sector contributing the highest aggregate wealth in the country. Cleaned via `fn_CleanText`. |
| `total_wealth_usd_m` | Decimal | Currency | No | Cumulative billionaire net worth in Millions of US Dollars ($M). |
| `total_wealth_usd` | Decimal | Currency | No | Cumulative billionaire net worth in absolute US Dollars (USD). |
| `mean_wealth_usd_m` | Double | Decimal Number | No | Arithmetic average wealth per billionaire ($M). |
| `median_wealth_usd_m` | Double | Decimal Number | No | Median wealth per billionaire ($M). |
| `max_wealth_usd_m` | Double | Decimal Number | No | Net worth of the single wealthiest individual in the country ($M). |
| `self_made_count` | Int64 | Whole Number | No | Headcount of self-made resident billionaires. |
| `self_made_ratio_pct` | Double | Decimal Number | No | Percentage of resident billionaires who are self-made (`self_made_count / billionaire_count * 100`). |
| `mean_age` | Double | Decimal Number | No | Average age of resident billionaires. |
| `country_wealth_gdp_pct` | Double | Percentage | No | Total billionaire wealth expressed as a percentage of nominal national GDP. Formatted as `0.00%`. |
| `wealth_gdp_comparison` | String | Text | No | High-level GDP benchmark: `"Below 100%"`, `"100% or above"`, or `"Not available"`. |
| `billionaires_per_million_pop` | Double | Decimal Number | No | Billionaire density per million residents (`billionaire_count / (population / 1,000,000)`). |
| `wealth_concentration_tier` | String | Text | No | Macroeconomic tier: `Extreme (≥40%)`, `Very High (20–40%)`, `High (10–20%)`, `Moderate (3–10%)`, `Low (<3%)`. |
| `wealth_concentration_sort` | Int64 | Whole Number | No | Numeric sort key (1 to 5) mapping to `wealth_concentration_tier`. |
| `gdp_per_billionaire_bn` | Double | Decimal Number | No | National economic output per billionaire (GDP / billionaire_count in $B USD). |
| `sector_dominance_score` | Double | Decimal Number | No | Share of national billionaire wealth held in the single leading sector (%). |
| `gdp_usd` | Decimal | Currency | No | Annual nominal GDP in US Dollars from World Bank. |
| `gdp_vintage_status` | String | Text | No | Macroeconomic reference tracking: `"2024 reference"`, `"2023 reference"`, `"Earlier vintage – review"`, or `"Missing GDP year"`. |
| `population` | Int64 | Whole Number | No | Total national population from World Bank. |
| `gdp_year` | Int64 | Whole Number | No | Baseline year of national GDP indicator. Country-level GDP and population values use the most recent available source data incorporated into the April 10, 2026 analytical snapshot. GDP reference years vary by country. Liechtenstein has a 2022 GDP observation and is retained as a documented historical-vintage exception pending source-level verification. Original source values are preserved to maintain reproducibility. |
| `snapshot_date` | DateTime (Date) | Date | No | Analytical snapshot date (`p_SnapshotDate`). |

---

## 3. Dedicated Measures Table (`_Measures`)

All analytical DAX metrics are centralized in the `_Measures` table:

| Measure Name | DAX Expression | Formatting | Description |
| :--- | :--- | :--- | :--- |
| `Billionaire Count` | `COUNTROWS(FactBillionaire)` | Whole Number (`#,##0`) | Dynamic count of billionaires based on active filter context. |
| `Total Billionaire Wealth USD` | `SUM(FactBillionaire[net_worth_usd])` | Currency (`$#,##0`) | Aggregate net worth across the filtered population in absolute USD. |

---

## 4. Power Query Parameters, Functions & Intermediate Tables

### A. Parameters
- **`p_DataFolderPath`**: Configurable root path for raw CSV files (`data\raw`).
- **`p_SnapshotDate`**: Parameterized date anchor for time-series modeling (`2026-04-10`).

### B. Custom M Functions
- **`fn_CleanText`**: Trims whitespace, cleans non-printable characters, and normalizes capitalization.
- **`fn_NormalizeISO3`**: Ensures 3-character uppercase ISO-3 codes with null protection.
- **`fn_SafeDivide`**: Protected division function preventing divide-by-zero or NaN exceptions.
- **`fn_StandardizeCountry`**: Standardizes country strings against global gazetteer names.
- **`fn_ParseIndustries`**: Splits comma-delimited industry strings into tabular rows.

### C. Intermediate & Bridge Tables
- **`int_BillionaireIndustryBridge`**: Normalized bridge table connecting each billionaire to one or more industries (`person_name`, `industry`, `rank`).
- **`int_IndustryLookup`**: Distinct deduped industry catalog feeding `DimIndustry`.
