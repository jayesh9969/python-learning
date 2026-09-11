import numpy as np

# prices = np.array([100, 250, 80, 500]) * 1.18

# #gst = prices * 1.18
# #gst = prices + prices * 0.18
# print(prices)


items = ["chai", "pizza", "auto", "recharge", "sabzi"]
amounts = np.array([20, 450, 80, 239, 120])
position = amounts.argmax()

print(f"Most expensive: {items[position]} - Rs {amounts[position]}")


above100 = amounts[amounts > 100]
print(f"list of expenses above Rs 100 are {above100}\nthere are {len(above100)} expenses above Rs 100")

   


