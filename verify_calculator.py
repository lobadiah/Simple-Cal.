import asyncio
from playwright.async_api import async_playwright
import time
import subprocess
import os

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        try:
            await page.goto("http://127.0.0.1:5000")
            print("Page loaded successfully.")

            # Test Basic Addition: 5 + 5 = 10
            await page.click("button:has-text('5')")
            await page.click("button:has-text('+')")
            await page.click("button:has-text('5')")
            await page.click("button:has-text('=')")

            # Wait for result to appear
            await page.wait_for_selector("#current-operand:has-text('10')")
            print("Addition test passed: 5 + 5 = 10")

            # Clear
            await page.click("button:has-text('AC')")

            # Test Scientific: sqrt(16) = 4
            await page.click("button:has-text('1')")
            await page.click("button:has-text('6')")
            # Select by the exact text √
            await page.click("button:text('√')")

            # JS toString() for 4.0 is "4"
            await page.wait_for_selector("#current-operand:has-text('4')")
            print("Scientific test passed: sqrt(16) = 4")

            # Take a screenshot for visual confirmation
            await page.screenshot(path="screenshot.png")
            print("Screenshot saved to screenshot.png")

        except Exception as e:
            print(f"Tests failed: {e}")
            await page.screenshot(path="failure_screenshot.png")
            raise e
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_tests())
