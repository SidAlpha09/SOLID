'''
O -> Open/Closed Principle (OCP)

Rule: Software entities should be open to extension, closed for modification.
'''

#Problem: Hard-coding behavior that changes often:

def calculateDiscount(order,discountType):
    if discountType=="seasonal":
        return order.total*0.1
    if discountType=="clearance":
        return order.total*0.5

#Every time you add a discount type you modify the function

#Refactor (use polymorphism):
from abc import ABC,abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(me,order):
        pass

class SeasonalDiscount(Discount):
    def apply(me,order):return order.total*0.1

class ClearanceDiscount(Discount):
    def apply(me,order):return order.total*0.5

class Order:
    def __init__(me,total,discount:Discount=None):
        me.total=total
        me.discount=discount

    def discountedTotal(me):
        if me.discount:
            return me.total-me.discount.apply(me)
        return me.total
    
#usage
order=Order(100,SeasonalDiscount())
print(order.discountedTotal())
        