import json
import os
import unittest


class TestStringMethods(unittest.TestCase):

    def test_imports(self):
        self.assertNotEqual(len(os.listdir("C://BigDataOnePiece/Images")), 0)

    # def test_image_analysis(self):
    #     # file exists
    #     self.assertTrue(os.path.isfile(const.DATA_FOLDER + "/data_analyzed.json"))
    #
    #     with open(const.DATA_FOLDER + '/data_analyzed.json') as json_file:
    #         json_decoded = json.load(json_file)
    #
    #     # json not empty
    #     self.assertNotEqual(json_decoded, "")
    #
    # def test_favorites(self):
    #     # file exists
    #     self.assertTrue(os.path.isfile(const.DATA_FOLDER + "/data_analyzed_with_favorites.json"))
    #
    #     with open(const.DATA_FOLDER + '/data_analyzed_with_favorites.json') as json_file:
    #         json_decoded = json.load(json_file)
    #
    #     # json not empty
    #     self.assertNotEqual(json_decoded, "")
    #
    # def test_recommended(self):
    #     # file exists
    #     self.assertTrue(os.path.isfile(const.DATA_FOLDER + "/data_recommended.json"))
    #
    #     with open(const.DATA_FOLDER + '/data_recommended.json') as json_file:
    #         json_decoded = json.load(json_file)
    #
    #     # json not empty
    #     self.assertNotEqual(json_decoded, "")


if __name__ == '__main__':
    unittest.main()
