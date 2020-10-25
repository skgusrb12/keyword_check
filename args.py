import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--script_list', type=str, help='path for total downloaded data',
                    default='./script_list')
parser.add_argument('--save_path', type=str, help='path for total downloaded data',
                    default='./save_list/keyword')
parser.add_argument('--destination_path', type=str, help='path for total downloaded data',
                    default='./save_list/original')
parser.add_argument('--max_count', type=int, help='the number of keyword count',
                    default=40)

args = parser.parse_args()
SCRIPT_LIST = args.script_list
DOWNLOAD_LIST = args.save_path
COPY_LIST = args.destination_path

MAX_COUNT = args.max_count
