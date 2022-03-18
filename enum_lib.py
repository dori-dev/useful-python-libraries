"""enum library
"""
import enum as en


# ValueError: duplicate values found in <enum 'Days' >: WWW -> WEN
# @en.unique  # decorator for unique values
class Days(en.Enum):
    """Week Days"""
    # DAY = en.auto()  # set unique and auto value
    MON = 0
    SUN = 1
    TUE = 2
    WEN = 3
    THE = 4
    FRI = 5
    SAT = 6
    WWW = 3
    # SAT = 10  TypeError: Attempted to reuse key: 'SAT'


class IntDay(en.IntEnum):
    MON = 0
    SUN = 1
    TUE = 2
    WEN = 3
    THE = 4
    FRI = 5
    SAT = 6


# Use variables
print(Days.WEN.name)  # WEN
print(Days.WEN.value)  # 3
print(repr(Days.FRI))  # <Days.FRI: 5>
print(type(Days.SUN))  # <enum 'Days'>
print(isinstance(Days.SUN, Days))  # True
print(Days(4))  # Days.THE
print(Days.SUN == Days.MON)  # False
# TypeError: '>' not supported between instances of 'Days' and 'Days'
# print(Days.FRI > Days.WEN)
print(IntDay.FRI > IntDay.WEN)  # True

# Loop
print("All days")
for day in Days:
    print(f'{day.name}: {day.value}')


# Variables Features
# Days.WEN = 5  AttributeError: Cannot reassign members.
print(id(Days.WWW) == id(Days.WEN))  # True
print(Days.WWW is Days.WEN)  # True

# Ordered Mapping
for day, val in Days.__members__.items():
    print(day, val.value)
