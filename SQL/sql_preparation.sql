SELECT * FROM ecommerce.products;

create view prod_cate_sales as
select products.product_category as category,
round(sum(payments.payment_value)) as sales
from products join order_items
on products.product_id = order_items.product_id
join payments
on payments.order_id = order_items.order_id
group by category; 


-- select *, case
-- when sales <= 10000 then 'Low'
-- when sales >=100000 then 'high'
-- else 'medium'
-- end as sales_type
-- from a;


