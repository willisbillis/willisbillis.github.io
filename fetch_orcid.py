import requests
import json
import os

# Replace with your actual ORCID iD
ORCID_ID = "0000-0001-8271-3394"
ORCID_API_URL = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"

headers = {
    'Accept': 'application/json'
}

def get_orcid_data():
    try:
        response = requests.get(ORCID_API_URL, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ORCID data: {e}")
        return None

def main():
    data = get_orcid_data()
    if data:
        works = data.get('group', [])
        
        # Process the works data to extract relevant publication details
        publications = []
        for work in works:
            summaries = work.get('work-summary', [])
            for summary in summaries:  # Process all summaries, not just the first
                # Fix title parsing - it's nested deeper
                title_obj = summary.get('title', {})
                if isinstance(title_obj, dict) and 'title' in title_obj:
                    if isinstance(title_obj['title'], dict):
                        title = title_obj['title'].get('value', 'N/A')
                    else:
                        title = title_obj.get('title', 'N/A')
                else:
                    title = 'N/A'
                
                journal = summary.get('journal-title', {}).get('value', 'N/A')
                
                # Fix publication date parsing - use year.value, month.value, day.value
                pub_date_dict = summary.get('publication-date', {})
                year = pub_date_dict.get('year', {}).get('value') if pub_date_dict.get('year') else None
                month = pub_date_dict.get('month', {}).get('value') if pub_date_dict.get('month') else None
                day = pub_date_dict.get('day', {}).get('value') if pub_date_dict.get('day') else None
                
                if year:
                    month_str = str(month).zfill(2) if month else '01'
                    day_str = str(day).zfill(2) if day else '01'
                    pub_date = f"{year}-{month_str}-{day_str}"
                else:
                    pub_date = 'N/A'
                
                doi = 'N/A'
                external_ids = summary.get('external-ids', {}).get('external-id', [])
                for external_id in external_ids:
                    if external_id.get('external-id-type') == 'doi':
                        doi = external_id.get('external-id-value')
                        break
                
                # Only add publications with valid titles
                if title != 'N/A':
                    publications.append({
                        'title': title,
                        'journal': journal,
                        'publication_date': pub_date,
                        'doi': doi
                    })

        # Save the processed data to a JSON file
        with open('publications.json', 'w') as f:
            json.dump(publications, f, indent=2)
        
        if len(publications) == 0:
            print("Warning: No publications found. Please check the ORCID record or API response.")
        print(f"Successfully updated publications.json with {len(publications)} publications")
    else:
        print("Failed to get ORCID data.")

if __name__ == "__main__":
    main()