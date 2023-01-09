import logging
import os
from dataclasses import dataclass
import cv2
from numpy.core._multiarray_umath import ndarray

log = logging.getLogger(__name__)


@dataclass
class Mask:
    """
    Masks to hide behind
    """

    @property
    def cascade_classifier(self) -> cv2.CascadeClassifier:
        try:
            project_root = os.environ['project_root']
        except KeyError:
            log.warning('Did you not source environment?')
            exit(-1)
        else:
            path = os.path.join(project_root, 'haarcascade_eye_tree_eyeglasses.xml')
            return cv2.CascadeClassifier(path)

    def detect(self, frame):
        a = self.cascade_classifier.detectMultiScale(frame)
        return a




