import json
import os
import re 

class extractor:
    
    def __init__(self, dformat):
        self.read_json(dformat)
        
    def __extract__(self, data):
        return self.extract_values(data)
    
    # reading data format from json file    
    def read_json(self, dformat):
        with open(os.path.join(os.getcwd(),'data.json'),'r') as file:
            data = json.load(file)
            self.extract_fields(data, dformat)
    
    # extract data fields
    def extract_fields(self, fmt_data, dformat):
        self.seps = fmt_data[dformat]['sep']
        self.ids = fmt_data[dformat]['ids']
        self.sensors = fmt_data[dformat]['sensors']

    # extract values corresponding to data fields
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


        
### example data
data1 = 'abcd,erefe@234424 45235!935235'
data2 = 'abcd,erefe,sigrhjs 234424 45235 935235'
data3 = 'abcd,erefe,234424,45235'

### data format
dfmt1 = 'f1'
dfmt2 = 'f2'
dfmt3 = 'f3'

### creating object with various data format
o1 = extractor(dfmt1)
o2 = extractor(dfmt2)
o3 = extractor(dfmt3)

### will return dictionary as defined in file.json
print(o1.__extract__(data1))
print(o2.__extract__(data2))
print(o3.__extract__(data3))
