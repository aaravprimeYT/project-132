import matplotlib.pyplot as plt
import csv
import seaborn as sns
import pandas as pd

rows = []

with open('project131_2.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader :
        rows.append(row)

headers = rows[0]
planetData = rows[1:]

df = pd.read_csv("project131_2.csv")

names = []
mass = []
radius = []
gravity = []

for data in planetData:
    names.append(data[3])
    mass.append(data[5])
    radius.append(data[6])
    gravity.append(data[7])

print(len(names))
print(len(mass))
print(len(radius))
print(len(gravity))
mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius, mass)
plt.title('Planet Radius and Mass')
plt.xlabel("Radius")
plt.ylabel('Mass')
plt.scatter(radius,mass)
plt.show()