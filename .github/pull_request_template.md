## Pull Request Overview

### Description
Provide a concise summary of the changes proposed in this Pull Request.

### Category of Change
- [ ] 📊 Data Transformation / Ingestion (`data/raw/`)
- [ ] 📐 Power BI Semantic Model / TMDL (`powerbi/*.SemanticModel/`)
- [ ] 🎨 Power BI Visual Report / Pages (`powerbi/*.Report/`)
- [ ] 📈 DAX Measure Addition or Optimization
- [ ] 📚 Documentation Update (`docs/` or `README.md`)
- [ ] ⚙️ CI / Automation Workflow (`.github/`)

---

## Technical Details

### Power BI / PBIP Verification
- [ ] Opened and validated in Power BI Desktop (Developer Mode enabled)
- [ ] No circular dependencies or broken relationships in `relationships.tmdl`
- [ ] DAX formatting complies with standard DAX guidelines (line breaks, explicit table qualifiers for columns, no table qualifiers for measures)
- [ ] Data sources use relative paths or documented parameters
- [ ] Report screenshots added to `exports/report_screenshots/` if visuals were altered

### Data Quality & Integrity Checks
- [ ] Verified row counts and total wealth reconciliation between individual and country tables
- [ ] No unexpected null values introduced
- [ ] Python validation script passes locally (`python -m unittest` or custom audit script)

---

## Screenshots / Artifacts (if visual changes apply)
*Please attach before/after screenshots of the updated Power BI report canvas below:*

---

## Related Issues
Closes #
