import os.path
import unittest
from json import loads,dumps


from app.errors.error import InvalidRequest
from app.services import processor


def mock(m):
    with open(os.path.dirname(os.path.realpath(__file__)) + "/mocks/{0}.json".format(m)) as mock:
        return mock.read()


class ProcessorTestCase(unittest.TestCase):
    def test_process(self):
        processed_list = processor.process(mock("payload_ok_in"))
        print(mock("payload_ok_out"))
        print(processed_list)
        self.assertEquals(loads(mock("payload_ok_out")), loads(dumps(processed_list)))

    def test_process_400(self):
        with self.assertRaises(InvalidRequest):
            processor.process(mock("payload_400_in"))

    def test_process_400_no_showImage(self):
        with self.assertRaises(InvalidRequest):
            processor.process(mock("payload_400_no_showImage_in"))