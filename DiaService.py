from pprint import pprint
import pyspark
sc = pyspark.SparkContext()

def service(line):
    fields = line.split(',')
    # field 25 is Tot_Srvcs
    try: total = int(fields[25])
    except: total = 0
    # (NPI, total services, HCPSC_Cd, HCPCS_Desc)
    return (fields[0], total, fields[19], fields[20])

servLines       = sc.textFile("./MedicareServices.gz")
serviceWords     = sc.textFile("./serviceWords")
serviceWords = serviceWords.collect()


# (NPI #, total services, HCPSC_Cd, HCPCS_Desc)
pairs         = servLines.map(service)

# filter for only lines with diabetic services in it
onlyDiabetic  = pairs.filter(lambda x: x[2] in serviceWords or x[3] in serviceWords)

# (NPI, total services)
npiAndService  = onlyDiabetic.map(lambda x: (x[0], x[1]))

# (NPI #, sum of the total day supply per NPI num)
sumDayService  = npiAndService.reduceByKey(lambda x, y: x + y)

# formatted - needed for the getRatios.
formatted      = sumDayService.map(lambda x: (x[0], str(x[1])))

# collect all of them
npiService   = formatted.collect()

for n in npiService:
    print(n[0] + "|" + n[1])
