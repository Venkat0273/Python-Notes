# -*- coding: utf-8 -*-
__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


def collection_list() -> None:
    a = [i for i in range(10)]
    print(a)
    print(a[1])
    print(a[:3])
    print(a[3:])
    print(a[::-1])
    print(reversed(a))
    a[0] = 11
    print(a[0])
    a[0:3] = [10, 11, 12]
    print(a)
    a.append(23)
    a.extend([12, 23, 34])
    print(a)
    a.append([23, 234, 2343])
    print(a)


# collection_list()

def collection_str():
    a = "venkat"
    print(a)
    print(a[0])
    print(a[-1])
    print(a[0:3])
    print(a[:5])
    print(a[2:])
    print(a[::-1])
    print(a)


# collection_str()

def collection_tuple():
    ip_addrs = ("0.0.0.0", "100")
    one_member = ("venkat",)
    print(one_member)


# collection_tuple()

def collection_dict():
    info = {
        "name": "venkat",
        "age": 27,
        "sex": "M",
        "place": "rct",
    }
    print(type(info))
    print(isinstance(info, dict))
    print(info["name"])
    print(info.get("name"))
    for key in info.keys():
        print(info[key])


# collection_dict()

def collection_set():
    values = {1, 2, 3, 4, 5}
    print(type(values))
    print(isinstance(values, set))
    for value in values:
        print(value)


# collection_set()


def collection_default_dict():
    from collections import defaultdict

    names = defaultdict(lambda: "venkat")

    names["one"] = "venky"
    names["two"] = "venkatarami"

    print(names["three"])
    print(names["one"])
    print(names["two"])


collection_default_dict()
