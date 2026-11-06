# TASK 5: Functions, default parameters and scope
def add_item_buggy(item, order=[]):
    order.append(item)
    return order
def add_item(item, order=None):
    if order is None: order = []
    order.append(item)
    return order

print("Buggy:", add_item_buggy("Tea"))
print("Buggy:", add_item_buggy("Vada"))
print("Buggy defaults:", add_item_buggy.__defaults__)
print("Correct:", add_item("Tea"))
print("Correct:", add_item("Vada"))
print("Correct:", add_item("Sandwich"))

def bill(price, quantity=1, *, gst_rate=0.05):
    subtotal = price * quantity
    gst = subtotal * gst_rate
    return subtotal + gst, gst
total, gst = bill(100, quantity=2, gst_rate=0.05)
print("Total:", total, "GST:", gst)

count = 0
def update_global():
    global count
    count += 1
def outer():
    message = "before"
    def inner():
        nonlocal message
        message = "after"
    inner()
    return message
update_global()
print("Global count:", count)
print("Nonlocal message:", outer())
