import urllib.request, urllib.parse, urllib.error, xml.dom.minidom

import json

def Geocoding_International_Geocode_v1_10(Key, Country, Location):
    """ The output is an array of key value pairs, the keys being:
        #Name
        #Latitude
        #Longitude
    """
    #Build the url
    requestUrl = "https://api.addressy.com/Geocoding/International/Geocode/v1.10/xmla.ws?"
    requestUrl += "&" +  urllib.parse.urlencode({"Key":Key})
    requestUrl += "&" +  urllib.parse.urlencode({"Country":Country})
    requestUrl += "&" +  urllib.parse.urlencode({"Location":Location})

    #Get the data
    dataDoc = xml.dom.minidom.parseString(urllib.request.urlopen(requestUrl).read())

    #Get references to the schema and data
    schemaNodes = dataDoc.getElementsByTagName("Column")
    dataNotes = dataDoc.getElementsByTagName("Row")

    #Check for an error
    if len(schemaNodes) == 4 and schemaNodes[0].attributes["Name"].value == "Error":
        raise Exception(dataNotes[0].attributes["Description"].value)

    #Work though the items in the response
    results = []
    for dataNode in dataNotes:

        rowData = dict()

        for schemaNode in schemaNodes:
            key = schemaNode.attributes["Name"].value
            value = dataNode.attributes[key].value
            rowData[key] = value
        results.append(rowData)

    return results
