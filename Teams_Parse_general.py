#!/usr/bin/env python

#incomplete - 22/11/2019
#Script to Parse PowerShell output from Teams, formatted as .csv file
#"<parse-criteria>.txt" is the file of criteria to parse for
#"user@domain.com"email address of user to parse for - this variable needs to come from looping through "<parse-criteria>.txt"


import re

namefile = "<parse-criteria>.txt"
datafile = "Teams_Spain_csv.csv"
emailaddress = "user@domain.com"

outfile = open("outputfile.txt","w")

#with open(namefile) as filetoread:
#    for line in filetoread:
#       text=(line)
#       print(text)

with open(datafile) as filetoread:
    for line in filetoread:
        match = re.search(r'user@domain.com.com(.*)', line)  #(need to parse "<parse-criteria>.txt" for this value
        if match:
            sysname = match.group(1)
            print(line)
            outfile.write((line)+"\n") 



