"""Some unit tests."""

import unittest
import datetime
from date2coord import mkdate, timedelta_to_coord


class TestDate2Coord(unittest.TestCase):

    """Testing Date2Coord functions."""

    def setUp(self):
        """Setting up the class."""
        self.known_values = [('2005-01-01', 600),
                             ('2006-01-01', 4200),
                             ('2007-01-01', 7800),
                             ('2008-01-01', 11400),
                             ('2009-01-01', 15000),
                             ('2010-01-01', 18600),
                             ('2011-01-01', 22200),
                             ('2012-01-01', 25800),
                             ('2013-01-01', 29400),
                             ('2014-01-01', 33000)]

    def test_mkdate(self):
        """Testing mkdate()."""
        value = self.known_values[0][0]
        expected_result = datetime.date(2005, 01, 01)
        self.assertEqual(mkdate(value), expected_result)

    def test_timedelta_to_coord(self):
        """Testing timedelta_to_coord()."""
        for date, expected_result in self.known_values:
            result = timedelta_to_coord(mkdate(date))
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
