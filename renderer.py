import jinja2


class Renderer:
    def __init__(self, template_name: str, output_name: str, cfg: dict):
        self.loaded = False
        self.jenv = jinja2.Environment(
            loader=jinja2.FileSystemLoader("."),
            autoescape=jinja2.select_autoescape(["html"]),
        )
        self.jtemplatename = template_name
        self.outstreamname = output_name
        self.data = cfg

    def load(self):
        self.jtemplate = self.jenv.get_template(self.jtemplatename)
        self.loaded = True
        return self

    def render(self):
        if self.loaded:
            rendered = self.jtemplate.render(self.data)
            with open(self.outstreamname, "w", encoding="utf8") as file:
                file.write(rendered)
        else:
            print(
                "<ERR!> Can't use function render(...) without loading this Renderer!\n<ERR!> You should call [Renderer].load() before calling render(...)!"
            )
