__author__ = 'rezenter'
import sys
import re


test_object = str(sys.argv[1])
print(test_object)
r = re.compile("^(\d\d\.|(\d\.|((([0-1]\d{2})|(2([0-4]\d)|2(5[0-5])))\.))){3}(\d\d|(\d|(([0-1]\d{2})|(2([0-4]\d)|2(5[0-5])))))$")
print(r.match(test_object) is not None)