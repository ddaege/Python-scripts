current_movies = {'The Grinch' : '11:00am',
		  'Rudolph' : '1:00pm',
		  'Frosty the Snowman' : '3:00pm',
		  'Chrismas Vacation' : '5:00pm'}
print("We're snowing the following movie:")
for key in current_movies:
    print(key)

movie = input('What movie would you like the snowtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, 'is playing at', showtime)
