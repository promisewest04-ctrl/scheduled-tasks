import os
import smtplib
from datetime import datetime as dt
from random import randint
import pandas as pd

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

today = (dt.now().month, dt.now().day)

df = pd.read_csv("birthdays.csv")
birthday_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}


if today in birthday_dict:
    friend_name = df.loc[0, "name"]
    friend_email = df.loc[0, "email"]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", friend_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=friend_email,
            msg=f"Subject: Happy birthday!\n\n{new_letter}")
        connection.close()

