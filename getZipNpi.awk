BEGIN {
    FS = ","
    OFS = "|"
    command = "zcat ./DoctorNPI.gz"

    # skip title line
    firstSkipped = 0
    while ((command | getline) > 0) {
	# make sure there is valid zip
	if (firstSkipped && length($25) >= 5)
	    # ZIP | NPI
	    print substr($25, 2, 5), substr($1, 2, 10)
	firstSkipped = 1
    }
    close(command)
}

