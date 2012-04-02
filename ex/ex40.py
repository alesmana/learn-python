cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}
# this one does not have order

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state): # Python has a function called map so...
    if state in themap:
        return themap[state]
    else:
        return "Not found"
        
# see see
cities['_find'] = find_city

# for loop it. Note the output
for key in cities:
    print cities[key]

while True:
    print "State? (Enter to quit)",
    state = raw_input("> ")
    
    if not state: break
    
    # important
    city_found = cities['_find'](cities, state)
    print city_found
