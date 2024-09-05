
from datetime import datetime
from flask import abort 
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(PEOPLE.values())

def create(person):
    lname = person.get("lname")
    fname = person.get("fname","")

    if fname and lname not in PEOPLE :
        PEOPLE[lname] = {
            "lname" : lname,
            "fname" : fname,
            "timestamp" : get_timestamp(),
        }

        return PEOPLE[lname],201
    else :
        abort(406, 
              f"Person with last name {lname} already exits",
              )


def read_one(lname):
    if lname in PEOPLE :
        return PEOPLE[lname]
    else :
        abort(
            404,
            f"Person with last name {lname} not found"
        )


def update_person(lname,person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname",PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else :
        abort(
            404,
            f"Person With last name {lname} not found ..")

def delete_person(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
    else :
        abort(
            404,
            f"Person with name {lname} does not exists .."
        )
