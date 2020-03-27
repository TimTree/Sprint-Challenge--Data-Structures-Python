from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.current is None or self.current == self.capacity - 1:
                self.current = 0
            else:
                self.current += 1
            #print(self.current.value)
            self.storage.remove_from_tail()
        self.storage.add_to_head(item)
        #print(self.current)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        x = self.storage.tail
        # TODO: Your code here
        if self.current is None:
            while True:
                try:
                    list_buffer_contents.append(x.value)
                    x = x.prev
                except AttributeError:
                    break
        else:
            x = self.storage.head
            y = self.current
            while y >= 0:
                try:
                    list_buffer_contents.insert(0, x.value)
                    x = x.next
                    y -= 1
                except AttributeError:
                    break
            x = self.storage.tail
            while len(list_buffer_contents) < self.storage.length:
                list_buffer_contents.append(x.value)
                x = x.prev
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
