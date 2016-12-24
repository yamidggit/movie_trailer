import media
import fresh_tomatoes 

# the following code calls the constructor media.Movie() to instantiate the movie 
# objects. It's possible to do this because the media.py module is imported above

titanic=media.Movie("Titanic",
                    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                    "https://youtu.be/ZQ6klONCq4s")                 

gladiator=media.Movie("Gladiator",
                    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                    "https://youtu.be/ol67qo3WhJk")

life_is_beautiful= media.Movie("Life is Beautiful",
                            "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
                            "https://youtu.be/pAYEQP8gx3w")
                            
the_wolf_of_wall_street=media.Movie("The Wolf of Wall Street",
                                "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                "https://youtu.be/iszwuX1AK6A")
                                
zootopia=media.Movie("Zootopia",
                    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                    "https://youtu.be/jWM0ct-OLsM")

charlies_angels=media.Movie("Charlie's Angels",
                            "https://upload.wikimedia.org/wikipedia/en/a/a6/Charlies_Angels_%282000%29_Poster.jpg",
                            "https://youtu.be/rRHRa80wVq8")
                            
madagascar=media.Movie("Madagascar",
                    "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",
                    "https://youtu.be/dm-eiFVtRws")
                    
minions=media.Movie("Minions",
                    "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                    "https://youtu.be/jc86EFjLFV4")
                    
moulin_rouge=media.Movie("Moulin Rouge",
                        "https://upload.wikimedia.org/wikipedia/en/d/d7/Moulin_Rouge_2_cover.jpg",
                        "https://youtu.be/SyZDaTZSFuo")
                    
# it creates a list data structure called movies to store the movies objects

movies=[titanic, gladiator, life_is_beautiful, the_wolf_of_wall_street, 
        zootopia, charlies_angels, madagascar, minions, moulin_rouge]

# the fresh_tomatoes.py module has a function called open_movies_page that takes
# a list of movies as argument, and creates an HTML file which visualizes all of these movies.

fresh_tomatoes.open_movies_page(movies)

