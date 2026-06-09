from playwright.sync_api import sync_playwright
import time


def login_linkedin(config):

    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(

        user_data_dir="./playwright_profile",

        headless=False,

        channel="chrome",

        args=[
            "--start-maximized"
        ]
    )

    # use existing page
    page = context.pages[0]

    print("\n===================================")
    print("🚀 NexusApply AI Starting...(made by xeze 💋)")
    print("🔐 Opening LinkedIn...")
    print("===================================\n")

    # open linkedin
    page.goto(
        "https://www.linkedin.com/feed/",
        timeout=120000
    )

    # WAIT FOR LOGIN
    print("⏳ Waiting for LinkedIn login...")

    try:

        page.wait_for_selector(
            "input[placeholder='Search']",
            timeout=1200
        )

        print("✅ Logged into LinkedIn successfully")

    except:

        print("⚠️ Login not detected")
        print("Please login manually")

        time.sleep(10)

    return context, page