import sys
import csv

def main():
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "Please pass me a csv file to parse!"
        return
    with open(sys.argv[1], 'rb') as bondinfo:
        reader = csv.reader(bondinfo, delimiter=',')
        for row in reader:
            print row

main()

