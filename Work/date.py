# date.py

# Class methods are most often used as a tool for
# defining alernate constructors.

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        import time
        # Notice how the class is passed as an argument
        tm = time.localtime()
        # Abd used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
    def __repr__(self):
        return f'Date({self.year}-{self.month}-{self.day})'
    

class NewDate(Date):
    pass
    
