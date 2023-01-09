from dataclasses import dataclass

import cv2

from numpy.core._multiarray_umath import ndarray


@dataclass
class Viewer:
    """
    View renders frames.
    """

    def display(self, frame: ndarray, title: str = 'Viewer'):
        return cv2.imshow(title, frame)
