with
    source as (select * from {{ source("jaffle_shop", "orders") }}),

    transform as (
        select
            id as order_id,
            user_id as customer_id,
            order_date as order_placed_at,
            status as order_status,
            min(order_placed_at) over (partition by customer_id) as fdos,
            max(order_placed_at) over (
                partition by customer_id
            ) as most_recent_order_date,
            count(order_id) over (partition by customer_id) as number_of_orders,
            iff(fdos = order_placed_at, 'new', 'return') as nvsr
        from source
    )

select *
from transform
