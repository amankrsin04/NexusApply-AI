
import time
import random


def random_wait(min_sec=2, max_sec=5):

    delay = random.uniform(
        min_sec,
        max_sec
    )

    print(
        f"Waiting {delay:.2f} sec"
    )

    time.sleep(delay)


def human_scroll(page):

    try:

        scroll_amount = random.randint(
            300,
            1500
        )

        page.mouse.wheel(
            0,
            scroll_amount
        )

        random_wait(1, 3)

    except Exception as e:

        print(
            "Scroll Error:",
            e
        )


def move_mouse_randomly(page):

    try:

        x = random.randint(
            100,
            800
        )

        y = random.randint(
            100,
            700
        )

        page.mouse.move(
            x,
            y,
            steps=random.randint(
                10,
                30
            )
        )

        random_wait(
            0.5,
            2
        )

    except Exception as e:

        print(
            "Mouse Error:",
            e
        )


def human_click(element, page):

    try:

        move_mouse_randomly(
            page
        )

        random_wait(
            1,
            3
        )

        element.click()

        random_wait(
            2,
            5
        )

    except Exception as e:

        print(
            "Click Error:",
            e
        )


def human_type(
    page,
    selector,
    text
):

    try:

        locator = page.locator(
            selector
        )

        locator.click()

        for char in str(text):

            locator.type(
                char,
                delay=random.randint(
                    50,
                    150
                )
            )

        random_wait(
            1,
            2
        )

    except Exception as e:

        print(
            "Typing Error:",
            e
        )


def read_job_page(page):

    try:

        human_scroll(page)

        random_wait(
            2,
            5
        )

        human_scroll(page)

        random_wait(
            2,
            4
        )

    except Exception as e:

        print(
            "Read Page Error:",
            e
        )
