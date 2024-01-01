# Prescribers-DiabeticDrugs
Hypothesis: Prescribers that live in wealthier neighborhoods are more “flexible”
to prescribe diabetic drugs to patients that don't necessarily have diabetes.

Recently there has been an influx of nondiabetic people taking diabetic drugs,
such as ozempic, to lose weight. This piqued my interest, and I wanted to research
this and see if there is a correlation between prescribers' wealth and whether
that affects their flexibility when prescribing diabetic drugs. 

I used Medicare datasets which provided access to the prescriptions that were
filled and the prescriber's information. Using these datasets, I assigned a score
to each prescriber to see how many more drug prescriptions than service prescriptions
they were prescribing. Then I used the Doctor NPI dataset to obtain the prescribers'
home zip code. Using the IRS Income Tax dataset, I calculated the average income in
each zip code. Then I was able to assign an income to each prescriber. Bringing it
all together, I plotted each prescriber using a scatter plot to determine the
correlation between living in a wealthier area and being more flexible when prescribing
diabetic drugs. I expected to see a positive linear graph, but unfortunately that was
not the case. Through my results, we can see there is a very slight correlation between
the prescriber's zip code’s wealth and their flexibility, but not enough to be
substantial to prove my hypothesis.

I believe that my hypothesis can be proven to be correct. The project that I conducted
has many bounds to it due to the scope limitations of public data sources. By using
Medicare datasets, it bound my data to patients that are 65+ and are using Medicare
insurance to purchase the prescriptions and services provided. It is extremely likely
that nondiabetic ozempic users are paying out of pocket and/or under the age of 65. This
project would also be more accurate if I had the prescribers real income, as opposed to
assigning them their zip code average income. If I had access to datasets that contain
prescriptions filled where there were no limitations on age and the recipient paid out
of pocket, the results would align more closely with my expectations. 
 

Steps taken:
      - Read through the Medicare Services dataset, determining which prescribers offer
        diabetic services and the quantity.
      - Read through the Medicare Drug Prescriptions dataset, determining which
        prescribers prescribe diabetic drugs and the quantity.
      - Then I compared the results of step 1 and 2, yielding a drug to service ratio
        for each prescriber.
      - Read through the IRS Income Tax dataset, yielding an average income for each zip
        code.
      - Read through the Doctor NPI dataset, collecting NPI and Zip for each prescriber.
      - Compared the results of steps 4 and 5, yielding the average income for the
        neighborhood each prescriber lives.
      - Compared steps 3 and 6, providing the NPI, income, and Ratio for each prescriber. 
      - Plotted a plot to visualize the results.


This data was found at:
https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Part-D-Prescriber.html

https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier.html

https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi

http://download.cms.gov/nppes/NPI_Files.html
