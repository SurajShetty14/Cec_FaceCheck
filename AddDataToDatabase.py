import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://cecfacecheck-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')
data = {
    "111":
        {
            "name": "Revathi",
            "major": "Designing",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-05-19 00:54:34"
        },
    "112":
        {
            "name": "Vijeth",
            "major": "Mechanical",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2024-05-19 00:54:34"
        },
    "113":
        {
            "name": "Prathviraj B R",
            "major": "Robotics",
            "starting_year": 2020,
            "total_attendance": 10,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2024-05-19 00:54:34"
        },
    "114":
        {
            "name": "Suraj Shetty",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-05-19 00:54:34"
        },
    "115":
        {
            "name": "Sushmitha",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 3,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-05-19 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
