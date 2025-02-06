import pandas
from collections import defaultdict as ddict


def read_wines(filename: str = "wine.xlsx"):
    read = pandas.read_excel(filename, keep_default_na=False, na_values=None).to_dict(orient="records")
    wines = ddict(list)
    for wine in read:
        wines[wine["Категория"]].append(wine)
    return wines
