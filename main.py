import bottle
import json
import data
import processing

import os.path
import data # This assumes that your functions from parts 2 & 3 are in a file named data.py
def load_data( ):
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
    info = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer',
    'administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, info, 'saved_data.csv')

load_data()
@bottle.route('/')
def index():
  return bottle.static_file("index.html", root=".")

@bottle.post('/line')
def line():
  content=bottle.request.body.read().decode()
  content1=json.loads(content)
  dataIn=data.load_data("saved_data.csv")
  dataNeeded=processing.copy_matching(dataIn,"location",content1)
  return json.dumps(dataNeeded)
    

@bottle.route('/ajax.js')
def ajax():
  return bottle.static_file('ajax.js',root='.')

@bottle.route('/extra.js',root='.')
def extra():
  return bottle.static_file('extra.js',root='.')


def barData():
  key=processing.max_value(data.load_data('saved_data.csv'),'date')
  data1=processing.copy_matching(data.load_data('saved_data.csv'),'date',key)
  return json.dumps(data1)

@bottle.route('/bar')
def showBar():
  return barData()

def pieData():
  key=processing.max_value(data.load_data('saved_data.csv'),'date')
  data1=processing.copy_matching(data.load_data('saved_data.csv'),'date',key)
  return json.dumps(data1)
  
@bottle.route('/pie')
def showPie():
  return pieData()

bottle.run(host='0.0.0.0',port=8080)