import json
import io

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

print(childrenNumber(a))