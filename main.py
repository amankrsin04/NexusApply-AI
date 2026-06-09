from login import login_linkedin
from scraper import search_jobs
from database import init_db
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


def main():

    browser, page = login_linkedin(config)

    init_db(config)

    print("\n🚀 NexusApply AI Started\n")

    search_jobs(
        page,
        config
    )

    print("\n✅ Job Search Completed\n")

    browser.close()


if __name__ == "__main__":
    main()