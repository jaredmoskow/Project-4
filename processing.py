def max_value(data,input):
  out=''
  for line in data:
    temp=line.get(input)
    if(temp>out):
      out=temp
  return out

def init_dictionary(data,input):
  final={}
  for line in data:
    temp=line.get(input,-1)
    if (temp!=-1):
      v=line.get(input)
      final[v]=0
  return final

def sum_matches(lod,k,v,tgt):
  num=0
  for line in lod:
    numk=line.get(k)
    if (numk==v):
      num+=line.get(tgt)
  return num

def copy_matching(lod,k,v):
  final=[]
  for line in lod:
    newk=line.get(k,-1)
    if(newk==v and newk!=-1):
      final.append(line)
  return final

