tickets = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]

plotList = []

def plotTrip(n):

  startPoint = 0
  
  while len(n) > len(plotList): #runs until our plotList is filled with start and end points
    if(len(plotList) < 1): #Keeps loop from running more than once.
      for i in range(0, len(n)):
        if(n[i][0] == None):
          plotList.append(n[i][1])
    
    for j in range(0,len(n)):
        if(n[j][0] == plotList[startPoint] and n[j][1] is not None):
          plotList.append(n[j][1])
          print(plotList)
    startPoint += 1 #increses our counter by one

plotTrip(tickets)