# # Write your MySQL query statement below
SELECT ROUND(COUNT(B.order_date)/COUNT(*)*100,2) AS immediate_percentage FROM (SELECT d.delivery_id
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS min_order_date
    FROM Delivery
    GROUP BY customer_id
) subquery
ON d.customer_id = subquery.customer_id AND d.order_date = subquery.min_order_date
GROUP BY d.customer_id, d.delivery_id) as A LEFT JOIN Delivery B ON A.delivery_id=B.delivery_id AND B.order_date=B.customer_pref_delivery_date ;

# SELECT d.customer_id, d.delivery_id, COUNT(*) AS delivery_count
# FROM Delivery d
# JOIN (
#     SELECT customer_id, MIN(order_date) AS min_order_date
#     FROM Delivery
#     GROUP BY customer_id
# ) subquery
# ON d.customer_id = subquery.customer_id AND d.order_date = subquery.min_order_date
# GROUP BY d.customer_id, d.delivery_id;
