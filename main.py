class DigitalCounter:
    def __init__(self, begin, end, state=0):
        self.begin = begin
        self.end = end


        if state == 0:
            self.state = self.begin
        else:
            self.state = state


    def up(self):
        self.state += 1
        if self.state == self.end + 1:
            self.state = 0

    def down(self):
        self.state -= 1
        if self.state == -1:
            self.state = self.end

    def get_value(self):
        return self.state


dc_first = DigitalCounter(0, 99999)
for _ in range(1000000):
    dc_first.down()
print(dc_first.get_value())