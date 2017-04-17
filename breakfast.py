"""Breakfast"""

def breakfast(food, extras=None):
    print("mix ingredents")
    print("Put pan on stove")
    print("turn on the fire")
    print("wait for pan to heat up")
    print("Add oil")
    print("Add" + food +" into pan")
    if extras:
        assert(isinstance(extras, list))
        extras = "with "+",".join(extras)
    print("Flip %s over" % food)
    breakfast = "----%s ready %s----" % (food, extras or "")
    return(breakfast)

print(breakfast("egg"))
print(breakfast("pancake"))
print(breakfast("egg", extras=["tomatoes"]))
