# Netflix Minimalistic BackEnd abstraction

## Covering:
- User registration 
- Server-side Login mechanism.
  (Auth, )
- User role support (admin, logued)
- Depending on the role the diferent functionalities would be available to execute trough respective end-points.
- Use of SQL & mongodb

## logued
  > Read all categories

  > Read all movies

  > Search movie by keyword

  > Search movie by name 

  > Search movie by id

  > Search movie by category

  > Add movie to favorites

  > Read favorite movies

  > Delete favorite movie

## Admin
  > All the logued one functionalities ...

  > Create new movie ( name, year director*, category, tags)
  
  > Update movie

  > Create new category (name)

  > Update category
## Anonymous (not-logued-users)
  > Register user

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