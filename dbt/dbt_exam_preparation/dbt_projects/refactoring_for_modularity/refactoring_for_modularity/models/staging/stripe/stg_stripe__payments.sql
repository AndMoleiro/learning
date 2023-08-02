with
    source as (select * from {{ source("stripe", "payment") }} where status <> 'fail'),

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
