# -*- coding: utf -*-

import json


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_linked_list2(data):
    data = json.loads(data)
    nodes = [TreeNode(val) for val in data]
    print(nodes)
    for i, node in enumerate(nodes):
        left = (i+1) * 2 - 1
        right = (i+1) * 2
        if left < len(nodes) and nodes[left].val is not None:
            node.left = nodes[left]
        if right < len(nodes) and nodes[right].val is not None:
            node.right = nodes[right]
    return nodes[0]


def get_linked_list(data):
    data = json.loads(data)[::-1]
    level = 0
    last_level = []
    current_level = []
    head = None

    while data:
        valid_nodes = len([n for n in last_level if n is not None])
        for i in range(valid_nodes * 2) or range(2**level):
            if not data:
                break
            val = data.pop()
            print('val', val)
            if val is None:
                current_level.append(None)
            else:
                node = TreeNode(val)
                if head is None:
                    head = node
                current_level.append(node)
        current = current_level[::-1]
        for last_node in last_level:
            if last_node is not None:
                if not current:
                    break
                last_node.left = current.pop()
                if not current:
                    break
                last_node.right = current.pop()
        last_level = current_level
        current_level = []
        level += 1
    return head


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
    if set(levels[-1]) != {None}:
        print(levels[-1])

if __name__ == '__main__':
    # head = get_linked_list2('[1,2,2,null,3,null,3]')
    # head = get_linked_list2('[1,2,3,4,5,6,7]')
    head = get_linked_list2('[1,null,2,null,4,null,5]')
    show_graph(head)


