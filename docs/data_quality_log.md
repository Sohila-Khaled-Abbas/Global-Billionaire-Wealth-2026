# Data Quality & Anomaly Log

This document records the automated validation audits, Power Query reconciliation tables (`05_QA & Reconciliation`), null handling rules, and referential integrity checks embedded within the Power BI semantic model.

---

## 1. Automated Power Query QA Tables (`05_QA & Reconciliation`)

The semantic model includes automated validation queries executed directly in Power Query during data refresh:

```
[01_Source] ──────────► [02_Staging] ──────────► [05_QA & Reconciliation]
                             │                            │
                             ▼                            ▼
                     [04_DataModel]             17 Automated Audits
                    (Clean & Modeled)          (Keys, Totals, Ties)
```

| QA Query Name | Scope of Validation | Expected Baseline | Status |
| :--- | :--- | :--- | :---: |
| `tmp_SourceValidation` | Verifies source file availability and raw row counts. | 3,384 ind / 80 agg rows | Passed |
| `tmp_StagingValidation` | Confirms header promotion and non-empty columns. | 25 ind / 23 agg columns | Passed |
| `tmp_StagingHealth` | Validates data types and schema conformance across staging. | 0 schema mismatches | Passed |
| `tmp_KeyAudit` | Checks primary key uniqueness on `rank` and `iso3`. | 0 duplicate keys | Passed |
| `tmp_IndustryCoverage` | Asserts all individual industries map to `DimIndustry`. | 100% coverage (18 sectors) | Passed |
| `tmp_IndustryDelimiterAudit` | Audits multi-value delimited industry strings. | Delimiters cleanly parsed | Passed |
| `tmp_IndividualQualityAudit` | Scans for negative net worth, extreme age outliers, or missing names. | 0 fatal anomalies | Passed |
| `tmp_NetWorthConsistency` | Compares `net_worth_usd_m * 1e6` against `net_worth_usd`. | Complete consistency | Passed |
| `tmp_RankAudit` | Audits rank monotonicity and identifies shared rank positions. | Valid ranking sequence | Passed |
| `tmp_RankTieAudit` | Analyzes tied ranks for billionaires with identical valuations. | Documented ties verified | Passed |
| `tmp_AgeBirthYearAudit` | Verifies `birth_year + age ≈ 2026` across all records. | Delta ≤ 1 year confirmed | Passed |
| `tmp_CountryNullAudit` | Verifies `iso3` and `country` are non-null across all rows. | 0 null country keys | Passed |
| `tmp_CountryNumericAudit` | Asserts national GDP, population, and wealth totals are > 0. | 80 valid positive records | Passed |
| `tmp_CountryPrecisionAudit` | Audits floating-point rounding precision between tables. | Delta < $1.00 USD | Passed |
| `qa_IndividualByCountry` | Aggregates individual fortunes grouped by `iso3`. | Matches country totals | Passed |
| `qa_CountryAggregate` | Direct extraction of country aggregate benchmarks. | Validated against source | Passed |
| `qa_CountryReconciliation` | Reconciles individual sums vs. country aggregate sums. | Exact balance ($19.64T) | Passed |
| `tmp_GalaxyFactReconciliation` | Cross-fact outer join audit comparing `FactBillionaire` and `FactCountrySnapshot` by `iso3`. | 0 mismatches across all 80 countries | Passed |
| `tmp_GalaxyFactReconciliationSummary` | High-level scorecard summarizing galaxy schema reconciliation KPIs. | 100% Passed across 7 core metrics | Passed |
| `tmp_SourceSchemaContract` | Automated schema contract verifying all required columns and invariant types. | All schema contracts satisfied | Passed |
| `tmp_SnapshotProvenanceValidation` | Cross-validates analytical snapshot date anchors across all model facts. | Single source of truth confirmed | Passed |
| `tmp_SnapshotProvenanceDetail` | Granular audit of snapshot dates, UTC timestamps, and data vintages. | 0 timestamp anomalies | Passed |
| `tmp_GDPVintageExceptionDetail` | Audits Liechtenstein 2022 GDP historical vintage and monitors reference years. | Documented vintage exception verified | Passed |
| `tmp_FinalFactGrainValidation` | Primary key uniqueness and grain validation for `FactBillionaire` and `FactCountrySnapshot`. | Strict grain enforcement (0 duplicates) | Passed |
| `tmp_FunctionLibraryValidation` | Unit test suite verifying M functions (`fn_CleanText`, `fn_NormalizeISO3`, `fn_SafeDivide`). | 100% function test pass rate | Passed |
| `tmp_DimCountryEnrichmentValidation` | Validates composite display labels and country name alignment flags. | 0 null display labels | Passed |

