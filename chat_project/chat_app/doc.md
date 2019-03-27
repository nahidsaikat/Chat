**API Urls**

* GET: /chat/    
Return Data Format:
```json
[
    {
        "id": 7,
        "to_user": 3,
        "message": "hello hello"
    },
    {
        "id": 8,
        "to_user": 3,
        "message": "hello"
    }
]
```
* POST: /chat/  
Posted Data Format:
```json
{
    "to_user": 2,
    "message": "this is the message"
}
```
* GET: /chat/1/?format=json 
Return Data Format:
```json
{
    "id": 1,
    "to_user": 3,
    "message": "hello"
}
```
* PUT: /chat/7/  
Posted Data Format:
```json
{
    "to_user": 3,
    "message": "hello hello hello"
}
```

* DELETE: /chat/7/  
Posted Data Format:
```json
{}
```

#####NOTE: All the api will work only for authenticated users.
