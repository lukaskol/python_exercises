import xml.sax
from xml.dom import minidom

names = []
prices = []
descriptions = []
calories = []


class FoodHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.CurrentData = ""
        self.name = ""
        self.price = ""
        self.description = ""
        self.calories = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "food":
            print("###### FOOD ######")

    def endElement(self, tag):
        if self.CurrentData == "name":
            print("Name: %s" % self.name)
            names.append(self.name)
        elif self.CurrentData == "price":
            print("Price: %s" % self.price)
            prices.append(self.price)
        elif self.CurrentData == "description":
            print("Description: %s" % self.description)
            descriptions.append(self.description)
        elif self.CurrentData == "calories":
            print("Calories: %s" % self.calories)
            calories.append(self.calories)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "description":
            self.description = content
        elif self.CurrentData == "calories":
            self.calories = content


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = FoodHandler()
    parser.setContentHandler(handler)

    parser.parse("./xml/simple.xml")
    for i in range(len(names)):
        if names[i] == 'Homestyle Breakfast':
            names[i] = 'English Breakfast'

    root = minidom.Document()
    xml = root.createElement('breakfast_menu')
    root.appendChild(xml)
    for i in range(len(names)):
        child = root.createElement('food')

        xml_name = root.createElement('name')
        xml_name.appendChild(root.createTextNode(names[i]))

        xml_price = root.createElement('price')
        xml_price.appendChild(root.createTextNode(prices[i]))

        xml_desc = root.createElement('description')
        xml_desc.appendChild(root.createTextNode(descriptions[i]))

        xml_calories = root.createElement('calories')
        xml_calories.appendChild(root.createTextNode(calories[i]))

        child.appendChild(xml_name)
        child.appendChild(xml_price)
        child.appendChild(xml_desc)
        child.appendChild(xml_calories)
        xml.appendChild(child)

    xml_str = root.toprettyxml(indent="  ")
    with open("./xml/SAX_output.xml", "w") as f:
        f.write(xml_str)
        f.close()
