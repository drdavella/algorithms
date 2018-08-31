#!/usr/bin/env python3

import csv
from random import randint


def read_graph_file(filename):
    graph = {}

    with open(filename) as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            graph[int(line[0])] = [int(x) for x in line[1:-1]]

    return graph


def find_min_cut(graph):

    while len(graph) > 2:
        v1 = list(graph.keys())[randint(0, len(graph)-1)]
        v2 = graph[v1][0]
        merged = graph[v1] + graph[v2]
        del graph[v1]
        del graph[v2]
        while v1 in merged:
            merged.remove(v1)
        while v2 in merged:
            merged.remove(v2)
        for v in graph:
            if v2 in graph[v]:
                graph[v].remove(v2)
                graph[v].append(v1)
        graph[v1] = merged
