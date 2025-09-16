# willisbillis.github.io

Personal website for M Elliott Williams, Bioinformatics Analyst at Emory University.

## ORCID Publications Integration

The site includes an automated system to fetch and display publications from ORCID:

### Usage

1. **Fetch Publications**: Run the Python script to fetch publications from ORCID API:
   ```bash
   python3 fetch_orcid.py
   ```

2. **View Publications**: The website automatically loads and displays publications from `publications.json` in the Publications tab.

### How it works

- `fetch_orcid.py` - Fetches publication data from ORCID API and saves to `publications.json`
- `index.html` - Loads and displays publications from the JSON file
- Publications are displayed with title, journal, publication date, and DOI (when available)