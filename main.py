class DigitalCounter:
    def __init__(self, begin, end, state=0):
        self.begin = begin
        self.end = end
        self.last_operation = None
        if state == 0:
            self.state = self.begin
        else:
            self.state = state

    def up(self):
        self.state += 1
        self.last_operation = True
        if self.state == self.end + 1:
            self.state = 0

    def down(self):
        self.state -= 1
        self.last_operation = False
        if self.state == -1:
            self.state = self.end

    def is_last_operation_up(self):
        if not self.last_operation:
            return False
        elif self.last_operation:
            return True

    def get_value(self):
        return self.state


dc_first = DigitalCounter(0, 99999)
for _ in range(1000000):
    dc_first.up()
print(dc_first.get_value())
print(dc_first.is_last_operation_up())
