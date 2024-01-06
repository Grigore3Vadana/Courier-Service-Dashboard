# app.py

from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#customers/add

@app.route('/customers/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        email = request.form['email']
        preferred_contact_method = request.form['preferred_contact_method']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Customers (Name, Address, Contact, Email, PreferredContactMethod)
            VALUES (?, ?, ?, ?, ?)
        """, (name, address, contact, email, preferred_contact_method))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('view_customers'))
    
    return render_template('add_customer.html')

#customer/update

@app.route('/customer/update/<int:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        email = request.form['email']
        preferred_contact_method = request.form['preferred_contact_method']
        
        cursor.execute("""
            UPDATE Customers
            SET Name = ?, Address = ?, Contact = ?, Email = ?, PreferredContactMethod = ?
            WHERE CustomerID = ?
        """, (name, address, contact, email, preferred_contact_method, customer_id))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('view_customers'))
    else:
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
        customer = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('update_customer.html', customer=customer)

#customer/delete

@app.route('/customer/delete/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Customers WHERE CustomerID = ?", (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_customers'))


#packages/add

@app.route('/packages/add', methods=['GET', 'POST'])
def add_package():
    if request.method == 'POST':
        description = request.form['description']
        weight = request.form['weight']
        delivery_date = request.form['delivery_date']
        customer_id = request.form['customer_id']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Packages (Description, Weight, DeliveryDate, CustomerID)
            VALUES (?, ?, ?, ?)
        """, (description, weight, delivery_date, customer_id))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('view_packages'))
    
    return render_template('add_package.html')

#package/update

@app.route('/package/update/<int:package_id>', methods=['GET', 'POST'])
def update_package(package_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        description = request.form['description']
        weight = request.form['weight']
        delivery_date = request.form['delivery_date']
        customer_id = request.form['customer_id']
        
        cursor.execute("""
            UPDATE Packages
            SET Description = ?, Weight = ?, DeliveryDate = ?, CustomerID = ?
            WHERE PackageID = ?
        """, (description, weight, delivery_date, customer_id, package_id))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('view_packages'))
    else:
        cursor.execute("SELECT * FROM Packages WHERE PackageID = ?", (package_id,))
        package = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('update_package.html', package=package)

#package/delete

@app.route('/package/delete/<int:package_id>', methods=['POST'])
def delete_package(package_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Packages WHERE PackageID = ?", (package_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_packages'))


#courier/add
@app.route('/courier/add', methods=['GET', 'POST'])
def add_courier():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        vehicle_type = request.form['vehicle_type']
        availability_status = request.form.get('availability_status') == 'on'
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Couriers (Name, Contact, VehicleType, AvailabilityStatus)
            VALUES (?, ?, ?, ?)
        """, (name, contact, vehicle_type, availability_status))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('view_couriers'))
    
    return render_template('add_courier.html')


#courier/update
@app.route('/courier/update/<int:courier_id>', methods=['GET', 'POST'])
def update_courier(courier_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        vehicle_type = request.form['vehicle_type']
        availability_status = request.form.get('availability_status') == 'on'

        cursor.execute("""
            UPDATE Couriers
            SET Name = ?, Contact = ?, VehicleType = ?, AvailabilityStatus = ?
            WHERE CourierID = ?
        """, (name, contact, vehicle_type, availability_status, courier_id))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('view_couriers'))
    else:
        cursor.execute("SELECT * FROM Couriers WHERE CourierID = ?", (courier_id,))
        courier = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('update_courier.html', courier=courier)

    
#courier/delete
@app.route('/courier/delete/<int:courier_id>', methods=['POST'])
def delete_courier(courier_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Couriers WHERE CourierID = ?", (courier_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_couriers'))

#delivery/add
@app.route('/delivery/add', methods=['GET', 'POST'])
def add_delivery():
    if request.method == 'POST':
        package_id = request.form['package_id']
        courier_id = request.form['courier_id']
        delivery_status = request.form['delivery_status']
        expected_delivery_date = request.form['expected_delivery_date']
        actual_delivery_date = request.form['actual_delivery_date']  # This can be NULL or a date

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Deliveries (PackageID, CourierID, DeliveryStatus, ExpectedDeliveryDate, ActualDeliveryDate)
            VALUES (?, ?, ?, ?, ?)
        """, (package_id, courier_id, delivery_status, expected_delivery_date, actual_delivery_date or None))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('view_deliveries'))
    
    return render_template('add_delivery.html')


