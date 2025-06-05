import aiosqlite
import asyncio


async def async_fetch_users():
    async with aiosqlite.connect('practice_db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users


async def async_fetch_older_users():
    async with aiosqlite.connect('practice_db') as db:
        async await db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            old_users = await cursor.fetchall()
            return old_users


async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users
        )
    return results

asyncio.run(fetch_concurrently())