import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"


class Event:
    def scrape(self, URL):
        """Scrape the page source from the URL"""
        response = requests.get(URL)
        text = response.text
        return text

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Database:

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)

    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE date=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        return rows


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "enio2298@gmail.com"
        password = "ekik jotj jhco yyqx"

        receiver = "enio2298@gmail.com"
        my_context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=my_context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message.encode("utf8"))


while True:
    event = Event()
    scraped = event.scrape(URL)
    extracted = event.extract(scraped)
    print(extracted)

    if extracted != "No upcoming tours":
        database = Database(database_path="data.db")
        row = database.read(extracted)
        if not row:
            database.store(extracted)
            email = Email()
            email.send(message="Hey, new event was found")
    time.sleep(2)
