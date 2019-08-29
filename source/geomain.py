from geomodules.geopipeline import *


def main():
    geodata = read_geofile('mongodb://localhost:27017/')
    top500 = geordering500(geodata)
    apidata = geoapi(top500)              #we do not concatenate it into the next function because it creates a csv(top500), we do import in the next function
    geocsv = geonormalizing('../data/top500.csv')

if __name__ == "__main__":
    main()
