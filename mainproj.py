import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql
from p import check_flight_price
import pandas as pd



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        import re
        import mysql.connector

        class LabelClickable(QLabel):
            def __init__(self, parent=None):
                super().__init__(parent)

            def mousePressEvent(self, event):
                if event.button() == Qt.LeftButton:
                    handle_click()


        font = QFont()
        font.setFamily("Oswald")
        font.setPointSize(15)

        # Adding the gif
        self.movie = QMovie("animation.gif")
        self.movie.setSpeed(int(1000 / 2))
        self.label = QLabel(self)
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)
        self.label.setGeometry(0, 0, 200, 200)

        # Adding the title
        self.title = QLabel(self)
        self.title.setText("AFFORDABLE FLIGHTS")
        self.title.setGeometry(self.label.width()-30, 0, self.title.width() + 400, self.label.height()-15)
        self.title.setContentsMargins(20,20,20,20)
        font.setPointSize(24)
        font.setBold(True)
        self.title.setFont(font)

        # Start the gif animation
        self.movie.start()

        font.setBold(False)

        #Question mark animation
        self.question = QMovie("question.gif")
        self.question.setSpeed(int(1000 / 4))
        self.question.start()
        self.label1 = QLabel(self)
        self.label1.setMovie(self.question)
        self.label1.setScaledContents(True)
        self.label1.setGeometry(0, 200, 400, 400)

        
        



        # Login Frame
        self.frame_login = QFrame(self)
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setGeometry(self.title.width()+self.label.width(), -225, 800, 400)
        self.frame_login.setStyleSheet("background-color: #FCFCFC; border: 0px; border-bottom-left-radius: 100px; border-top-right-radius: 30px;")

        # Decor Frame
        self.frame_login = QFrame(self)
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setGeometry(1250, 0, 800, 800)
        self.frame_login.setStyleSheet("background-color: #FCFCFC; border: 0px; border-bottom-left-radius: 100px; border-top-right-radius: 30px;")


        self.frame_2 = QFrame(self)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setGeometry(self.label1.width(), 175, 850, 400)
        self.frame_2.setStyleSheet("background-color: #FCFCFC;border: 0px;")
        
        
        self.frame_3 = QFrame(self)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setGeometry(self.label1.width(), 175, 850, 400)
        self.frame_3.setStyleSheet("background-color: #1df6f6; border: 0px; border-bottom-left-radius: 30px; border-top-right-radius: 50px;")

        # Register frame
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setGeometry(self.label1.width(), 225, 800, 400)
        self.frame.setStyleSheet("background-color: #FCFCFC; border: 0px; border-bottom-left-radius: 30px; border-top-right-radius: 30px;")
        
        #down anim
        self.downarr = QMovie("downarrow.gif")
        self.downarr.setSpeed(int(1000 / 5))
        self.downarr.start()
        self.label3 = QLabel(self)
        self.label3.setMovie(self.downarr)
        self.label3.setScaledContents(True)
        self.label3.setGeometry(810, 227, 75, 75)


        # Already lable
        self.already = QLabel(self)
        self.already.setAttribute(Qt.WA_TranslucentBackground, True)
        self.already.setText("Already Registered? \nLogin Here")
        self.already.setGeometry(self.title.width()+self.label.width()+75, -20, 500, 200)
        self.already.setContentsMargins(20,20,20,20)
        font.setPointSize(13)
        self.already.setFont(font)


        #login gif
        self.login_gif = QMovie("login.gif")
        self.login_gif.setSpeed(int(1000 / 5))
        self.login_gif.start()
        self.login_button = LabelClickable(self)
        self.login_button.setMovie(self.login_gif)
        self.login_button.setScaledContents(True)
        self.login_button.setGeometry(1000,0,175,175)



        # first time lable
        self.first = QLabel(self)
        self.first.setAttribute(Qt.WA_TranslucentBackground, True)
        self.first.setText("First time user? Register here")
        self.first.setGeometry(410, 165, 500, 200)
        self.first.setContentsMargins(20,20,20,20)
        font.setPointSize(18)
        self.first.setFont(font)

        # first name lable
        self.first_name = QLabel(self)
        self.first_name.setAttribute(Qt.WA_TranslucentBackground, True)
        self.first_name.setText("First Name")
        self.first_name.setGeometry(self.label1.width()+50, self.label.height()+40, 500, 200)
        self.first_name.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.first_name.setFont(font)

        #first name textbox
        self.first_name_text = QLineEdit(self)
        self.first_name_text.setGeometry(610, self.label.height()+127,175,30)
        self.first_name_text.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.first_name_text.setFont(font)

        # Last name lable
        self.last_name = QLabel(self)
        self.last_name.setAttribute(Qt.WA_TranslucentBackground, True)
        self.last_name.setText("Last Name")
        self.last_name.setGeometry(self.label1.width()+380, self.label.height()+40, 500, 200)
        self.last_name.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.last_name.setFont(font)

        # Last name textbox
        self.last_name_text = QLineEdit(self)
        self.last_name_text.setGeometry(935, self.label.height()+127,175,30)
        self.last_name_text.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.last_name_text.setFont(font)

        # email lable
        self.email = QLabel(self)
        self.email.setAttribute(Qt.WA_TranslucentBackground, True)
        self.email.setText("Email")
        self.email.setGeometry(self.label1.width()+50, self.label.height()+100, 500, 200)
        self.email.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.email.setFont(font)

        #email textbox
        self.email_textbox = QLineEdit(self)
        self.email_textbox.setGeometry(610, self.label.height() + 187, 500, 30)
        self.email_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.email_textbox.setFont(font)
        regex = QRegExp("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
        validator = QRegExpValidator(regex)
        self.email_textbox.setValidator(validator)
        self.email_textbox.textChanged.connect(self.update_text)

        # password label
        self.password_text = QLabel(self)
        self.password_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.password_text.setText("Password")
        self.password_text.setGeometry(self.label1.width()+50, self.label.height()+160, 500, 200)
        self.password_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.password_text.setFont(font)

        #password textbox
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.password_textbox.setGeometry(610, self.label.height()+247,500,30)
        self.password_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")

        #Submit Button
        self.submit_button = QPushButton("SUBMIT", self)
        self.submit_button.setGeometry(self.label1.width() + 250, 515, 300, 50)
        self.submit_button.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px;")
        font = self.submit_button.font()
        font.setPointSize(14)
        self.submit_button.setFont(font)
        self.submit_button.clicked.connect(self.submit_function_resgister)

        

        # Add stylesheet for hover effect
        self.submit_button.setStyleSheet("""
            QPushButton:hover{
                background-color: #2196F3;
                color: white;
            }
            QPushButton{
                background-color: #ebebeb;
                border: 0px solid transparent;
                border-radius: 7px;
            }
        """)

        self.error_label = QLabel(self)
        self.error_label.setGeometry(610, self.email_textbox.height() + self.email_textbox.y() + 20, 500, 30)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.hide()

        # Window settings
        self.setWindowTitle("Flight Prices")
        self.resize(1280, 720)
        self.setStyleSheet("background-color: #1df6f6;")



        def handle_click():


            font = QFont()
            font.setFamily("Oswald")
            font.setPointSize(15)

            
            self.first_name.setVisible(False)
            self.first_name_text.setVisible(False)
            self.last_name.setVisible(False)
            self.last_name_text.setVisible(False)
            self.label3.setVisible(False)
            self.email.move(self.label1.width()+50,270)
            self.email_textbox.move(610,355)
            self.password_text.move(450,335)
            self.password_textbox.move(610,420)

            self.email_textbox.clear()
            self.password_textbox.clear()

            self.first.setText("Welcome Back! Lets get Started")
            font.setPointSize(17)
            self.first.setFont(font)
            self.first.move(420, 175)

            self.already.setText("First time user? \nTry reloading the page")
            self.already.setGeometry(self.title.width()+self.label.width()+25, -20, 500, 200)
            self.login_button.setVisible(False)

            self.register_gif = QMovie("question_white.gif")
            self.register_gif.setSpeed(int(1000 / 5))
            self.register_gif.start()
            self.register_button = QLabel(self)
            self.register_button.setMovie(self.register_gif)
            self.register_button.setScaledContents(True)
            self.register_button.setGeometry(1000,0,175,175)
            self.register_button.setVisible(True)




            self.login_blue = QMovie("login_blue.gif")
            self.login_blue.setSpeed(int(1000 / 5))
            self.login_blue.start()
            self.label1.setMovie(self.login_blue)


            self.submit_button.setVisible(False)

            #Submit Button
            self.submit_button_login = QPushButton("SUBMIT", self)
            self.submit_button_login.setVisible(True)
            self.submit_button_login.setGeometry(self.label1.width() + 250, 515, 300, 50)
            self.submit_button_login.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px;")
            font = self.submit_button_login.font()
            font.setPointSize(14)
            self.submit_button_login.setFont(font)
            self.submit_button_login.clicked.connect(self.submit_function_login)
            # Add stylesheet for hover effect
            self.submit_button_login.setStyleSheet("""
                QPushButton:hover{
                    background-color: #2196F3;
                    color: white;
                }
                QPushButton{
                    background-color: #ebebeb;
                    border: 0px solid transparent;
                    border-radius: 7px;
                }
            """)
            print("Label clicked") 
            self.error_label = QLabel(self)
            self.error_label.setGeometry(610, self.email_textbox.height() + self.email_textbox.y() + 20, 500, 30)
            self.error_label.setAlignment(Qt.AlignCenter)
            self.error_label.hide()

            


    def onTextChangedOrigin(self):
        # Get the text from the QLineEdit widget
        text = self.iata_text_origin.text()

        # Check if the text is in the full names list
        if text in self.full_names:
            # If it is, get the corresponding IATA code from the dictionary
            self.iata_code = self.iata_full_name_dict[text]
            
            # Set the text of the QLineEdit widget to the IATA code
            self.iata_text_origin.setText(self.iata_code)

    def onTextChangeddestination(self):
        # Get the text from the QLineEdit widget
        text = self.iata_text_destination.text()

        # Check if the text is in the full names list
        if text in self.full_names:
            # If it is, get the corresponding IATA code from the dictionary
            self.iata_code = self.iata_full_name_dict[text]
            
            # Set the text of the QLineEdit widget to the IATA code
            self.iata_text_destination.setText(self.iata_code)

    def start_animation(self, event):
        self.login_anim.start()
        
    def stop_animation(self, event):
        self.login_anim.stop()

    def submit_function_login(self):
        print("Login")

        
        
        email = self.email_textbox.text()
        password = self.password_textbox.text()

        if not (email and password):
            QMessageBox.warning(self, "Warning", "Please fill in all fields")
            return

        db = mysql.connector.connect(host='127.0.0.1', port=3306, username = 'root' , password = 'user901', database ='flight_system')
        cursor = db.cursor()

        # Check if email already exists
        cursor.execute(f"SELECT password FROM user_info WHERE email = '{email}'")
        stored_password = cursor.fetchone()[0]
        if stored_password == password:
            font = QFont()
            font.setFamily("Oswald")
            font.setPointSize(15)
            self.frame_2 = QFrame(self)
            self.frame_2.setFrameShape(QFrame.StyledPanel)
            self.frame_2.setGeometry(self.label1.width(), 225, 800, 400)
            self.frame_2.setStyleSheet("background-color: #FCFCFC; border: 0px; border-bottom-left-radius: 30px; border-top-right-radius: 30px;")
            self.frame_2.setVisible(True)





            self.first_name.setVisible(False)
            self.first_name_text.setVisible(False)
            self.last_name.setVisible(False)
            self.last_name_text.setVisible(False)
            self.email.setVisible(False)
            self.email_textbox.setVisible(False)
            self.password_text.setVisible(False)
            self.password_textbox.setVisible(False)
            self.label3.setVisible(False)
            self.first.setVisible(False)
            self.submit_button.setVisible(False)
           


            self.threshhold_price_text = QLabel(self)
            self.threshhold_price_text.setAttribute(Qt.WA_TranslucentBackground, True)
            self.threshhold_price_text.setText("Threshold Price (INR)")
            self.threshhold_price_text.setGeometry(self.label1.width()+20, self.label.height()+40, 500, 200)
            self.threshhold_price_text.setContentsMargins(20,20,20,20)
            font.setPointSize(15)
            self.threshhold_price_text.setFont(font)
            self.threshhold_price_text.setVisible(True)

            self.threshhold_price_textbox = QLineEdit(self)
            self.threshhold_price_textbox.setGeometry(700, self.label.height()+127,175,30)
            self.threshhold_price_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
            font.setPointSize(13)
            self.threshhold_price_textbox.setFont(font)

            validator = QIntValidator()
            self.threshhold_price_textbox.setValidator(validator)

            self.threshhold_price_textbox.setVisible(True)


            #everyting about IATA

        # Load the CSV file into a pandas DataFrame
            self.df = pd.read_csv('cleaned_iata.csv')

            # Get a list of IATA codes
            self.iata_codes = self.df['iata_code'].tolist()

            # Get a list of full names of airports
            self.full_names = self.df['name'].tolist()

            # Create a dictionary with full names as keys and IATA codes as values
            self.iata_full_name_dict = dict(zip(self.full_names, self.iata_codes))

            # Create a Origin widget
            self.iata_text_origin = QLineEdit(self)
            self.iata_text_origin.setGeometry(700, self.label.height()+187,175,30)
            self.iata_text_origin.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
            font.setPointSize(13)
            self.iata_text_origin.setFont(font)
            # Set a completion list for the Origin widget
            completer = QCompleter(self.iata_codes + self.full_names)
            self.iata_text_origin.setCompleter(completer)
            self.iata_text_origin.textChanged.connect(self.onTextChangedOrigin)
            self.iata_text_origin.setVisible(True)


            # Create a Origin widget
            self.iata_text_destination = QLineEdit(self)
            self.iata_text_destination.setGeometry(700, self.label.height()+247,175,30)
            self.iata_text_destination.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
            font.setPointSize(13)
            self.iata_text_destination.setFont(font)
            # Set a completion list for the Origin widget
            completer = QCompleter(self.iata_codes + self.full_names)
            self.iata_text_destination.setCompleter(completer)
            self.iata_text_destination.textChanged.connect(self.onTextChangeddestination)
            self.iata_text_destination.setVisible(True)
            print("hii")

            
            self.Origin_text = QLabel(self)
            self.Origin_text.setAttribute(Qt.WA_TranslucentBackground, True)
            self.Origin_text.setText("Origin")
            self.Origin_text.setGeometry(self.label1.width()+20, self.label.height()+100, 500, 200)
            self.Origin_text.setContentsMargins(20,20,20,20)
            font.setPointSize(15)
            self.Origin_text.setFont(font)
            self.Origin_text.setVisible(True)

            self.Destination_text = QLabel(self)
            self.Destination_text.setAttribute(Qt.WA_TranslucentBackground, True)
            self.Destination_text.setText("Destination")
            self.Destination_text.setGeometry(self.label1.width()+20, self.label.height()+160, 500, 200)
            self.Destination_text.setContentsMargins(20,20,20,20)
            font.setPointSize(15)
            self.Destination_text.setFont(font)
            self.Destination_text.setVisible(True)


            self.Date_of_departure = QLabel(self)
            self.Date_of_departure.setAttribute(Qt.WA_TranslucentBackground, True)
            self.Date_of_departure.setText("Date of Departure")
            self.Date_of_departure.setGeometry(self.label1.width()+20, self.label.height()+220, 500, 200)
            self.Date_of_departure.setContentsMargins(20,20,20,20)
            font.setPointSize(15)
            self.Date_of_departure.setFont(font)
            self.Date_of_departure.setVisible(True)

            # Last name textbox
            self.Date_of_Departure_textbox = QLineEdit(self)
            self.Date_of_Departure_textbox.setGeometry(700, self.label.height()+307,175,30)
            self.Date_of_Departure_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
            font.setPointSize(13)
            self.Date_of_Departure_textbox.setFont(font)
            self.Date_of_Departure_textbox.setVisible(True)

            
            self.clndr= QCalendarWidget(self)
            self.clndr.setGeometry(10,10,500,500)
            # Set a validator to only allow dates in the format "YYYY-MM-DD"
            date_validator = QRegExpValidator(QRegExp("\d{4}-\d{2}-\d{2}"))
            self.Date_of_Departure_textbox.setValidator(date_validator)

            # Connect the textEdited signal to the custom slot
            self.Date_of_Departure_textbox.textEdited.connect(self.check_date_validity)
            



        #everyting about IATA

        # Load the CSV file into a pandas DataFrame
            self.df = pd.read_csv('cleaned_iata.csv')

            # Get a list of IATA codes
            self.iata_codes = self.df['iata_code'].tolist()

            # Get a list of full names of airports
            self.full_names = self.df['name'].tolist()

            # Create a dictionary with full names as keys and IATA codes as values
            self.iata_full_name_dict = dict(zip(self.full_names, self.iata_codes))

            # Create a Origin widget
            self.iata_text_origin = QLineEdit(self)
            self.iata_text_origin.setGeometry(700, self.label.height()+187,175,30)
            self.iata_text_origin.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
            font.setPointSize(13)
            self.iata_text_origin.setFont(font)
            # Set a completion list for the Origin widget
            completer = QCompleter(self.iata_codes + self.full_names)
            self.iata_text_origin.setCompleter(completer)
            self.iata_text_origin.textChanged.connect(self.onTextChangedOrigin)
            self.iata_text_origin.setVisible(True)


            # Create a Origin widget
            self.iata_text_destination = QLineEdit(self)
            self.iata_text_destination.setGeometry(700, self.label.height()+247,175,30)
            self.iata_text_destination.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
            font.setPointSize(13)
            self.iata_text_destination.setFont(font)
            # Set a completion list for the Origin widget
            completer = QCompleter(self.iata_codes + self.full_names)
            self.iata_text_destination.setCompleter(completer)
            self.iata_text_destination.textChanged.connect(self.onTextChangeddestination)
            self.iata_text_destination.setVisible(True)
            print("hii")



            self.submit_Data = QPushButton("GET MY DATA", self)
            self.submit_Data.setGeometry(self.label1.width() + 500, 325, 215, 215)
            self.submit_button.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 20px;")
            font = self.submit_Data.font()
            font.setPointSize(14)
            self.submit_Data.setFont(font)
            self.submit_Data.clicked.connect(self.get_data_login)
            self.submit_Data.setVisible(True)

            # Add stylesheet for hover effect
            self.submit_Data.setStyleSheet("""
                QPushButton:hover{
                    background-color: #2196F3;
                    color: white;
                }
                QPushButton{
                    background-color: #ebebeb;
                    border: 0px solid transparent;
                    border-radius: 7px;
                }
            """)

        else:
            print("Error")
        # Insert the new data
        db.commit()
        db.close()

    def get_data_login(self):
        threshold = int(self.threshhold_price_textbox.text())
        origin = self.iata_text_origin.text()
        destination = self.iata_text_destination.text()
        date = self.Date_of_Departure_textbox.text()
        email = self.email_textbox.text() 
        check_flight_price(threshold, origin, destination, date, gmail_user = "it.b.03.naman.mishra@gmail.com", gmail_password="usvcxvgnmttbrpiv", to = email)
        print("DKMKC")

    def get_data_register(self):
        threshold = int(self.threshhold_price_textbox.text())
        origin = self.iata_text_origin.text()
        destination = self.iata_text_destination.text()
        date = self.Date_of_Departure_textbox.text()
        email = self.email_textbox.text() 
        check_flight_price(threshold, origin, destination, date, gmail_user = "it.b.03.naman.mishra@gmail.com", gmail_password="usvcxvgnmttbrpiv", to = email)
        print("DKMKC")

    def submit_function_resgister(self):
        print("register")
        import re
        first_name = self.first_name_text.text()
        last_name = self.last_name_text.text()
        email = self.email_textbox.text()
        password = self.password_textbox.text()

        if not (first_name and last_name and email and password):
            QMessageBox.warning(self, "Warning", "Please fill in all fields")
            return

        email_regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        if not re.match(email_regex, email):
            self.error_label = QLabel("Please enter a valid email address.", self)
            self.error_label.setGeometry(self.email_textbox.x(), self.email_textbox.y() + self.email_textbox.height(), 500, 30)
            self.error_label.show()
            self.error_label.setStyleSheet("QLabel { color: red; background-color: rgba(255, 0, 0, 0); }")
            QTimer.singleShot(3000, self.error_label.hide)
            return

        db = mysql.connector.connect(host='127.0.0.1', port=3306, username = 'root' , password = 'user901', database ='flight_system')
        cursor = db.cursor()

        # Check if email already exists
        cursor.execute("SELECT email FROM user_info")
        existing_emails = [row[0] for row in cursor.fetchall()]
        if email in existing_emails:
            self.error_label = QLabel("This email is already registered. Please use a different Email or try logging in.", self)
            self.error_label.setGeometry(self.email_textbox.x(), self.email_textbox.y() + self.email_textbox.height(), 500, 30)
            self.error_label.show()
            self.error_label.setStyleSheet("QLabel { color: red; background-color: rgba(255, 0, 0, 0); }")
            QTimer.singleShot(3000, self.error_label.hide)
            return

        # Insert the new data
        query = f"INSERT INTO user_info (first_name, last_name, email, password) VALUES ('{first_name}', '{last_name}','{email}','{password}')"
        cursor.execute(query)
        db.commit()
        db.close()
        self.details(50)

        font = QFont()
        font.setFamily("Oswald")
        font.setPointSize(15)

        self.already.setVisible(False)
        self.login_button.setVisible(False)
        self.first_name.setVisible(False)
        self.first_name_text.setVisible(False)
        self.last_name.setVisible(False)
        self.last_name_text.setVisible(False)
        self.email.setVisible(False)
        self.email_textbox.setVisible(False)
        self.password_text.setVisible(False)
        self.password_textbox.setVisible(False)
        self.label3.setVisible(False)
        self.first.setVisible(False)
        self.submit_button.setVisible(False)


                


        self.threshhold_price_text = QLabel(self)
        self.threshhold_price_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.threshhold_price_text.setText("Threshold Price (INR)")
        self.threshhold_price_text.setGeometry(self.label1.width()+20, self.label.height()+40, 500, 200)
        self.threshhold_price_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.threshhold_price_text.setFont(font)
        self.threshhold_price_text.setVisible(True)

        self.threshhold_price_textbox = QLineEdit(self)
        self.threshhold_price_textbox.setGeometry(700, self.label.height()+127,175,30)
        self.threshhold_price_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.threshhold_price_textbox.setFont(font)

        validator = QIntValidator()
        self.threshhold_price_textbox.setValidator(validator)

        self.threshhold_price_textbox.setVisible(True)


        #everyting about IATA

    # Load the CSV file into a pandas DataFrame
        self.df = pd.read_csv('cleaned_iata.csv')

        # Get a list of IATA codes
        self.iata_codes = self.df['iata_code'].tolist()

        # Get a list of full names of airports
        self.full_names = self.df['name'].tolist()

        # Create a dictionary with full names as keys and IATA codes as values
        self.iata_full_name_dict = dict(zip(self.full_names, self.iata_codes))

        # Create a Origin widget
        self.iata_text_origin = QLineEdit(self)
        self.iata_text_origin.setGeometry(700, self.label.height()+187,175,30)
        self.iata_text_origin.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.iata_text_origin.setFont(font)
        # Set a completion list for the Origin widget
        completer = QCompleter(self.iata_codes + self.full_names)
        self.iata_text_origin.setCompleter(completer)
        self.iata_text_origin.textChanged.connect(self.onTextChangedOrigin)
        self.iata_text_origin.setVisible(True)

        # Create a Origin widget
        self.iata_text_destination = QLineEdit(self)
        self.iata_text_destination.setGeometry(700, self.label.height()+247,175,30)
        self.iata_text_destination.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.iata_text_destination.setFont(font)
        # Set a completion list for the Origin widget
        completer = QCompleter(self.iata_codes + self.full_names)
        self.iata_text_destination.setCompleter(completer)
        self.iata_text_destination.textChanged.connect(self.onTextChangeddestination)
        self.iata_text_destination.setVisible(True)
        print("hii")

        
        self.Origin_text = QLabel(self)
        self.Origin_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Origin_text.setText("Origin")
        self.Origin_text.setGeometry(self.label1.width()+20, self.label.height()+100, 500, 200)
        self.Origin_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.Origin_text.setFont(font)
        self.Origin_text.setVisible(True)

        self.Destination_text = QLabel(self)
        self.Destination_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Destination_text.setText("Destination")
        self.Destination_text.setGeometry(self.label1.width()+20, self.label.height()+160, 500, 200)
        self.Destination_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.Destination_text.setFont(font)
        self.Destination_text.setVisible(True)


        self.Date_of_departure = QLabel(self)
        self.Date_of_departure.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Date_of_departure.setText("Date of Departure")
        self.Date_of_departure.setGeometry(self.label1.width()+20, self.label.height()+220, 500, 200)
        self.Date_of_departure.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.Date_of_departure.setFont(font)
        self.Date_of_departure.setVisible(True)

        # Last name textbox
        self.Date_of_Departure_textbox = QLineEdit(self)
        self.Date_of_Departure_textbox.setGeometry(700, self.label.height()+307,175,30)
        self.Date_of_Departure_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.Date_of_Departure_textbox.setFont(font)
        self.Date_of_Departure_textbox.setVisible(True)


        # Set a validator to only allow dates in the format "YYYY-MM-DD"
        date_validator = QRegExpValidator(QRegExp("\d{4}-\d{2}-\d{2}"))
        self.Date_of_Departure_textbox.setValidator(date_validator)

        # Connect the textEdited signal to the custom slot
        self.Date_of_Departure_textbox.textEdited.connect(self.check_date_validity)



        self.submit_Data = QPushButton("GET MY DATA", self)
        self.submit_Data.setGeometry(self.label1.width() + 500, 325, 215, 215)
        self.submit_button.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 20px;")
        font = self.submit_Data.font()
        font.setPointSize(14)
        self.submit_Data.setFont(font)
        self.submit_Data.clicked.connect(self.get_data_register)
        self.submit_Data.setVisible(True)

        # Add stylesheet for hover effect
        self.submit_Data.setStyleSheet("""
            QPushButton:hover{
                background-color: #2196F3;
                color: white;
            }
            QPushButton{
                background-color: #ebebeb;
                border: 0px solid transparent;
                border-radius: 7px;
            }
        """)


        

    def details(self, arg1):

        font = QFont()
        font.setFamily("Oswald")
        font.setPointSize(15)


        self.first_name.setVisible(False)
        self.first_name_text.setVisible(False)
        self.last_name.setVisible(False)
        self.last_name_text.setVisible(False)
        self.email.setVisible(False)
        self.email_textbox.setVisible(False)
        self.password_text.setVisible(False)
        self.password_textbox.setVisible(False)
        self.label3.setVisible(False)
        self.first.setVisible(False)
        self.submit_button.setVisible(False)

        self.threshhold_price_text = QLabel(self)

        self.threshhold_price_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.threshhold_price_text.setText("Threshold Price")
        self.threshhold_price_text.setGeometry(self.label1.width()+380, self.label.height()+40, 500, 200)
        self.threshhold_price_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.threshhold_price_text.setFont(font)

    def check_date_validity(self):
        pos = 0
        is_valid = self.Date_of_Departure_textbox.validator().validate(self.Date_of_Departure_textbox.text(), pos)[0]
        if is_valid == QValidator.Acceptable:
            self.Date_of_Departure_textbox.setStyleSheet("background-color: #ebebeb; border: 1px solid green; border-radius: 7px")
        else:
            self.Date_of_Departure_textbox.setStyleSheet("background-color: #ebebeb; border: 1px solid red; border-radius: 7px")

    def update_text(self, text):
        validator = self.email_textbox.validator()
        state, text, _ = validator.validate(text, 0)
        if state == validator.Acceptable:
            self.email_textbox.setStyleSheet("background-color: #ebebeb; border: 1px solid green; border-radius: 7px")
        else:
            self.email_textbox.setStyleSheet("background-color: #ebebeb; border: 1px solid red; border-radius: 7px")


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon("airplane.jpg"))
    sys.exit(app.exec_())