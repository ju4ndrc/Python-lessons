class Counter:
    count = 0 

    @classmethod
    def increment(cls):
        cls.count = cls.count + 1

    

Counter.increment()

print(Counter.count)
