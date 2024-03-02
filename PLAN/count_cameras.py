import cv2

def count_connected_cameras():
    num_cameras = 0
    cams = list()

    for i in range(10):  # Check up to 10 cameras
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            num_cameras += 1
            cams.append(i)

        cap.release()
    return num_cameras, cams


num_connected_cameras, cams = count_connected_cameras()
print("Number of connected cameras:", num_connected_cameras)

for c in cams:
    print("Camera ", c)
