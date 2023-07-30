with source as (
    select * from raw.jaffle_shop.customers
),

transform as (
    select
        id as customer_id,
        first_name as customer_first_name,
        last_name as customer_last_name
    from source
)

select * from transform