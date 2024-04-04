import sys
import os
import time
from lxml import etree

from util import StringTabulator
from util import prettyprint

class SectorDatabase:
    def __init__(self):
        self.sectors = dict()
        self.skiptags = StringTabulator()
        self.sectordupes = list()

    def load_data_directory(self, data_dir):
        print(f"Loading data in {data_dir}")
        start_time = time.time()
        n_files = 0
        for file in os.listdir(data_dir):
            filename = os.fsdecode(file)
            if 'sector_data' in filename and '.xml' in filename:
                self.parse_file(filename)
                n_files += 1
        print(f"Finished loading {len(self.sectors)} sectors from {n_files} files in {(time.time() - start_time):0.3f}s")        

    def parse_file(self, filename):
        print(f" Loading {filename}")
        parser = etree.XMLParser(recover=True)
        fullpath = os.path.join(data_dir, filename)
        tree = etree.parse(fullpath, parser)
        root = tree.getroot()
        for elem in root:
            if elem.tag == 'sectorDescription':
                sc = Sector(elem)
                self.add_sector(sc)
                print(f"  >{sc.name}")                
            else:
                self.skiptags.submit(elem.tag)

    def add_sector(self, sector):
        if sector.name in self.sectors:
            print(f"Duplicate sector name {sector.name} already loaded!")
            self.sectordupes.append(sector)
            return
        self.sectors[sector.name] = sector

class Sector:
    def __init__(self, root):
        self.root = root
        self.name = root.attrib['name']
        self.unique = root.attrib['unique'] == 'true'
        
'''
        for elem in root:
            if elem.tag == 'nameList':
                self.parse_name_list(elem)
            elif elem.tag == 'trackList':
                pass
            elif elem.tag == 'rarityList':
                pass
            elif elem.tag == 'startEvent':
                self.startEvent = elem.text
            elif elem.tag == 

    def parse_name_list(self, elem):
        for child in elem:
            if child.tag == 'name':
                self.nameList.append(child.text)
            elif child.tag is etree.Comment:
                pass
            else:
                prettyprint(child)
                print(child.tag)
                assert(False)
'''

if __name__ == '__main__':

    if len(sys.argv) < 2:
        data_dir = r'C:/Users/Lucy/Downloads/Multiverse 5.4.4  - Data/data'
    else:
        data_dir = sys.argv[1]
    
    sdb = SectorDatabase()
    sdb.load_data_directory(data_dir)
    print(sdb.skiptags)
    dupenames = [sec.name for sec in sdb.sectordupes]
    print(dupenames)