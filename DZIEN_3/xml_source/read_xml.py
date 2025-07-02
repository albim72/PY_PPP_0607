import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    print(f"Tytuł:{title} Autor: {author}")
