import pandas
from collections import defaultdict as defdict


def read_wines(filename: str = "wine.xlsx"):
    wines_dict_raw = pandas.read_excel(filename, keep_default_na=False, na_values=None).to_dict(orient="records")
    wines = defdict(list)
    for wine in wines_dict_raw:
        wines[wine["Категория"]].append(wine)
    return wines
