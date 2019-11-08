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

        # -- DATA LOADING

        # Earthquake Data
        with open(self.earthFile) as f:
            earth_reader = csv.reader(f)
            eq_header = next(earth_reader)

        # Oil Data
        with open(self.oilFile) as f:
            oil_reader = csv.reader(f)
            oil_header = next(oil_reader)

            oil_production_a = []
            for row in oil_reader:
                oil_production_a.append(row[5])


mainCall = Data('Oil.csv', 'Earthquakes.csv')
Data.data_loader(mainCall)

print('test')
