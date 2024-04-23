from PyQt6 import QtWidgets # type: ignore
import Logos_rc, Icons_rc
import random
import GUIBuilder
import flightDataAPI as fdapi

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
def generate_strings(airlineIndex):

    # Map the airlineIndex to the corresponding airline code
    airline_codes = {1: 'SW', 2: 'UA', 3: 'AA'}
    airline_code = airline_codes.get(airlineIndex, '')

    strings = []
    for _ in range(3):

        # Generate a random number between 1111 and 9999
        number = random.randint(1111, 9999) 
        # Append the airline code and the number to the list
        strings.append(f'{airline_code}{number}')  

    #print(strings)
    return strings

def select_aircraft():
    aircraft_list = [
        "A319-100",
        "A320-200",
        "A321-200NX",
        "B737-700",
        "B737 MAX 8",
        "B737-800",
        "B737 MAX 9",
        "B737-900"
    ]
    return random.choice(aircraft_list)

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
    elif(ui.UAButton.isChecked()):
        airlineIndex = 2
    elif(ui.AAButton.isChecked()):
        airlineIndex = 3
    else: airlineIndex = 0

    ## Debug point ##
    #print("airline id:", airlineIndex)
    #print("airport id:", airportIndex)

    # this code actuates the lie!!!!!!!!!!!!!!!!!!!!
    strings = fdapi.flightdata()

    ui.flight1GridLayout.setTitle(strings[0])
    ui.flight2GridLayout.setTitle(strings[5])
    ui.flight3GridLayout.setTitle(strings[10])

    
    ui.flight1Aircraft.setText(strings[1])
    ui.flight1ActualStatusMain.setText(strings[4])
    ui.flight1Destination.setText(strings[2])
    ui.flight1Distance.setText(strings[3] + "Mi")
    
    ui.flight2Aircraft.setText(strings[6])
    ui.flight2ActualStatusMain.setText(strings[9])
    ui.flight2Destination.setText(strings[7])
    ui.flight2Distance.setText(strings[8] + "Mi")

    ui.flight3Aircraft.setText(strings[11])
    ui.flight3ActualStatusMain.setText(strings[14])
    ui.flight3Destination.setText(strings[12])
    ui.flight3Distance.setText(strings[13] + "Mi")

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

    button = ui.SWButton.isChecked() or ui.UAButton.isChecked() or ui.AAButton.isChecked()
    #print("airline buttons set to:", button)
    return button

def checkButtons():

    # Check if both an airport and an airline radio button are checked
    airportChecked = ui.MCOButton.isChecked() or ui.MIAButton.isChecked() or ui.JAXButton.isChecked()
    airlineChecked = ui.SWButton.isChecked() or ui.UAButton.isChecked() or ui.AAButton.isChecked()

    # Enable LtoRPageButton if both an airport and an airline radio button are checked, disable it otherwise
    ui.LtoRPageButton.setEnabled(airportChecked and airlineChecked)

if __name__ == "__main__":
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
    ui.UAButton.clicked.connect(airlineButtons_clicked)
    ui.AAButton.clicked.connect(airlineButtons_clicked)

    ui.MCOButton.clicked.connect(checkButtons)
    ui.MIAButton.clicked.connect(checkButtons)
    ui.JAXButton.clicked.connect(checkButtons)

    ui.SWButton.clicked.connect(checkButtons)
    ui.UAButton.clicked.connect(checkButtons)
    ui.AAButton.clicked.connect(checkButtons)


    sys.exit(app.exec())