#!/usr/bin/pyhton3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        dictionary_2 = {key: value}
        a_dictionary.update(dictionary_2)
        return (a_dictionary)
    else:
        return (None)
