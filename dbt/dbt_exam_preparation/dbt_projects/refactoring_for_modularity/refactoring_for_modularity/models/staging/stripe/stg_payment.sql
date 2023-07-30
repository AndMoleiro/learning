with source as (
    select * from {{ source("stripe", "payment") }}
),

transform as (
    select 
        orderid as order_id,
        status as payment_status,
        created,
        amount
    from source
)

select * from transform