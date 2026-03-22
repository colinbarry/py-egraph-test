from union_find import UnionFind


class EGraph:
    def __init__(self):
        self._union_find = UnionFind()
        # hashcons is mapping between hashes and class-ids
        self._hashcons = {}

    def add(self, node):
        children_class_ids = [self.add(child) for child in node.children()]
        key = node.key(children_class_ids)

        if key in self._hashcons:
            return self._union_find.find(self._hashcons[key])
        else:
            class_id = self._hashcons[key] = self._union_find.make_set()
            return class_id

    def merge(self, id1, id2):
        return self._union_find.merge(id1, id2)

    def find(self, id):
        return self._union_find.find(id)


