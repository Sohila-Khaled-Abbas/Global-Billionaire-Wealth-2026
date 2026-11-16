# Data Dictionary: Global Billionaire Wealth to GDP (2026)

This document provides complete field-level definitions, data types, validation constraints, and analytical notes for both tables in the semantic model.

---

## 1. Individual Billionaires Table (`billionaire_individual_2026`)

- **Primary Grain**: One record per billionaire individual / family entity.
- **Record Count**: 3,384 records.
- **Source**: Forbes Real-Time Billionaires List (Scraped: April 10, 2026) combined with World Bank GDP & Population Indicators.

| Column Name | Data Type | Nullable | Example Value | Description & Business Rules |
| :--- | :--- | :---: | :--- | :--- |
| `rank` | Integer | No | `1` | Global billionaire rank ordered by total net worth descending. |
| `person_name` | String | No | `Elon Musk` | Full legal or recognized name of the billionaire or family unit. |
| `gender` | String | No | `M` | Gender classification (`M` for Male, `F` for Female). |
| `age` | Float | Yes (48 nulls) | `54.0` | Age of individual in years as of the 2026 assessment. |
| `country` | String | No | `United States` | Primary country of citizenship or primary economic residence. |
| `iso3` | String | No | `USA` | Standard ISO 3166-1 alpha-3 country code. |
| `wb_country_name` | String | No | `United States` | Official country name standardized according to World Bank nomenclature. |
| `state` | String | Yes (1,842 nulls)| `Texas` | Administrative state/province (primarily populated for US billionaires). |
| `city` | String | Yes (49 nulls) | `Austin` | City of primary residence or family office base. |
| `net_worth_usd_m` | Float | No | `800629.06` | Total estimated net worth in millions of US Dollars (USD M). |
| `net_worth_usd` | Float | No | `800629059000.0` | Total estimated net worth in absolute US Dollars (USD). |
| `source_of_wealth` | String | No | `Tesla, SpaceX` | Primary commercial venture, firm, or asset source generating the wealth. |
| `industries` | String | No | `Technology` | Industry sector categorization listed in the Forbes source. |
| `primary_industry` | String | No | `Technology` | Standardized primary industrial sector used for comparative analytics. |
| `self_made` | Boolean | No | `True` | Flag indicating whether wealth was self-generated (`True`) or inherited (`False`). |
| `wealth_gdp_ratio_pct` | Float | Yes (4 nulls) | `2.7847` | Individual net worth expressed as a percentage of the country's annual nominal GDP. |
| `wealth_per_citizen_usd`| Float | Yes (4 nulls) | `2354.02` | Hypothetical wealth distribution per citizen if distributed equally across the population. |
| `wealth_country_share_pct`| Float | No | `9.5966` | Percentage of the country's total billionaire wealth held by this single individual. |
| `sector_dominance_score`| Float | No | `23.35` | Percentage of total country billionaire wealth concentrated in this individual's sector. |
| `gdp_usd` | Float | No | `28750956130731.2` | Nominal GDP of the billionaire's country in US Dollars (World Bank 2023/2024). |
| `population` | Float | No | `340110988.0` | Total national population of the country (World Bank 2023/2024). |
| `gdp_year` | Float | No | `2024.0` | Reference baseline calendar year for the macroeconomic GDP figure. |
| `forbes_uri` | String | No | `elon-musk` | Unique identifier slug for the Forbes profile page. |
| `scrape_timestamp` | String | No | `2026-04-10 21:32 UTC` | UTC timestamp of data retrieval and calculation. |
| `birth_year` | Float | Yes (48 nulls) | `1971.0` | Inferred year of birth (`2026 - age`). |

---

## 2. Country Aggregate Table (`billionaire_country_aggregate_2026`)

- **Primary Grain**: One record per sovereign state or economic territory.
- **Record Count**: 80 countries.
- **Relationship**: 1-to-many relationship with `billionaire_individual_2026` via the `country` key.

