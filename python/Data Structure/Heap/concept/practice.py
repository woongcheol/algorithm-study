class Heap():
    def __init__(self, value) -> None:
        self.array_list = list()
        self.array_list.append(None)
        self.array_list.append(value)

    def move_up(self, current_idx):
        parent_idx = current_idx // 2
        if parent_idx == 0:
            return
        elif self.array_list[current_idx] < self.array_list[parent_idx]:
            self.array_list[current_idx], self.array_list[parent_idx] = self.array_list[parent_idx], self.array_list[current_idx]
            current_idx = parent_idx
            self.move_up(current_idx)

    def move_down(self, poped_idx):
        if poped_idx >= len(self.array_list):
            return
        
        # 자식 노드 변수 선언
        left = poped_idx * 2
        right = poped_idx * 2 + 1

        # 자식 노드가 모두 없을 경우
        if left >= len(self.array_list):
            return

        # 자식 노드가 좌측에만 있을 경우
        elif right >= len(self.array_list):
            if self.array_list[left] < self.array_list[poped_idx]:
                self.array_list[left], self.array_list[poped_idx] = self.array_list[poped_idx], self.array_list[left]
                poped_idx = left
                self.move_down(poped_idx)
            else:
                return

        # 자식 노드가 모두 있을 경우
        elif right <= len(self.array_list):
            if self.array_list[left] < self.array_list[right]:
                if self.array_list[left] < self.array_list[poped_idx]:
                    self.array_list[left], self.array_list[poped_idx] = self.array_list[poped_idx], self.array_list[left]
                    poped_idx = left
                    self.move_down(poped_idx)
                else:
                    return
            if self.array_list[left] > self.array_list[right]:
                if self.array_list[right] < self.array_list[poped_idx]:
                    self.array_list[right], self.array_list[poped_idx] = self.array_list[poped_idx], self.array_list[right]
                    poped_idx = right
                    self.move_down(poped_idx)
                else:
                    return


    def pop(self):
        retruned_data = self.array_list[1]
        self.array_list[1] = self.array_list[-1]
        del self.array_list[-1]
        poped_idx = 1
        self.move_down(poped_idx)
        print(retruned_data)
        return

    def insert(self, value):
        # Defensive programming
        if len(self.array_list) == 0:
            self.array_list = list()
            self.array_list.append(None)
            self.array_list.append(value)
            return
        
        # 데이터 삽입
        self.array_list.append(value)

        # 데이터 이동
        current_idx = len(self.array_list) - 1
        self.move_up(current_idx)

heap = Heap(5)
heap.insert(4)
heap.insert(3)
heap.insert(1)
heap.insert(2)
heap.insert(0)
print(heap.array_list)
heap.pop()
heap.pop()
heap.pop()
heap.pop()
print(heap.array_list)