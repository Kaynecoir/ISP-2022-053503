from Fabr_Ser import Fabric
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-w', '--write', metavar="FILE", default='file', help="write in file")
parser.add_argument('-r', '--read', metavar="FILE", default='file', help="read file")
parser.add_argument("-t", "--type", default="json", help="type of file")
args = parser.parse_args()


f = Fabric()
f.creat_serialiser(args.type)

a1 = {"1": 12, "23": 34, "43": 123}
a2 = [None, None]
a3 = ["asd", "hgtj", "gh"]
a4 = list(range(3))
a5 = True
a6 = {"cv": 34, "o": {0: {"5": []}}, "00": a1}
a7 = [{}, {"a": 4.5}]
a = {"a": a1, "B": a2, 3: a3, "four": a4, "v": a5, "6": a6, "sin": a7}

f.dump(a, args.write)
print(f.load(args.read))