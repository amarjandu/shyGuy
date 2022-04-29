from src.camera import Camera
import cv2


def main():
    cam = Camera(0)
    while True:
        cam.display()
        # waitKey returns `-1` if input is not detected in time, anything else
        # is the int from the key input.
        if cv2.waitKey(1) != -1:
            break
    cam.release()
    cv2.destroyAllWindows()
    exit(0)


if __name__ == '__main__':
    main()
