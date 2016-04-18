# import nola data
import csv
import glob
import sys

output = ''
header = 'commonCalls, medianResponseTime, meanResponseTime, conditionalProb, decreasedType, '+\
            'deltaDisposition, districtSize, priority\n'

print(header)
output += header


folder = '/Users/ceara/PycharmProjects/nolaData/'
for filename in glob.glob(folder + '/*.csv'):

    data = {}
    with open(filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        labels = []
        reader.next()

        try:
            for row in reader:
                print(row[0])



        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

