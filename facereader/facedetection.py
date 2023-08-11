import os
import face_recognition
import cv2
import numpy as np
from student.models import attendance, student
from face_attendance.settings import BASE_DIR

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)


def facerecognition(video_path, day, month, year):
    video_capture = cv2.VideoCapture(video_path)

    # Load a sample picture and learn how to recognize it.
    # jeff_image = face_recognition.load_image_file("known/2/image1.jpeg")
    # jeff_face_encoding = face_recognition.face_encodings(jeff_image)[0]

    # Load a second sample picture and learn how to recognize it.
    # bill_image = face_recognition.load_image_file("known/1/image1.jpeg")
    # bill_face_encoding = face_recognition.face_encodings(bill_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = {
    }
    dir = os.path.join(BASE_DIR, 'static/known')
    for pathname, subdirnames, filenames in os.walk(dir):
        if pathname == dir:
            continue
        key = os.path.basename(pathname)
        known_face_encodings[key] = []
        for filename in filenames:
            image = face_recognition.load_image_file(
                os.path.join(pathname, filename))
            known_face_encodings[key].append(
                face_recognition.face_encodings(image)[0])

    if day == 1:
        attendance.objects.filter(
            month=month, year=year).update(d_1=0)
    elif day == 2:
        attendance.objects.filter(
            month=month, year=year).update(d_2=0)
    elif day == 3:
        attendance.objects.filter(
            month=month, year=year).update(d_3=0)
    elif day == 4:
        attendance.objects.filter(
            month=month, year=year).update(d_4=0)
    elif day == 5:
        attendance.objects.filter(
            month=month, year=year).update(d_5=0)
    elif day == 6:
        attendance.objects.filter(
            month=month, year=year).update(d_6=0)
    elif day == 7:
        attendance.objects.filter(
            month=month, year=year).update(d_7=0)
    elif day == 8:
        attendance.objects.filter(
            month=month, year=year).update(d_8=0)
    elif day == 9:
        attendance.objects.filter(
            month=month, year=year).update(d_9=0)
    elif day == 10:
        attendance.objects.filter(
            month=month, year=year).update(d_10=0)
    elif day == 11:
        attendance.objects.filter(
            month=month, year=year).update(d_11=0)
    elif day == 12:
        attendance.objects.filter(
            month=month, year=year).update(d_12=0)
    elif day == 13:
        attendance.objects.filter(
            month=month, year=year).update(d_13=0)
    elif day == 14:
        attendance.objects.filter(
            month=month, year=year).update(d_14=0)
    elif day == 15:
        attendance.objects.filter(
            month=month, year=year).update(d_15=0)
    elif day == 16:
        attendance.objects.filter(
            month=month, year=year).update(d_16=0)
    elif day == 17:
        attendance.objects.filter(
            month=month, year=year).update(d_17=0)
    elif day == 18:
        attendance.objects.filter(
            month=month, year=year).update(d_18=0)
    elif day == 19:
        attendance.objects.filter(
            month=month, year=year).update(d_19=0)
    elif day == 20:
        attendance.objects.filter(
            month=month, year=year).update(d_20=0)
    elif day == 21:
        attendance.objects.filter(
            month=month, year=year).update(d_21=0)
    elif day == 22:
        attendance.objects.filter(
            month=month, year=year).update(d_22=0)
    elif day == 23:
        attendance.objects.filter(
            month=month, year=year).update(d_23=0)
    elif day == 24:
        attendance.objects.filter(
            month=month, year=year).update(d_24=0)
    elif day == 25:
        attendance.objects.filter(
            month=month, year=year).update(d_25=0)
    elif day == 26:
        attendance.objects.filter(
            month=month, year=year).update(d_26=0)
    elif day == 27:
        attendance.objects.filter(
            month=month, year=year).update(d_27=0)
    elif day == 28:
        attendance.objects.filter(
            month=month, year=year).update(d_28=0)
    elif day == 29:
        attendance.objects.filter(
            month=month, year=year).update(d_29=0)
    elif day == 30:
        attendance.objects.filter(
            month=month, year=year).update(d_30=0)
    elif day == 31:
        attendance.objects.filter(
            month=month, year=year).update(d_31=0)

    count = 0
    while True:
        # if True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        # frame = cv2.imread("image/image1.jpeg", cv2.IMREAD_COLOR)
        if not ret:
            break
        # small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        small_frame = frame
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = small_frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)

        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            # top*=2
            # right*=2
            # bottom*=2
            # left*=2
            for key in known_face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings[key], face_encoding)

                name = "-1"

                # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings[key], face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = key
                    if day == 1:
                        attendance.objects.filter(student=name).update(d_1=1)
                    elif day == 2:
                        attendance.objects.filter(student=name).update(d_2=1)
                    elif day == 3:
                        attendance.objects.filter(student=name).update(d_3=1)
                    elif day == 4:
                        attendance.objects.filter(student=name).update(d_4=1)
                    elif day == 5:
                        attendance.objects.filter(student=name).update(d_5=1)
                    elif day == 6:
                        attendance.objects.filter(student=name).update(d_6=1)
                    elif day == 7:
                        attendance.objects.filter(student=name).update(d_7=1)
                    elif day == 8:
                        attendance.objects.filter(student=name).update(d_8=1)
                    elif day == 9:
                        attendance.objects.filter(student=name).update(d_9=1)
                    elif day == 10:
                        attendance.objects.filter(
                            student=name).update(d_10=1)
                    elif day == 11:
                        attendance.objects.filter(
                            student=name).update(d_11=1)
                    elif day == 12:
                        attendance.objects.filter(
                            student=name).update(d_12=1)
                    elif day == 13:
                        attendance.objects.filter(
                            student=name).update(d_13=1)
                    elif day == 14:
                        attendance.objects.filter(
                            student=name).update(d_14=1)
                    elif day == 15:
                        attendance.objects.filter(
                            student=name).update(d_15=1)
                    elif day == 16:
                        attendance.objects.filter(
                            student=name).update(d_16=1)
                    elif day == 17:
                        attendance.objects.filter(
                            student=name).update(d_17=1)
                    elif day == 18:
                        attendance.objects.filter(
                            student=name).update(d_18=1)
                    elif day == 19:
                        attendance.objects.filter(
                            student=name).update(d_19=1)
                    elif day == 20:
                        attendance.objects.filter(
                            student=name).update(d_20=1)
                    elif day == 21:
                        attendance.objects.filter(
                            student=name).update(d_21=1)
                    elif day == 22:
                        attendance.objects.filter(
                            student=name).update(d_22=1)
                    elif day == 23:
                        attendance.objects.filter(
                            student=name).update(d_23=1)
                    elif day == 24:
                        attendance.objects.filter(
                            student=name).update(d_24=1)
                    elif day == 25:
                        attendance.objects.filter(
                            student=name).update(d_25=1)
                    elif day == 26:
                        attendance.objects.filter(
                            student=name).update(d_26=1)
                    elif day == 27:
                        attendance.objects.filter(
                            student=name).update(d_27=1)
                    elif day == 28:
                        attendance.objects.filter(
                            student=name).update(d_28=1)
                    elif day == 29:
                        attendance.objects.filter(
                            student=name).update(d_29=1)
                    elif day == 30:
                        attendance.objects.filter(
                            student=name).update(d_30=1)
                    elif day == 31:
                        attendance.objects.filter(
                            student=name).update(d_31=1)

            # Draw a box around the face
                    cv2.rectangle(frame, (left, top),
                                (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35),
                                (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6),
                                font, 1.0, (255, 255, 255), 1)
                    break

        # Display the resulting image
        cv2.imshow('Video', frame)
        # cv2.waitKey(0)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
