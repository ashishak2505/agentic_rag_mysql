import json
import asyncio
from pathlib import Path
from db import get_connection

RAW_FILE = Path("pipeline/data/raw/documents.json")

async def process_and_store():
    data = json.loads(RAW_FILE.read_text())["results"]

    conn = await get_connection()
    cur = await conn.cursor()

    for doc in data:
        await cur.execute(
            """
            INSERT IGNORE INTO federal_docs
            (doc_id, title, type, summary, topics, publication_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                doc["document_number"],
                doc["title"],
                doc["type"],
                doc.get("abstract"),
                ", ".join(doc.get("topics", [])),
                doc["publication_date"]
            )
        )

    await cur.close()
    conn.close()

    print("✅ Data processed & stored")

if __name__ == "__main__":
    asyncio.run(process_and_store())
