import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
year = int(input("oh hey give me a year and ill tell you all the movies that came out after it: "))
yea = int(input("now give me a year and ill tell you all the movies before it: "))
ye = int(input("same thing but noe ill tell you all the movies that came out that year"))
titl = input("search for the exact title of a movie: ")

for i in range (len(data)):
    '''if (data[i]['year']) > year:
        print({data[i]['title']})
    if(data[i]['year']) <  yea:
        print({data[i]['title']})
    if(data[i]['year']) ==  ye:
        print({data[i]['title']})'''
    if(data[i]['title']) == titl:
        print({data[i]['title']})