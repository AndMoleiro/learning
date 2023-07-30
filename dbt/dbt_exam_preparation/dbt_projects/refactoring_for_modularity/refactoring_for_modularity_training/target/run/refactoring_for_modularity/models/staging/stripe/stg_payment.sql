
  create or replace   view analytics.DBT_AMOLEIRO.stg_payment
  
   as (
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
  );

