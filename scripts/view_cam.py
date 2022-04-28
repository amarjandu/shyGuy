from src.camera import Camera
import cv2


def main():
    cam = Camera(1)
    while True:
        cam.display()
        # waitKey returns `-1` if input is not detected in time, anything else
        # is a value
        if cv2.waitKey(1) != -1:
            break
    cv2.destroyAllWindows()
    exit(0)


if __name__ == '__main__':
    main()
