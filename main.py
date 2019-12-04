
# --- Main ---
#
# Version 1.0 // 12-3-2019
#
# By Carlos Miller


class Data:
    """
    data:
    data_load, data_process, data_compile

    oil_file; the name of the CSV file with USA Annual Crude Oil Production Data
    earth_file; the name of the CSV file with Earthquake data
    is_interactive; tells the program to either run interactively or not, with this being False it will run with
                    default settings, and no input points. Will only print needed info when the operation is
                    complete.

    Creates a nicely packaged list, featuring processed data ready for visualization.

    """

    def __init__(self, oil_file, earth_file, is_interactive):
        self.oilFile = oil_file
        self.earthFile = earth_file

        self.can_vis = False
        self.interactive = is_interactive

        # OIL DATA STORAGE VAR
        self.oil_data_amt = []
        self.oil_data_date = []

        # EARTHQUAKE DATA STORAGE VAR
        self.earth_data_mag = []
        self.earth_data_date = []

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
            Loaded rows: 0, 4, 13
            Cells loaded: 8757 
            ## NOTICE - Cells Loaded; May increase upon final version, as the earthquake data set will be updated to
                                      its latest version. 
            
            Actions:
                1. Check if location is within defined list, 'key_areas' if so, continue operation.
                2. Append magnitude to list 'earth_data_mag'
                3. Append raw time of earthquake to list 'earth_data_date'
                4. Pass all values to 'data_process' : FINISH
            
            Oil:
            Loaded rows: 1, 2, 4
            Cells loaded: 228
            
            Actions:
                1. Check if country code is 'USA', if so, continue operation and skip over all other countries.
                2. Append the year to list 'oil_data_date'
                3. Grab the value for oil located in column 4, then pass it through 'twh_conversion'   
                4. Pass all values to 'data_process' : FINISH
                
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

    def data_process(self):
        """
        data_process, ## DOCUMENTATION COMING SOON
        """
        pass

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


mainCall = Data('Oil.csv', 'Earthquakes.csv', None)
Data.data_load(mainCall)
Data.data_test(mainCall)
