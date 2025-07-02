import xml.etree.ElementTree as ET

library = ET.Element('library')
book = ET.SubElement(library, 'book')
ET.SubElement(book, 'title').text = 'Python - uczenie maszynowe'
ET.SubElement(book, 'author').text = 'Piotr Mośkowski'

tree = ET.ElementTree(library)
tree.write('new_books.xml',encoding='utf-8',xml_declaration=True)
