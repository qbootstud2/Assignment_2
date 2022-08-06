from src.html_generator import HtmlDoc


class SvgCanvas:
    """ This class holds the characteristic values of an SVG canvas within an HTML page and it can write the
     opening and closing SVG tags """

    def __init__(self, w: int, h: int) -> None:
        self.__w: int = w
        self.__h: int = h

    def write_svg_head(self, hd: HtmlDoc) -> None:
        """generate svg head tag"""
        svg_head: str = f'<svg width="{self.__w}" height="{self.__h}">'
        hd.write_html_line(1, svg_head)

    @staticmethod
    def write_svg_tail(hd: HtmlDoc) -> None:
        """generate svg tail tag"""
        hd.write_html_line(1, "</svg>")
