# from source.modules.pipeline import *
# from Pipelines.test import *
from modules.pipeline import *

def main():
    data = read_file('mongodb://localhost:27017/')
    data_clean = cleaning(data)
    # pdf_file = PDFgenerator(data_clean)

if __name__ == "__main__":
    main()
