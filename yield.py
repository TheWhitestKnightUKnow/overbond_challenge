import sys
import csv

def main():
    # If there wasn't a CSV passed, or user is looking for help,
    # let them know what to do!
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "Please pass me a csv file to parse!"
        return
    try:
        # Otherwise, open up the file...
        bondinfo = open(sys.argv[1], 'rb')
    except IOError as e:
        print "Yield.py failed to open this file: " + sys.argv[1]
        print "Please pass it a valid csv file containing bond information!"
        return
    else:
        # ...and parse its rows.
        corporate_bonds  = []
        government_bonds = []
        reader = csv.reader(bondinfo, delimiter=',')
        for row in reader:
            if row[0] == 'bond': # first row
                continue
            elif row[1] == 'corporate':
                corporate_bonds.append({
                    "name": row[0],
                    "term": float(row[2].split(' ')[0]),
                    "yield": float(row[3][:-1])
                })
            elif row[1] == 'government':
                government_bonds.append({
                    "name": row[0],
                    "term": float(row[2].split(' ')[0]),
                    "yield": float(row[3][:-1])
                })
            else:
                print 'This CSV contained a bond that wasn\'t government or corporate!'
                return

main()
