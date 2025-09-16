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
            summary = work.get('work-summary', [{}])[0]
            title = summary.get('title', {}).get('title', 'N/A')
            journal = summary.get('journal-title', {}).get('value', 'N/A')
            pub_date_dict = summary.get('publication-date', {}).get('date', {})
            pub_date = f"{pub_date_dict.get('year')}-{pub_date_dict.get('month', '01')}-{pub_date_dict.get('day', '01')}"
            doi = 'N/A'
            for external_id in summary.get('external-ids', {}).get('external-id', []):
                if external_id.get('external-id-type') == 'doi':
                    doi = external_id.get('external-id-value')
                    break
            
            publications.append({
                'title': title,
                'journal': journal,
                'publication_date': pub_date,
                'doi': doi
            })

        # Save the processed data to a JSON file
        with open('publications.json', 'w') as f:
            json.dump(publications, f, indent=2)
        
        print("Successfully updated publications.json")
    else:
        print("Failed to get ORCID data.")

if __name__ == "__main__":
    main()