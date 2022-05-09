from Fabr_Ser import Fabric
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-w', '--write', metavar="FILENAME", default='test', help="write in file")
parser.add_argument('-r', '--read', metavar="FILENAME", default='test', help="read file")
parser.add_argument("-t", "--type", default="json", help="type of file", choices=["json", "toml", "yaml"])
parser.add_argument("-s", "--see", action="store_true", help="see data")
args = parser.parse_args()


f = Fabric()
temp = f.load(args.read)
if args.see:
	print(temp)
f.creat_serialiser(args.type)

f.dump(temp, args.write)
