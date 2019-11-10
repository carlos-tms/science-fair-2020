class Data:
    """
    data()

    The backbone and housing for all data related code, only data
    loading and processing will occur in this class.
    """

    def __init__(self, oil_file, earth_file):
        self.oilFile = oil_file
        self.earthFile = earth_file

        self.oilProduction = []
        self.earthPlace = []
        self.magnitudesOverFour = []
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

    def data_loader(self):
        """
        data_loader()

        This function loads all data used in the program.
        """

        # -- IMPORTS
        import csv
        from conversions import twh_conversion
        # -- DATA LOADING

        # Earthquake Data
        with open(self.earthFile) as f:
            reader = csv.reader(f)
            eq_header = next(reader)

            # Columns to be loaded, (1, 5, 14)

        # Oil Data
        with open(self.oilFile) as f:
            reader = csv.reader(f)

            oil_prod_amt, oil_prod_date = [], []
            for line in reader:
                if line[1] == 'USA':
                    oil_prod_date.append(line[2])

                    oil_prod = line[4]
                    oil_prod_amt.append(twh_conversion(float(oil_prod)))

        # TEST
        # print(oil_prod_date)
        # print(oil_prod_amt)


mainCall = Data('Oil.csv', 'Earthquakes.csv')
Data.data_loader(mainCall)
