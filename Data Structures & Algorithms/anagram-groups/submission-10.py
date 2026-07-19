class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord('z') - ord(c)] += 1
            
            if tuple(count) not in res:
                res[tuple(count)] = []
            
            res[tuple(count)].append(s)
        
        return list(res.values())





















#"We're building the backend for a warehouse inventory system. In-memory, single-threaded. Start with:

# add_product(product_id, quantity) — adds stock. If the product is new, creates it;
#  if it exists, adds to its existing quantity. Always returns the product's new total quantity.

# order(order_id, product_id, quantity) — a customer orders. 
# Succeeds only if the product exists and has enough stock; on success, deducts the stock and returns True. 
# Fails (returns False) if the product doesn't exist, stock is insufficient, 
# or the order_id was already used — order IDs are globally unique, even across failed... no, 
# correction: only successful orders consume an order_id.

# get_quantity(product_id) — current stock, or None if the product doesn't exist.

# cancel_order(order_id) — cancels a previously successful order: 
# restores the stock to the product and frees nothing else
# — but the order_id stays consumed forever (no reuse after cancellation). 
# Returns True, or False if the order_id doesn't exist or was already cancelled.

# get_top_products(n) — the top n products by total quantity successfully ordered 
# (cancelled orders still count toward this — ops wants gross demand, not net). Format "product_id(total_ordered)", 
# highest first, ties by product_id ascending. 
# Products never ordered count as 0 and are included. Fewer than n products → return all."

# products = {} # {product_id : quantity}
# orders = {} # {order_id : quantity}

# def add_product(product_id, quantity):

#     if product_id in products:
#         products[product_id] += quantity
#     else:
#         products[product_id] = quantity
#     return products[product_id]

# def order(order_id, product_id, quantity):

#     if product_id not in products or order_id in orders:
#         return False
    
#     stock = products[product_id]
#     remaining = stock - quantity

#     if remaining < 0:
#         return False
    
#     orders[order_id] = (product_id, quantity, False)
#     products[product_id] = remaining
#     return True

# def get_quantity(product_id):

#     if product_id not in products:
#         return None
    
#     return products[product_id]

# def cancel_order(order_id):

#     if order_id not in orders and orders[order_id][2] == True:
#         return False
    
#     # extract the quantity from the order
#     quantity_ordered = orders[order_id][1]

#     # extract product id
#     product_ordered = orders[order_id][0]

#     products[product_ordered] += quantity_ordered
#     orders[order_id][3] == True
#     return True

# def get_top_products(n):

#     top_products = {}
#     for product_id in products:
#         top_products[product_id] = 0
#     for order_id, order_data in orders.items():
#         product_id, quantity, order_status = order_data
#         top_products[product_id] += quantity

    
#     matches = []
#     for product, quantity in top_products.items():
#         matches.append((product, quantity))

        
#     matches.sort(key = lambda x : (-x[1], x[0]))

#     res = []
#     for product, quantity in matches[:n]:
#         res.append(f"{product}({quantity})")
    
#     return res






# # Test cases:

# print(add_product(123, 10)) #10
# print(add_product(345, 15)) #15
# print(add_product(678, 3))  #3
# print(add_product(678, 10))  #13

# print(order(1, 123, 4))     #6
# print(order(1, 345, 4))     # False (order_id exists already)
# print(order(2, 123, 7))     # False (out of stock)
# print(order(3, 345, 20))    # False (not enough quantitity)
# print(order(4, 678, 3))     # True 
# print(order(5, 990, 7))     # False (product doesnt exist)
# print(order(2, 345, 5))     # True


# print(get_quantity(123))    # 6
# print(get_quantity(345))    # 4
# print(get_quantity(678))    # 10
# print(get_quantity(990))    # None

# print(get_top_orders(2))

