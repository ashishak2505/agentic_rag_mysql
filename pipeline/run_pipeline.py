from downloader import download_data
import asyncio
from processor import process_and_store

def run_pipeline():
    download_data()
    asyncio.run(process_and_store())

if __name__ == "__main__":
    run_pipeline()
