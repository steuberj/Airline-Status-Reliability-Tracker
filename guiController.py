def startGui():
    from PyQt6 import QtWidgets # type: ignore
    import Logos_rc, Icons_rc
    import random
    import GUIBuilder
    import flightDataAPI as fdapi
    import probability_Algorithm as pa

    # if __name__ == "__main__":
    #     import sys
    #     app = QtWidgets.QApplication(sys.argv)
    #     MainWindow = QtWidgets.QMainWindow()
    #     ui = Ui_MainWindow()
    #     ui.setupUi(MainWindow)
    #     MainWindow.show()

    #     def LtoRPageButton_clicked(self):
    #         # Set the currentIndex of the stacked widget to 1
    #         ui.stackedWidget.setCurrentIndex(1)

    #     def RtoLPageButton_clicked(self):
    #         # Set the currentIndex of the stacked widget to 0
    #         ui.stackedWidget.setCurrentIndex(0)

    #     ui.LtoRPageButton.clicked.connect(LtoRPageButton_clicked)
    #     ui.RtoLPageButton.clicked.connect(RtoLPageButton_clicked)

    #     sys.exit(app.exec())

    # the functions below will LIE to you. Mostly for demo purposes, here in case we cant break into the flight dictionaries
    # def generate_strings(airlineIndex):

    #     # Map the airlineIndex to the corresponding airline code
    #     airline_codes = {1: 'SW', 2: 'UA', 3: 'AA'}
    #     airline_code = airline_codes.get(airlineIndex, '')

    #     strings = []
    #     for _ in range(3):

    #         # Generate a random number between 1111 and 9999
    #         number = random.randint(1111, 9999) 
    #         # Append the airline code and the number to the list
    #         strings.append(f'{airline_code}{number}')  

    #     #print(strings)
    #     return strings

    # def select_aircraft():
    #     aircraft_list = [
    #         "A319-100",
    #         "A320-200",
    #         "A321-200NX",
    #         "B737-700",
    #         "B737 MAX 8",
    #         "B737-800",
    #         "B737 MAX 9",
    #         "B737-900"
    #     ]
    #     return random.choice(aircraft_list)

    def LtoRPageButton_clicked():

        # set the currentIndex of the stacked widget to 1
        if airportButtons_clicked() and airlineButtons_clicked() == True:
            ui.stackedWidget.setCurrentIndex(1)
        
        global airportIndex
        global airlineIndex

        if (ui.MCOButton.isChecked()):
            airportIndex = 1
        elif(ui.MIAButton.isChecked()):
            airportIndex = 2
        elif(ui.JAXButton.isChecked()):
            airportIndex = 3
        else: airportIndex = 0

        if (ui.SWButton.isChecked()):
            airlineIndex = 1
        elif(ui.DAButton.isChecked()):
            airlineIndex = 2
        elif(ui.AAButton.isChecked()):
            airlineIndex = 3
        else: airlineIndex = 0

        ## Debug point ##
        #print("airline id:", airlineIndex)
        #print("airport id:", airportIndex)

        

        if airportIndex == 1 and airlineIndex == 1:
            strings = fdapi.flightdata("MCO", "SWA")
            predictedstatus = pa.controlFunction('SWMCO_delmodel', 'SWMCO_arrmodel')
        elif airportIndex == 1 and airlineIndex == 2:
            strings = fdapi.flightdata("MCO", "DAL")
            predictedstatus = pa.controlFunction('DLMCO_delmodel', 'DLMCO_arrmodel')
        elif airportIndex == 1 and airlineIndex == 3:
            strings = fdapi.flightdata("MCO", "AAL")
            predictedstatus = pa.controlFunction('AAMCO_delmodel', 'AAMCO_arrmodel')
        elif airportIndex == 2 and airlineIndex == 1:
            strings = fdapi.flightdata("MIA", "SWA")
            predictedstatus = pa.controlFunction('SWMIA_delmodel', 'SWMIA_arrmodel')
        elif airportIndex == 2 and airlineIndex == 2:
            strings = fdapi.flightdata("MIA", "DAL")
            predictedstatus = pa.controlFunction('DLMIA_delmodel', 'DLMIA_arrmodel')
        elif airportIndex == 2 and airlineIndex == 3:
            strings = fdapi.flightdata("MIA", "AAL")
            predictedstatus = pa.controlFunction('AAMIA_delmodel', 'AAMIA_arrmodel')
        elif airportIndex == 3 and airlineIndex == 1:
            strings = fdapi.flightdata("JAX", "SWA")
            predictedstatus = pa.controlFunction('SWJAX_delmodel', 'SWJAX_arrmodel')
        elif airportIndex == 3 and airlineIndex == 2:
            strings = fdapi.flightdata("JAX", "DAL")
            predictedstatus = pa.controlFunction('DLJAX_delmodel', 'DLJAX_arrmodel')
        elif airportIndex == 3 and airlineIndex == 3:
            strings = fdapi.flightdata("JAX", "AAL")
            predictedstatus = pa.controlFunction('AAJAX_delmodel', 'AAJAX_arrmodel')
        
        ui.flight1GridLayout.setTitle(strings[0])
        ui.flight2GridLayout.setTitle(strings[5])
        ui.flight3GridLayout.setTitle(strings[10])
        
        ui.flight1Aircraft.setText(strings[1])
        if int(strings[4]) <= 0:
            ui.flight1ActualStatusMain.setText("On Time")
        elif int(strings[4]) >= 500:
            ui.flight1ActualStatusMain.setText("Major Delay")
        else:
            ui.flight1ActualStatusMain.setText("Delayed")
        ui.flight1Destination.setText(strings[2])
        ui.flight1Distance.setText(strings[3] + "Mi")
        ui.flight1PredictedStatusMain.setText(predictedstatus)
        
        ui.flight2Aircraft.setText(strings[6])
        if int(strings[9]) <= 0:
            ui.flight2ActualStatusMain.setText("On Time")
        elif int(strings[9]) >= 500:
            ui.flight2ActualStatusMain.setText("Major Delay")
        else:
            ui.flight2ActualStatusMain.setText("Delayed")
        ui.flight2Destination.setText(strings[7])
        ui.flight2Distance.setText(strings[8] + "Mi")
        ui.flight2PredictedStatusMain.setText(predictedstatus)

        ui.flight3Aircraft.setText(strings[11])
        if int(strings[14]) <= 0:
            ui.flight3ActualStatusMain.setText("On Time")
        elif int(strings[14]) >= 500:
            ui.flight3ActualStatusMain.setText("Major Delay")
        else:
            ui.flight3ActualStatusMain.setText("Delayed")
        ui.flight3Destination.setText(strings[12])
        ui.flight3Distance.setText(strings[13] + "Mi")
        ui.flight3PredictedStatusMain.setText(predictedstatus)

    def RtoLPageButton_clicked():

        # set the currentIndex of the stacked widget to 0. very simple. we could use this to uncheck every radio button again but its unnecessary.
        ui.stackedWidget.setCurrentIndex(0)


    # function to set airportButtonSelected to true if ANY airport button is selected
    def airportButtons_clicked():

        button = ui.MCOButton.isChecked() or ui.MIAButton.isChecked() or ui.JAXButton.isChecked()
        #print("airport buttons set to:", button)
        return button

    # function to set airlineButtonSelected to true if ANY airline button is selected
    def airlineButtons_clicked():

        button = ui.SWButton.isChecked() or ui.DAButton.isChecked() or ui.AAButton.isChecked()
        #print("airline buttons set to:", button)
        return button

    def checkButtons():

        # Check if both an airport and an airline radio button are checked
        airportChecked = ui.MCOButton.isChecked() or ui.MIAButton.isChecked() or ui.JAXButton.isChecked()
        airlineChecked = ui.SWButton.isChecked() or ui.DAButton.isChecked() or ui.AAButton.isChecked()

        # Enable LtoRPageButton if both an airport and an airline radio button are checked, disable it otherwise
        ui.LtoRPageButton.setEnabled(airportChecked and airlineChecked)


    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUIBuilder.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.LtoRPageButton.setEnabled(False)

    # initialize airport/airline radio buttons to false (unselected)
    airportButtonSelected = False
    airlineButtonSelected = False

    # ------------------------------- #
    # index for airport and airlines. #
    # 0 : NOTHING       0: NOTHING    #
    # 1 : Southwest     1: Orlando    #
    # 2 : United        2: Miami      #
    # 3 : American      3: Jacksonv.  #
    # ------------------------------- #
    global airportIndex
    global airlineIndex
    airportIndex = 0
    airlineIndex = 0

    ### debug point ###
    #print("airport buttons set to:", airportButtonSelected)
    #print("airline buttons set to:", airlineButtonSelected)

    ui.LtoRPageButton.clicked.connect(LtoRPageButton_clicked)
    ui.RtoLPageButton.clicked.connect(RtoLPageButton_clicked)

    ui.MCOButton.clicked.connect(airportButtons_clicked)
    ui.MIAButton.clicked.connect(airportButtons_clicked)
    ui.JAXButton.clicked.connect(airportButtons_clicked)

    ui.SWButton.clicked.connect(airlineButtons_clicked)
    ui.DAButton.clicked.connect(airlineButtons_clicked)
    ui.AAButton.clicked.connect(airlineButtons_clicked)

    ui.MCOButton.clicked.connect(checkButtons)
    ui.MIAButton.clicked.connect(checkButtons)
    ui.JAXButton.clicked.connect(checkButtons)

    ui.SWButton.clicked.connect(checkButtons)
    ui.DAButton.clicked.connect(checkButtons)
    ui.AAButton.clicked.connect(checkButtons)


    sys.exit(app.exec())

    # if __name__ == "__main__":
    #     import sys
    #     app = QtWidgets.QApplication(sys.argv)
    #     MainWindow = QtWidgets.QMainWindow()
    #     ui = GUIBuilder.Ui_MainWindow()
    #     ui.setupUi(MainWindow)
    #     MainWindow.show()
    #     ui.LtoRPageButton.setEnabled(False)

    #     # initialize airport/airline radio buttons to false (unselected)
    #     airportButtonSelected = False
    #     airlineButtonSelected = False

    #     # ------------------------------- #
    #     # index for airport and airlines. #
    #     # 0 : NOTHING       0: NOTHING    #
    #     # 1 : Southwest     1: Orlando    #
    #     # 2 : United        2: Miami      #
    #     # 3 : American      3: Jacksonv.  #
    #     # ------------------------------- #
    #     global airportIndex
    #     global airlineIndex
    #     airportIndex = 0
    #     airlineIndex = 0

    #     ### debug point ###
    #     #print("airport buttons set to:", airportButtonSelected)
    #     #print("airline buttons set to:", airlineButtonSelected)

    #     ui.LtoRPageButton.clicked.connect(LtoRPageButton_clicked)
    #     ui.RtoLPageButton.clicked.connect(RtoLPageButton_clicked)

    #     ui.MCOButton.clicked.connect(airportButtons_clicked)
    #     ui.MIAButton.clicked.connect(airportButtons_clicked)
    #     ui.JAXButton.clicked.connect(airportButtons_clicked)

    #     ui.SWButton.clicked.connect(airlineButtons_clicked)
    #     ui.DAButton.clicked.connect(airlineButtons_clicked)
    #     ui.AAButton.clicked.connect(airlineButtons_clicked)

    #     ui.MCOButton.clicked.connect(checkButtons)
    #     ui.MIAButton.clicked.connect(checkButtons)
    #     ui.JAXButton.clicked.connect(checkButtons)

    #     ui.SWButton.clicked.connect(checkButtons)
    #     ui.DAButton.clicked.connect(checkButtons)
    #     ui.AAButton.clicked.connect(checkButtons)


    #     sys.exit(app.exec())
