import sys
import csv

def main():
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "Please pass me a csv file to parse!"
        return
    # These two will be sorted by term length
    corporate_bonds, government_bonds = populateLists(sys.argv[1])
    # Print header
    print "bond,spread_to_curve"
    # Print corporate bonds
    for cbond in corporate_bonds:
        # Find the two government bonds to use as 
        # interpolation points
        i = 0
        while i < len(government_bonds) - 1:
            if government_bonds[i]["term"] < cbond["term"]:
                i = i + 1
            else:
                break
        x  = cbond["term"]
        x1 = government_bonds[i-1]["term"]
        y1 = government_bonds[i-1]["bondYield"]
        x2 = government_bonds[i]["term"]
        y2 = government_bonds[i]["bondYield"]
        m  = ((y2 - y1)/(x2 - x1))
        y0 = ((x - x1) * m)
        y  = round (cbond["bondYield"] - y0  - y1, 2)
        print '%s,%s' % (cbond["name"], str(y) + '%')

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
                # This will sort coporate bonds in order
                # of term length
                i = 0
                while i < len(corporate_bonds):
                    if corporate_bonds[i]["term"] < float(row[2].split(' ')[0]):
                        i = i + 1
                    else:
                        break
                corporate_bonds.insert(i, {
                    "name": row[0],
                    "term": float(row[2].split(' ')[0]),
                    "bondYield" : float(row[3][:-1])
                })
            elif row[1] == 'government':
                # This will sort government bonds in order
                # of term length
                i = 0
                while i < len(government_bonds):
                    if government_bonds[i]["term"] < float(row[2].split(' ')[0]):
                        i = i + 1
                    else:
                        break
                government_bonds.insert(i, {
                    "name": row[0],
                    "term": float(row[2].split(' ')[0]),
                    "bondYield" : float(row[3][:-1])
                })
            else:
                print 'This CSV contained a bond that wasn\'t government or corporate!'
                quit()
    return corporate_bonds, government_bonds

main()