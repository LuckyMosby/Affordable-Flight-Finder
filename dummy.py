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

        # Last name textbox
        self.threshhold_price_textbox = QLineEdit(self)
        self.threshhold_price_textbox.setGeometry(700, self.label.height()+127,175,30)
        self.threshhold_price_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.threshhold_price_textbox.setFont(font)

        
        self.Origin_text = QLabel(self)
        self.Origin_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Origin_text.setText("Origin")
        self.Origin_text.setGeometry(self.label1.width()+20, self.label.height()+100, 500, 200)
        self.Origin_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.Origin_text.setFont(font)

        self.Destination_text = QLabel(self)
        self.Destination_text.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Destination_text.setText("Destination")
        self.Destination_text.setGeometry(self.label1.width()+20, self.label.height()+160, 500, 200)
        self.Destination_text.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.Destination_text.setFont(font)


        self.Date_of_departure = QLabel(self)
        self.Date_of_departure.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Date_of_departure.setText("Date of Departure")
        self.Date_of_departure.setGeometry(self.label1.width()+20, self.label.height()+220, 500, 200)
        self.Date_of_departure.setContentsMargins(20,20,20,20)
        font.setPointSize(15)
        self.Date_of_departure.setFont(font)

        # Last name textbox
        self.Date_of_Departure_textbox = QLineEdit(self)
        self.Date_of_Departure_textbox.setGeometry(700, self.label.height()+307,175,30)
        self.Date_of_Departure_textbox.setStyleSheet("background-color: #ebebeb; border: 0px solid transparent; border-radius: 7px")
        font.setPointSize(13)
        self.Date_of_Departure_textbox.setFont(font)

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