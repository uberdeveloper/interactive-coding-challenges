import unittest


class TestSetOfStacks(unittest.TestCase):
    def test_set_of_stacks(self):
        print("Test: Push on an empty stack")
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print("Test: Push on a non-empty stack")
        stacks.push(5)

        print("Test: Push on a capacity stack to create a new one")
        stacks.push("a")

        print("Test: Pop on a stack to destroy it")
        self.assertEqual(stacks.pop(), "a")

        print("Test: Pop general case")
        self.assertEqual(stacks.pop(), 5)
        self.assertEqual(stacks.pop(), 3)

        print("Test: Pop on no elements")
        self.assertEqual(stacks.pop(), None)

        print("Success: test_set_of_stacks")


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == "__main__":
    main()
