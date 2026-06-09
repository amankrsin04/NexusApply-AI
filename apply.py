
import time
from human_behav import *

def apply_to_job(page, job, config):

    print("\n====================================")
    print(f"Opening Job: {job['title']}")
    print(f"Company: {job['company']}")
    print("====================================")

    try:

        print("\nJOB URL:")
        print(job["link"])

        page.goto(
            job["link"],
            timeout=120000,
            wait_until="domcontentloaded"
        )

        try:
            page.wait_for_load_state(
                "domcontentloaded",
                timeout=10000
            )
        except Exception:
            pass

        print("\nCURRENT URL:")
        print(page.url)

        random_wait(5, 10)

        try:
            page.mouse.wheel(0, 2500)
        except Exception:
            pass

        random_wait(3, 5)

        print("\nPAGE TITLE:")
        print(page.title())

        page_text = page.content().lower()

        print(
            f"Easy Apply Exists In HTML: {'easy apply' in page_text}"
        )

        print(
            "Easy Apply Count:",
            page_text.count("easy apply")
        )

        print("\nSearching for Easy Apply...")

        easy_apply = None

        # Method 1
        try:

            locator = page.locator(
                "text=Easy Apply"
            )

            if locator.count() > 0:

                easy_apply = locator.first

                print(
                    "Found using text locator"
                )

        except Exception:
            pass

        # Method 2
        if easy_apply is None:

            try:

                locator = page.locator(
                    "button:has-text('Easy Apply')"
                )

                if locator.count() > 0:

                    easy_apply = locator.first

                    print(
                        "Found using button locator"
                    )

            except Exception:
                pass

        # Method 3
        if easy_apply is None:

            try:

                buttons = page.locator(
                    "button"
                ).all()

                print(
                    f"Found {len(buttons)} buttons"
                )

                for button in buttons:

                    try:

                        text = (
                            button.inner_text()
                            .strip()
                            .lower()
                        )

                        if text:
                            print(
                                "BUTTON:",
                                text
                            )

                        if (
                            "easy apply" in text
                            or "apply now" in text
                            or "continue application" in text
                        ):

                            easy_apply = button

                            print(
                                "Found by button scan"
                            )

                            break

                    except Exception:
                        pass

            except Exception:
                pass

        # CLICK EASY APPLY
        if easy_apply:

            print(
                "\nEASY APPLY FOUND"
            )

            human_click(
                easy_apply,
                page
            )

            random_wait(3, 6)

            upload_resume(
                page,
                config
            )

            fill_details(
                page,
                config
            )

            submit_application(
                page,
                config
            )

            return

        print(
            "\nNo Easy Apply button found"
        )

        page.screenshot(
            path="logs/no_easy_apply.png",
            full_page=True
        )

        print(
            "Screenshot saved to logs/no_easy_apply.png"
        )

    except Exception as e:

        print(
            "Apply Error:",
            e
        )


def upload_resume(page, config):

    try:

        uploads = page.locator(
            "input[type='file']"
        ).all()

        for upload in uploads:

            try:

                upload.set_input_files(
                    config["resume"]["path"]
                )

                print(
                    "Resume Uploaded"
                )

            except:
                pass

    except Exception as e:

        print(
            "Resume Upload Error:",
            e
        )


def fill_details(page, config):

    try:

        inputs = page.locator(
            "input"
        ).all()

        for input_box in inputs:

            try:

                label = (
                    input_box.get_attribute(
                        "aria-label"
                    )
                )

                if not label:
                    continue

                label = label.lower()

                if "phone" in label:

                    input_box.fill(
                        config["application"]["phone"]
                    )

                elif "experience" in label:

                    input_box.fill(
                        config["application"]["experience"]
                    )

                elif "notice" in label:

                    input_box.fill(
                        config["application"]["notice_period"]
                    )

            except:
                pass

    except Exception as e:

        print(
            "Fill Details Error:",
            e
        )


def submit_application(page, config):

    try:

        while True:

            fill_details(
                page,
                config
            )

            random_wait(2, 4)

            buttons = page.locator(
                "button"
            ).all()

            next_found = False

            for button in buttons:

                try:

                    text = (
                        button
                        .inner_text()
                        .strip()
                        .lower()
                    )

                    if "next" in text:

                        print(
                            "Clicking Next"
                        )

                        button.click()

                        next_found = True

                        break

                    elif "review" in text:

                        print(
                            "Clicking Review"
                        )

                        button.click()

                        next_found = True

                        break

                    elif (
                        "submit application"
                        in text
                    ):

                        print(
                            "Submitting Application"
                        )

                        button.click()

                        print(
                            "Application Submitted Successfully"
                        )

                        return

                except:
                    pass

            if not next_found:

                print(
                    "No more action buttons found"
                )

                break

    except Exception as e:

        print(
            "Submit Error:",
            e
        )