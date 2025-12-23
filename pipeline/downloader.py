import requests
import json
from datetime import date, timedelta
from pathlib import Path

RAW_DIR = Path("pipeline/data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://www.federalregister.gov/api/v1/documents.json"

def download_data():
    params = {
        "conditions[publication_date][gte]": (date.today() - timedelta(days=60)).isoformat(),
        "conditions[type][]": "PRESDOCU",
        "per_page": 100
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    output_file = RAW_DIR / "documents.json"
    output_file.write_text(json.dumps(response.json(), indent=2))

    print("✅ Data downloaded")

if __name__ == "__main__":
    download_data()
