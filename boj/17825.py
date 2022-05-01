from collections import deque

start_node = None
finish_node = None


class node:
    def __init__(self, score):
        self.score = score
        self.next_blue = None
        self.next_red = None

    def add_red_node(self, red_node):
        self.next_red = red_node

    def add_blue_node(self, blue_node):
        self.next_blue = blue_node

    def find_node_by_score(self, score):
        if self.score == score:
            return self
        else:
            return self.next_red.find_node_by_score(score)


def make_board():
    global start_node, finish_node
    start_node = node(-1)
    finish_node = node(0)
    cur_node = start_node
    for i in range(1, 21):
        new_node = node(i * 2)
        cur_node.add_red_node(new_node)
        cur_node = new_node
    cur_node.add_red_node(finish_node)

    node25 = node(25)
    # 가운데의 왼쪽 부분을 만든다.
    node10 = start_node.find_node_by_score(10)
    node13 = node(13)
    node16 = node(16)
    node19 = node(19)
    node10.add_blue_node(node13)
    node13.add_red_node(node16)
    node16.add_red_node(node19)
    node19.add_red_node(node25)

    # 가운데 아래쪽을 만든다.
    node20 = start_node.find_node_by_score(20)
    node22 = node(22)
    node24 = node(24)
    node20.add_blue_node(node22)
    node22.add_red_node(node24)
    node24.add_red_node(node25)

    # 가운데 오른쪽을 만든다.
    node30 = start_node.find_node_by_score(30)
    node28 = node(28)
    node27 = node(27)
    node26 = node(26)
    node30.add_blue_node(node28)
    node28.add_red_node(node27)
    node27.add_red_node(node26)
    node26.add_red_node(node25)

    # 가운데 위쪽을 만든다.
    node40 = start_node.find_node_by_score(40)
    node30 = node(30)
    node35 = node(35)
    node25.add_red_node(node30)
    node30.add_red_node(node35)
    node35.add_red_node(node40)


def print_node(parent_score, node):
    print(parent_score, node.score)
    if node.next_blue:
        print_node(node.score, node.next_blue)
    if node.next_red:
        print_node(node.score, node.next_red)


# print_node(0, start_node)
make_board()
dices = deque(list(map(int, input().split())))
max_score = -1
dice_position = {0: start_node, 1: start_node, 2: start_node, 3: start_node}


def move(pos, step):
    global dice_position
    if pos.next_blue:
        pos = pos.next_blue
    else:
        pos = pos.next_red
    step -= 1
    while step > 0:
        if pos.score == 0:
            break
        pos = pos.next_red
        step -= 1
    is_possible = True
    for key, items in dice_position.items():
        if items == pos and pos.score != 0:
            is_possible = False
    return (is_possible, pos, pos.score)


def solve(cur_score, depth):
    global max_score, dice_position, dices
    if depth == 10:
        # if max_score < cur_score:
        #     for k, i in dice_position.items():
        #         print(k, i.score)
        max_score = max(max_score, cur_score)
        return

    cur_dice = dices.popleft()
    for i in range(4):
        if dice_position[i].score == 0:
            continue
        prev_pos = dice_position[i]
        possible, new_pos, score = move(prev_pos, cur_dice)
        if possible:
            dice_position[i] = new_pos
            solve(cur_score + score, depth + 1)
        dice_position[i] = prev_pos
    dices.appendleft(cur_dice)


solve(0, 0)
print(max_score)
