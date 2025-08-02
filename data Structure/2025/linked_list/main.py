from linked import LinkedList

def main():
    ll = LinkedList()

    print("Initial size1: ", len(ll))
    print("Initial size2: ", ll.__len__())
    print("empty: ",ll.empty())
    print("value_at: ",ll.value_at(3))
    print("push_front: ",ll.push_front(2))
    print("pop_front: ",ll.pop_front())
    print("push_back: ",ll.push_back(4))
    print("get_front: ",ll.front())
    print("get_back: ",ll.back())
    print("insert: ",ll.insert(2,5))
    print("erase: ",ll.erase(3))
    print("get_value_n_from_end: ",ll.value_n_from_end(3))
    print("reverse: ",ll.reverse())
    print("remove_value: ",ll.remove_value(3))

if __name__ == "__main__":
    main()