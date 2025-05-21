import aiohttp
import asyncio

# Asinxron gözləmə üçün asyncio.sleep istifadə edirik
async def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 404:
                print(f"Username '{username}' mövcud deyil.")
            elif response.status == 200:
                print(f"Username '{username}' artıq istifadə olunur.")
            else:
                print("Xəta baş verdi, daha sonra yenidən yoxlayın.")

# Əsas asinxron funksiya
async def main():
    while True:
        # İstifadəçidən username alınır
        username = input("Yoxlamaq istədiyiniz Instagram username-i daxil edin (çıxmaq üçün 'exit' yazın): ")
        
        # Əgər istifadəçi 'exit' yazarsa dövrü dayandırır
        if username.lower() == 'exit':
            print("Proqramdan çıxılır...")
            break
        
        # Username yoxlanır
        await check_username(username)
        await asyncio.sleep(1)  # 1 saniyəlik asinxron gözləmə, digər yoxlamalara mane olmur

if __name__ == "__main__":
    asyncio.run(main())
