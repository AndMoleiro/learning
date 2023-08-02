
  create or replace   view analytics.DBT_AMOLEIRO.int_paid_orders
  
   as (
    with

    orders as (
        select * from analytics.DBT_AMOLEIRO.stg_jaffle_shop__orders
    ),

    payments as (
        select * from analytics.DBT_AMOLEIRO.stg_stripe__payments
    ),

    paid_orders as (
        select
            orders.*,
            payments.total_amount_paid,
            payments.payment_finalized_date,
            sum(total_amount_paid) over (
                partition by orders.customer_id 
                order by orders.order_id asc
                rows between unbounded preceding and current row) as customer_lifetime_value,
            row_number() over (order by orders.order_id) as transaction_seq,
            row_number() over (
                partition by orders.customer_id order by orders.order_id
            ) as customer_sales_seq
        from orders
        left join payments on orders.order_id = payments.order_id
    )

    select * from paid_orders
  );

