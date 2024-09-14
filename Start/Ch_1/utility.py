# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates the use of the any, all, and sum functions
import json

values = [0, 1, 2, 3, 4, 5]

# TODO: any() can be used to see if any value in a sequence is True
# print(any(values))

# TODO: all() will detect if all of the values in a sequence are True
# print(all(values))

# TODO: sum() can be use to add all of the values in a sequence
# print(sum(values))

# these utility functions don't have callbacks like min or max,
# but we can use a generator for more fine control

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# TODO: are there any quake reports that were felt by more than 25,000 people?
if any(quoke['properties']['felt'] is not None and quoke['properties']['felt'] > 25000 for quoke in data['features']):
    print("Is at least one of this")


# TODO: how many quakes were felt by more than 500 people?
quakes = [quoke['properties']['felt'] for quoke in data['features'] if quoke['properties']['felt'] is not None and quoke['properties']['felt'] > 500]
print(len(quakes))

print(sum(quoke['properties']['felt']
           is not None and quoke['properties']['felt'] >= 500
             for quoke in data['features']))

# TODO: how many quakes had a magnitude of 6 or larger?
# solution list comprehension 
largemag = [quoke['properties']['mag'] for quoke in data['features'] if quoke['properties']['mag'] is not None and quoke['properties']['mag'] >= 6]
print(f"The amount of quakes with larger then 6 mag are {len(largemag)}")

# solution filter
largemag_count = len(list(filter(lambda q: q['properties']['mag'] is not None and q['properties']['mag'] >=6, data['features'])))
print(f"The amount of quakes with a magnitude of 6 or larger is {largemag_count}")

# solution sum
print(sum(quoke['properties']['mag']
           is not None and quoke['properties']['mag'] >=6
             for quoke in data['features']))

