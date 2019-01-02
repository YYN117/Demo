class jishuqi():
    def __init__(self,start = 0):
        self.count = 0
    def increment(self):
        self.count += 1
        if self.count>9:
            self.count = 0
        return self.count
    def reset(self,value=0):
        current_value = self.count
        if 0<value<9:
            self.count = value
        else:
            raise ValueError('ERROR')
        print(current_value)

