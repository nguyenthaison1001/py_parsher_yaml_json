import ruamel.yaml
import json
import time

start_time = time.time()

fileIn = 'Wednesday.yaml'
fileOut = 'Wednesday_02.json'

yaml = ruamel.yaml.YAML(typ='safe')
with open(fileIn, 'r') as fpi:
    data = yaml.load(fpi)
with open(fileOut, 'w') as fpo:
    json.dump(data, fpo, indent=4)

print("Successfully converted!\nSaved to file:", fileOut)
print("Executed time: %s seconds." % (time.time() - start_time))
