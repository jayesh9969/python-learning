

delivery_info = """Hamari dukaan subah 9 baje khulti hai aur raat 9 baje band hoti hai. Order cancel
karne par paisa 7 din mein wapas mil jaata hai. Lekin agar order bhej diya gaya hai
to refund nahi milega, sirf exchange hoga. Delivery Mumbai mein free hai, baaki
shehron mein 50 rupaye lagte hain."""

size = 120
overlap = 30

for i in range(0, len(delivery_info), size - overlap):
    chunk = delivery_info[i:i+size]

    if len(chunk) > 40:

        print(chunk)



