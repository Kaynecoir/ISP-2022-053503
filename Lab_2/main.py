from Fabr_Ser import Fabric

f = Fabric()

a1 = {"1": 12, "23": 34, "43": 123}
a2 = [None, None]
a3 = ["asd", "hgtj", "gh"]
a4 = list(range(3))
a5 = True
a6 = {"cv": 34, "o": {0: {"5": []}}, "00": a1}
a7 = [{}, {"a": 4.5}]
a = {"a": a1, "B": a2, 3: a3, "four": a4, "v": a5, "6": a6, "sin": a7}

f.dump(a, "file")