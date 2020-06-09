import pandas as pd
from geopy.geocoders import ArcGIS


class GeoCoder:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        gis = ArcGIS()
        self.data["Location"] = self.data["Address"].apply(gis.geocode)
        self.data["Latitude"] = self.data["Location"].apply(lambda x: x.latitude)
        self.data["Longitude"] = self.data["Location"].apply(lambda x: x.longitude)
        self.data = self.data.drop(columns=["Location"])
        self.data.to_csv(csv_file.filename, index=None)

    def show_html_table(self):
        return self.data.to_html()
