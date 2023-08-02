with
    paid_orders as (select * from analytics.DBT_AMOLEIRO.int_paid_orders),

    customers as (select * from analytics.DBT_AMOLEIRO.stg_jaffle_shop__customers),

    paid_orders_with_customer_info as (
        select
            paid_orders.*, customers.customer_first_name, customers.customer_last_name
        from paid_orders
        left join customers on paid_orders.customer_id = customers.customer_id
    ),

    final as (
        select
            customer_id,
            order_id,
            order_placed_at,
            order_status,
            total_amount_paid,
            payment_finalized_date,
            customer_first_name,
            customer_last_name,
            transaction_seq,
            customer_sales_seq,
            nvsr,
            customer_lifetime_value,
            fdos
        from paid_orders_with_customer_info
        order by order_id
    )

select *
from final