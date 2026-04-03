import sys
import os
import unittest

# converter.py を tests/ の親ディレクトリから読み込む
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    fahrenheit_to_kelvin, kelvin_to_fahrenheit,
)

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_freezing(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)

class TestFahrenheitToCelsius(unittest.TestCase):
    def test_freezing(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)

    def test_boiling(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)

    def test_negative(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)

class TestCelsiusToKelvin(unittest.TestCase):
    def test_freezing(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)

    def test_absolute_zero(self):
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0.0)

class TestKelvinToCelsius(unittest.TestCase):
    def test_freezing(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0.0)

    def test_absolute_zero(self):
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

class TestFahrenheitToKelvin(unittest.TestCase):
    def test_freezing(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)

    def test_boiling(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(212), 373.15)

class TestKelvinToFahrenheit(unittest.TestCase):
    def test_freezing(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32.0)

    def test_boiling(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212.0)

if __name__ == "__main__":
    unittest.main()
