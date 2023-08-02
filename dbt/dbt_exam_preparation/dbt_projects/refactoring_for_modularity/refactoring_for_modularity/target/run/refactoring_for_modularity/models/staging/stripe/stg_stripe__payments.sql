
  create or replace   view analytics.DBT_AMOLEIRO.stg_stripe__payments
  
   as (
    with
    source as (select * from raw.stripe.payment where status <> 'fail'),

    transform as (
        select
            orderid as order_id,
            status as order_status,
            max(created) payment_finalized_date,
            sum(amount) / 100.0 as total_amount_paid
        from source
        group by order_id, order_status
    )

select *
from transform
  );

