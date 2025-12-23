from agent.tools import search_docs


async def agent_chat(user_query: str):
    query_lower = user_query.lower()

    # ---- Intent extraction ----
    if "artificial intelligence" in query_lower or "ai" in query_lower:
        keyword = "artificial intelligence"
    elif "security" in query_lower or "defense" in query_lower:
        keyword = "security"
    elif "technology" in query_lower:
        keyword = "technology"
    else:
        keyword = None

    # ---- DB retrieval ----
    results = await search_docs(keyword=keyword)

    if not results:
        return "No relevant records were found in the database."

    # ---- Deterministic formatting ----
    formatted = []
    for title, pub_date in results:
        formatted.append(f"• {title} ({pub_date})")

    return "\n".join(formatted)
