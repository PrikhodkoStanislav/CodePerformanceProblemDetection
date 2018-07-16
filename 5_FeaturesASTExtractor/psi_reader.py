import io
import json
from collections import *

filename = "Application.kt.json"

f = open(filename, 'r')
nodes = f.read()
f.close()
a = json.loads(nodes)
print(a)

def bfs(a):
    for node in a:
        if 'children' in node:
            print(node)
            bfs(node['children'])

def childrenNumber(a):
    result = 0
    for node in a:
        if 'children' in node:
            result += childrenNumber(node['children'])
        else:
            result += 1
    return result

def nodeNumber(a):
    result = 0
    for node in a:
        result += 1
        if 'children' in node:
            result += nodeNumber(node['children'])
    return result

def successorNumber(node):
    result = 0
    if 'children' in node:
        result = len(node['children'])
    return result

# def numberNodesWithSingleSuccessor(a):
#     result = 0
#     for node in a:
#         if successorNumber(node) == 1:
#             result += 1
#         if 'children' in node:
#             result += numberNodesWithSingleSuccessor(node['children'])
#     return result
#
# def numberNodesWithTwoSuccessors(a):
#     result = 0
#     for node in a:
#         if successorNumber(node) == 2:
#             result += 1
#         if 'children' in node:
#             result += numberNodesWithTwoSuccessors(node['children'])
#     return result
#
# def numberNodesWithMoreThenTwoSuccessors(a):
#     result = 0
#     for node in a:
#         if successorNumber(node) > 2:
#             result += 1
#         if 'children' in node:
#             result += numberNodesWithMoreThenTwoSuccessors(node['children'])
#     return result

# print(numberNodesWithSingleSuccessor(a))
# print(numberNodesWithTwoSuccessors(a))
# print(numberNodesWithMoreThenTwoSuccessors(a))

def treeMap(tree, func):
    result = 0
    for node in tree:
        if func(node):
            result += 1
        if 'children' in node:
            result += treeMap(node['children'], func)
    return result

def treeReduce(tree, func):
    result = 0
    def treeReduceRecursive(tree, func, depth):
        result = 0
        for node in tree:
            if func(node, depth):
                result += 1
            if 'children' in node:
                result += treeReduceRecursive(node['children'], func, depth + 1)
        return result
    return treeReduceRecursive(tree, func, 0)

print(childrenNumber(a))
print(nodeNumber(a))

print(treeMap(a, lambda node: successorNumber(node) == 1))
print(treeMap(a, lambda node: successorNumber(node) == 2))
print(treeMap(a, lambda node: successorNumber(node) > 2))

print(treeReduce(a, lambda _, depth: depth == 1))
print(treeReduce(a, lambda _, depth: depth == 2))
print(treeReduce(a, lambda _, depth: depth > 2))

print(treeReduce(a, lambda node, depth: successorNumber(node) == 1 and depth == 1))
print(treeReduce(a, lambda node, depth: successorNumber(node) == 1 and depth == 2))
print(treeReduce(a, lambda node, depth: successorNumber(node) == 2 and depth == 1))
print(treeReduce(a, lambda node, depth: successorNumber(node) == 2 and depth == 2))
print(treeReduce(a, lambda node, depth: successorNumber(node) > 2 and depth > 2))

# count number of node types and add in dict

def countNodeTypes(a):
    cnt = Counter()
    for node in a:
        cnt[node['type']] += 1
        if 'children' in node:
            cnt += countNodeTypes(node['children'])
    return cnt

print(countNodeTypes(a))