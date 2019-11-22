import csv 
import matplotlib.pyplot as plt

# pie chart for men's hockey medal colours in 2014 (gold, silver, bronze)
# arrays fpr each color
Gold = []
silver = []
bronze = []

categories = []

with open("test_hockey.csv") as csvfile:
		reader = csv.reader(csvfile)

		line_count = 0

		for row in reader:
			if line_count == 0:
				#parse that first row of text data out of the file
				#this gets rid of the first row because its useless data
				categories.append(row)
				line_count += 1
			else:
				if row[7] == "Gold":
					print("won Gold")
					Gold.append(row[7])

				elif row[7] == "silver":
					print("won silver")
					silver.append(row[7])

				elif row[7] == "bronze":
					print("won bronze. Thats bad :/")
					bronze.append(row[7])

				line_count += 1

print("gold medals:" , len(Gold))
print("silver medals:" , len(silver))
print("bronze medals:" , len(bronze))

# plot the pit chart
labels = ("Gold", "silver", "bronze")
# sizes are how many and how large the slices of the pit chart will be
sizes = [len(Gold), len(silver), len(bronze)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend (labels, loc=1)
plt.title('Medals for Mens Hockey')
plt.xlabel("medals since 2014")
plt.show()