---

## 2. Null Value Treatment & Fallen Billionaires

| Column Name | Table | Null Count | Root Cause | Model Handling |
| :--- | :--- | :---: | :--- | :--- |
| `state` | `FactBillionaire` | 1,842 (54.4%) | State/province data is captured primarily for US, Canadian, and Australian entries. | Preserved as `null` for drill-down reporting in North American filter contexts. |
| `city` | `FactBillionaire` | 49 (1.45%) | Unspecified urban base for island residents or private trusts. | Retained as `null`; visual cards default to country-level aggregation. |
| `age` / `birth_year` | `FactBillionaire` | 48 (1.42%) | Private individuals with undisclosed birth dates. | Ignored in average age calculations; does not affect wealth aggregates. |
| `wealth_gdp_ratio_pct` | Raw CSV | 4 records | Fallen billionaires with $0 net worth (bankruptcies/judgments). | Filtered in staging or coerced to 0.00; net worth reflects $0.00. |

### Detail: Fallen Billionaire Registry
The dataset retains 4 high-profile historical billionaires whose fortunes collapsed to zero:
- **Elizabeth Holmes** (Rank 3381, United States, Theranos)
- **Sam Bankman-Fried** (Rank 3381, United States, FTX)
- **Gary Wang** (Rank 3381, United States, FTX)
- **Rene Benko** (Rank 3381, Austria, Signa Holding)

---

## 3. Referential & Balance-Sheet Integrity

1. **Foreign Key Alignment**:
   - `FactBillionaire.iso3` $\to$ `DimCountry.iso3`: **3,384 of 3,384 rows (100.0%)** cleanly mapped to an existing dimension record.
   - `FactBillionaire.industry` $\to$ `DimIndustry.industry`: **3,384 of 3,384 rows (100.0%)** mapped to the 18 standardized sectors.
   - `FactCountrySnapshot.iso3` $\to$ `DimCountry.iso3`: **80 of 80 rows (100.0%)** matched in a 1-to-1 relationship.

2. **Reconciliation Formula**:
   $$\sum \text{FactBillionaire}[net\_worth\_usd] = \sum \text{FactCountrySnapshot}[total\_wealth\_usd] = \$19,639,549,700,000\text{ USD}$$
   The balance sheet reconciles to the exact penny ($0.00 delta).

---

## 4. Macroeconomic Vintage & Historical-Vintage Exceptions

Country-level GDP and population values use the most recent available source data incorporated into the April 10, 2026 analytical snapshot. GDP reference years vary by country. Liechtenstein has a 2022 GDP observation and is retained as a documented historical-vintage exception pending source-level verification. Original source values are preserved to maintain reproducibility.

| Country | ISO3 | GDP Reference Year | GDP (USD) | Population | Billionaire Wealth ($M) | Treatment |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Liechtenstein** | `LIE` | 2022 | \$7.79 Billion | 39,584 | \$1,362.00 | Documented historical-vintage exception; preserved as-is. |
| **All Other Nations (79)** | Various | 2023 / 2024 | Standard World Bank | Standard World Bank | Standard Forbes | Standard baseline. |
