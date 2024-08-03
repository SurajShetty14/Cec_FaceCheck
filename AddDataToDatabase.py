import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the Firebase app with service account and database URL
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-ef3ce-default-rtdb.firebaseio.com/"
})

# Reference to the Students node
ref = db.reference('Students')

# Data to be inserted
data = {
    "111": {
        "name": "Revathi",
        "major": "AI",
        "starting_year": 2021,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-19 00:54:34"
    },
    "112": {
        "name": "Vijeth",
        "major": "Mechanical",
        "starting_year": 2022,
        "total_attendance": 12,
        "standing": "B",
        "year": 2,
        "last_attendance_time": "2024-05-19 00:54:34"
    },
    "113": {
        "name": "Prathviraj B R",
        "major": "Robotics",
        "starting_year": 2020,
        "total_attendance": 10,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2024-05-19 00:54:34"
    },
    "114": {
        "name": "Suraj Shetty",
        "major": "CSE",
        "starting_year": 2020,
        "total_attendance": 12,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-19 00:54:34"
    },
    "115": {
        "name": "Sushmitha",
        "major": "CSE",
        "starting_year": 2020,
        "total_attendance": 3,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-19 00:54:34"
    }
}

# Insert data into the database
for key, value in data.items():
    ref.child(key).set(value)
    print(f"Inserted data for student ID: {key}")

print("Data insertion completed.")
