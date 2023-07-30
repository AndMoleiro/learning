with source as (
    select * from raw.stripe.payment
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