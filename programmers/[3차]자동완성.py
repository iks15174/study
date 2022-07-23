class node:
    
    def __init__(self, val, num = 1):
        self.val = val
        self.child = {}
        self.num = 1
    
    def is_in_child(self, alpha):
        if alpha in self.child:
            return True
        else:
            return False
    def add_child(self, childn):
        self.child[childn.val] = childn
    def increase_num(self):
        self.num += 1
    def get_child(self, alpha):
        return self.child[alpha]
    
def solution(words):
    root = node(0, -1)
    for w in words:
        cur_node = root
        for alphabet in w:
            if cur_node.is_in_child(alphabet):
                cur_node = cur_node.get_child(alphabet)
                cur_node.increase_num()
            else:
                temp = node(alphabet)
                cur_node.add_child(temp)
                cur_node = temp
    answer = 0
    for w in words:
        cur_node = root
        search = 0
        for a in w:
            cur_node = cur_node.get_child(a)
            search += 1
            if cur_node.num == 1:
                break
        answer += search
    return answer
            
                
                