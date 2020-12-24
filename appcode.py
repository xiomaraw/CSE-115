import csv
import json
import os.path
import urllib.request
import urllib.parse

#Loading and filtering data into a CSV
def readDataFromCSVFile(filename):
  newData = []
  with open(filename, newline = '', encoding = "utf-8") as f:
    reader = csv.reader(f)
    header = True
    for data in reader:
      if header:
        headerRow = data
        header = False
      else:
        valueRow = data
        value = {}
        for i in range(len(headerRow)):
          value[headerRow[i]] = valueRow[i]
        newData.append(value)
  return newData
#print(readDataFromCSVFile("animalintake.csv"))

def writeDataToCSVFile(filename, data, headers, headerRow):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        if headerRow: 
            writer.writerow(headers)
            for line in data:
              writer.writerow([line[8],line[9], line[10],line[11], line[12], line[13], line[14], line[15], line[16]])

def loadData(filenameRoot):
   csvFile = filenameRoot
   if not os.path.isfile(csvFile):
       uri = "https://data.lacity.org/api/views/8cmr-fbcu/rows.json?accessType=DOWNLOAD" 
       response = urllib.request.urlopen(uri)
       content_string = response.read().decode()
       content = json.loads(content_string)
       content = content['data']
       writeDataToCSVFile(csvFile,content,['Shelter','Animal ID#','Intake Date', 'Intake Type','Intake Condition','Animal Type', 'Group', 'Breed 1', 'Breed 2'],True)
loadData("animalintake.csv")

#############################################################################FILTER

#Filters Animal Intake data by year
def filterYear(data, year):
  listofYears = []
  for years in data:
    if int(years["Intake Date"][:4]) == year:
      listofYears.append(years)
  return listofYears
#print(filterYear(readDataFromCSVFile("animalintake.csv"), 2011))

#############################################################################PIE CHART DATA / 2011

#PIE CHART DATA
#Returns the count of DOGS admitted in 2011
def doggos11():
  dog = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count['Animal Type'] == 'DOG':
      dog += 1
  return dog
#print(doggos11())

#Returns the count of CATS admitted in 2011
def cattos11():
  cat = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count['Animal Type'] == 'CAT':
      cat += 1
  return cat
#print(cattos11())

#Returns the count of BIRDS admitted in 2011
def birdos11():
  bird = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count['Animal Type'] == 'BIRD':
      bird += 1
  return bird
#print(birdos11())

#Returns the count of OTHER animals admitted in 2011
def otheros11():
  other = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count['Animal Type'] == 'OTHER':
      other += 1
  return other
#print(otheros11())

#Returns the count of ALL the animals admitted in 2011
def count2011():
  dogtotal = doggos11()
  cattotal = cattos11()
  birdtotal = birdos11()
  othertotal = otheros11()
  overall = dogtotal + cattotal + birdtotal + othertotal 
  return overall
#print(count2011())

#############################################################################2012

#Returns the count of DOGS admitted in 2012
def doggos12():
  dog = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count['Animal Type'] == 'DOG':
      dog += 1
  return dog
#print(doggos12())

#Returns the count of CATS admitted in 2012
def cattos12():
  cat = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count['Animal Type'] == 'CAT':
      cat += 1
  return cat
#print(cattos12())

#Returns the count of BIRDS admitted in 2012
def birdos12():
  bird = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count['Animal Type'] == 'BIRD':
      bird += 1
  return bird
#print(birdos12())

#Returns the count of OTHER animals admitted in 2012
def otheros12():
  other = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count['Animal Type'] == 'OTHER':
      other += 1
  return other
#print(otheros12())

#Returns the count of ALL the animals admitted in 2012
def count2012():
  dogtotal = doggos12()
  cattotal = cattos12()
  birdtotal = birdos12()
  othertotal = otheros12()
  overall = dogtotal + cattotal + birdtotal + othertotal 
  return overall
#print(count2012())

#############################################################################2013

#Returns the count of DOGS admitted in 2013
def doggos13():
  dog = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count['Animal Type'] == 'DOG':
      dog += 1
  return dog
#print(doggos13())

#Returns the count of CATS admitted in 2013
def cattos13():
  cat = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count['Animal Type'] == 'CAT':
      cat += 1
  return cat
#print(cattos13())

#Returns the count of BIRDS admitted in 2013
def birdos13():
  bird = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count['Animal Type'] == 'BIRD':
      bird += 1
  return bird
#print(birdos13())

#Returns the count of OTHER animals admitted in 2013
def otheros13():
  other = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count['Animal Type'] == 'OTHER':
      other += 1
  return other
#print(otheros13())

#Returns the count of ALL the animals admitted in 2013
def count2013():
  dogtotal = doggos13()
  cattotal = cattos13()
  birdtotal = birdos13()
  othertotal = otheros13()
  overall = dogtotal + cattotal + birdtotal + othertotal 
  return overall
#print(count2013())

##################################################################OVERALL YEARS 
#List of overall counts for all years
def overallAnimals():
  lisanimals = []
  c11 = count2011()
  c12 = count2012()
  c13 = count2013()
  lisanimals.append(c11)
  lisanimals.append(c12)
  lisanimals.append(c13)
  return lisanimals
#print(overallAnimals())

#List of overall dog counts in for all years
def overallDogs():
  lisdogs = []
  d11 = doggos11()
  d12 = doggos12()
  d13 = doggos13()
  lisdogs.append(d11)
  lisdogs.append(d12)
  lisdogs.append(d13)
  return lisdogs
