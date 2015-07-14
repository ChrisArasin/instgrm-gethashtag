#!/usr/bin/python

import json
import requests
import time

# data will be stored here after each loop
theData = []

#instagram api url for first call. 
#change the /tags/YOURHASHTAG url segment to the desired hasthag
#change ?client_id=YOURCLIENTID parameter to your client id

nextLink = "https://api.instagram.com/v1/tags/YOURHASHTAG/media/recent?client_id=YOURCLIENTID"

def instaCall():
  global theData
  global nextLink
  i = 0

  while nextLink and i < 5000:
    i += 1
    print i

    # router was throwing a requests.exceptions.ConnectionError: ('Connection aborted.', error(65, 'No route to host')) 
    # error sporaddically. To avoid getting kicked out, timed this out. May want to play with how much you need. 
    #wait 1 second every 3 requests
    if i % 3 == 0:
      time.sleep(1)
    #wait 10 seconds every 10 requests. even though I was not exceeding the call limit, 


    if i % 10 == 0:
      print 'waiting'
      time.sleep(10)

    r = requests.get(nextLink)
    print r.headers
    theJson = r.json()
    theData = theData + theJson["data"]
    nextLink = False
    if 'pagination' in theJson:
      if 'next_url' in theJson['pagination']:
        nextLink = theJson["pagination"]["next_url"]
        print 'yep'

#run the function
instaCall()

# Open a file for writing
out_file = open("instagramdata.json","w")

# Save the dictionary into this file
# (the 'indent=4' is optional, but makes it more readable)
json.dump(theData, out_file, indent=4)    
                            
# Close the file
out_file.close()
