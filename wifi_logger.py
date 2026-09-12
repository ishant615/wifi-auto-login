from playwright.async_api import async_playwright
import asyncio
import time

username = "username"
password = "password"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("http://detectportal.firefox.com/")
        try:
            result = await page.evaluate("""
                ({username, password}) => {
                    
                    username_inp = document.getElementById("ft_un");
                    password_inp = document.getElementById("ft_pd");
                    submit_button = document.querySelector('input[type="submit"]');

                    username_inp.value = username;
                    password_inp.value = password;
                    submit_button.click();

                    return 0;
                }
            """, {
                "username": username,
                "password":password
            })
            if result == 0:
                print("Logged In Successfully") 
        except Exception as e:
            result = await page.evaluate("""
                () => {

                    return document.documentElement.innerText.trim();
                }
            """)
            # print("Already Logged In") if result == "success" else print(e)
        time.sleep(0.5)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
            