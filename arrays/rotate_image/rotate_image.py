class RotateImage:
    def rotate_image(self):
        return [list(reversed(x)) for x in zip(*self)]