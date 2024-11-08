#!/usr/bin/python3

import sys
import argparse
import os
from latenseer.myparser import JSONParser

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-r', '--rps', 
                       help='wrk request per second', type=int)
my_parser.add_argument('-s', '--sample',
                       help='sample one request every s requests', type=str)
my_parser.add_argument('-w', '--workload',
                       help='workload: post, home, user or mix136', type=str)
my_parser.add_argument('-t', '--type',
                       help='type: local or mig_{service}', type=str)
args = my_parser.parse_args()


## Pull traces from jaeger
config_path = '/users/suho/LatenSeer/src/config/config.yml'
jsonparser = JSONParser(config_path)
#traces = jsonparser.pull_traces()
traces = jsonparser.handle_traces('/Users/sumyahoque/LatenSeer/src/compose_review_data/compose-review-default.json')
print(len(traces))

## Convert json traces to csv format
filepath = '/Users/sumyahoque/LatenSeer/src/' \
            + '/rps' + str(args.rps) \
            + '/s' + args.sample \
            + '/' + str(args.workload)
filename = str(args.type) + '.csv'

# Create filepath if not exist
if not os.path.exists(filepath):
    os.makedirs(filepath)

jsonparser.convert_json_to_csv_slack(traces, filepath + '/' + filename)
