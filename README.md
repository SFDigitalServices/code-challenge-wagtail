# Coding Challenge - Wagtail

Repository for the coding challenge.

## Prompt

### Backstory

At the company Widgets and More, we pride ourselves making the best widgets in the industry and for all your widgety needs. However, in this day and age, one needs a digital presence in order to get the word out about our wonderful widgets, any information and documentation regarding said widgets, and ways to interact with our widget-buying customers and clients.

With a launch of the newest and shiniest Widget, yet, we need to get the news out there and need a new type of page in our content management system (CMS).

### Task at Hand

Time Limit: 90 minutes

* Create a new Page Type within the Wagtail CMS. This page type should contain a Rich Text field in which we can enter text and formatting.
* After creating a new Page Type, we will need to create a template in order for it to be rendered in a browser.

## Development Environment

### Requirements

* Python > 3.8

### Setup

0. (Optional but recommended) Create a virtual environment and activate it

    ```bash
    python -m venv venv
    source ./venv/bin/activate
    ```

1. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

2. Get the server up and running

    ```bash
    python manage.py runserver
    ```

3. Visit the site in a browser at `http://localhost:8000`

### Notes

* Super User Login (username/password): admin/admin
* To stop the server, use ctrl + c or cmd + c
* To deactivate your environment

    ```shell
    deactivate
    ```
