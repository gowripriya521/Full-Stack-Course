products=[
    {"id":1,"name":"samsung","price":45000},
    {"id":2,"name":"vivo","price":50000},
    {"id":3,"name":"iphone","price":70000},
    {"id":4,"name":"oopo","price":55000},
    {"id":5,"name":"oneplus","price":60000}
]

cart={}
def add_cart(data):
    email=data.get("email")
    product_id=data.get("product_id")
    quantity=data.get("quantity")
    product_name=data.get("product_name")
    if not email or not product_id or not quantity or not product_name:
        return None
    for product in products:
        if product["id"]==product_id:
            if email not in cart:
                cart[email]=[]
            cart[email].append({
                "product_id":product_id,
                "quantity":quantity,
                "product_name":product_name
            })
            return cart[email]
    return None


def get_products():
    return products


def cal_total(email):
    total_amount=0
    total_products=0
    if email not in cart:
        return None
    for item in cart[email]:
        for product in products:
            if product["id"]==item["product_id"]:
                total_amount=(product["price"]*item["quantity"])
                total_products=total_products+item["quantity"]
    return {
        "email":email,
        "total_amount":total_amount,
        "total_products":total_products
    }

def check_out(email):
    if email not in cart:
        return None
    total=cal_total(email)
    del cart[email]
    return total

