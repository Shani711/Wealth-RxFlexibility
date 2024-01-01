function loadTable(name, arr) {
    while ((getline < name) > 0){
	arr[$1] = $2
    }

    if (close(name)) {
        print "Couldn't properly close file: " name > "/dev/stderr"
        return 0
    }

    return 1
}

BEGIN {
    FS = OFS = "|"
    print "Loading tables... " > "/dev/stderr"

    if (!loadTable("ratios.txt", ratios)) {
        print "FAILED TO PROPERLY LOAD ONE OR MORE TABLES!!" > "/dev/stderr"
        exit -1
    }

    print "DONE loading tables... " > "/dev/stderr"

    cmd = "cat ./npiIncome.txt"
    # npi|income

    # read through NpiIncome
    while ((cmd | getline) > 0){
	# if NPI is in the ratios file:
        if ($1 in ratios)
	    # NPI|Income|Ratio
	    print $1, $2, ratios[$1]
    }

    print "All done!!!" > "/dev/stderr"
}
