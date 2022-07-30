import json
import os
import re 

class extractor:
    
    def __init__(self, data):
        # self.data = data
        self.fmt = data[:2]
        self.read_json()
        self.extract_values(data)

    def read_json(self):
        with open(os.path.join(os.getcwd(),'data.json'),'r') as file:
            data = json.load(file)
            self.extract_fields(data)
    
    def extract_fields(self, fmt_data):
        self.seps = fmt_data[self.fmt]['sep']
        self.ids = fmt_data[self.fmt]['ids']
        self.sensors = fmt_data[self.fmt]['sensors']

    def extract_values(self, data):
        temp = data.split(self.seps[0])
        regexPattern = '|'.join(map(re.escape, tuple(self.seps)))
        print(re.split(regexPattern, data))  


        

data = 'f1abcd,erefe@234424 45235!935235'

o1 = extractor(data)
