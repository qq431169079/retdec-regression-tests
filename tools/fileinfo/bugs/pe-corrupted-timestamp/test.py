from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='1d77747bf1e810f172b55fd8c3905f2fb5478725eaab95424b5b839dceb617ed'
    )

    def test_has_timestamp(self):
        self.assertEqual(self.fileinfo.output['timestamp'], '2006-10-27 09:17:31')

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='6f5f3bd509c22f0aec4a55fd4d08b7527be4708145b760bc3bd955c6e7538064'
    )

    def test_has_timestamp(self):
        self.assertEqual(self.fileinfo.output['timestamp'], '2017-07-03 23:54:35')
