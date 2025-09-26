import requests
import json

# Make an API call and store the response.
url = 'https://api.fbi.gov/wanted/v1/list'
r = requests.get(url)
print(f"Status code: {r.status_code}\n")  # code of 200 is successful api call

# Create an output file so we can see the json response that was 
# returned by the API call
with open('output.json', 'w') as outfile:
    response = r.json()
    json.dump(response, outfile, indent=4)

#list of wanted persons from the 'items' key
list_of_wanted = response['items']

# To access the title of each wanted person
print("ARMED AND DANGEROUD INDIVIDUALS:")
for person in list_of_wanted:
    name = person['title'].title()


    if person["warning_message"] == "SHOULD BE CONSIDERED ARMED AND DANGEROUS":
        print(f"Person name: {name}")
        print(f"FBI direct link: {person['url']}")
        print(f"Gender: {person['sex']}")
        for subject in person['subjects']:
            print(f"Subject: {subject}")
        print()


#Count of crimes

violent_count = 0
white_collar_count = 0
kidnap_and_missing_count = 0
criminal_count = 0
seeking_info_count = 0
vicap_missing_count = 0
vicap_homicides_count = 0
case_of_the_week_count = 0
crimes_against_children_count = 0
bank_robbers_count = 0

for person in list_of_wanted:
    for crime in person['subjects']:
        if crime == 'Violent Crime - Murders':
            violent_count += 1
        elif crime == 'White-Collar Crime':
            white_collar_count += 1
        elif crime == 'Kidnappings and Missing Persons':
            kidnap_and_missing_count += 1
        elif crime == 'Criminal Enterprise Investigations':
            criminal_count += 1
        elif crime == 'Seeking Information':
            seeking_info_count += 1
        elif crime == 'ViCAP Missing Persons':
            vicap_missing_count += 1
        elif crime == 'ViCAP Homicides and Sexual Assaults':
            vicap_homicides_count += 1
        elif crime == 'Case of the Week':
            case_of_the_week_count += 1
        elif crime == 'Crimes Against Children':
            crimes_against_children_count += 1
        elif crime == 'Known Bank Robbers':
            bank_robbers_count += 1
        
crime_counts_list = [
    ('Violent Crime - Murders',  violent_count),
    ('White-Collar Crime',  white_collar_count),
    ('Kidnappings and Missing Persons',kidnap_and_missing_count),
    ('Criminal Enterprise Investigations',criminal_count),
    ('Seeking Information', seeking_info_count),
    ('ViCAP Missing Persons',vicap_missing_count),
    ('ViCAP Homicides and Sexual Assaults', vicap_homicides_count),
    ('Case of the Week',case_of_the_week_count),
    ('Crimes Against Children',  crimes_against_children_count),
    ('Known Bank Robbers', bank_robbers_count),
]

crime_counts_list.sort(key=lambda x: x[1], reverse=True)


print("Crime Frequencies:")
for crime, count in crime_counts_list:
    print(f"Crime: {crime} Count: {count}")
