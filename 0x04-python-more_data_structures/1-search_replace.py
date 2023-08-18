#!/usr/bin/python3
def search_replace(my_list, search, replace):

    def searchs(num):
        return num if search != num else replace
    return list(map(lambda a: searchs(a), my_list))
