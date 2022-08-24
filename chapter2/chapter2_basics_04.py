def forward_order_status(order):
    if order["status"] == "NEW":
        order["status"] = "IN_PROGRESS"
    elif order["status"] == "IN_PROGRESS":
        order["status"] = "SHIPPED"
    else:
        order["status"] = "DONE"
    return order

