class Counter:
    value = 0

    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def display(self):
        print('Текущее значение счтчика' + ' = ' + str(self.value))


cl = Counter()
cl.start_from(2)
cl.increment()
cl.display()
cl.increment()
cl.display()
cl.reset()
cl.display()
