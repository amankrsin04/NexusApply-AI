
import time
import random

from apply import apply_to_job
from database import save_job


def search_jobs(page, config):

    keywords = config["search"]["keywords"]
    locations = config["search"]["locations"]

    all_jobs = []

    # STEP 1: SCRAPE EVERYTHING FIRST
    for keyword in keywords:

        for location in locations:

            search_url = (
                f"https://www.linkedin.com/jobs/search/"
                f"?keywords={keyword}"
                f"&location={location}"
                f"&f_AL=true"
                f"&f_TPR=r86400"
                f"&sortBy=DD"
            )

            print(f"\nSearching: {keyword} in {location}")

            try:

                page.goto(
                    search_url,
                    timeout=120000,
                    wait_until="domcontentloaded"
                )

                time.sleep(
                    random.randint(5, 10)
                )

            except Exception as e:

                print(
                    "Search page failed:",
                    e
                )

                continue

            try:

                page.mouse.wheel(
                    0,
                    3000
                )

                time.sleep(
                    random.randint(3, 6)
                )

                jobs = page.query_selector_all(
                    "div.job-card-container"
                )

                print(
                    f"Found {len(jobs)} raw jobs"
                )

                for job in jobs:

                    try:

                        title_element = (
                            job.query_selector("a")
                        )

                        company_element = (
                            job.query_selector(
                                ".artdeco-entity-lockup__subtitle"
                            )
                        )

                        if not title_element:
                            continue

                        title = (
                            title_element
                            .inner_text()
                            .strip()
                        )

                        company = (
                            company_element
                            .inner_text()
                            .strip()
                            if company_element
                            else "Unknown"
                        )

                        link = (
                            title_element
                            .get_attribute("href")
                        )

                        if not link:
                            continue

                        if link.startswith("/"):

                            link = (
                                "https://www.linkedin.com"
                                + link
                            )

                        all_jobs.append({
                            "title": title,
                            "company": company,
                            "link": link
                        })

                    except Exception as e:

                        print(
                            "Scrape Error:",
                            e
                        )

            except Exception as e:

                print(
                    "Main scrape error:",
                    e
                )

    # STEP 2: REMOVE DUPLICATES

    unique_jobs = []

    seen_links = set()

    for job in all_jobs:

        if job["link"] not in seen_links:

            seen_links.add(
                job["link"]
            )

            unique_jobs.append(
                job
            )

    print(
        f"\nTotal Unique Jobs: {len(unique_jobs)}"
    )

    # STEP 3: APPLY

    for job in unique_jobs:

        try:

            print(
                "\n----------------------------"
            )

            print(
                "JOB FOUND"
            )

            print(
                "Title :",
                job["title"]
            )

            print(
                "Company :",
                job["company"]
            )

            print(
                "----------------------------"
            )

            save_job(
                config,
                job
            )

            apply_to_job(
                page,
                job,
                config
            )

            time.sleep(
                random.randint(
                    15,
                    30
                )
            )

        except Exception as e:

            print(
                "Apply Error:",
                e
            )