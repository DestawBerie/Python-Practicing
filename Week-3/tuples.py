t=tuple()
print(t)
print(type(t))
years=(2012,2015,2016,2018,2020,2022, 2023)
print(years[0])
print(years[1])
print(years[-1])

print(2023 in years)
start_year=2010
for year in years:
    print(f"how many items in {year}",years.count(year))
    print(year-start_year)

# dictionaries
"""
first_name ="Destaw"
last_name="Berie"
age=150

country="Ethiopia"
"""
print({})
print(type({}))
d=dict()
print(d)
print(type(d))

finished_english={
    "talo": "house",
    "kira":"book",
    "mies":"man",
    "nainen":"woman",
    "poika":"boy"
}
person={
    "first_name":"Destaw",
    "last_name":"Berie",
    "is_maried":True,
    "age":250,
    "country":"Ethiopia",
    "kids":("john","amanues"),
    "skills":["python", "react", "node", "c#",],
    "address":{
        "city":"addis ababa",
        "street_name":"space street",
        "zipcode":"02270"

    }
    


}
print(person)