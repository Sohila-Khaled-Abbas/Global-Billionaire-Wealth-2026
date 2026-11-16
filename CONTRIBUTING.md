# Contributing to Global Billionaire Wealth (2026) Analytics

Thank you for your interest in contributing to this open-source macroeconomic and business intelligence project! We welcome contributions that improve data quality, expand analytical dimensions, refine DAX measures, or enhance visual storytelling.

---

## 1. Development Principles

- **PBIP First**: All Power BI changes must be authored and committed using Power BI Desktop Developer Mode (`.pbip`), ensuring human-readable TMDL and JSON tracking.
- **Data Integrity**: Any transformation or modeling adjustment must maintain exact wealth reconciliation between individual and country aggregate tables.
- **Clear DAX Standards**:
  - Always qualify columns with table names: `TableName[ColumnName]`.
  - Never qualify measures with table names: `[MeasureName]`.
  - Use `DIVIDE(numerator, denominator, alternateResult)` for all division operations to prevent divide-by-zero exceptions.
  - Wrap variables cleanly with `VAR` and `RETURN`.

---

## 2. Git Workflow & Branch Strategy

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/<your-username>/Global-Billionaire-Wealth-2026.git
   cd Global-Billionaire-Wealth-2026
   ```
3. **Create a topic branch** from `main`:
   ```bash
   git checkout -b feat/macro-gini-index
   # or
   git checkout -b fix/fallen-billionaire-handling
   ```
4. **Make your changes**:
   - For Power BI: Open `powerbi/Global_Billionaire_Wealth_2026.pbip` in Power BI Desktop.
   - For Documentation: Edit or add markdown files under `docs/`.
   - For Data validation: Run Python audit scripts locally.
5. **Commit your changes** with clear, descriptive commit messages:
   ```bash
   git commit -m "feat(dax): add dynamic Lorenz curve and Gini proxy measure"
   ```
6. **Push to your branch** and open a Pull Request against `main`.

---

## 3. Pull Request Review Criteria

Every Pull Request will be evaluated against:
1. **Automated CI Validation**: Passing GitHub Actions data schema and PBIP integrity workflows.
2. **Reconciliation**: No divergence in aggregate wealth totals ($19.64 Trillion USD benchmark).
3. **Documentation**: Updates to `docs/data_dictionary.md` or `docs/business_questions.md` when new columns or analytical queries are added.
4. **Visual Previews**: High-resolution screenshots placed in `exports/report_screenshots/` for any report canvas modifications.
