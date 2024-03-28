
import cv2


class Detect:

    @staticmethod
    def count_cameras():
        cam_num = list()
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                cam_num.append(f"Camera {i}")
                print(f"Camera {i} is available...")
            else:
                break

            cap.release()
        return cam_num
