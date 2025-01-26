class Singleton_Pattern:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton_Pattern, cls).__new__(cls)
        return cls._instance
    
singleton_pattern_1 = Singleton_Pattern()
singleton_pattern_2 = Singleton_Pattern()
print(singleton_pattern_1)
print(singleton_pattern_2)
print(singleton_pattern_1 is singleton_pattern_2)

