with source as (
    select * from raw.jaffle_shop.orders
),

transform as (
    select
        id as order_id,
        user_id as customer_id,
        order_date as order_placed_at,
        status as order_status
    from source
)

select * from transform