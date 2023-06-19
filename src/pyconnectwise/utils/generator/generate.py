import sys, getopt
import argparse
from parser import generate

def main(argv):
    parser = argparse.ArgumentParser(description='Generate PyWise Endpoints and Models from ConnectWise Manage OpenAPI Schema', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', help='Input OpenAPI Schema (JSON)', required=True)
    parser.add_argument('-mo', '--modeloutput', help='Model Output Directory', required=True)
    parser.add_argument('-eo', '--endpointoutput', help='Endpoint Output Directory', required=True)
    parser.add_argument('-co', '--clientoutput', help='Client Output Directory', required=True)
    args = parser.parse_args()
    config = vars(args)
    generate(config['i'], config['eo'], config['mo'], config['co'])

if __name__ == "__main__":
    main(sys.argv[1:])