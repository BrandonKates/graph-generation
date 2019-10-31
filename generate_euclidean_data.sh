#!/bin/bash
mkdir ./data/
python generate_graphs.py --num_graphs 10000 --num_nodes 10 --filename ./data/MST10_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 20 --filename ./data/MST20_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 30 --filename ./data/MST30_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 40 --filename ./data/MST40_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 50 --filename ./data/MST50_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 60 --filename ./data/MST60_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 70 --filename ./data/MST70_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 80 --filename ./data/MST80_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 90 --filename ./data/MST90_10000_Euclidean.txt
python generate_graphs.py --num_graphs 10000 --num_nodes 100 --filename ./data/MST100_10000_Euclidean.txt
