storage = {}


def store(key, geocoder):
    storage[key] = geocoder


def retrieve(key):
    return storage[key]
