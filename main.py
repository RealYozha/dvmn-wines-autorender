import logging
from renderer import Renderer
from http.server import HTTPServer, SimpleHTTPRequestHandler
from year import get_year_word as year_word
from readwine import read_wines
from dotenv import load_dotenv
from os import getenv
from datetime import datetime as dt


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s ~/%(filename)s:%(funcName)s")

    cfgvar_wines = read_wines(getenv("XLSX_WINES", "wine3.xlsx"))
    cfgvar_years = int(dt.today().year) - int(getenv("YEAR_OF_CREATION", 1920))
    cfgvar_years_word = year_word(cfgvar_years)
    cfg = {
        "YEARS": cfgvar_years,
        "YEARS_WORD": cfgvar_years_word,
        "CATEGORIZED_WINES": cfgvar_wines
    }

    renderer = Renderer("index_template.html", "index.html", cfg).load()
    renderer.render()

    server = HTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
    logging.info("Сайт запускается...")
    server.serve_forever()
