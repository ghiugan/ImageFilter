import unittest
from ImageFilter import *

class TestMethods(unittest.TestCase):

    
    def test_mirror(self):

        # Test Case 1
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
                [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
        
        expected = [[[255, 255, 255], [0, 0, 0], [233, 100, 115]],
                   [[255, 255, 255], [1, 9, 0], [199, 201, 116]]]
        
        self.assertEqual(expected, mirror(input))

        # Test Case 2
        input = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
        
        expected = [[[7, 8, 9], [4, 5, 6], [1, 2, 3]]]
        
        self.assertEqual(expected, mirror(input))

        # Test Case 3
        input = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
        
        expected = [[[7, 8, 9], [4, 5, 6], [1, 2, 3]],
                    [[16, 17, 18], [13, 14, 15], [10, 11, 12]],
                     [[25, 26, 27], [22, 23, 24], [19, 20, 21]]]
        
        # Test Case 4
        input = [[[1,2,3]]]
        expected = [[[1,2,3]]]

        # Test Case 5
        input = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
                 [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]],
                 [[31, 32, 33, 34, 35], [36, 37, 38, 39, 40], [41, 42, 43, 44, 45]]]
        
        expected = [[[11, 12, 13, 14, 15], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]],
                    [[26, 27, 28, 29, 30], [21, 22, 23, 24, 25], [16, 17, 18, 19, 20]],
                    [[41, 42, 43, 44, 45], [36, 37, 38, 39, 40], [31, 32, 33, 34, 35]]]
        

        self.assertEqual(expected, mirror(input))

    def test_grey(self):
        # Test Case 1
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
                   [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
        expected = [[[149, 149, 149], [0, 0, 0], [255, 255, 255]],
                    [[172, 172, 172], [3, 3, 3], [255, 255, 255]]]
        self.assertEqual(expected, grey(input))

        # Test Case 2
        input = [[[1, 2, 3]]]
        expected = [[[2, 2, 2]]]
        self.assertEqual(expected, grey(input))

        # Test Case 3
        input = [[[0, 50, 100], [50, 50, 50]],
                  [[1, 2, 3], [0, 60, 90]],
                  [[27, 72, 83], [123, 1, 3]]]
        expected = [[[50, 50, 50], [50, 50, 50]],
                    [[2, 2, 2], [50, 50, 50]],
                    [[60, 60, 60], [42, 42, 42]]]
        self.assertEqual(expected, grey(input))

    def test_invert(self):
        # Test Case 1
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
                   [[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
        expected = [[[100, 233, 115], [0, 0, 0], [0, 0, 255]],
                    [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
        invert(input)
        self.assertEqual(expected, input)

        # Test Case 2
        input = [[[1, 2, 3]]]
        expected = [[[3, 2, 1]]]
        invert(input)
        self.assertEqual(expected, input)

        # Test Case 3
        input = [[[255, 0, 0], [0, 255, 255]],
                  [[255, 255, 0], [0, 255, 0]],
                  [[0, 255, 255], [255, 0, 255]]]
        expected = [[[0, 255, 255], [255, 0, 0]],
                    [[0, 0, 255], [255, 0, 255]],
                    [[255, 0, 0], [0, 255, 0]]]
        invert(input)
        self.assertEqual(expected, input)

        # Test Case 4
        input = [[[1, 1, 1]]]
        expected = [[[1, 1, 1]]]
        invert(input)
        self.assertEqual(expected, input)

    def test_compress(self):
        # Test Case 1
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]],
                 [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
                 [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
                 [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10]]]
        expected = [[[108, 77, 57], [153, 115, 26]],
                    [[63, 79, 87], [191, 51, 33]]]
        self.assertEqual(expected, compress(input))

        # Test Case 2
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]]]
        expected = [[[116, 50, 57], [129, 130, 3]]]
        self.assertEqual(expected, compress(input))

        # Test Case 3
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
                 [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
                 [[123, 233, 151], [111, 99, 10], [0, 1, 1]]]
        expected = [[[108, 77, 57], [255, 177, 50]],
                    [[117, 166, 80], [0, 1, 1]]]
        self.assertEqual(expected, compress(input))

        # Test Case 4
        input = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7], [1, 1, 1]],
                 [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0], [1, 1, 1]],
                 [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0], [1, 1, 1]],
                 [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10], [1, 1, 1]]]
        expected = [[[108, 77, 57], [153, 115, 26], [1, 1, 1]],
                    [[63, 79, 87], [191, 51, 33], [1, 1, 1]]]
        self.assertEqual(expected, compress(input))

        # Test Case 5
        input = [[[233, 100, 115]]]
        expected = [[[233, 100, 115]]]
        self.assertEqual(expected, compress(input))


def mirror_image_test():
    raw_image = get_raw_image("tree.png")

    mirror(raw_image)

    image_from_raw(raw_image, "mirror.png")

def grey_image_test():
    raw_image = get_raw_image("tree.png")

    grey(raw_image)

    image_from_raw(raw_image, "grey.png")

def invert_image_test():
    raw_image = get_raw_image("tree.png")

    invert(raw_image)

    image_from_raw(raw_image, "invert.png")

def compress_image_test():
    raw_image = get_raw_image("tree.png")

    compress(raw_image)

    image_from_raw(raw_image, "compress.png")

if __name__ == '__main__':
    
    mirror_image_test()
    grey_image_test()
    invert_image_test()
    compress_image_test()

    unittest.main()