import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-ef3ce-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-ef3ce.appspot.com"
})

# Import student images
folderPath = 'Images'
if not os.path.exists(folderPath):
    raise FileNotFoundError(f"The folder '{folderPath}' does not exist.")

pathList = os.listdir(folderPath)
print(f"Found {len(pathList)} images in '{folderPath}': {pathList}")

imgList = []
studentIds = []

bucket = storage.bucket()

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    if img is None:
        print(f"Warning: Unable to read image '{path}'. Skipping.")
        continue

    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    print(f"Uploaded '{fileName}' to Firebase Storage.")

print(f"Student IDs: {studentIds}")

def findEncoding(imagesList):
    encodeList = []
    for img in imagesList:
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_img)
        if encodings:
            encodeList.append(encodings[0])
        else:
            print(f"Warning: No faces found in image. Skipping encoding for this image.")
    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncoding(imgList)
print(f"Encoding complete. Encoded {len(encodeListKnown)} images.")
encodeListKnownWithIds = [encodeListKnown, studentIds]

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
