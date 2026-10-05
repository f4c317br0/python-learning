class TelepathicDictionary(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        return f"Телепатически угадано: {key}"

    def __setitem__(self, key, value):
        print(f"Телепатически записано: {key} = {value}")
        super().__setitem__(key, value)

    def recall(self):
        for key in sorted(self):
            print(f"{key}: {self[key]}")

    def __add__(self, other):
        result = TelepathicDictionary()
        for key, value in other.items():
            result[key] = value
        for key, value in self.items():
            result[key] = value
        return result
