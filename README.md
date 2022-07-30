# sensor-data-extractor

## JSON file
Edit data.json file following the example. Add separators used for a data format, add how many ids and sensor data you're fetching
```
{
    "f1": {
            "sep":[","," ","!","@"],
            "ids":{"id1":{} ,"id2":{}},
            "sensors":{"s1":{}, "s2":{}, "s3":{}}
        },
    
    "f2": {
            "sep":[","," "],
            "ids":{"id1":{} ,"id2":{}, "id3":{}},
            "sensors":{"s1":{}, "s2":{}, "s3":{}}
        },

    "f3": {
            "sep":[","],
            "ids":{"id1":{} ,"id2":{}},
            "sensors":{"s1":{}, "s2":{}}
        }
            
            
}
```

## python code
Following is an example python code showing how you can fetch data according to data format

```
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

```
