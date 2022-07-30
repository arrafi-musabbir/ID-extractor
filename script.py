import json
import os
import re 

class extractor:
    
    def __init__(self, data, dformat):
        self.read_json(dformat)
        self.extract_values(data)

    def read_json(self, dformat):
        with open(os.path.join(os.getcwd(),'data.json'),'r') as file:
            data = json.load(file)
            self.extract_fields(data, dformat)
    
    def extract_fields(self, fmt_data, dformat):
        self.seps = fmt_data[dformat]['sep']
        self.ids = fmt_data[dformat]['ids']
        self.sensors = fmt_data[dformat]['sensors']

    def extract_values(self, data):
        regexPattern = '|'.join(map(re.escape, tuple(self.seps)))
        data = re.split(regexPattern, data)
        return {**self.extract_ids(data) , **self.extract_sensors(data)} 
    
    def extract_ids(self, data):
        i = 0
        for key in self.ids.keys():
            self.ids[key] = data[i]
            i+=1 
        return self.ids 
            
    def extract_sensors(self, data):
        i = len(self.ids)
        for key in self.sensors.keys():
            self.sensors[key] = data[i]
            i+=1 
        return self.sensors  


        

data = 'abcd,erefe@234424 45235!935235'
dformat = 'f1'

o1 = extractor(data, dformat)
print(o1)
