def line(queue):
    if len(queue) < 1: 
        print("The line is currently empty.")
    else:
        line = [f"{i + 1}. {name}" for i, name in enumerate(queue)]
        print(f"The line is currently: {' '.join(line)}")

def take_a_number(queue, name):
    queue.append(name)

    print(f"Welcome, {name}. You are number {queue.index(name) + 1} in line.")

def now_serving(queue):
    if len(queue) < 1: 
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {queue.pop(0)}.")