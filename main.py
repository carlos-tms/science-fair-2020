
# --- Main ---
#
# Version 2.1 // 1/27/2020
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
        self.oil_data = {}
        self.oil_data_amt = []
        self.oil_data_date = []

        # EARTHQUAKE DATA STORAGE VAR
        self.earth_data = {}
        self.earth_data_mag = []
        self.earth_data_date = []
        self.sev1 = {}
        self.sev2 = {}
        self.yearly_amount = {}

        # self.earthquakes = {
        #    'new mexico': [],
        #    'california': [],
        #    'oklahoma': [],
        #    'texas': [],
        #    'other': []
        # }

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
                    self.oil_data_amt.append(line[4])

    def data_process(self):
        """
        data_process, ## DOCUMENTATION COMING SOON
        """

        def oil_process():

            from algorithms import twh_conversion

            for i in range(0, len(self.oil_data_amt)):
                self.oil_data_amt[i] = twh_conversion(float(self.oil_data_amt[i]))

            self.oil_data = {'Amount Produced': self.oil_data_amt, 'Date of Production': self.oil_data_date}

        def earthquake_process():

            from algorithms import yearly_amt, yearly_sev, list_half

            self.yearly_amount = yearly_amt(self.earth_data_date)

            for year, amount in self.yearly_amount.items():
                for x in amount:
                    self.yearly_amount[year] = x

            LH1 = list_half(self.earth_data_date)
            LH2 = list_half(self.earth_data_mag)

            self.sev1 = yearly_sev(self.earth_data_date[0:LH1], self.earth_data_mag[0:LH2])
            self.sev2 = yearly_sev(self.earth_data_date[LH1:], self.earth_data_mag[LH2:])

        if self.interactive:
            prompt = '\n** DATA PROCESS **'
            prompt += '\nWould you like to process Oil (o) or Earthquake (e) or All (a) data? '

            try:
                user_input = raw_input(prompt)
            except NameError:
                user_input = input(prompt)

            if user_input == 'o':
                oil_process()
            elif user_input == 'e':
                earthquake_process()
            elif user_input == 'a':
                oil_process()
                earthquake_process()

        else:
            oil_process()
            earthquake_process()

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

    def data_visualization(self):
        """
        data_visualization; will graph any provided dictionary, ONLY if in the following format:
        dict_name = {x:[values],y:[values]}
        Visualization is hardcoded due to MPL limitations and in avoidance of over-complication
        """
        from algorithms import dict_to_graph, dict_to_box_plot
        dict_to_graph(self.oil_data, 'Annual Oil Production')
        dict_to_box_plot(self.sev1, 'Yearly Severity (1)', 'Year', 'Magnitude')
        dict_to_box_plot(self.sev2, 'Yearly Severity (2)', 'Year', 'Magnitude')
        dict_to_graph(self.yearly_amount, 'Annual Earthquake Amount', 'Year', 'Earthquakes')


def app_main(interactive=False):
    if interactive:
        main_call = Data('Oil.csv', 'Earthquakes.csv', True)
        Data.data_load(main_call)
        Data.data_test(main_call)

    if not interactive:
        main_call = Data('Oil.csv', 'Earthquakes.csv', False)
        Data.data_load(main_call)
        Data.data_process(main_call)
        Data.data_visualization(main_call)


app_main()
