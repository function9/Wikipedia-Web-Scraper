import requests
from bs4 import BeautifulSoup
from csv import writer

while(1):
    #prompt user for input on wiki page
    name = input("What Wikipedia Page Do You Want To Look Up?\n")
    #format input for wiki url
    name_format = name.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + name_format

    #requesting information
    response = requests.get(url)
    #check to see if url exists
    if response.status_code == 200:
        break
    else:
        print('That Wikipedia page does not exist\nRemember that page names are case sensitive\nTry Again')

#creating the BeautifulSoup object used to parsing
soup = BeautifulSoup(response.text, 'html.parser')

#finding title of page
title = soup.find(class_='firstHeading').text

#creating a list of all paragraphs on the page
paragraph = soup.find(class_='mw-parser-output').findAll('p')
#creating csv file with information
filename = name + '.csv'
with open(filename, 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['Title', title])
    csv_writer.writerow(['Paragraphs'])
    #for each paragraph find corresponding information and write it
    for p in paragraph:
        para = p.text
        #writing to csv file
        csv_writer.writerow([para])
final = 'Wikipedia page ' + name + ' scraped to ' + filename
print(final)