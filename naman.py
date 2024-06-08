import http.client
import smtplib
import json
import mysql.connector

def send_email(gmail_user, gmail_password, to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(gmail_user, to, message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_flight_price(threshold_price, origin, destination, departure_date, gmail_user, gmail_password, to):
    conn = http.client.HTTPSConnection("skyscanner44.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "391b963115mshce04a831da08a63p108593jsne68fc1cf2ede",
        'X-RapidAPI-Host': "skyscanner44.p.rapidapi.com"
    }
    path = f"/search?adults=1&origin={origin}&destination={destination}&departureDate={departure_date}&currency=INR"
    conn.request("GET", path, headers=headers)
    res = conn.getresponse()
    flight_data = json.loads(res.read().decode())
    ##print(flight_data)

    flight_prices = []
    booking_links = []  ##isko comment kiya tha
    pricing_options = flight_data['itineraries']['buckets'][0]['items']

    for item in pricing_options:
        flight_prices.append(item['price']['raw'])
        deeplink = item.get("deeplink", None)
        if deeplink:
            booking_links.append(deeplink)
    if len(flight_prices) > 0:
        if min(flight_prices) <= threshold_price:
            
              
            
            conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="user901",
            database="flight_system"
            )
            cursor = conn.cursor()
            query = f"INSERT INTO last_info2 (email,prices,origin,destination,departure_date) VALUES ('{to}', '{flight_prices}', '{origin}',{destination},{departure_date})"
            cursor.execute(query)
            conn.commit()
            subject = "Cheap flight alert!"
            body = f"The following flights can be booked for INR {flight_prices}:\n{booking_links}"
            send_email(gmail_user, gmail_password, to, subject, body)
        else:
            print("No flights available for the given criteria.")
    else:
        print("No flights available for the given criteria.")

def register(first_name, last_name, email, password):
 conn = mysql.connector.connect(
 host="127.0.0.1",
 user="root",
 password="user901",
 database="flight_system"
 )
 cursor = conn.cursor()
 query = f"INSERT INTO user_info (first_name, last_name, email, password) VALUES ('{first_name}', '{last_name}', '{email}', '{password}')"
 cursor.execute(query)
 conn.commit()
 print("User registered successfully.")
 print("Registeration successful , re-run the program and login")

def login(email, password):
 conn = mysql.connector.connect(
 host="127.0.0.1",
 user="root",
 password="user901",
 database="flight_system"
 )
 cursor = conn.cursor()
 query = f"SELECT * FROM user_info WHERE email = '{email}' AND password = '{password}'"
 cursor.execute(query)
 result = cursor.fetchone()
 if result:
  print("Login successful.")
  threshold_price = int(input("Enter the maximum price you're willing to pay for the flight: "))
  origin = input("Enter the origin airport code (e.g. SFO): ")
  destination = input("Enter the destination airport code (e.g. JFK): ")
  departure_date = input("Enter the departure date (YYYY-MM-DD): ")
  gmail_user = "it.b.03.naman.mishra@gmail.com"
  gmail_password = "usvcxvgnmttbrpiv"
  to=email
  ##to = input("Enter the email address you want to send the alert to: ")
  check_flight_price(threshold_price, origin, destination, departure_date, gmail_user, gmail_password, to)
 else:
  print("Login failed. Email or password is incorrect.")
  
if __name__ == '__main__':
    
    n = int(input("Enter a choice: \n1.Register \n 2.Login \n3.Exit \n "))
    if n==1:
        first_name= input("Enter your first name:")
        last_name=input("Enter your last name:")
        email=input("Enter your email:")
        password=input("Enter your password:")
        register(first_name, last_name, email, password)
    elif n==2:
        email=input("Enter your email:")
        password=input("Enter your password:")
        login(email, password)
    else:
        print("Exit sucessfull")