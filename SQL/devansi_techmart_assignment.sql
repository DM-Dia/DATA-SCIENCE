USE TechMart;

-- 1st
SELECT product_name, price, stock_quantity
FROM Products
WHERE price > 500 AND stock_quantity >= 50
ORDER BY price DESC;

-- 2nd
SELECT CONCAT(first_name, ' ', last_name) AS full_name, email, city
FROM Customers
WHERE YEAR(registration_date) = 2023 AND loyalty_points > 200;

-- 3rd
UPDATE Customers 
SET loyalty_points = loyalty_points + 50 
WHERE state = 'TX' AND customer_id > 0;

-- 4th
SELECT product_id, product_name, stock_quantity
FROM Products
WHERE stock_quantity < 30;

-- 5th
SELECT pc.category_name, AVG(p.price) AS avg_price
FROM Products p
JOIN ProductCategories pc ON p.category_id = pc.category_id
GROUP BY pc.category_name
HAVING AVG(p.price) > 200;

-- 6th
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- 7th
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_spent
FROM Customers c JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, customer_name
ORDER BY total_spent DESC LIMIT 5;

-- 8th
SELECT p.product_name, p.price, AVG(r.rating) AS avg_rating
FROM Products p
LEFT JOIN Reviews r ON p.product_id = r.product_id
GROUP BY p.product_id, p.product_name, p.price;

-- 9th
SELECT p.product_name, 
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name, o.order_date
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
WHERE YEAR(o.order_date) = 2024 AND MONTH(o.order_date) = 2;

-- 10th
SELECT e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    CONCAT(m.first_name, ' ', m.last_name) AS manager_name
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id;

-- 11th
SELECT p.product_id, p.product_name
FROM Products p
LEFT JOIN Reviews r ON p.product_id = r.product_id
WHERE r.review_id IS NULL;

-- 12th
SELECT c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(DISTINCT pc.category_id) AS distinct_categories
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
JOIN ProductCategories pc ON p.category_id = pc.category_id
GROUP BY c.customer_id, customer_name
HAVING COUNT(DISTINCT pc.category_id) >= 3;

-- 13th
SELECT p.product_id, p.product_name
FROM Products p
WHERE p.product_id NOT IN (
    SELECT pp.product_id
    FROM ProductPromotions pp
    JOIN Promotions pr ON pp.promotion_id = pr.promotion_id
    WHERE pr.is_active = TRUE
);

-- 14th
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, 
	p.product_name, COUNT(*) AS purchase_count
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, customer_name, p.product_id, p.product_name
HAVING COUNT(*) > 1;

USE TechMart;
 
-- 15th
SELECT department, COUNT(*) AS employee_count
FROM Employees
GROUP BY department
HAVING COUNT(*) > 3;

-- 16th
SELECT MONTH(order_date) AS month,
    SUM(total_amount) AS monthly_revenue
FROM Orders
WHERE YEAR(order_date) = 2023
GROUP BY MONTH(order_date)
ORDER BY month;

-- 17th
SELECT pc.category_name, COUNT(*) AS order_count
FROM Orders o JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
JOIN ProductCategories pc ON p.category_id = pc.category_id
GROUP BY pc.category_name
ORDER BY order_count DESC
LIMIT 1;

-- 18th
SELECT e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.department, e.salary, dept_avg.avg_salary
FROM Employees e
JOIN (
    SELECT department, AVG(salary) AS avg_salary
    FROM Employees GROUP BY department
) dept_avg ON e.department = dept_avg.department
WHERE e.salary > dept_avg.avg_salary;

-- 19th
SELECT p.product_id, p.product_name, COUNT(*) AS total_reviews,
    SUM(CASE WHEN r.rating >= 4 THEN 1 ELSE 0 END) AS high_rating_reviews,
    (SUM(CASE WHEN r.rating >= 4 THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS percentage_high_rating
FROM Products p
JOIN Reviews r ON p.product_id = r.product_id
GROUP BY p.product_id, p.product_name
HAVING COUNT(*) >= 2;

-- 20th
SELECT payment_method, COUNT(*) AS order_count,
    AVG(total_amount) AS avg_order_value
FROM Orders
GROUP BY payment_method;

-- 21st
SELECT DAYNAME(order_date) AS day_of_week,
    COUNT(*) AS order_count
FROM Orders
GROUP BY day_of_week
ORDER BY order_count DESC
LIMIT 1;

-- 22nd
SELECT pc.category_name,
    QUARTER(o.order_date) AS quarter,
    SUM(o.total_amount) AS quarterly_sales
FROM Orders o
JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
JOIN ProductCategories pc ON p.category_id = pc.category_id
WHERE YEAR(o.order_date) = 2023
GROUP BY pc.category_name, quarter
ORDER BY pc.category_name, quarter;

-- 23rd
CREATE VIEW CustomerPurchaseSummary AS
SELECT 
    ct.customer_id,
    ct.customer_name,
    ct.total_spend,
    ct.order_count,
    cc.category_name AS most_purchased_category
FROM (
    -- CustomerTotals subquery
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        SUM(o.total_amount) AS total_spend,
        COUNT(DISTINCT o.order_id) AS order_count
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, customer_name
) ct
LEFT JOIN (
    -- CustomerCategories subquery with filtering for rank=1
    SELECT * FROM (
        SELECT 
            c.customer_id,
            CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
            pc.category_name,
            COUNT(*) AS category_purchases,
            RANK() OVER (PARTITION BY c.customer_id ORDER BY COUNT(*) DESC) AS category_rank
        FROM Customers c
        JOIN Orders o ON c.customer_id = o.customer_id
        JOIN OrderItems oi ON o.order_id = oi.order_id
        JOIN Products p ON oi.product_id = p.product_id
        JOIN ProductCategories pc ON p.category_id = pc.category_id
        GROUP BY c.customer_id, customer_name, pc.category_name
    ) ranked_categories
    WHERE category_rank = 1
) cc ON ct.customer_id = cc.customer_id;

-- 24th
WITH RECURSIVE OrgChart AS (
    -- Start with top-level executives
    SELECT 
        employee_id,
        first_name,
        last_name,
        manager_id,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL
    UNION
    -- Add employees reporting to managers in previous level
    SELECT 
        e.employee_id,
        e.first_name,
        e.last_name,
        e.manager_id,
        oc.level + 1
    FROM Employees e
    JOIN OrgChart oc ON e.manager_id = oc.employee_id
)
SELECT 
    employee_id,
    CONCAT(first_name, ' ', last_name) AS employee_name,
    level
FROM OrgChart
ORDER BY level, last_name, first_name;

-- 25th
SELECT p.product_id, p.product_name, p.price,
    AVG(r.rating) AS avg_rating,
    -- This is a simple correlation indicator 
    CASE 
        WHEN AVG(r.rating) > 3.5 AND p.price > 500 THEN 'High price, high rating'
        WHEN AVG(r.rating) > 3.5 AND p.price <= 500 THEN 'Low price, high rating'
        WHEN AVG(r.rating) <= 3.5 AND p.price > 500 THEN 'High price, low rating'
        ELSE 'Low price, low rating'
    END AS price_rating_relationship
FROM Products p
LEFT JOIN Reviews r ON p.product_id = r.product_id
GROUP BY p.product_id, p.product_name, p.price
ORDER BY p.price DESC;