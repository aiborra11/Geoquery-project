from Pipelines.pipeline import *


def main():
    data = read_file('mongodb://localhost:27017/')
    data_clean = cleaning(data)

if __name__ == "__main__":
    main()