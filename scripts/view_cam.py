import logging

from src.camera import Camera
from src.mask import Mask
from src.viewer import Viewer

import cv2

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def main():
    cam = Camera(0)
    viewer = Viewer()
    mask = Mask()
    while True:
        time_start = cv2.getTickCount()
        _, frame = cam.read()
        data = mask.detect(frame)
        # if data:
        #     x, y = data.array[0].array[0], data.array[0].array[1]
        #     if len(data.array) > 1:
        #         # both eyes are visible
        #         w, h = data.array[1].array[0] + data.array[1].array[2], data.array[1].array[1] + data.array[1].array[3]
        #     else:
        #         #only one eye was found.
        #         w, h = data.array[0].array[0] + data.array[0].array[2], data.array[0].array[1] + data.array[0].array[3]
            
        for x, y, w, h in data:
            sub_face = frame[y:y + h, x:x + w]
            sub_face = cv2.GaussianBlur(sub_face, (23, 23), 30)
            # merge this blurry rectangle to our final image
            frame[y:y + sub_face.shape[0], x:x + sub_face.shape[1]] = sub_face
        viewer.display(frame)
        time_end = cv2.getTickCount()
        # waitKey returns `-1` if input is not detected in time, anything else
        # is the int from the key input.
        duration = (time_end - time_start) / cv2.getTickFrequency()
        log.warning('Elaspsed Time: %s', duration)
        if cv2.waitKey(1) != -1:
            break
    cam.release()
    cv2.destroyAllWindows()
    exit(0)


if __name__ == '__main__':
    main()
