from pprint import pprint
import re
import pyspark
sc = pyspark.SparkContext()

def format(line):
    unit   = line.split('|')
    # use search and regex to pull out the total and turn into int
    total  = unit[1]
    try: total = int(total)
    except: total = 0

    # return (npi, total)
    return (unit[0], total)

# (NPI #, total Rx)
rxLines       = sc.textFile("./diabeticRx.txt")
useRx         = rxLines.map(format)

# (NPI #, total services)
serLines      = sc.textFile("./diabeticService.txt")
useSer        = serLines.map(format)

unioned       = useRx.union(useSer)

# (NPI,(total Rx, total Services))
combinedNPI   = unioned.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]) if isinstance(x, tuple) and isinstance(y, tuple) else (x, y))

# filter to make sure all fields are taken (NPI, (Rx, Service)) 
hasRxService  = combinedNPI.filter(lambda x: len(x) == 2 and isinstance(x[1], tuple) and x[1][1] > 0)


# ratios included (NPI, Rx, Service, Rx/Service)
hasRatios     = hasRxService.map(lambda x: (x[0], x[1][0], x[1][1], x[1][0]/x[1][1]))

# (NPI, Ratio)
npiRatio      = hasRatios.map(lambda x: (x[0], x[3]))

collected     = npiRatio.collect()

for n in collected:
    print(n[0] + "|" + str(n[1]))
