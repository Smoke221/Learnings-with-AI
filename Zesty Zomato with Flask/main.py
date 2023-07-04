from flask import Flask, request, render_template

app = Flask(__name__)

menu = []
orders = []
order_id_counter = 1

# Helper function to generate HTML code for displaying the menu
def display_menu():
    if len(menu) > 0:
        table_rows = ""
        for dish in menu:
            table_rows += f"<tr><td>{dish['dish_id']}</td><td>{dish['name']}</td><td>{dish['price']}</td><td>{dish['availability']}</td></tr>"
        table_html = f"<table><thead><tr><th>Dish ID</th><th>Dish Name</th><th>Price</th><th>Availability</th></tr></thead><tbody>{table_rows}</tbody></table>"
        return f"<h2>Menu:</h2>{table_html}"
    else:
        return "<p>No dishes in the menu.</p>"

# Route for adding a new dish to the menu
@app.route('/menu/add', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        dish = request.form
        menu.append(dish)
        return display_menu()
    return render_template('add_dish.html')

# Route for removing a dish from the menu
@app.route('/menu/remove/<dish_id>', methods=['GET', 'POST'])
def remove_dish(dish_id):
    if request.method == 'POST':
        for dish in menu:
            if dish['dish_id'] == dish_id:
                menu.remove(dish)
                return 'Dish removed successfully.'
        return 'Dish not found.'
    return render_template('remove_dish.html')

# Route for updating dish availability
@app.route('/menu/update/<dish_id>', methods=['GET', 'POST'])
def update_availability(dish_id):
    if request.method == 'POST':
        availability = request.form.get('availability')
        for dish in menu:
            if dish['dish_id'] == dish_id:
                dish['availability'] = availability
                return 'Availability updated successfully.'
        return 'Dish not found.'
    return render_template('update_availability.html')


# Route for taking a new order
@app.route('/orders/place', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        customer_name = request.form.get('customer_name')
        dish_ids = request.form.get('dish_ids').split(',')
        ordered_dishes = []

        for dish_id in dish_ids:
            dish = next((d for d in menu if d['dish_id'] == dish_id and d['availability'] == 'yes'), None)
            if dish:
                ordered_dishes.append(dish)
            else:
                return f"Dish with ID {dish_id} is not available."

        order = {
            'order_id': order_id_counter,
            'customer_name': customer_name,
            'dishes': ordered_dishes,
            'status': 'received'
        }
        orders.append(order)
        order_id_counter += 1
        return f"Order {order['order_id']} placed successfully."
    return render_template('place_order.html')


# Route for updating order status
@app.route('/orders/update/<order_id>', methods=['GET', 'POST'])
def update_order_status(order_id):
    if request.method == 'POST':
        status = request.form.get('status')

        order = next((o for o in orders if o['order_id'] == int(order_id)), None)
        if order:
            order['status'] = status
            return 'Order status updated successfully.'
        else:
            return 'Order not found.'
    return render_template('update_order_status.html')


# Route for reviewing orders
@app.route('/orders')
def review_orders():
    if len(orders) == 0:
        return 'No orders placed yet.'

    return render_template('review_orders.html', review=orders)


if __name__ == '__main__':
    app.run()
