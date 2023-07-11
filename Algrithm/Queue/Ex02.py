from queue import Queue

def my_len(data):
    count=0
    while not data.empty():
        data.get()
        count += 1
    return count

def my_sum(data):
    hap=0
    while not data.empty():
       hap=hap +data.get()
    return hap

def my_max(data):
    max_value=data.get()

    while not data.empty():
        item=data.get()
        if item > max_value:
            max_value=item
    return max_value

if __name__ == "__main__":
    queue=Queue()
    queue.put(66)                                                   
    queue.put(77)
    queue.put(88)
    queue.put(66)                                                   
    queue.put(77)

    # print(my_len(queue))
    # print(my_sum(queue))
    print(my_max(queue))