BEGIN {
    FS = ","
    OFS = "|"
    command = "zcat ./IRSIncomeTax.gz"

    while ((command | getline) > 0) {
	# people[zip] += num of returns
        people[$3] += $5
	# dollars[zip] += gross income * 1000(all money amount are reported in thousands of dollars)
        dollars[$3] += $21 * 1000
    }
    close(command)

    for (zip in people) {
        if (people[zip] != 0)
	    # ($21*1000)/$5 is the avg income
            print zip, dollars[zip] / people[zip]
    }
}
