# Weather SQL WebScrape

This Python project scrapes tour events from a webpage, stores them in an SQLite database, and sends email notifications when new events are detected. The project runs continuously in a loop, checking for new events every 2 seconds.
Features

    Web Scraping: Scrapes tour event data from a specified URL using requests and selectorlib.
    SQLite Database: Stores the scraped data in an SQLite database to avoid duplicate notifications.
    Email Notification: Sends an email when a new event is detected using SMTP.
    Continuous Monitoring: Runs in a loop, checking for new events at regular intervals (every 2 seconds).

Prerequisites

Before running the project, ensure you have the following:

    Python 3.x installed.
    The required Python libraries installed:

bash

pip install requests selectorlib smtplib sqlite3

    Create the required SQLite database and table:

bash

sqlite3 data.db

CREATE TABLE events (
  band TEXT,
  city TEXT,
  date TEXT
);

    YAML file for Selectorlib: Ensure that the extract.yaml file is present in the same directory. It contains the extraction logic for scraping the webpage.

Example extract.yaml

yaml

tours:
    css: "div.tours"
    type: Text

Configuration
URL

The script scrapes data from the following URL by default:

python

URL = "http://programmer100.pythonanywhere.com/tours/"

You can change this URL to the target page you want to scrape.
Email Credentials

Update the email credentials in the Email class:

python

username = "your_email@gmail.com"
password = "your_email_password"
receiver = "receiver_email@gmail.com"

Make sure to generate an app-specific password if you are using Gmail with two-factor authentication.
How It Works

    Scraping the Webpage: The Event class scrapes the webpage using the requests library and extracts relevant data (tour information) using selectorlib.

    Storing Data: The Database class interacts with an SQLite database. It stores the scraped tour data to prevent sending duplicate notifications for the same event.

    Email Notifications: The Email class is responsible for sending email notifications when a new event is detected.

    Looping and Monitoring: The script runs indefinitely in a loop, checking the URL every 2 seconds for new events.

Running the Project

    Clone or download the project.
    Make sure the required CSV files and extract.yaml are in the same directory.
    Set up your SQLite database as described above.
    Run the Python script:

bash

python scraper.py

    The script will scrape the URL, detect new events, store them in the SQLite database, and send an email if a new event is found.

Example Output

csharp

No upcoming tours
Band X, City Y, 2024-10-04
Hey, new event was found

When a new event is detected, you'll receive an email notification that looks like this:

vbnet

Subject: New Event Found
Message: Hey, new event was found

Project Structure

bash

project-folder/
│
├── data.db              # SQLite database
├── scraper.py           # Main Python script
├── extract.yaml         # Selectorlib YAML configuration
└── README.md            # This readme file

Notes

    Ensure the YAML configuration matches the structure of the webpage you are scraping.
    Use an app-specific password if using Gmail for email notifications.
