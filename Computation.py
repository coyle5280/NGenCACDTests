import unittest
import Computation_Package
import Plane_Object

__author__ = 'coyle'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_within_distance_true(self):
        my_class = Computation_Package

        plane1 = Plane_Object
        plane1.current_long = -65.41584
        plane1.current_lat = -104.48541
        plane1.current_vel = 180

        plane2 = Plane_Object
        plane2.current_long = -70.41584
        plane2.current_lat = -115.48541
        plane2.current_vel = 162

        self.assertTrue(my_class.within_distance(plane1))
        self.assertTrue(my_class.within_distance(plane2))

    def test_within_distance_false(self):
        my_class = Computation_Package
        plane3 = Plane_Object
        plane4 = Plane_Object
        self.assertFalse(my_class.within_distance(plane3))
        self.assertFalse(my_class.within_distance(plane4))

    def test_verify_data_true(self):
        my_class = Computation_Package
        plane5 = Plane_Object
        plane6 = Plane_Object
        self.assertFalse(my_class.verify_data(plane5))
        self.assertFalse(my_class.verify_data(plane6))

    def test_verify_data_false(self):
        my_class = Computation_Package
        plane7 = Plane_Object
        plane8 = Plane_Object
        self.assertFalse(my_class.verify_data(plane7))
        self.assertFalse(my_class.verify_data(plane8))

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
