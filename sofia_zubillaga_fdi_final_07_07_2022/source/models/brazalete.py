class Brazalete:
    def __init__(self, date, dna, blod_sugar_level, emotion_level):
        self.date = date
        self.dna = dna
        self.blod_sugar_level = blod_sugar_level
        self.emotion_level = emotion_level

    def serialize(self):
        return {
            'date': self.date,
            'dna': self.dna,
            'blod_sugar_level': self.blod_sugar_level,
            'emotion_level': self.emotion_level
        }







