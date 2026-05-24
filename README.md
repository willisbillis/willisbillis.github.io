# willisbillis.github.io

Personal website for M Elliott Williams, Bioinformatics Analyst at Emory University.

## ORCID Publications Integration

The site includes an automated system to fetch and display publications from ORCID.

[![Update Publications from ORCID](https://github.com/willisbillis/willisbillis.github.io/actions/workflows/update_publications.yml/badge.svg)](https://github.com/willisbillis/willisbillis.github.io/actions/workflows/update_publications.yml)

### Automatic updates (GitHub Actions)

Publications are automatically refreshed daily via:

- `.github/workflows/update_publications.yml`
- Scheduled run at `08:00 UTC`
- Manual trigger via `workflow_dispatch`

### Expected update timing

- New ORCID entries should appear on the site within 24 hours of being visible in ORCID.
- If you need an immediate refresh, run the workflow manually via `workflow_dispatch` or run `python3 fetch_orcid.py` locally and commit the updated `publications.json`.

### Usage

1. **Fetch Publications Locally**: Run the Python script to fetch publications from ORCID API:

   ```bash
   python3 fetch_orcid.py
   ```

2. **View Publications**: The website automatically loads and displays publications from `publications.json` in the Publications tab.

### How it works

- `fetch_orcid.py` - Fetches publication data from ORCID API and saves to `publications.json`
- `index.html` - Loads and displays publications from the JSON file
- Publications are displayed with title, journal, publication date, and DOI (when available)
