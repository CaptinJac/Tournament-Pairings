class player:
    record = []

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def update_record(self, result):
        self.record.append(result)
        