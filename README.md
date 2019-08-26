## Project definition

The idea for this project is to show the best location where setting up a bar/restaurant whose objective is to serve as a nexus between different companies. 
After-work culture is gaining relevance and even becoming an essential part in every business. Sacred liquids (also known as beer) allow humans to socialize and often create synergies, businesses and even new ventures. 

**Criterion to optimize the location:**
- Funded companies. They pay income to their employees (instead of equity) that can be spent at our restaurant/bar.
- Companies with at least 10 employees but less than 300. Making business with a very large companies is not very easy if your startup is not big enough. I cannot see SpaceX buying a bunch of nanosatelites to a recent startup. Basically the young startup will not be able to produce the amount, neither deliver on time.
- Sometimes there is someone who ends up feeling too sacred (gets too drunk). It might be interesting not having so many news agencies around to prevent bad PR. Otherwise, we cannot eliminate these companies since they might be extremly helpful for businesses when creating awareness. Therefore, let's affect it slightly negative to the final score. 
- Using Google's API, find metro/bus station. It is important our customers can go home safely. Check also for other bars near around. Would be good to have competitors (it always pushes you to work harder and means it is a good place for this business), but let's try to find not a lot of them near around.
- Select the best location.

**Steps:**
1. Using MongoDB, create a new database and import the json with the data.
2. Write a first query filtering essential data.
3. Clean and prepare the dataset to work with.
4. Export a json including the geopoint and set a geoquery using MongoDB.
5. Print a map showing all the companies we filtered before.
6. Do some querys using Google's API.
7. Choose the best point and create a report using a pipelines.

## My solution
![bar_location](https://raw.githubusercontent.com/aiborra11/visualizing-real-world-data-project/images/barlocation.png)

## Links & Resources

- https://docs.mongodb.com/manual/geospatial-queries/
- https://developers.google.com/maps/documentation/geocoding/intro
- https://data.crunchbase.com/docs
- https://developers.google.com/places/web-service/search
- https://www.youtube.com/watch?v=PtV-ZnwCjT0
- https://developers.google.com/places/web-service/search


