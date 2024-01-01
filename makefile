all: plot.pdf

clean:
	rm diabeticService.txt diabeticRx.txt ratios.txt zipIncome.txt zipNpi.txt npiIncome.txt npiRatioIncome.txt plot.pdf

# create plot
plot.pdf: plot.py npiRatioIncome.txt
	python3 ./plot.py

# NPI|Zip Income|Ratio
npiRatioIncome.txt: ratios.txt npiIncome.txt getRatioIncome.awk
	gawk -f getRatioIncome.awk > npiRatioIncome.txt

# NPI|Zip Income 
npiIncome.txt: zipNpi.txt zipIncome.txt getNpiIncome.awk
	gawk -f getNpiIncome.awk > npiIncome.txt

# Zip|NPI
zipNpi.txt: DoctorNPI.gz getZipNpi.awk
	gawk -f getZipNpi.awk > zipNpi.txt

# ZIP|Income
zipIncome.txt: IRSIncomeTax.gz getZipIncomes.awk
	gawk -f getZipIncomes.awk > zipIncome.txt

# NPI|Ratio of Rx/Service
ratios.txt: diabeticRx.txt diabeticService.txt getRatios.py
	spark-submit ./getRatios.py  > ratios.txt

# NPI|Total Supply
diabeticRx.txt: MedicarePrescriptions.gz drugWords DiaRx.py
	spark-submit ./DiaRx.py > diabeticRx.txt

# NPI|Total Diabetic Services
diabeticService.txt: MedicareServices.gz serviceWords DiaService.py
	spark-submit ./DiaService.py > diabeticService.txt
