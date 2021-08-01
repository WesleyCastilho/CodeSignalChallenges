import unittest

from arrays.rotate_image.rotate_image import RotateImage


class TestRotateImage(unittest.TestCase):
    def test_rotate_image(self):
        matrix_input = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]

        matrix_output = [[7, 4, 1],
                         [8, 5, 2],
                         [9, 6, 3]]

        response = RotateImage.rotate_image(matrix_input)
        self.assertEqual(matrix_output, response)
