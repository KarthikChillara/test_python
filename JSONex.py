import json

# Sample Json object
somejson = '{"Firstname" : "Karthik" ,"LastName" :"Chillara" ,"Country" :"India"}'

persondetails = json.loads(somejson)
print(persondetails)
print(persondetails["Country"])

familydetails = {"Father":"Harigopal","Mother":"Sarvani","Spouse":"Sushma","Daughter":"Sahithi"}
somejson1 = json.dumps(familydetails,indent=4,sort_keys=True)
print(somejson1)