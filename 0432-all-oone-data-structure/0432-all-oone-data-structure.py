class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}
        self.count_bucket = {}

    def _add_node_after(self, new_node, prev_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_bucket[node.count]

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1
        curr_bucket = self.count_bucket.get(count)
        next_bucket = self.count_bucket.get(count + 1)

        if not next_bucket:
            next_bucket = Node(count + 1)
            self.count_bucket[count + 1] = next_bucket
            self._add_node_after(next_bucket, curr_bucket if curr_bucket else self.head)

        next_bucket.keys.add(key)

        if curr_bucket:
            curr_bucket.keys.remove(key)
            if not curr_bucket.keys:
                self._remove_node(curr_bucket)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return

        count = self.key_count[key]
        curr_bucket = self.count_bucket[count]
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1
            prev_bucket = self.count_bucket.get(count - 1)
            if not prev_bucket:
                prev_bucket = Node(count - 1)
                self.count_bucket[count - 1] = prev_bucket
                self._add_node_after(prev_bucket, curr_bucket.prev)
            prev_bucket.keys.add(key)

        curr_bucket.keys.remove(key)
        if not curr_bucket.keys:
            self._remove_node(curr_bucket)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""
