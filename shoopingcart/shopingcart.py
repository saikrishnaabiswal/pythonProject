import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title('Zwiggy')
root.configure(bg='light blue')
root.geometry("800x800")
root.resizable(False,False)
load=Image.open('shp.jpg')
render = ImageTk.PhotoImage(load)
img = tk.Label(root, image=render)
img.place(x=0,y=0)
items = [{"name": "Samsung", "mrp": 12000, "image": "samsung.jpg", "category": "Electronics"},
         {"name": "I Phone", "mrp": 25000, "image": "iphone.jpg", "category": "Electronics"},
         {"name": "Redmi", "mrp": 19000, "image": "redmi.jpg", "category": "Electronics"},
         {"name": "Aloo (potato)", "mrp": 400, "image": "", "category": "Grocery"},
         {"name": "Shirt", "mrp": 3400, "image": "", "category": "Fashion"}]
current_widgets = []
img_fix = []
cart = []
categories = list(set([item["category"] for item in items]))
category_images = {"Electronics": "samsung.jpg"}
def find_in_cart(item_name):
    for i in range(len(cart)):
        if cart[i][0]["name"] == item_name:
            return i
    return -1
def buy_now(item_name):
    for item in items:
        if item["name"] == item_name:
            cart_index = find_in_cart(item_name)
            messagebox.showinfo("Added to Cart", f"Added {item_name} to cart")
            if cart_index == -1:
                cart.append([item, 1])
            else:
                cart[cart_index] = [item, cart[cart_index][1] + 1]
def shop_now(category):
    clear()
    category_items = [item for item in items if item["category"] == category]
    title = tk.Label(root, text=category, font=("monospace", 15))
    title.place(x=230, y=50)
    current_widgets.append(title)

    t = [f'{item["name"]}\nRs. {item["mrp"]}' for item in category_items]
    i = [item["image"] for item in category_items]

    display_cards(t, i, 300, True)

    back_btn = tk.Button(root, text="Main menu", bg="salmon", command=main_menu)
    back_btn.place(x=360, y=600)
    current_widgets.append(back_btn)
def display_cards(titles, images, ycor, item=False):
    xcor = 150
    for i in range(len(titles)):
        if not images[i]:
            images[i] = "placeholder.jpg"
        load = Image.open(f"img/{images[i]}")
        render = ImageTk.PhotoImage(load)
        img_label = tk.Label(root, image=render)
        img_label.place(x=xcor, y=ycor)

        title_label = tk.Label(root, text=titles[i], font=("monospace", 10),)
        title_label.place(x=xcor, y=ycor + 120)

        if item:
            btn = tk.Button(root, text="Buy Now", bg="violet",activebackground="purple", command=lambda i=i: buy_now(titles[i].split('\n')[0]))
        else:
            btn = tk.Button(root, text="Shop Now", bg="violet",activebackground="purple", command=lambda i=i: shop_now(titles[i]))
        btn.place(x=xcor, y=ycor + 200)

        xcor += 200
        current_widgets.extend([img_label, title_label, btn])
        img_fix.append(render)
def main_menu():
    clear()
    title = tk.Label(root, text="Welcome to DASH Shopping", font=("monospace", 15))
    title.place(x=230, y=50)
    current_widgets.append(title)

    i = [category_images[category] if category in category_images else "" for category in categories]
    display_cards(categories, i, 300)

    bill_btn = tk.Button(root, text="Bill", bg="white",activebackground="violet",borderwidth=0, command=billing)
    bill_btn.place(x=360, y=600)
    current_widgets.append(bill_btn)


def billing():
    clear()
    if not cart:
        title = tk.Label(root, text="There are no items in your cart\nAdd some and come back", font=("monospace", 15)
                         )
        title.place(x=230, y=50)
        current_widgets.append(title)

    else:
        item_price_list = ""
        for item in cart:
            item_price_list += f"{item[0]['name']} ({item[1]}X) - Rs. {item[0]['mrp']*item[1]}\n"

        item_list_label = tk.Label(root, text=item_price_list, font=("monospace", 15))
        item_list_label.place(x=160, y=100)
        current_widgets.append(item_list_label)

    back_btn = tk.Button(root, text="Main menu", command=main_menu)
    back_btn.place(x=360, y=600)
    current_widgets.append(back_btn)


def clear():
    for widget in current_widgets:
        widget.destroy()


def quit():
    if messagebox.askokcancel("Quit", "sure?"):
        root.destroy()


main_menu

# search_btn = tk.Button(root, text="Search", bg="salmon", command=quit)
# search_btn.place(x=550, y=150)
#
# clear_btn = tk.Button(root, text="Clear", bg="salmon", command=clear)
# clear_btn.place(x=550, y=450)
#
# quit_btn = tk.Button(root, text="Quit", bg="salmon", command=quit)
# quit_btn.place(x=400, y=600)
root.mainloop()



