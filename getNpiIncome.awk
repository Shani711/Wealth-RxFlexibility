function loadTable(name, arr) {
    while ((getline < name) > 0)
        arr[$1] = $2

    if (close(name)) {
        print "Couldn't properly close file: " name > "/dev/stderr"
        return 0
    }

    return 1
}

BEGIN {
    FS = OFS = "|"
    print "Loading tables... " > "/dev/stderr"

    if (!loadTable("zipIncome.txt", zipIncome)) {
        print "FAILED TO PROPERLY LOAD ONE OR MORE TABLES!!" > "/dev/stderr"
        exit -1
    }

    print "DONE loading tables... " > "/dev/stderr"

    cmd = "cat ./zipNpi.txt"
    # zip|income

    # read through NPI file
    while ((cmd | getline) > 0){
	# if zip is in the ZipIncome file:
        if ($1 in zipIncome)
	    # NPI | Income
	    print $2, zipIncome[$1]
    }

    print "All done!!!" > "/dev/stderr"
}
