## Project definition

The idea for this project is to show the best location where setting up a bar/restaurant whose objective is to serve as a nexus between different companies. 
After-work culture is gaining relevance and even becoming an essential part in every business. Sacred liquids (also known as beer) allow humans to socialize and often create synergies, businesses and even new ventures. 

**Criterion to optimize the location:**
- Funded companies. They pay income to their employees (instead of equity) that can spend in our restaurant/bar.
- Companies with at least 10 employees but less than 300. Making business with a very large companies is not very easy if your startup is not big enough. I cannot see SpaceX buying a bunch of nanosatelites to a recent startup. Basically the young startup will not be able to produce the amount, neither deliver on time. Therefore, it might be interesting to locate the bar/restaurant near to "medium size startups", if there are enough around.
- Technological companies might be more interesting since trending topics meetups might attract more consumers.
- Try to avoid competition (companies working in the same 'category_code'). It is not really a big issue. Most interesting synergies arise between competitors and competition is good. It always push yourself to your work at 200%. Only apply a low score because almost every company will be within the technological sector despite being a social, web, news, etc., category. Therefore, businesses will arise. 


**Steps:**
1. Using MongoDB, create a new database and import the json with the data.
2. Write a first query filtering essential data.
3. Clean and prepare the dataset to work with.
4. Export a json including the geopoint and set a geoquery using MongoDB.
5. Print a map showing all the companies we filtered before.
6. Choose the best point and create a report using a pipelines.



## Links & Resources

- https://docs.mongodb.com/manual/geospatial-queries/
- https://developers.google.com/maps/documentation/geocoding/intro
- https://data.crunchbase.com/docs
- https://developers.google.com/places/web-service/search
- https://www.youtube.com/watch?v=PtV-ZnwCjT0