from flask import abort, jsonify
USERS ={
   "1":  {
       "uid" : 1,
       "firstName": "Anas",
       "lastName": "Bahjat",
       "email": "anasyasine22@gmail.com",
       "age": 24
    },
    "2":  {
       "uid" : 2,
       "firstName": "Mohammad",
       "lastName": "Bahjat",
       "email": "mohb@gmail.com",
       "age": 30
    },
    "3":  {
       "uid" : 3,
       "firstName": "Tamer",
       "lastName": "Bahjat",
       "email": "tb@gmail.com",
       "age": 36
    },
    "4":  {
       "uid" : 4,
       "firstName": "Sama",
       "lastName": "Bahjat",
       "email": "samb@gmail.com",
       "age": 37
    }
}

def get_users():
    return list(USERS.values())

def get_user_by_id(uid):
    user_id_str = str(uid)  # Convert the uid to a string to match the dictionary keys
    if user_id_str in USERS:
        return jsonify(USERS[user_id_str])
    else :
        abort(
            404,
            f"The User id {uid} doesn't exists .."
        )
