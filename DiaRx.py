from pprint import pprint
import pyspark
sc = pyspark.SparkContext()

def prescription(line):
    fields = line.split(',')
    try: supply = int(fields[12])
    except: supply = 0
    # (NPI #, total day supply, Brnd_Name, Gnrc_Name) 
    return (fields[0], supply, fields[8], fields[9])

rxLines       = sc.textFile("./MedicarePrescriptions.gz")
drugWords     = sc.textFile("./drugWords")
drugWords = drugWords.collect()


# (NPI #, total day supply, Brnd_Name, Gnrc_Name)
pairs         = rxLines.map(prescription)

# filter for only lines with diabetic drugs in it
onlyDiabeticDrugs = pairs.filter(lambda x: x[2] in drugWords or x[3] in drugWords)

# (NPI, total day Supply)
npiAndSupply  = onlyDiabeticDrugs.map(lambda x: (x[0], x[1]))

# (NPI #, sum of the total day supply per NPI num)
sumDaySupply  = npiAndSupply.reduceByKey(lambda x, y: x + y)

formatted     = sumDaySupply.map(lambda x: (x[0], str(x[1])))

# collect all of them
npiRxSupply   = formatted.collect()

for n in npiRxSupply:
    print(n[0] + "|" + n[1])