| Column Name | Data Type | Nullable | Example Value | Description & Business Rules |
| :--- | :--- | :---: | :--- | :--- |
| `country_wealth_rank` | Integer | No | `1` | Global rank of nation ordered by total national billionaire wealth descending. |
| `country` | String | No | `United States` | Primary common country name. |
| `iso3` | String | No | `USA` | Standard ISO 3166-1 alpha-3 country identifier. |
| `wb_country_name` | String | No | `United States` | Standard World Bank nation name. |
| `billionaire_count` | Integer | No | `978` | Total number of billionaires identified in the country. |
| `total_wealth_usd_m` | Float | No | `8342857.33` | Aggregate wealth of all billionaires in the country (USD Millions). |
| `total_wealth_usd` | Float | No | `8342857350000.0` | Aggregate wealth of all billionaires in the country (absolute USD). |
| `mean_wealth_usd_m` | Float | No | `8530.53` | Arithmetic mean net worth per billionaire in the country (USD Millions). |
| `median_wealth_usd_m` | Float | No | `3075.92` | Median net worth per billionaire in the country (USD Millions). |
| `max_wealth_usd_m` | Float | No | `800629.06` | Net worth of the single richest individual in the country (USD Millions). |
| `top_billionaire` | String | No | `Elon Musk` | Name of the wealthiest individual in the country. |
| `dominant_industry_by_wealth` | String | No | `Technology` | Industry accounting for the highest cumulative wealth in the country. |
| `self_made_count` | Integer | No | `706` | Count of billionaires in the country classified as self-made. |
| `self_made_ratio_pct` | Float | No | `72.2` | Proportion of self-made billionaires in the country (`self_made_count / billionaire_count * 100`). |
| `mean_age` | Float | No | `66.6` | Average age of billionaires in the country. |
| `country_wealth_gdp_pct` | Float | No | `29.02` | Cumulative billionaire wealth as a percentage of nominal national GDP. |
| `billionaires_per_million_pop`| Float | No | `2.8755` | Billionaires per million residents (`billionaire_count / (population / 1,000,000)`). |
| `wealth_concentration_tier` | String | No | `Very High (20–40%)` | Qualitative macro tier categorizing billionaire wealth relative to national GDP. |
| `gdp_per_billionaire_bn` | Float | No | `29.40` | National GDP divided by billionaire count (USD Billions of economic output per billionaire). |
| `sector_dominance_score` | Float | No | `23.35` | Percentage of national billionaire wealth held in the leading industry sector. |
| `gdp_usd` | Float | No | `28750956130731.2` | Annual nominal GDP in US Dollars from World Bank. |
| `population` | Float | No | `340110988.0` | National population from World Bank. |
| `gdp_year` | Float | No | `2024.0` | Calendar year of reference GDP figure. |

---

## 3. Wealth Concentration Tier Reference

The variable `wealth_concentration_tier` classifies nations into five economic concentration regimes:

| Concentration Tier | Benchmark Range (% of GDP) | Country Count | Representative Examples |
| :--- | :---: | :---: | :--- |
| **Extreme** | $\ge 40\%$ | 9 | Hong Kong (103.9%), Cyprus (148.7%), St. Kitts & Nevis (860.7%), Israel (42.4%) |
| **Very High** | $20\% \text{ to } <40\%$ | 12 | United States (29.0%), Russia (30.1%), India (25.3%), Germany (21.0%) |
| **High** | $10\% \text{ to } <20\%$ | 21 | China (11.4%), France (18.7%), Canada (19.8%), Italy (19.5%), Brazil (12.1%) |
| **Moderate** | $3\% \text{ to } <10\%$ | 29 | United Kingdom (7.3%), Japan (5.4%), South Korea (8.7%), Turkey (8.4%) |
| **Low** | $< 3\%$ | 9 | Netherlands (2.9%), Saudi Arabia (2.1%), Poland (1.6%), South Africa (1.9%) |
