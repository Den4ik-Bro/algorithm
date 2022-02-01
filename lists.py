class ListItem:

    def __init__(self, value):
        self.value = value
        self.next = None


class UniDirectionalList:

    def __init__(self):
        self.head = None
        self.current = None

    def add(self, value):
        """добавление элемента"""
        if self.head == None:
            self.head = ListItem(value)
        else:
            self.current = self.head
            while self.current.next != None:
                self.current = self.current.next
            self.current.next = ListItem(value)

    def list_demo(self):
        """демонстрация списка"""
        if self.head != None:
            self.current = self.head
            while self.current != None:
                print(self.current.value)
                self.current = self.current.next
        else:
            print('Пустой список')

    def del_instance(self, value):
        """Удаление элемента по значению"""
        if self.head == None:
            print('Список пустой')
        else:
            self.current = self.head
            temp = self.current
            while self.current:
                if self.current.value == value and self.current.next == None:
                    self.current = None
                    temp.next = None
                    break
                elif self.current.value == value and self.current.next != None and self.head != self.current:
                    self.current = self.current.next
                    temp.next = self.current
                    break
                elif self.current.value == value and self.current.next != None and self.head == self.current:
                    self.current = self.current.next
                    self.head = self.current
                    break
                temp = self.current
                self.current = self.current.next

    def search(self, value):
        """поиск элемента"""
        if self.head == None:
            print('Список пустой')
        else:
            self.current = self.head
        while True:
            self.current = self.current.next
            if self.current == None:
                return None
            if self.current.value == value:
                return self.current.value

    def buble_party(self):
        """Сортировка пузырьком"""
        if self.head == None:
            print('Список пустой')
        else:
            self.current = self.head
        len = self.len_list()
        count = 0
        while count != len:
            if self.current.next == None:
                self.current = self.head
                count += 1
            elif self.current.value > self.current.next.value:
                self.current.value, self.current.next.value = self.current.next.value, self.current.value
                self.current = self.current.next
                # continue
            elif self.current.value < self.current.next.value:
                self.current = self.current.next
            elif self.current.value == self.current.next.value:
                self.current = self.current.next

    def len_list(self):
        """возвращает длинну списка"""
        if self.head == None:
            return None
        else:
            self.current = self.head
        count = 1
        while self.current.next != None:
            count += 1
            self.current = self.current.next
        return count

x = UniDirectionalList()
x.add(5)
x.add(3)
x.add(2)
x.add(4)
x.add(1)
x.add(10)
x.add(4)
x.add(5)
print('неотсортированный список:')
x.list_demo()
print('отсортированный:')
x.buble_party()
x.list_demo()

