import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

gmail = os.getenv('EMAIL')
passwo = os.getenv('PASSWORD')

connection = smtplib.SMTP('smtp.gmail.com',587)

connection.starttls()


def gmail_transfer(to_gmail, name, text_data):
    
    connection.login(user=gmail,password=passwo)

    connection.sendmail(from_addr=gmail, to_addrs=to_gmail, msg=f"Subject: Hi {name} , Here is your report from MyDoctorAlly\n\n {text_data} ")

    connection.close()





































'''
import smtplib

try:
    connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    connection.login('your_email@gmail.com', 'your_password')
    print("Connected successfully")
    connection.quit()
except Exception as e:
    print(f"An error occurred: {e}")

'''