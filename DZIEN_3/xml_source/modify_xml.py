import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

book2 = root.findall('book')[1]
book2.find('title').text = 'Python - uczenie maszynowe'
book2.find('author').text = 'Anna Potocka'

tree.write('new_books.xml',encoding='utf-8',xml_declaration=True)
