# import smtplib

# my_email = "something@gmail.com"
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#         to_addrs="",
#         msg="Subject:Hello\n\n")


# import datetime as dt

# now = dt.datetime.now()
# year = now.year 
# month = now.month
# day = now.day
# day_of_the_week = now.weekday()

# date_of_birth = dt.datetime(year=1985, month=6, day=9, hour=9, minute=11)


import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("server@url.com") as connection: 
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivation\n\n{quote}")