#delivery/update
@app.route('/delivery/update/<int:delivery_id>', methods=['GET', 'POST'])
def update_delivery(delivery_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        package_id = request.form['package_id']
        courier_id = request.form['courier_id']
        delivery_status = request.form['delivery_status']
        expected_delivery_date = request.form['expected_delivery_date']
        actual_delivery_date = request.form['actual_delivery_date'] or None

        cursor.execute("""
            UPDATE Deliveries
            SET PackageID = ?, CourierID = ?, DeliveryStatus = ?, ExpectedDeliveryDate = ?, ActualDeliveryDate = ?
            WHERE DeliveryID = ?
        """, (package_id, courier_id, delivery_status, expected_delivery_date, actual_delivery_date, delivery_id))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('view_deliveries'))
    else:
        cursor.execute("SELECT * FROM Deliveries WHERE DeliveryID = ?", (delivery_id,))
        delivery = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('update_delivery.html', delivery=delivery)


#delivery/delete
@app.route('/delivery/delete/<int:delivery_id>', methods=['POST'])
def delete_delivery(delivery_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Deliveries WHERE DeliveryID = ?", (delivery_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_deliveries'))

#Simple Queries

#Deliveries with Courier Names and Package Descriptions
@app.route('/deliveries_couriers_packages')
def deliveries_couriers_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.DeliveryID, c.Name AS CourierName, p.Description AS PackageDescription
        FROM Deliveries d
        JOIN Couriers c ON d.CourierID = c.CourierID
        JOIN Packages p ON d.PackageID = p.PackageID;
    """)
    deliveries = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('deliveries_couriers_packages.html', deliveries=deliveries)

#Customers with Their Package Details
@app.route('/customers_packages')
def customers_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cu.Name AS CustomerName, p.PackageID, p.Description
        FROM Customers cu
        JOIN Packages p ON cu.CustomerID = p.CustomerID;
    """)
    customers_packages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('customers_packages.html', customers_packages=customers_packages)

#Packages with the Latest Location Updates
@app.route('/packages_latest_locations')
def packages_latest_locations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.PackageID, p.Description, l.CurrentLocation, MAX(l.Timestamp) AS LatestUpdate
        FROM Packages p
        JOIN Locations l ON p.PackageID = l.PackageID
        GROUP BY p.PackageID, p.Description, l.CurrentLocation;
    """)
    packages_locations = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('packages_latest_locations.html', packages_locations=packages_locations)

#Customers with Their Total Billing Amount
@app.route('/customers_total_billing')
def customers_total_billing():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cu.Name AS CustomerName, SUM(b.Amount) AS TotalBilled
        FROM Customers cu
        JOIN Billing b ON cu.CustomerID = b.CustomerID
        GROUP BY cu.Name;
    """)
    customers_billing = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('customers_total_billing.html', customers_billing=customers_billing)

#Couriers and the Number of Deliveries Completed
@app.route('/couriers_deliveries_count')
def couriers_deliveries_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.Name AS CourierName, COUNT(d.DeliveryID) AS DeliveriesCount
        FROM Couriers c
        JOIN Deliveries d ON c.CourierID = d.CourierID
        WHERE d.DeliveryStatus = 'Delivered'
        GROUP BY c.Name;
    """)
    couriers_count = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('couriers_deliveries_count.html', couriers_count=couriers_count)

#Deliveries Including Customer Names and Delivery Status
@app.route('/deliveries_customers_status')
def deliveries_customers_status():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Corrected SQL query to join Deliveries, Packages, and Customers.
    cursor.execute("""
        SELECT d.DeliveryID, cu.Name AS CustomerName, d.DeliveryStatus
        FROM Deliveries d
        JOIN Packages p ON d.PackageID = p.PackageID
        JOIN Customers cu ON p.CustomerID = cu.CustomerID;
    """)
    deliveries_status = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('deliveries_customers_status.html', deliveries_status=deliveries_status)

#Let's create a simple query that retrieves all packages with their corresponding customer names and contact details
@app.route('/packages_with_customers')
def packages_with_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.PackageID, p.Description, c.Name as CustomerName, c.Contact
        FROM Packages p
        JOIN Customers c ON p.CustomerID = c.CustomerID
    """)
    packages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('packages_with_customers.html', packages=packages)



