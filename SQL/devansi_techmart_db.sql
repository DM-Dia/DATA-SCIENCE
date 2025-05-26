-- Create the TechMart database
CREATE DATABASE TechMart;
-- Use the TechMart database
USE TechMart;
-- Customers table
CREATE TABLE Customers (
customer_id INT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone VARCHAR(20),
address VARCHAR(200),
city VARCHAR(50),
state VARCHAR(50),
zip_code VARCHAR(20),
registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
loyalty_points INT DEFAULT 0
);
-- Product Categories table
CREATE TABLE ProductCategories (
category_id INT PRIMARY KEY,
category_name VARCHAR(50) NOT NULL,
description TEXT,
parent_category_id INT,
FOREIGN KEY (parent_category_id) REFERENCES ProductCategories(category_id)
);
-- Products table
CREATE TABLE Products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100) NOT NULL,
description TEXT,
category_id INT,
price DECIMAL(10, 2) NOT NULL,
stock_quantity INT DEFAULT 0,
manufacturer VARCHAR(100),
release_date DATE,
is_active BOOLEAN DEFAULT TRUE,
FOREIGN KEY (category_id) REFERENCES ProductCategories(category_id)
);
-- Orders table
CREATE TABLE Orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
total_amount DECIMAL(12, 2) NOT NULL,
shipping_address VARCHAR(200),
shipping_city VARCHAR(50),
shipping_state VARCHAR(50),
shipping_zip_code VARCHAR(20),
status VARCHAR(50) DEFAULT 'Pending',
payment_method VARCHAR(50),
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
-- Order Items table (junction table between Orders and Products)
CREATE TABLE OrderItems (
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT NOT NULL,
unit_price DECIMAL(10, 2) NOT NULL,
discount DECIMAL(10, 2) DEFAULT 0.00,
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
-- Employees table
CREATE TABLE Employees (
employee_id INT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone VARCHAR(20),
hire_date DATE NOT NULL,
job_title VARCHAR(100),
department VARCHAR(100),
manager_id INT,
salary DECIMAL(10, 2),
FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);
-- Reviews table
CREATE TABLE Reviews (
review_id INT PRIMARY KEY,
product_id INT,
customer_id INT,
rating INT CHECK (rating BETWEEN 1 AND 5),
comment TEXT,
review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (product_id) REFERENCES Products(product_id),
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
-- Promotions table
CREATE TABLE Promotions (
promotion_id INT PRIMARY KEY,
promotion_name VARCHAR(100) NOT NULL,
description TEXT,
discount_percentage DECIMAL(5, 2),
start_date DATE NOT NULL,
end_date DATE NOT NULL,
is_active BOOLEAN DEFAULT TRUE
);
-- Product Promotions mapping (junction table between Products and Promotions)
CREATE TABLE ProductPromotions (
product_id INT,
promotion_id INT,
PRIMARY KEY (product_id, promotion_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id),
FOREIGN KEY (promotion_id) REFERENCES Promotions(promotion_id)
);

-- Insert data into Customers table
INSERT INTO Customers (customer_id, first_name, last_name, email, phone,
address, city, state, zip_code, registration_date, loyalty_points)
VALUES
(1, 'John', 'Smith', 'john.smith@email.com', '555-123-4567', '123 Main St', 'Austin', 'TX', '78701',
'2023-01-15', 250),
(2, 'Emma', 'Johnson', 'emma.j@email.com', '555-234-5678', '456 Elm St', 'Seattle', 'WA', '98101',
'2023-02-20', 175),
(3, 'Michael', 'Williams', 'michael.w@email.com', '555-345-6789', '789 Oak Ave', 'Chicago', 'IL', '60601',
'2023-03-10', 320),
(4, 'Sophia', 'Brown', 'sophia.b@email.com', '555-456-7890', '101 Pine Rd', 'New York', 'NY', '10001',
'2023-04-05', 100),
(5, 'Robert', 'Jones', 'robert.j@email.com', '555-567-8901', '202 Maple Dr', 'Los Angeles', 'CA', '90001',
'2023-04-12', 280),
(6, 'Olivia', 'Garcia', 'olivia.g@email.com', '555-678-9012', '303 Birch Ln', 'Miami', 'FL', '33101',
'2023-05-18', 150),
(7, 'William', 'Miller', 'william.m@email.com', '555-789-0123', '404 Cedar Ct', 'Denver', 'CO', '80201',
'2023-06-22', 90),
(8, 'Ava', 'Davis', 'ava.d@email.com', '555-890-1234', '505 Walnut Pl', 'Portland', 'OR', '97201',
'2023-07-14', 210),
(9, 'James', 'Rodriguez', 'james.r@email.com', '555-901-2345', '606 Spruce Way', 'Boston', 'MA',
'02101', '2023-08-08', 170),
(10, 'Isabella', 'Martinez', 'isabella.m@email.com', '555-012-3456', '707 Fir Blvd', 'Phoenix', 'AZ',
'85001', '2023-09-19', 300),
(11, 'David', 'Anderson', 'david.a@email.com', '555-321-7654', '808 Cypress St', 'San Francisco', 'CA',
'94101', '2024-01-10', 220),
(12, 'Mia', 'Taylor', 'mia.t@email.com', '555-432-8765', '909 Redwood Dr', 'Atlanta', 'GA', '30301',
'2024-02-05', 180);

INSERT INTO ProductCategories (category_id, category_name, description,
parent_category_id)
VALUES
(1, 'Electronics', 'Electronic devices and accessories', NULL),
(2, 'Computers', 'Desktop and laptop computers', 1),
(3, 'Smartphones', 'Mobile phones and accessories', 1),
(4, 'Audio', 'Headphones, speakers, and audio equipment', 1),
(5, 'Gaming', 'Video games and gaming equipment', NULL),
(6, 'Consoles', 'Gaming consoles and accessories', 5),
(7, 'PC Gaming', 'PC gaming hardware and accessories', 5),
(8, 'Home Appliances', 'Household electronic appliances', NULL),
(9, 'Kitchen', 'Kitchen appliances and equipment', 8);

-- Insert data into Products table
INSERT INTO Products (product_id, product_name, description, category_id,
price, stock_quantity, manufacturer, release_date, is_active)
VALUES
(101, 'UltraBook Pro', '15-inch laptop with high performance', 2, 1299.99, 50, 'TechCorp', '2023-03-15',
TRUE),
(102, 'SmartPhone X', 'Latest smartphone with advanced features', 3, 899.99, 120, 'MobiTech',
'2023-05-20', TRUE),
(103, 'Noise Cancelling Headphones', 'Premium headphones with noise cancellation', 4, 249.99, 85,
'AudioMax', '2023-02-10', TRUE),
(104, 'Gaming Console Pro', 'Next-gen gaming console', 6, 499.99, 30, 'GameTech', '2023-11-05',
TRUE),
(105, 'Smart Watch', 'Fitness and notification tracker', 1, 199.99, 75, 'MobiTech', '2023-07-14', TRUE),
(106, 'Bluetooth Speaker', 'Portable bluetooth speaker with 20hr battery', 4, 129.99, 60, 'AudioMax',
'2023-08-22', TRUE),
(107, 'Desktop Computer', 'High-performance desktop for professionals', 2, 1599.99, 25, 'TechCorp',
'2023-09-30', TRUE),
(108, 'Tablet Pro', '12-inch tablet with stylus support', 1, 699.99, 40, 'MobiTech', '2023-10-15', TRUE),
(109, 'Wireless Gaming Mouse', 'High precision gaming mouse', 7, 89.99, 100, 'GameTech',
'2023-04-18', TRUE),
(110, 'Coffee Maker', 'Programmable coffee maker with timer', 9, 149.99, 35, 'HomeElectronics',
'2023-06-25', TRUE),
(111, 'Microwave Oven', 'Digital microwave with multiple cooking modes', 9, 179.99, 30,
'HomeElectronics', '2023-07-05', TRUE),
(112, 'Gaming Keyboard', 'Mechanical RGB gaming keyboard', 7, 129.99, 45, 'GameTech', '2023-08-10',
TRUE),
(113, 'Wireless Earbuds', 'True wireless earbuds with charging case', 4, 159.99, 90, 'AudioMax',
'2023-09-18', TRUE),
(114, 'External Hard Drive', '2TB portable external hard drive', 2, 119.99, 70, 'DataStore', '2023-05-28',
TRUE),
(115, 'Smartphone Y', 'Mid-range smartphone with excellent camera', 3, 599.99, 65, 'MobiTech',
'2023-10-25', TRUE),
(116, 'Ultra HD Monitor', '27-inch 4K monitor for professionals', 2, 349.99, 55, 'ViewTech',
'2023-11-15', TRUE),
(117, 'Smart Blender', 'Programmable blender with multiple speeds', 9, 89.99, 40, 'HomeElectronics',
'2023-12-10', FALSE),
(118, 'Gaming Headset', 'Surround sound gaming headset with mic', 7, 149.99, 60, 'GameTech',
'2024-01-05', TRUE),
(119, 'Wireless Router', 'High-speed dual-band wireless router', 1, 129.99, 50, 'NetConnect',
'2024-02-12', TRUE),
(120, 'Portable Power Bank', '20000mAh fast charging power bank', 3, 49.99, 80, 'PowerTech',
'2024-03-20', TRUE);

-- Insert data into Orders table
INSERT INTO Orders (order_id, customer_id, order_date, total_amount, shipping_address, shipping_city, 
shipping_state, shipping_zip_code, status, payment_method)
VALUES
(1001, 1, '2023-05-10 14:30:00', 1549.98, '123 Main St', 'Austin', 'TX', '78701', 'Delivered', 'Credit Card'),
(1002, 2, '2023-05-15 10:15:00', 899.99, '456 Elm St', 'Seattle', 'WA', '98101', 'Delivered', 'PayPal'),
(1003, 3, '2023-06-02 09:45:00', 379.98, '789 Oak Ave', 'Chicago', 'IL', '60601', 'Delivered', 'Credit Card'),
(1004, 4, '2023-06-10 16:20:00', 499.99, '101 Pine Rd', 'New York', 'NY', '10001', 'Delivered', 'Debit Card'),
(1005, 5, '2023-07-05 11:30:00', 329.98, '202 Maple Dr', 'Los Angeles', 'CA', '90001', 'Delivered', 'Credit Card'),
(1006, 1, '2023-07-20 14:45:00', 699.99, '123 Main St', 'Austin', 'TX', '78701', 'Delivered', 'Credit Card'),
(1007, 6, '2023-08-08 13:10:00', 449.98, '303 Birch Ln', 'Miami', 'FL', '33101', 'Delivered', 'PayPal'),
(1008, 7, '2023-08-25 15:25:00', 1599.99, '404 Cedar Ct', 'Denver', 'CO', '80201', 'Shipped', 'Credit Card'),
(1009, 8, '2023-09-12 10:05:00', 249.99, '505 Walnut Pl', 'Portland', 'OR', '97201', 'Delivered', 'Debit Card'),
(1010, 9, '2023-09-30 17:40:00', 219.98, '606 Spruce Way', 'Boston', 'MA', '02101', 'Delivered', 'Credit Card'),
(1011, 10, '2023-10-15 09:30:00', 1099.98, '707 Fir Blvd', 'Phoenix', 'AZ', '85001', 'Shipped', 'PayPal'),
(1012, 11, '2023-11-05 14:15:00', 679.97, '808 Cypress St', 'San Francisco', 'CA', '94101', 'Processing', 'Credit Card'),
(1013, 12, '2023-11-20 11:50:00', 279.98, '909 Redwood Dr', 'Atlanta', 'GA', '30301', 'Shipped', 'Debit Card'),
(1014, 3, '2023-12-10 16:05:00', 849.98, '789 Oak Ave', 'Chicago', 'IL', '60601', 'Delivered', 'Credit Card'),
(1015, 5, '2023-12-28 13:40:00', 399.98, '202 Maple Dr', 'Los Angeles', 'CA', '90001', 'Delivered', 'PayPal'),
(1016, 2, '2024-01-15 10:25:00', 1129.98, '456 Elm St', 'Seattle', 'WA', '98101', 'Shipped', 'Credit Card'),
(1017, 8, '2024-02-02 15:10:00', 459.98, '505 Walnut Pl', 'Portland', 'OR', '97201', 'Processing', 'Debit Card'),
(1018, 1, '2024-02-20 09:55:00', 349.99, '123 Main St', 'Austin', 'TX', '78701', 'Processing', 'Credit Card'),
(1019, 4, '2024-03-08 12:30:00', 279.98, '101 Pine Rd', 'New York', 'NY', '10001', 'Pending', 'PayPal'),
(1020, 6, '2024-03-25 14:20:00', 549.98, '303 Birch Ln', 'Miami', 'FL', '33101', 'Pending', 'Credit Card');

-- Insert data into OrderItems table
INSERT INTO OrderItems (order_item_id, order_id, product_id, quantity,
unit_price, discount)
VALUES
(2001, 1001, 101, 1, 1299.99, 0.00),
(2002, 1001, 103, 1, 249.99, 0.00),
(2003, 1002, 102, 1, 899.99, 0.00),
(2004, 1003, 103, 1, 249.99, 0.00),
(2005, 1003, 106, 1, 129.99, 0.00),
(2006, 1004, 104, 1, 499.99, 0.00),
(2007, 1005, 105, 1, 199.99, 0.00),
(2008, 1005, 106, 1, 129.99, 0.00),
(2009, 1006, 108, 1, 699.99, 0.00),
(2010, 1007, 109, 1, 89.99, 0.00),
(2011, 1007, 113, 1, 159.99, 0.00),
(2012, 1007, 110, 1, 149.99, 0.00),
(2013, 1008, 107, 1, 1599.99, 0.00),
(2014, 1009, 103, 1, 249.99, 0.00),
(2015, 1010, 109, 1, 89.99, 0.00),
(2016, 1010, 120, 1, 49.99, 0.00),
(2017, 1010, 114, 1, 119.99, 40.00),
(2018, 1011, 115, 1, 599.99, 0.00),
(2019, 1011, 116, 1, 349.99, 0.00),
(2020, 1011, 119, 1, 129.99, 0.00),
(2021, 1012, 118, 1, 149.99, 0.00),
(2022, 1012, 116, 1, 349.99, 0.00),
(2023, 1012, 120, 2, 49.99, 0.00),
(2024, 1013, 113, 1, 159.99, 0.00),
(2025, 1013, 120, 1, 49.99, 0.00),
(2026, 1013, 109, 1, 89.99, 20.00),
(2027, 1014, 102, 1, 899.99, 50.00),
(2028, 1015, 110, 1, 149.99, 0.00),
(2029, 1015, 111, 1, 179.99, 0.00),
(2030, 1015, 120, 1, 49.99, 0.00),
(2031, 1016, 101, 1, 1299.99, 200.00),
(2032, 1016, 109, 1, 89.99, 0.00),
(2033, 1016, 120, 1, 49.99, 0.00),
(2034, 1017, 118, 1, 149.99, 0.00),
(2035, 1017, 113, 1, 159.99, 0.00),
(2036, 1017, 120, 3, 49.99, 0.00),
(2037, 1018, 116, 1, 349.99, 0.00),
(2038, 1019, 113, 1, 159.99, 0.00),
(2039, 1019, 120, 1, 49.99, 0.00),
(2040, 1019, 106, 1, 129.99, 60.00),
(2041, 1020, 104, 1, 499.99, 0.00),
(2042, 1020, 120, 1, 49.99, 0.00);

-- Insert data into Employees table
INSERT INTO Employees (employee_id, first_name, last_name, email, phone,
hire_date, job_title, department, manager_id, salary)
VALUES
(501, 'Thomas', 'Wilson', 'thomas.w@techmart.com', '555-111-2222', '2022-01-15', 'CEO', 'Executive',
NULL, 250000.00),
(502, 'Sarah', 'Johnson', 'sarah.j@techmart.com', '555-222-3333', '2022-02-20', 'CTO', 'Executive', 501,
200000.00),
(503, 'Daniel', 'Brown', 'daniel.b@techmart.com', '555-333-4444', '2022-03-10', 'CFO', 'Executive', 501,
200000.00),
(504, 'Jessica', 'Smith', 'jessica.s@techmart.com', '555-444-5555', '2022-04-05', 'IT Manager', 'IT', 502,
120000.00),
(505, 'Andrew', 'Davis', 'andrew.d@techmart.com', '555-555-6666', '2022-05-12', 'Sales Manager',
'Sales', 501, 110000.00),
(506, 'Lisa', 'Miller', 'lisa.m@techmart.com', '555-666-7777', '2022-06-18', 'Marketing Manager',
'Marketing', 501, 110000.00),
(507, 'Robert', 'Taylor', 'robert.t@techmart.com', '555-777-8888', '2022-07-22', 'HR Manager', 'HR',
501, 105000.00),
(508, 'Emily', 'Anderson', 'emily.a@techmart.com', '555-888-9999', '2022-08-14', 'IT Specialist', 'IT',
504, 85000.00),
(509, 'Michael', 'Clark', 'michael.c@techmart.com', '555-999-0000', '2022-09-08', 'IT Specialist', 'IT',
504, 85000.00),
(510, 'Amanda', 'Wright', 'amanda.w@techmart.com', '555-000-1111', '2022-10-19', 'Sales
Representative', 'Sales', 505, 65000.00),
(511, 'Joshua', 'Garcia', 'joshua.g@techmart.com', '555-111-3333', '2022-11-10', 'Sales Representative',
'Sales', 505, 65000.00),
(512, 'Melissa', 'Martinez', 'melissa.m@techmart.com', '555-222-4444', '2022-12-05', 'Marketing
Specialist', 'Marketing', 506, 70000.00),
(513, 'Christopher', 'Lee', 'christopher.l@techmart.com', '555-333-5555', '2023-01-15', 'HR Specialist',
'HR', 507, 65000.00),
(514, 'Nicole', 'Harris', 'nicole.h@techmart.com', '555-444-6666', '2023-02-20', 'IT Support', 'IT', 504,
60000.00),
(515, 'Brian', 'Young', 'brian.y@techmart.com', '555-555-7777', '2023-03-18', 'Sales Representative',
'Sales', 505, 65000.00);

-- Insert data into Reviews table
INSERT INTO Reviews (review_id, product_id, customer_id, rating, comment, review_date)
VALUES
(3001, 101, 1, 5, 'Excellent laptop, very fast and reliable', '2023-05-20 15:30:00'),
(3002, 102, 2, 4, 'Great phone but battery life could be better', '2023-05-25 10:45:00'),
(3003, 103, 3, 5, 'Amazing sound quality, best headphones I have owned', '2023-06-10 09:20:00'),
(3004, 104, 4, 3, 'Good console but lacks some features compared to competitors', '2023-06-18 14:10:00'),
(3005, 105, 5, 4, 'Nice smart watch, tracks fitness well', '2023-07-12 11:25:00'),
(3006, 106, 6, 5, 'Incredible sound for such a small speaker', '2023-07-28 16:40:00'),
(3007, 107, 7, 4, 'Powerful desktop, great for my work needs', '2023-09-05 13:15:00'),
(3008, 108, 8, 5, 'The tablet is perfect for my design work', '2023-09-20 10:30:00'),
(3009, 109, 9, 4, 'Responsive gaming mouse, comfortable to use', '2023-10-08 17:50:00'),
(3010, 110, 10, 5, 'Makes great coffee and easy to program', '2023-10-25 09:10:00'),
(3011, 111, 11, 3, 'Works well but a bit noisy', '2023-11-12 12:45:00'),
(3012, 112, 12, 5, 'Keys feel great, RGB lighting is awesome', '2023-11-30 15:20:00'),
(3013, 113, 1, 4, 'Good sound quality but fit is a bit loose', '2023-12-15 14:35:00'),
(3014, 101, 3, 4, 'Good performance but runs hot under heavy load', '2023-12-28 11:55:00'),
(3015, 102, 5, 5, 'Camera quality is exceptional!', '2024-01-10 10:15:00'),
(3016, 104, 7, 4, 'Great gaming experience', '2024-01-25 16:30:00'),
(3017, 105, 9, 3, 'Battery life is shorter than advertised', '2024-02-08 13:40:00'),
(3018, 108, 11, 5, 'Perfect for both work and entertainment', '2024-02-22 09:25:00'),
(3019, 113, 2, 4, 'Sound quality is great, battery life could be better', '2024-03-10 14:50:00'),
(3020, 116, 4, 5, 'Amazing display quality, perfect for my graphic design work', '2024-03-28 11:05:00');

-- Insert data into Promotions table
INSERT INTO Promotions (promotion_id, promotion_name, description,
discount_percentage, start_date, end_date, is_active)
VALUES
(401, 'Summer Sale', 'Annual summer discount event', 15.00, '2023-06-01', '2023-06-30', FALSE),
(402, 'Back to School', 'Discounts on electronics for students', 10.00, '2023-08-01', '2023-08-31',
FALSE),
(403, 'Black Friday', 'Biggest sale of the year', 25.00, '2023-11-24', '2023-11-27', FALSE),
(404, 'Holiday Season', 'End of year holiday promotions', 20.00, '2023-12-15', '2023-12-31', FALSE),
(405, 'New Year Sale', 'Start the year with savings', 15.00, '2024-01-01', '2024-01-15', FALSE),
(406, 'Winter Clearance', 'Clearing inventory for new products', 30.00, '2024-02-01', '2024-02-28',
FALSE),
(407, 'Spring Tech Fest', 'Discounts on latest technology products', 12.00, '2024-03-15', '2024-04-15',
TRUE);

-- Insert data into ProductPromotions table
INSERT INTO ProductPromotions (product_id, promotion_id)
VALUES
(101, 402), -- UltraBook Pro in Back to School promotion
(102, 401), -- SmartPhone X in Summer Sale
(103, 401), -- Noise Cancelling Headphones in Summer Sale
(104, 403), -- Gaming Console Pro in Black Friday
(105, 401), -- Smart Watch in Summer Sale
(106, 402), -- Bluetooth Speaker in Back to School
(107, 403), -- Desktop Computer in Black Friday
(108, 404), -- Tablet Pro in Holiday Season
(109, 402), -- Wireless Gaming Mouse in Back to School
(110, 404), -- Coffee Maker in Holiday Season
(111, 405), -- Microwave Oven in New Year Sale
(112, 403), -- Gaming Keyboard in Black Friday
(113, 402), -- Wireless Earbuds in Back to School
(114, 401), -- External Hard Drive in Summer Sale
(115, 404), -- Smartphone Y in Holiday Season
(116, 405), -- Ultra HD Monitor in New Year Sale
(118, 406), -- Gaming Headset in Winter Clearance
(119, 406), -- Wireless Router in Winter Clearance
(120, 407), -- Portable Power Bank in Spring Tech Fest
(101, 407), -- UltraBook Pro in Spring Tech Fest
(102, 407), -- SmartPhone X in Spring Tech Fest
(103, 407), -- Noise Cancelling Headphones in Spring Tech Fest
(104, 407); -- Gaming Console Pro in Spring Tech Fest

