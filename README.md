
# Movie Trailer Website

The Movie Trailer Website is the first proyect of the Full Stack Web Developer
Nanodegree at Udacity. This project consists of server-side python code to store
a list of movies titles, along with its respective box art imagery and  movie 
trailer website(YouTube). The code generates a static web page allowing visitors 
to browse their movies and watch the trailers. 

## Python version

The Python version used was Python 2.7.6

## How to Run Things

### Starting from the Terminal

To try the Movie Trailer application, type the following in the terminal:

```
cd MovieTrailer
python entertainment_center.py
```
##  How the application works

A Python Movie class it is defined in the media.py module. From the 
entertainment_center.py it is called the constructor media.Movie() to
instantiate movie objects which are stored in a list data structure called 
movies. Then the movies list is passed as argument of the open_movies_page 
function (defined in the fresh_tomatoes module) which generates an HTML file 
that visualizes all of these movies

## License

Movie Trailer Website is Copyright © 2016 Yamilet Diaz. 
It is free software, and may be redistributed under the MIT License.

The MIT License is a permissive license that is short and to the point. It lets
people do anything they want with your code as long as they provide attribution
back to you and don’t hold you liable.

