#!/bin/bash

input_owl=
output_pkl=
if [ $# -lt 2 ]; then
  echo "Please provide the path to the owl input file and pkl output"
  exit
else
  echo "Input file: $1 Output file: $2"
  input_owl=$1
  output_pkl=$2
fi

python3 aurum-datadiscovery/create_pkl_ontology.py $input_owl $output_pkl