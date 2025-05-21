import aiohttp
import asyncio

async def check_username(username):
    url = f"https://www.instagram.com/{username}/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/119.0.0.0 Safari/537.36"
        )
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                html = await response.text()

                # HTML içindən səhifənin olub-olmadığını müəyyən edirik
                if "Sorry, this page isn't available" in html:
                    print(f"❌ Username '{username}' mövcud deyil.")
                else:
                    print(f"✅ Username '{username}' artıq istifadə olunur.")
        except aiohttp.ClientError as e:
            print(f"🌐 Şəbəkə xətası: {e}")

async def main():
    while True:
        username = input("🔍 Yoxlamaq istədiyiniz Instagram username-i daxil edin (çıxmaq üçün 'exit'): ")
        if username.lower() == 'exit':
            print("🚪 Proqramdan çıxılır...")
            break

        if not username.strip():
            print("⚠️  Username boş ola bilməz.")
            continue

        await check_username(username)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
