import sys
import csv

def main():
    # If there wasn't a CSV passed, or user is looking for help,
    # let them know what to do!
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "Please pass me a csv file to parse!"
        return
    corporate_bonds, government_bonds = populateLists(sys.argv[1])
    #Main logic
    results = []
    for cbond in corporate_bonds:
        bestDiff = float("inf")
        best = {}
        for gbond in government_bonds:
            if abs(cbond["term"] - gbond["term"]) < bestDiff:
                best = gbond
                bestDiff = abs(cbond["term"] - gbond["term"])
        results.append({
            "bond": cbond["name"],
            "benchmark": best["name"],
            "spread_to_benchmark": '%.2f' % abs(cbond["bondYield"] - best["bondYield"]) + '%'
        })
    # Print results to stdout
    print "bond,benchmark,spread_to_benchmark"
    for result in results:
        print '%s,%s,%s' % (result["bond"], result["benchmark"], result["spread_to_benchmark"])

# Populate the government and corporate bond lists
def populateLists(filename):
    try:
        # Otherwise, open up the file...
        bondinfo = open(filename, 'rb')
    except IOError as e:
        print "Yield.py failed to open this file: " + sys.argv[1]
        print "Please pass it a valid csv file containing bond information!"
        quit()
    else:
        # ...and parse its rows.
        corporate_bonds  = []
        government_bonds = []
        reader = csv.reader(bondinfo, delimiter=',')
        for row in reader:
            if row[1] == 'type': # first row
                continue
            elif row[1] == 'corporate':
                corporate_bonds.append({
                    "name": row[0],
                    round(float(row[2].split(' ')[0]), 2),
                    "bondYield" : float(row[3][:-1])
                })
            elif row[1] == 'government':
                government_bonds.append({
                    "name": row[0],
                    round(float(row[2].split(' ')[0]), 2),
                    "bondYield": float(row[3][:-1])
                })
            else:
                print 'This CSV contained a bond that wasn\'t government or corporate!'
                quit()
    return corporate_bonds, government_bonds

main()

