import re
ret_map ="model name       :  AMD EPYC 7551P 32-Core Processor"
retttt="model :  AMD EPYC 7551P 32-Core Processor"
LAKE_PATTERN = ("model\s+name\s+\:\s+AMD\s+[A-Za-z]+\s+")
mathobj=re.match(r'model name(.*):(.*)AMD.*(\d{4}.?)',ret_map)
if mathobj:
    print(mathobj.group(3))