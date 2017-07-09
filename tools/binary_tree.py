# -*- coding: utf -*-

import json


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_linked_list(data):
    data = json.loads(data)
    nodes = [TreeNode(val) for val in data]
    for i, node in enumerate(nodes):
        left = (i+1) * 2 - 1
        right = (i+1) * 2
        if left < len(nodes) and nodes[left].val is not None:
            node.left = nodes[left]
        if right < len(nodes) and nodes[right].val is not None:
            node.right = nodes[right]
    return nodes[0]


def pre_order(root, level, res):
    if len(res) < level + 1:
        res.append([])
    if not root:
        res[level].append(None)
        return
    res[level].append(root.val)
    pre_order(root.left, level+1, res)
    pre_order(root.right, level+1, res)
    return res


def show_graph(node):
    levels = pre_order(node, 0, [])
    for item in levels[:-1]:
        print(item)
    if len(set(levels[-1])) != 1:
        print(levels[-1])

if __name__ == '__main__':
    head = get_linked_list('[1,2,2,null,3,null,3]')
    show_graph(head)


