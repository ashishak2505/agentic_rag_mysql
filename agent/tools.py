# agent/tools.py
import keyword
import aiomysql

from datetime import date

async def search_docs(keyword=None, start_date=None, end_date=None):
    # ---- sanitize date inputs ----
    today = date.today().isoformat()

    invalid_date_values = {"present", "now", "today", "current"}

    if isinstance(start_date, str) and start_date.lower() in invalid_date_values:
        start_date = None  # ignore invalid start date

    if isinstance(end_date, str) and end_date.lower() in invalid_date_values:
        end_date = today  # treat "present" as today
        


    conn = await aiomysql.connect(
        host="localhost",
        user="rag_user",
        password="rag_password",
        db="rag_db",
        autocommit=True
    )

    cur = await conn.cursor()

    query = "SELECT title, publication_date FROM federal_docs WHERE 1=1"
    params = []

    DOMAIN_MAP = {
        "ai": [
            "defense",
            "security",
            "cyber",
            "data",
            "technology",
            "automation"
        ],
        "technology": [
            "technology",
            "digital",
            "cyber",
            "data"
        ],
        "security": [
            "security",
            "defense",
            "national"
        ]
    }
    if not keyword:
        return []
    if keyword:
        keyword = keyword.lower()

# intent extraction
    if "ai" in keyword:
        keyword = "ai"
    elif "security" in keyword:
        keyword = "security"
    elif "technology" in keyword:
        keyword = "technology"

    DOMAIN_MAP = {
        "ai": ["artificial intelligence"],
        "technology": ["technology", "digital", "data"],
        "security": ["security", "defense", "national"]
    }

    terms = DOMAIN_MAP.get(keyword, [keyword])

    conditions = []
    params = []

    for term in terms:
        conditions.append("(title LIKE %s OR summary LIKE %s)")
        params.extend([f"%{term}%", f"%{term}%"])
    query += " AND (" + " OR ".join(conditions) + ")"


    if start_date:
        query += " AND publication_date >= %s"
        params.append(start_date)

    if end_date:
        query += " AND publication_date <= %s"
        params.append(end_date)

    await cur.execute(query, params)
    rows = await cur.fetchall()

    conn.close()
    return rows
