def celsius_to_fahrenheit(c):
    """摂氏を華氏に変換する"""
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    """華氏を摂氏に変換する"""
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    """摂氏をケルビンに変換する"""
    return c + 273.15

def kelvin_to_celsius(k):
    """ケルビンを摂氏に変換する"""
    return k - 273.15

def fahrenheit_to_kelvin(f):
    """華氏をケルビンに変換する"""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    """ケルビンを華氏に変換する"""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))
