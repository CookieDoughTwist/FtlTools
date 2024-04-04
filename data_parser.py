import sys
import os
import time
from lxml import etree

from util import StringTabulator
from util import prettyprint

class EventDatabase:
    def __init__(self):
        self.events = dict()
        self.skiptags = StringTabulator()
        self.eventdupes = list()

    def load_data_director(self, data_dir):
        print(f"Loading data in {data_dir}")
        start_time = time.time()
        n_files = 0
        for file in os.listdir(data_dir):
            filename = os.fsdecode(file)
            if 'events' in filename and '.xml' in filename:
                self.parse_file(filename)
                n_files += 1
        print(f"Finished loading {len(self.events)} events from {n_files} files in {(time.time() - start_time):0.3f}s")        

    def parse_file(self, filename):
        print(f" Loading {filename}")
        parser = etree.XMLParser(recover=True)
        fullpath = os.path.join(data_dir, filename)
        tree = etree.parse(fullpath, parser)
        root = tree.getroot()
        for elem in root:
            if elem.tag == 'event' or elem.tag == 'eventList':
                ev = Event(elem)
                self.add_event(ev)
                print(f"  >{ev.name}")
                '''
                try:
                    print(ev)
                except Exception as e:
                    print(f"Print error: {e}")
                '''
            else:
                self.skiptags.submit(elem.tag)

    def add_event(self, event):
        if event.name in self.events:
            print(f"Duplicate event name {event.name} already loaded!")
            self.eventdupes.append(event)
            return
            #prettyprint(event.root)
            #prettyprint(self.events[event.name].root)
            #assert False
        self.events[event.name] = event

    def get_event(self, name):
        if name in self.events:
            return self.events[name]
        return None

class Event:
    def __init__(self, root):
        self.root = root
        self.name = root.attrib['name'] if 'name' in root.attrib else ''
    
    def __str__(self):
        s = self.name if self.name else "ANONYMOUS"
        return s





def parse_events(data_dir):
    edb = EventDatabase()
    edb.load_data_director(data_dir)
    print(edb.skiptags)
    return edb

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        data_dir = r'C:/Users/Lucy/Downloads/Multiverse 5.4.4  - Data/data'
    else:
        data_dir = sys.argv[1]
    
    edb = parse_events(data_dir)    
    print(f"Event duplicates: {len(edb.eventdupes)}")
    dupenames = [event.name for event in edb.eventdupes]
    print(dupenames)































'''
class Event:
    def __init__(self, elem):
        self.name = elem.attrib['name'] if 'name' in elem.attrib else ''
        self.text = ''
        self.event_list = []
        for node in elem:
            if node.tag is etree.Comment:
                continue

    def __str__(self):
        s = f"{self.name}"
        s += f"\n"
        s += f"{self.text}"
        return s
'''


'''
if node.tag == 'text':
    self.text = node.text
elif node.tag == 'event':
    self.event_list.append(Event(node))
elif node.tag == 'store':
    pass
elif node.tag == 'reveal_map':
    pass
elif node.tag == 'modifyPursuit':
    pass
elif node.tag == 'choice':
    pass
elif node.tag == 'metaVariable':
    pass
elif node.tag == 'queueEvent':
    pass
elif node.tag =='deathEvent':
    pass
elif node.tag == 'eventButton':
    pass
elif node.tag == 'removeNebula':
    pass
elif node.tag == 'beaconType':
    pass
elif node.tag == 'img':
    pass
elif node.tag == 'item_modify':
    pass
elif node.tag == 'ship':
    pass
elif node.tag == 'autoReward':
    pass
elif node.tag == 'damage':
    pass
elif node.tag == 'weapon':
    pass
elif node.tag == 'crewMember':
    pass
elif node.tag == 'boarders':
    pass
elif node.tag == 'distressBeacon':
    pass
elif node.tag == 'loadEventList':
    pass
elif node.tag == 'environment':
    pass
elif node.tag == 'drone':
    pass
elif node.tag == 'augment':
    pass
elif node.tag == 'upgrade':
    pass
elif node.tag == 'enemyDamage':
    pass
elif node.tag == 'preventQuest':
    pass
elif node.tag is etree.Comment:
    pass
else:
    print(f"Unkown tag: {node.tag}")
    prettyprint(node)                
    assert False
    '''