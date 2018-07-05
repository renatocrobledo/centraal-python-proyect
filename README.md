# Netflix Minimalistic BackEnd abstraction

## covering:
- User registration
- Server-side Login mechanism.
- User role support (admin, logued)
- Depending on the role the diferent functionalities would be available to execute trough respective end-points.

## logued:
  > read all categories

  > read all movies

  > search by keyword

  > search by name 

  > search by id

  > add movie to favorites

  > read favorite movies

  > delete favorite movie

## Admin:
  > all the logued one functionalities ...

  > create new movie ( name, year director*, category, tags)
  
  > update movie

  > create new category (name)

  > update category
## Anonymous (not-logued-users)
  > register user



## endpoints:
  > POST /login
    {
      username,
      password
    }

  > POST /register
    {
      mail,
      username,
      password
    }

  > GET /favorites

  > GET /movies

  > POST /movies
    {
      name,
      year,
      director,
      category,
      tags
    }

  > PUT /movies
    {
      id,
      name,
      year,
      director,
      category,
      tags
    }
  
  > GET /categories

  > POST /categories
    {
      name
    }
  
  > PUT /categories
    {
      id,
      name
    }


Notes: 
  * users without session will be treated as "anonymous". 
  * category must be defined before movies! 
  * tags are keywords asociated with a movie.
  * (*) optional fields