
import json
import bottle
import appcode

@bottle.route("/")
def handleRequestHTML():
  return bottle.static_file("index.html", root="")

@bottle.route("/animals.js")
def handleRequestJS():
  return bottle.static_file("animals.js", root="")

####################################################
#This is the bottle route server for the POST Request for the Pie Charts which displays the total amount of animals admitted into a Los Angeles animal shelter in the years 2011, 2012, and 2013. The POST Request is used when a user clicks a button of a certain animal, a pie chart of how many times that animal has been admitted into an Animal Shelter from the year 2011 to 2013. 
@bottle.route('/AnimalsPerYear')
def handleRequestOverall():
  return json.dumps(appcode.overallAnimals())

@bottle.route('/DogsPerYear')
def handleRequestDogs():
  return json.dumps(appcode.overallDogs())

@bottle.route('/CatsPerYear')
def handleRequestCats():
  return json.dumps(appcode.overallCats())

@bottle.route('/BirdsPerYear')
def handleRequestBirds():
  return json.dumps(appcode.overallBirds())

@bottle.route('/OtherPerYear')
def handleRequestOther():
  return json.dumps(appcode.overallOther())

#POST REQUEST
@bottle.post('/dogPie')
def dogGraphs():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.overallDogs()
  return handleRequestDogs()

@bottle.post('/catPie')
def catGraphs():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.overallCats()
  return handleRequestCats()

@bottle.post('/birdPie')
def birdGraphs():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.overallBirds()
  return handleRequestBirds()

@bottle.post('/otherPie')
def otherGraphs():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.overallOther()
  return handleRequestOther()

################################################
#This is the bottle route server for the POST Request for the Table which displays how many times an animal is admitted into one of Los Angeles Animal Shelters (East and West Valley, South and West Los Angeles, Harbor, and North Centra) from 2011 to 2013. The POST Request is used when a user clicks a button of a certain year, a table of that year will appear that shows the total amount of animals admitted in all of the Los Angeles Shelters.
@bottle.route('/table')
def handleRequesttable():
  return json.dumps(appcode.overallshelters())

@bottle.route('/table11')
def handleRequesttable11():
  return json.dumps(appcode.overallshelters())

@bottle.route('/table12')
def handleRequesttable12():
  return json.dumps(appcode.overallshelters())

@bottle.route('/table13')
def handleRequesttable13():
  return json.dumps(appcode.overallshelters())

#POST REQUEST
@bottle.post('/t11')
def table2011():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.shelters11()
  return handleRequesttable11()

@bottle.post('/t12')
def table2012():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.shelters12()
  return handleRequesttable12()

@bottle.post('/t13')
def table2013():
  content = bottle.request.body.read()
  #print(content)
  content = content.decode()
  #print(content)
  content = json.loads(content)
  appcode.shelters13()
  return handleRequesttable13()

bottle.run(host="0.0.0.0", port=8080, debug=True)