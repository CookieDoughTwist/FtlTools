from lxml import etree

class StringTabulator:
    def __init__(self):
        self.table = dict()

    def submit(self, entry):
        if entry not in self.table:
            self.table[entry] = 0
        self.table[entry] += 1

    def __str__(self):
        s = ""
        for key, value in self.table.items():
            s += f"{key}: {value}\n"
        return s
    
def prettyprint(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')