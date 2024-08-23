class Distance:
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches
    def getData(self):
        return self.feet, self.inches
    def setData(self, feet, inches):
        self.feet = feet
        self.inches = inches
    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches %= 12
        return Distance(total_feet, total_inches)
    def __sub__(self, other):
        total_feet = self.feet - other.feet
        total_inches = self.inches - other.inches
        if total_inches < 0:
            total_feet -= 1
            total_inches += 12
        return Distance(total_feet, total_inches)
distance1 = Distance(3, 9)
distance2 = Distance(2, 6)
distance_sum = distance1 + distance2
print("Sum of distances:", distance_sum.getData())
distance_diff = distance1 - distance2
print("Difference of distances:", distance_diff.getData())
