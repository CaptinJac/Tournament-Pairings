class player:
    record = []

    def __init__(self, name):
        self.name = name
    
    def update_record(self, result):
        self.record.append(result)
        