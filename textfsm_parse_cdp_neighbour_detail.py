import textfsm
import json
from pprint import pprint
import re

# Load cisco output into file_data
input_file = open("show_cdp.txt", encoding='utf-8')
file_data = input_file.read()
input_file.close()

# Use textfsm show cdp neighbour detail template
template = open("templates/cisco_ios_show_cdp_neighbors_detail.textfsm")
re_table = textfsm.TextFSM(template)
parsed_output = re_table.ParseText(file_data)

# Parsed output into Dict and print using pretty print
results = [dict(zip(re_table.header, textfsm)) for textfsm in parsed_output]
pprint(results)

# open csv file for output
output = open("cdp_report.csv", "w+")
cdp_report = output

# Write the csv headers on first row
print(re_table.header)
for s in re_table.header:
    cdp_report.write("%s;" % s)
cdp_report.write("\n")

# Write each result to a new row in cdp report
counter = 0
for row in parsed_output:
    print(row)
    for s in row:
        cdp_report.write("%s;" % s)
    cdp_report.write("\n")
    counter += 1

# Print to screen how many rows printed
print("\nWrote %d devices" % counter)