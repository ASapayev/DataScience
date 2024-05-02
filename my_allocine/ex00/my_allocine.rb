requests['Display all actors'] = "SELECT * FROM actors;"
requests['Display all genres'] = "SELECT * FROM genres"
requests['Display the name and year of the movies'] = "SELECT mov_title, mov_year FROM movies"
requests['Display reviewer name from the reviews table'] = "SELECT rev_name FROM reviews"

requests["Find the year when the movie American Beauty released"] = "SELECT mov_year FROM movies WHERE mov_title == 'American Beauty'"
requests["Find the movie which was released in the year 1999"] = "SELECT mov_title FROM movies WHERE mov_year == '1999'"
requests["Find the movie which was released before 1998"] = "SELECT mov_title FROM movies WHERE mov_year < '1998'"
requests["Find the name of all reviewers who have rated 7 or more stars to their rating order by reviews rev_name (it might have duplicated names :-))"] = "SELECT rev_name FROM movies_ratings_reviews INNER JOIN reviews ON movies_ratings_reviews.rev_id = reviews.id WHERE rev_stars >= '7' ORDER BY rev_name"
requests["Find the titles of the movies with ID 905, 907, 917"] = "SELECT mov_title FROM movies WHERE ID IN('905', '907', '917')"
requests["Find the list of those movies with year and ID which include the words Boogie Nights"] = "SELECT ID, mov_title, mov_year FROM movies WHERE mov_title == 'Boogie Nights '"
requests["Find the ID number for the actor whose first name is 'Woody' and the last name is 'Allen'"] = "SELECT ID FROM actors WHERE (act_fname == 'Woody' AND act_lname == 'Allen')"

requests["Find the actors with all information who played a role in the movies 'Annie Hall'"] = "SELECT act_id, act_fname, act_lname, act_gender FROM movies INNER JOIN movies_actors ON movies.id = movies_actors.mov_id INNER JOIN actors ON movies_actors.act_id = actors.id WHERE mov_title == 'Annie Hall'"
requests["Find the first and last names of all the actors who were cast in the movies 'Annie Hall', and the roles they played in that production"] = "SELECT act_fname, act_lname, role FROM movies INNER JOIN movies_actors ON movies.id = movies_actors.mov_id INNER JOIN actors ON movies_actors.act_id = actors.id WHERE mov_title == 'Annie Hall'"

requests["Find the name of movie and director who directed a movies that casted a role as Sean Maguire"] = "SELECT dir_fname, dir_lname, mov_title FROM movies INNER JOIN movies_actors ON movies.id = movies_actors.mov_id INNER JOIN actors ON movies_actors.act_id = actors.id INNER JOIN directors_movies ON directors_movies.mov_id = movies.id JOIN directors ON directors_movies.dir_id = directors.id WHERE role == 'Sean Maguire'"
requests["Find all the actors who have not acted in any movie between 1990 and 2000 (select only actor first name, last name, movie title and release year)"] = "SELECT DISTINCT act_fname, act_lname, mov_title, CAST(strftime('%Y', mov_dt_rel) as INTEGER) FROM movies INNER JOIN movies_actors ON movies.id = movies_actors.mov_id INNER JOIN actors ON movies_actors.act_id = actors.id WHERE (mov_dt_rel < '1990-01-01' OR mov_dt_rel > '2000-01-01') AND mov_YEAR != '2004'"