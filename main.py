from renderer import Renderer
from http.server import HTTPServer, SimpleHTTPRequestHandler
from year import get_year_word as year_word
from readwine import read_wines
from pprint import pprint


if __name__ == "__main__":
    ## <config>
    print("<log> (main:renderer) loading renderer config")
    wines = read_wines("wine3.xlsx")  # .xlsx файл с винами
    cfg = {
        "YEARS": 103, # года
        "YEARS_WORD": year_word(103), # тоже года, но слово
        "CATEGORIZED_WINES": wines # вина
    }
    ## </config>
    ## <render>
    print("<log> (main:renderer) rendering")
    renderer = Renderer("index_template.html", "index.html", cfg).load()
    renderer.render()
    ## </render>

    print("<log> (main:chore) starting server")
    server = HTTPServer(("127.0.0.1", 8080), SimpleHTTPRequestHandler)
    server.serve_forever()
