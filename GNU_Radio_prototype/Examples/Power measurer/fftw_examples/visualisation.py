import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv




x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100]


with open('in.csv') as csvfile_in:
	readCSV = csv.reader(csvfile_in, delimiter=';')
	input = []
	for row in readCSV:
		input.append(row)

with open('out.csv') as csvfile_out:
	readCSV_ = csv.reader(csvfile_out, delimiter=';')
	output = []
	for row in readCSV_:
		output.append(row)

output = output[0]
print output


for i in range(0, output.__len__(), 1):
	#print type(output[i])
	output[i] = int(output[i])

print output

t = np.arange(0, output.__len__(), 1)
plt.plot(t, output)

plt.xlabel('time (s)')
plt.ylabel('voltage (V)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.show()



#
# num_bins = 100
# n, bins, patches = plt.hist(output, num_bins, facecolor='blue', alpha=0.5)
# plt.show()