#Complex Queries

#Customers with Billing Above Average
@app.route('/customers_billing_above_average')
def customers_billing_above_average():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cu.Name AS CustomerName, b.Amount
        FROM Billing b
        JOIN Customers cu ON b.CustomerID = cu.CustomerID
        WHERE b.Amount > (
            SELECT AVG(Amount) FROM Billing
        );
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('customers_billing_above_average.html', results=results)

#Couriers with the Highest Number of Deliveries This Month
@app.route('/top_couriers_this_month')
def top_couriers_this_month():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.Name AS CourierName, COUNT(d.DeliveryID) AS DeliveryCount
        FROM Couriers c
        JOIN Deliveries d ON c.CourierID = d.CourierID
        WHERE MONTH(d.ExpectedDeliveryDate) = MONTH(GETDATE())
        AND YEAR(d.ExpectedDeliveryDate) = YEAR(GETDATE())
        GROUP BY c.Name
        HAVING COUNT(d.DeliveryID) = (
            SELECT MAX(DeliveryCount) FROM (
                SELECT COUNT(d.DeliveryID) AS DeliveryCount
                FROM Deliveries d
                WHERE MONTH(d.ExpectedDeliveryDate) = MONTH(GETDATE())
                AND YEAR(d.ExpectedDeliveryDate) = YEAR(GETDATE())
                GROUP BY d.CourierID
            ) AS SubQuery
        );
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('top_couriers_this_month.html', results=results)

#Customers with Deliveries in More Than One City
@app.route('/customers_multi_city_deliveries')
def customers_multi_city_deliveries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cu.Name AS CustomerName, COUNT(DISTINCT l.CurrentLocation) AS CitiesCount
        FROM Customers cu
        JOIN Packages p ON cu.CustomerID = p.CustomerID
        JOIN Deliveries d ON p.PackageID = d.PackageID
        JOIN Locations l ON p.PackageID = l.PackageID
        GROUP BY cu.CustomerID, cu.Name
        HAVING COUNT(DISTINCT l.CurrentLocation) > 1;
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('customers_multi_city_deliveries.html', results=results)

#Customers Who Have Sent a Package Weighing More Than the Average
@app.route('/customers_heavy_packages')
def customers_heavy_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cu.Name AS CustomerName, p.PackageID, p.Weight
        FROM Packages p
        JOIN Customers cu ON p.CustomerID = cu.CustomerID
        WHERE p.Weight > (
            SELECT AVG(Weight) FROM Packages
        );
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('customers_heavy_packages.html', results=results)

#Now, a complex query that finds customers who have sent packages weighing over 5 kg and lists the heaviest package they sent in 2024
@app.route('/heavy_packages_2024')
def heavy_packages_2024():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.Name as CustomerName, MAX(p.Weight) as MaxWeight
        FROM Customers c
        JOIN Packages p ON c.CustomerID = p.CustomerID
        WHERE p.Weight > 5 AND YEAR(p.DeliveryDate) = 2024
        GROUP BY c.Name
    """)
    heavy_packages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('heavy_packages_2024.html', heavy_packages=heavy_packages)




#############################___________________________________##################################################################

@app.route('/customers')
def view_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_customers.html', customers=customers)

@app.route('/packages')
def view_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Packages")
    packages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_packages.html', packages=packages)

@app.route('/couriers')
def view_couriers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Couriers")
    couriers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_couriers.html', couriers=couriers)

@app.route('/deliveries')
def view_deliveries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Deliveries.*, Packages.Description as PackageDescription, Couriers.Name as CourierName
        FROM Deliveries
        JOIN Packages ON Deliveries.PackageID = Packages.PackageID
        JOIN Couriers ON Deliveries.CourierID = Couriers.CourierID
    """)
    deliveries = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_deliveries.html', deliveries=deliveries)

@app.route('/billing')
def view_billing():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Billing")
    billing = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_billing.html', billing=billing)

@app.route('/locations')
def view_locations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Locations")
    locations = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_locations.html', locations=locations)

@app.route('/ratings')
def view_ratings():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ratings")
    ratings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_ratings.html', ratings=ratings)

@app.route('/servicetypes')
def view_servicetypes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ServiceTypes")
    servicetypes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_servicetypes.html', servicetypes=servicetypes)



#################################_________________________________________________________________________________________

if __name__ == '__main__':
    app.run(debug=True)
