import xml.sax

class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentTag = ""
        self.title = ""
        self.author = ""
        self.count = 0

    def startElement(self, tag, attributes):
        self.CurrentTag = tag
        if tag == "book":
            self.title = ""
            self.author = ""

    def characters(self, content):
        if self.CurrentTag == "title":
            self.title += content
        elif self.CurrentTag == "author":
            self.author += content

    def endElement(self, tag):
        if tag == "book":
            self.count += 1
            print(f"[Książka #{self.count}]")
            print(f"  Tytuł: {self.title.strip()}")
            print(f"  Autor: {self.author.strip()}")
            print("-" * 30)
        self.CurrentTag = ""

# Uruchomienie parsera
if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = BookHandler()
    parser.setContentHandler(handler)

    parser.parse("books.xml")

    print(f"\nLiczba książek: {handler.count}")
