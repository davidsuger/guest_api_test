import time, sys
import os
import unittest
import HtmlTestRunner
from db_fixture import test_data

test_dir = os.path.join(os.getcwd(), 'tests')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py', top_level_dir=None)
print(discover)

if __name__ == '__main__':
    test_data.init_data()

    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = './report/' + now + '_result.html'
    # fp = open(filename, 'wb')

    runner = HtmlTestRunner.HTMLTestRunner(output='example_dir')
    runner.run(discover)
    # fp.close()
