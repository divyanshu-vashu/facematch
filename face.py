import face_recognition
known = face_recognition.load_image_file("/Users/vashusingh/Vashu/PYTHONFACE/IMAGE/IMG1.jpg")
unknown = face_recognition.load_image_file("/Users/vashusingh/Vashu/PYTHONFACE/IMAGE/IMG2.jpeg")
image1 = face_recognition.face_encodings(known)[0]
image2 = face_recognition.face_encodings(unknown)[0]

results= face_recognition.compare_faces([image1],image2)
print (results)
