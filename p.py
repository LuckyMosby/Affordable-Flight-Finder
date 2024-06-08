import http.client
import smtplib
import json
import mysql
import tkinter as tk

def send_email(gmail_user, gmail_password, to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(gmail_user, to, message)
        server.quit()
        show_success_window()
    except Exception as e:
        show_failed_window()
        
def show_success_window():
    window = tk.Tk()

# Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate x and y coordinates for the top-left corner of the window
    x = (screen_width // 2) - (200 // 2)
    y = (screen_height // 2) - (100 // 2)
    window.geometry("300x100+{}+{}".format(x, y))  # Set window position and size
    window.configure(bg="#1df6f6")  # Set background color of window
    label = tk.Label(window, text="Email Sent!", anchor="center", font=("Oswald", 15))
    label.configure(bg="#1df6f6")  # Set background color of label
    window.title("Email Automation")
    label.pack(pady=20)
    window.after(3000, lambda: window.destroy())
    window.mainloop()
    
    
def show_failed_window():
    window = tk.Tk()

# Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate x and y coordinates for the top-left corner of the window
    x = (screen_width // 2) - (200 // 2)
    y = (screen_height // 2) - (100 // 2)
    window.geometry("300x100+{}+{}".format(x, y))  # Set window position and size
    window.configure(bg="#1df6f6")  # Set background color of window
    label = tk.Label(window, text="Failed to send the email!", anchor="center", font=("Oswald", 15))
    label.configure(bg="#1df6f6")  # Set background color of label
    window.title("Email Automation")
    label.pack(pady=20)
    window.after(3000, lambda: window.destroy())
    window.mainloop()

def check_flight_price(threshold_price, origin, destination, departure_date, gmail_user, gmail_password, to):
    conn = http.client.HTTPSConnection("skyscanner44.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "ca21c55823msh3e75d5f792b1255p178fefjsn3bbf77a1eb13",
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
            subject = "Cheap flight alert!"
            body = f"The following flights can be booked for {flight_prices[0]}:\n{booking_links[0]} \n {flight_prices[1]}:\n{booking_links[1]}  \n {flight_prices[2]}:\n{booking_links[2]}"  
            send_email(gmail_user, gmail_password, to, subject, body)
            conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="user901",
            database="flight_system"
            )
            cursor = conn.cursor()
            query = f"INSERT INTO naya (email,prices,links) VALUES ('{to}', '{json.dumps(flight_prices)}', '{json.dumps(booking_links)}')"
            cursor.execute(query)
            conn.commit()
        else:
            window = tk.Tk()
            # Get screen width and height
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            # Calculate x and y coordinates for the top-left corner of the window
            x = (screen_width // 2) - (200 // 2)
            y = (screen_height // 2) - (100 // 2)
            window.geometry("400x100+{}+{}".format(x, y))  # Set window position and size
            window.configure(bg="#1df6f6")  # Set background color of window
            label = tk.Label(window, text="No flights available for the given criteria.", anchor="center", font=("Oswald", 15))
            label.configure(bg="#1df6f6")  # Set background color of label
            window.title("Email Automation")
            label.pack(pady=20)
            window.after(3000, lambda: window.destroy())
            window.mainloop()
    else:
        window = tk.Tk()
        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Calculate x and y coordinates for the top-left corner of the window
        x = (screen_width // 2) - (200 // 2)
        y = (screen_height // 2) - (100 // 2)
        window.geometry("400x100+{}+{}".format(x, y))  # Set window position and size
        window.configure(bg="#1df6f6")  # Set background color of window
        label = tk.Label(window, text="No flights available for the given criteria.", anchor="center", font=("Oswald", 15))
        label.configure(bg="#1df6f6")  # Set background color of label
        window.title("Email Automation")
        label.pack(pady=20)
        window.after(3000, lambda: window.destroy())
        window.mainloop()