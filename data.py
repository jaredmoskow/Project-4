import csv
import json
import urllib.request

def dic_list_gen(list1,list2):
  final=[]
  for val in range(len(list2)):
    out={}
    for val2 in range(len(list1)):
      out[list1[val2]]=list2[val][val2]
    final.append(out)
  return final
  
def read_values(x):
  out=[]
  with open(x) as fp:
    reader=csv.reader(fp)
    next(reader)
    for line in reader:
      out.append(line)
  return out

def make_lists(x,dics):
  out=[]
  for line in dics:
    final=[]
    for val in x:
      final.append(line.get(val))
    out.append(final)
  return out

def write_values(filename,lists):
  with open(filename,'a') as fp:
    writer=csv.writer(fp)
    for line in lists:
      writer.writerow(line)

def json_loader(url):
  response=urllib.request.urlopen(url)
  content_string=response.read().decode()
  out=json.loads(content_string)
  return out

def make_values_numeric(keys,dict):
  for val in keys:
    dict[val]=float(dict[val])
  return dict

def save_data(keys,dicts,filename):
  with open(filename, 'w') as fp:
    writer=csv.writer(fp)
    writer.writerow(keys)
    for val in dicts:
      temp=[]
      for name in keys:
        temp.append(val[name])
      writer.writerow(temp)

def load_data(filename):
  final=[]
  with open(filename) as fp:
    reader=csv.reader(fp)
    keys=next(reader)
    for line in reader:
      out={}
      for key in keys:
        num=(keys.index(key))
        out[key]=line[num]
      final.append(out)
  return final