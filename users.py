PEOPLE = {
    "User 1": {
        "firstName": "Anas",
        "lname": "Bahjat",
        "age": "24",
        "major" : "Computer Engineer"
    },
    "User 2": {
        "firstName": "Mohammad",
        "lname": "Ahmad",
        "age": "18",
        "major" : "Student"
    },
    "User 3": {
        "firstName": "Tala",
        "lname": "Tamer",
        "age": "12",
        "major" : "School student"
    }
}


def get_all_users():
    return list(PEOPLE.values())