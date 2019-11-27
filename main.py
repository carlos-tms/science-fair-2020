class Data:
    """
    data()

    The backbone and housing for all data related code, only data
    loading and processing will occur in this class.
    """

    def __init__(self, oil_file, earth_file):
        self.oilFile = oil_file
        self.earthFile = earth_file

        self.can_vis = False

        # OIL DATA STORAGE VAR
        self.oil_data_amt = []
        self.oil_data_date = []

        # EARTHQUAKE DATA STORAGE VAR
        self.earth_data_mag = []
        self.earth_data_date = []
        self.allMagnitudes = []

        self.earthquakes = {
            'new mexico': [],
            'california': [],
            'oklahoma': [],
            'texas': [],
            'other': []
        }

        self.keyAreas = [
            "California", "CA", "New Mexico", "NM", "Oklahoma", "OK",
            "Texas", "TX"
        ]

    def data_load(self):
        """
        data_loader()

        This function loads all data used in the program.
        """

        # -- IMPORTS
        import csv
        from algorithms import twh_conversion

        """
        Data Loading Specifics
            
            Earthquakes:
            Loaded Rows: 0, 4, 13
            Cells loaded: 8757
            
            Actions:
                1. Check if location is within defined list, 'key_areas' if so, continue operation.
                2. Append magnitude to
            
            Oil:
            Loaded Rows: 1, 2, 4
            Cells loaded: 228
            
            Actions:
                1. Check if country code is 'USA', if so, continue operation and skip over all other countries.
                2. Append the year to list 'oil_data_date'
                3. Grab the value for oil located in column 4, then pass it through 'twh_conversion'
                
                    # The conversion is made to better analyze the ACTUAL amount of oil produced, since the recorded
                      value is in tWh (Terra-watt-hours) and to better understand how much was produced, I pass it
                      through the mathematical conversion of [tWh * 614175.1627564]; then for visualization purposes,
                      round the value to the nearest whole number.
                      
                4. Pass all values to 'data_test' : FINISH
                
        """

        # Earthquakes
        with open(self.earthFile) as f:
            reader = csv.reader(f)

            for line in reader:
                if any(key in line[13] for key in self.keyAreas):
                    self.earth_data_mag.append(line[4])
                    self.earth_data_date.append(line[0])

        # Oil
        with open(self.oilFile) as f:
            reader = csv.reader(f)

            for line in reader:
                if line[1] == 'USA':
                    self.oil_data_date.append(line[2])
                    self.oil_data_amt.append(twh_conversion(float(line[4])))

    def data_test(self):
        """
        data_test, used for testing purposes only; just in case a value isn't working how it's supposed to.

        Checks for any value errors, then after human approval, will allow the data to be visualized (by changing
        'can_visualize' from False to True)
        """

        print('** OIL DATA')
        for x, y in zip(self.oil_data_amt, self.oil_data_date):
            print('\nAmt: ' + x)
            print('Date: ' + y)
        try:
            oil_approval = raw_input('\nIs data ok? y/n ')
        except NameError:
            oil_approval = input('\nIs data ok? y/n ')

        print('\n** EARTHQUAKE DATA')
        for x, y in zip(self.earth_data_date, self.earth_data_mag):
            print('\nMag: ' + str(y))
            print('Date: ' + str(x))
        try:
            earthquake_approval = raw_input('\nIs data ok? y/n ')
        except NameError:
            earthquake_approval = input('\nIs data ok? y/n ')

        if earthquake_approval == 'y' and oil_approval == 'y':
            self.can_vis = True
            print('** READY FOR VISUALIZATION')
        else:
            print('** ERROR: Data not ready for vis')


mainCall = Data('Oil.csv', 'Earthquakes.csv')
Data.data_load(mainCall)
Data.data_test(mainCall)
