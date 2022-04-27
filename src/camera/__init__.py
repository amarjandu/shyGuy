import contextlib
from dataclasses import (
    dataclass
)
import logging
import typing

import cv2

log = logging.getLogger(__name__)


@dataclass
class Camera:
    """
    Wrapper around the cv2 camera, has some checks in place
    """
    camera_number: int
    video_capture: typing.Optional["cv2.VideoCapture"] = None

    def __post_init__(self):
        self.video_capture = cv2.VideoCapture(self.camera_number)
        if not self.read():
            raise ConnectionError('Unable to connect to camera: ', self.camera_number)

    # TODO: Might want to encapsulate this within a context manager so
    #       VideoCapture.release() does not have to be called.
    def read(self) -> typing.Tuple[bool, 'Array']:
        return self.video_capture.read()

    def release(self):
        self.video_capture.release()
        log.warning('Camera is released')

    def display(self):
        cv2.imshow(f'Camera {self.camera_number}', self.read()[1])
        if cv2.waitKey(0):
            cv2.destroyAllWindows()
