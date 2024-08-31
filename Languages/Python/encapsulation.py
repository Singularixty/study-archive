class Workers:
    def __init__(self, name):
        self.name = name
        self._salary = 25000
        self._currency = "Baht"

worker_1 = Workers("Somsak")
print(worker_1._salary)