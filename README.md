# Coding Challenge - Wagtail

Repository for the coding challenge.

## Prompt

### Backstory

At the company Widgets and More, we pride ourselves making the best widgets in the industry and for all your widgety needs. However, in this day and age, one needs a digital presence in order to get the word out about our wonderful widgets, any information and documentation regarding said widgets, and ways to interact with our widget-buying customers and clients.

With a launch of the newest and shiniest Widget, yet, we need to get the news out there and need a new type of page in our content management system (CMS).

### Task at Hand

Time Limit: 90 minutes

Requirements:

* Create a `WidgetDocumentation` within the Wagtail CMS. This page type should be able to handle a title, description, and body content as rich text.

* Since the documentation page can become rather long, we'll want a table of contents at the top of the page that can deeplink to the different major sections/headings

## Development Environment

### Requirements

* Python > 3.8

### Setup

0. (Optional but recommended) Create a virtual environment and activate it

    ```sh
    python -m venv venv
    source ./venv/bin/activate
    ```

1. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

2. Install browsers for Playwright

    ```sh
    playwright install
    ```

3. Get the server up and running

    ```sh
    python manage.py runserver
    ```

4. Manually test the site in a browser at `http://localhost:8000`

5. Test Playwright (automated testing framework) is working

    ```sh
    pytest
    ```

6. Assuming steps 4 and 5 worked for you, you're all set! 🎉

### Notes

* Super User Login (username/password): admin/admin
* To stop the server, use ctrl + c or cmd + c
* To deactivate your environment

    ```shell
    deactivate
    ```

## Reference Links

* [Wagtail](https://docs.wagtail.org/en/stable/)
* [Playwright](https://playwright.dev/python/)