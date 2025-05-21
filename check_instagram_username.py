import aiohttp
import asyncio

# Username yoxlama funksiyası
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
                if response.status == 404:
                    print(f"❌ Username '{username}' mövcud deyil.")
                elif response.status == 200:
                    print(f"✅ Username '{username}' artıq istifadə olunur.")
                elif response.status == 403:
                    print("⚠️  Instagram sorğunu blokladı (403 Forbidden).")
                elif response.status == 429:
                    print("⚠️  Çox sayda sorğu göndərildi (429 Too Many Requests). Zəhmət olmasa gözləyin.")
                else:
                    print(f"⚠️  Naməlum cavab: {response.status}")
        except aiohttp.ClientError as e:
            print(f"🌐 Şəbəkə xətası: {e}")

# Əsas proqram dövrü
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
        await asyncio.sleep(1)  # Serverə yük salmamaq üçün gözləmə

# Proqram başlanğıcı
if __name__ == "__main__":
    asyncio.run(main())
