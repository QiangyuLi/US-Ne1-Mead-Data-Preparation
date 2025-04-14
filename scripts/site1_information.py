import csv

# Data for site1_information.csv
data = [
    ["Year", "Crop", "Cultivar", "Plant Population (plants/ha)", "Planting Date", "Emergence Date", "Harvest Date", "Yield (Mg/ha)", "Location"],
    [2001, "M", "Pioneer 33P67", 81500, "May 10", "May 16", "October 18", 13.51, "Site 1"],
    [2002, "M", "Pioneer 33P67", 71300, "May 9", "May 18", "November 4", 12.97, "Site 1"],
    [2003, "M", "Pioneer 33B51", 77000, "May 15", "May 27", "October 27", 12.12, "Site 1"],
    [2004, "M", "Pioneer 33B51", 79800, "May 3", "May 13", "October 15", 12.24, "Site 1"],
    [2005, "M", "DeKalb 63-75", 69200, "May 4", "May 17", "October 13", 12.02, "Site 1"],
    [2006, "M", "Pioneer 33B53", 80600, "May 5", "May 16", "October 5", 10.46, "Site 1"],
    [2007, "M", "Pioneer 31N30", 75300, "May 1", "May 10", "November 5", 12.80, "Site 1"],
    [2008, "M", "Pioneer 31N30", 76500, "April 29", "May 9", "November 18", 11.99, "Site 1"],
    [2009, "M", "Pioneer 32N73", 78500, "April 20", "May 5", "November 9", 13.35, "Site 1"],
    [2010, "M", "DeKalb 65-63 VT3", 78700, "April 19", "May 4", "September 21", 2.03, "Site 1"],
    [2011, "M", "Pioneer 32T88", 80200, "May 18", "May 26", "October 26", 11.97, "Site 1"],
    [2012, "M", "DeKalb 62-97 VT3", 77200, "April 24", "May 2", "October 10", 13.02, "Site 1"],
]

# Write to CSV
output_file = "/workspaces/US-Ne1-Mead-Data-Preparation/data/site1_information.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"File generated: {output_file}")