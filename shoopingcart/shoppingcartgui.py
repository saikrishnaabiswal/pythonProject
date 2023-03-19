import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

BG_COLOR = "WHITE"
FG_COLOR = "black"

root = tk.Tk()
root.title("Z SHOPPING")
root.geometry("800x800")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

load = Image.open('shp.jpg')
render = ImageTk.PhotoImage(load)
img = tk.Label(root, image=render)
img.place(x=-2, y=-2)

items = [{"name": "Samsung", "mrp": 12000, "image": "samsung.jpg", "category": "Electronics"},
         {"name": "iPhone 15 pro", "mrp": 19000, "image": "samsung.jpg", "category": "Electronics"},
         {"name": "Aloo (potato)", "mrp": 400, "image": "", "category": "Grocery"},
         {"name": "Shirt", "mrp": 3400, "image": "", "category": "Fashion"}]

current_widgets = []             # hold widgets to destroy later
img_fix = []                     # hold image renders otherwise they won't show
cart = []                        # [item(dict), quantity]
valid_coupons = {"DIWALI10": 0.1, "HMM5": 0.05}

categories = list(set([item["category"] for item in items]))
category_images = {"Electronics": "samsung.jpg"}


def find_in_cart(item_name):
    for i in range(len(cart)):
        if cart[i][0]["name"] == item_name:
            return i
    return -1


# add item to cart and update quantity if already present
def buy_now(item_name):
    for item in items:
        if item["name"] == item_name:
            cart_index = find_in_cart(item_name)
            messagebox.showinfo("Added to Cart", f"Added {item_name} to cart")
            if cart_index == -1:
                cart.append([item, 1])
            else:
                cart[cart_index] = [item, cart[cart_index][1] + 1]


# display items in category
def shop_now(category):
    clear()
    category_items = [item for item in items if item["category"] == category]
    title = tk.Label(root, text=category, font=("monospace", 15), bg=BG_COLOR, fg=FG_COLOR)
    title.place(x=230, y=50)
    current_widgets.append(title)

    t = [f'{item["name"]}\nRs. {item["mrp"]}' for item in category_items]
    i = [item["image"] for item in category_items]

    display_cards(t, i, 300, True)

    back_btn = tk.Button(root, text="Main menu", bg="salmon", command=main_menu)
    back_btn.place(x=360, y=600)
    current_widgets.append(back_btn)


# display cards(card = image,text and button)
def display_cards(titles, images, ycor, item=False):
    xcor = 150
    for i in range(len(titles)):
        if not images[i]:
            images[i] = "samsung.jpg"
        load = Image.open(f"img/{images[i]}")
        render = ImageTk.PhotoImage(load)
        img_label = tk.Label(root, image=render)
        img_label.place(x=xcor, y=ycor)

        title_label = tk.Label(root, text=titles[i], font=("monospace", 10), bg=BG_COLOR, fg=FG_COLOR)
        title_label.place(x=xcor, y=ycor + 120)

        if item:
            btn = tk.Button(root, text="Buy Now", bg="violet", activebackground="purple",
                            command=lambda i=i: buy_now(titles[i].split('\n')[0]))
        else:
            btn = tk.Button(root, text="Shop Now", bg="violet", activebackground="purple",
                            command=lambda i=i: shop_now(titles[i]))
        btn.place(x=xcor, y=ycor + 200)

        xcor += 200
        current_widgets.extend([img_label, title_label, btn])
        img_fix.append(render)


def main_menu():
    clear()
    title = tk.Label(root, text="Welcome to DASH Shopping", font=("monospace", 15), bg=BG_COLOR, fg=FG_COLOR)
    title.place(x=230, y=50)
    current_widgets.append(title)

    i = [category_images[category] if category in category_images else "" for category in categories]
    display_cards(categories, i, 300)

    bill_btn = tk.Button(root, text="Bill", bg="white", activebackground="violet", borderwidth=0, command=billing)
    bill_btn.place(x=360, y=600)
    current_widgets.append(bill_btn)


def calc_total():
    total = 0
    for item in cart:
        total += item[0]["mrp"] * item[1]
    return total


def billing():
    clear()

    def apply_coupon():
        nonlocal total
        coupon_code = coupon_entry.get()
        if coupon_code in valid_coupons:
            discount = total*valid_coupons[coupon_code]
            total -= discount

            coupon_entry.configure(state="disabled")
            coupon_btn.configure(state="disabled")

            charges_label.configure(text=f"Subtotal: Rs. {sub_total}\nDelivery: Rs. {delivery}\nTax: Rs. {tax}\nDiscount: Rs. {discount} \nTotal: Rs. {total}")
            messagebox.showinfo("Coupon Applied", f"Discount of {valid_coupons[coupon_code] * 100}% applied")

        else:
            messagebox.showerror("Invalid Coupon", "Try DIWALI10 or HMM5")

    def checkout():
        messagebox.showinfo("Checkout", f"Total: Rs. {total}\nThank you for shopping with us")
        cart.clear()
        main_menu()

    if not cart:
        title = tk.Label(root, text="There are no items in your cart\nAdd some and come back", font=("monospace", 15),
                         bg=BG_COLOR, fg=FG_COLOR)
        title.place(x=180, y=300)
        current_widgets.append(title)

    else:
        # itemized bill
        item_price_list = ""
        for item in cart:
            item_price_list += f"{item[0]['name']} ({item[1]}X) - Rs. {item[0]['mrp'] * item[1]}\n"

        item_list_label = tk.Label(root, text=item_price_list, font=("monospace", 12), bg=BG_COLOR, fg=FG_COLOR)
        item_list_label.place(x=160, y=100)

        # discounts/taxes/delivery charges
        sub_total = total = calc_total()
        delivery = 50 if total < 500 else 0
        total += delivery
        tax = 0.13 * total
        total += tax
        charges_label = tk.Label(root, text=f"Subtotal: Rs. {sub_total}\nDelivery: Rs. {delivery}\nTax: Rs. {tax}\nTotal: Rs. {total}", font=("monospace", 13), bg=BG_COLOR, fg=FG_COLOR, justify="left")
        charges_label.place(x=160, y=300)

        # coupons
        coupon_label = tk.Label(root, text="Coupon :", font=("monospace", 15), bg=BG_COLOR, fg=FG_COLOR)
        coupon_label.place(x=150, y=500)
        coupon_entry = tk.Entry(root)
        coupon_entry.place(x=350, y=500)
        coupon_btn = tk.Button(root, text="Apply", bg="violet", activebackground="purple", command=apply_coupon)
        coupon_btn.place(x=500, y=500)

        # checkout
        proceed_btn = tk.Button(root, text="Proceed", bg="violet", activebackground="purple", command=checkout)
        proceed_btn.place(x=360, y=590)
        current_widgets.extend([coupon_label, coupon_entry, item_list_label, proceed_btn, coupon_btn, charges_label])

    back_btn = tk.Button(root, text="Main menu", command=main_menu)
    back_btn.place(x=360, y=680)
    current_widgets.append(back_btn)


# remove all active widgets
def clear():
    for widget in current_widgets:
        widget.destroy()


def quit():
    if messagebox.askokcancel("Quit", "sure?"):
        root.destroy()


main_menu()
root.mainloop()