#print(overallDogs())

#List of overall cat in for all years
def overallCats():
  liscats = []
  ca11 = cattos11()
  ca12 = cattos12()
  ca13 = cattos13()
  liscats.append(ca11)
  liscats.append(ca12)
  liscats.append(ca13)
  return liscats
#print(overallCats())

#List of overall bird counts for all years
def overallBirds():
  lisbirds = []
  b11 = birdos11()
  b12 = birdos12()
  b13 = birdos13()
  lisbirds.append(b11)
  lisbirds.append(b12)
  lisbirds.append(b13)
  return lisbirds
#print(overallBirds())

#List of overall other animal counts for all years
def overallOther():
  lisother = []
  o11 = otheros11()
  o12 = otheros12()
  o13 = otheros13()
  lisother.append(o11)
  lisother.append(o12)
  lisother.append(o13)
  return lisother
#print(overallOther())
#############################################################################TABLE DATA / E&W VALLEY FROM 2011 - 2013
#Returns a count of how many times an animal is admitted into the East Valley or West Valley Shelter in 2011
def valley11():
  valley = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count["Shelter"] == 'E VALLEY' or 'W VALLEY':
      valley += 1
  return valley
#print(valley11())

#Returns a count of how many times an animal is admitted into the East Valley or West Valley Shelter in 2012
def valley12():
  valley = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count["Shelter"] == 'E VALLEY' or 'W VALLEY':
      valley += 1
  return valley
#print(valley12())

#Returns a count of how many times an animal is admitted into the East Valley or West Valley Shelter in 2013
def valley13():
  valley = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count["Shelter"] == 'E VALLEY' or 'W VALLEY':
      valley += 1
  return valley
#print(valley13())

#############################################################################S&W LA FROM 2011 - 2013

#Returns a count of how many times an animal is admitted into the South LA or West LA Shelter in 2011
def la11():
  la = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count["Shelter"] == 'S LA' or 'W LA':
      la += 1
  return la
#print(la11())

#Returns a count of how many times an animal is admitted into the South LA or West LA Shelter in 2012
def la12():
  la = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count["Shelter"] == 'S LA' or 'W LA':
      la += 1
  return la
#print(la12())

#Returns a count of how many times an animal is admitted into the South LA or West LA Shelter in 2013
def la13():
  la = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count["Shelter"] == 'S LA' or 'W LA':
      la += 1
  return la
#print(la13())

#############################################################################HARBOR FROM 2011 - 2013

#Returns a count of how many times an animal is admitted into the Harbor Shelter in 2011
def harbor11():
  har = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count["Shelter"] == 'HARBOR':
      har += 1
  return har
#print(harbor11())

#Returns a count of how many times an animal is admitted into the Harbor Shelter in 2012
def harbor12():
  har = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count["Shelter"] == 'HARBOR':
      har += 1
  return har
#print(harbor12())

#Returns a count of how many times an animal is admitted into the Harbor Shelter in 2013
def harbor13():
  har = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count["Shelter"] == 'HARBOR':
      har += 1
  return har
#print(harbor13())

#############################################################################NORTH CENTRA FROM 2011 - 2013

#Returns a count of how many times an animal is admitted into the North Centra Shelter in 2011
def centra11():
  cent = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2011)
  for count in data:
    if count["Shelter"] == 'N CENTRA':
      cent += 1
  return cent
#print(centra11())

#Returns a count of how many times an animal is admitted into the North Centra Shelter in 2012
def centra12():
  cent = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2012)
  for count in data:
    if count["Shelter"] == 'N CENTRA':
      cent += 1
  return cent
#print(centra12())

#Returns a count of how many times an animal is admitted into the North Centra Shelter in 2013
def centra13():
  cent = 0
  data = filterYear(readDataFromCSVFile("animalintake.csv"), 2013)
  for count in data:
    if count["Shelter"] == 'N CENTRA':
      cent += 1
  return cent
#print(centra13())

#############################################################################OVERALL SHELTERS

#Appends all the shelters animal admitted counts for 2011, 2012, 2013 to a list
def overallshelters():
  lis = []
  s11 = shelters11()
  s12 = shelters12()
  s13 = shelters13()
  lis.append(s11)
  lis.append(s12)
  lis.append(s13)
  return lis
#print(overallshelters())

#Appends all the shelters animal admitted counts in 2011 to a list
def shelters11():
  lisShelters11 = []
  va = valley11()
  la = la11()
  ha = harbor11()
  cen = centra11()
  lisShelters11.append(va)
  lisShelters11.append(la)
  lisShelters11.append(ha)
  lisShelters11.append(cen)
  return lisShelters11
#print(shelters11())

#Appends all the shelters animal admitted counts in 2012 to a list
def shelters12():
  lisShelters12 = []
  va = valley12()
  la = la12()
  ha = harbor12()
  cen = centra12()
  lisShelters12.append(va)
  lisShelters12.append(la)
  lisShelters12.append(ha)
  lisShelters12.append(cen)
  return lisShelters12
#print(shelters12())

#Appends all the shelters animal admitted counts in 2013 to a list
def shelters13():
  lisShelters13 = []
  va = valley13()
  la = la13()
  ha = harbor13()
  cen = centra13()
  lisShelters13.append(va)
  lisShelters13.append(la)
  lisShelters13.append(ha)
  lisShelters13.append(cen)
  return lisShelters13
#print(shelters13())