import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

"INSERT INTO events VALUES ('Paramore', 'Tijuana', '2089.09.22')"

URL = "http://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data.db")

def scrape(URL):
    """Scrape the page source from the URL"""
    response = requests.get(URL)
    text = response.text
    return text

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value
def send_email():
    print("Email was sent!")

def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE date=? AND city=? AND date=?",(band, city, date))
    rows = cursor.fetchall()
    return rows

def send_email(message):
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
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    if extracted != "No upcoming tours":
        row = read(extracted)
        if not row:
            store(extracted)
            send_email(message="Hey, new event was found")
    time.sleep(2)


