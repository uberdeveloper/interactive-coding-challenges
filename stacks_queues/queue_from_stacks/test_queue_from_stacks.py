import unittest


class TestQueueFromStacks(unittest.TestCase):
    def test_queue_from_stacks(self):
        print("Test: Dequeue on empty stack")
        queue = QueueFromStacks()
        self.assertEqual(queue.dequeue(), None)

        print("Test: Enqueue on empty stack")
        print("Test: Enqueue on non-empty stack")
        print("Test: Multiple enqueue in a row")
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        print("Test: Dequeue on non-empty stack")
        print("Test: Dequeue after an enqueue")
        self.assertEqual(queue.dequeue(), 0)

        print("Test: Multiple dequeue in a row")
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

        print("Test: Enqueue after a dequeue")
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)

        print("Success: test_queue_from_stacks")


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == "__main__":
    main()
