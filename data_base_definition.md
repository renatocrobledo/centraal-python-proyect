Database engine: mongoDb

Collections:

```js
Users= {
  id,
  mail: string,
  username: string,
  password: string
}
```

```js
Role = {
  id,
  userId: pointer,
  name: string
}
```
```js
Sessions = {
  id,
  log_date: date,
  userId: pointer,
  hash: string
}
```
```js
Movies = {
  id,
  title: string,
  category: [] or string,
  keywords: array ['string', 'string',...],
  favorite: boolean | True, False
}
```
