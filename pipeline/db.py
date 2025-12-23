import aiomysql

async def get_connection():
    return await aiomysql.connect(
        host="localhost",
        user="rag_user",
        password="rag_password",
        db="rag_db",
        autocommit=True
    )
