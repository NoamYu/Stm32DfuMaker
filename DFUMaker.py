from BinFile import BinFile
from DFUFileClass import DFUFile
import argparse

DEFAULT_ADDRESS = 0x8000000

class FileAddressPair:    
    def __init__(self, path, address=0x8000000):
        self.path = path
        self.address = int(address)

    def __init__(self, str):
        x = str.split(",", 1)
        if len(x) == 1:
            x.append(DEFAULT_ADDRESS)
        self.path = x[0]
        self.address = int(x[1], base=16)

cmdParser = argparse.ArgumentParser(
    description='Converts a production params bin file to a DFU', prog="DFUMaker")
cmdParser.add_argument(
    '--bin', action='append', nargs=1, type=FileAddressPair, required=True,
    help='Path and address to the bin file that should be converted, can be passed more then once for multiple bin files\n\
    should be passed as --bin[path][address]\n\
    path can be a relative or absolute path\n\
    address should be passed as hex(will defult to {}'.format(hex(DEFAULT_ADDRESS)))
cmdParser.add_argument(
    '--dst', action='store', nargs=1, required=True, help='Path to the DFU file that should be created')

args = cmdParser.parse_args()

productionParamsBin = BinFile(
    args.bin[0][0].path, args.bin[0][0].address)
productionParamsDfu = DFUFile([productionParamsBin])
productionParamsDfu.write_DFU_to_file(args.dst[0])