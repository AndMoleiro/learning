with source_orders as (
    select * from {{ source("jaffle_shop", "orders") }}
),

source_customers as (
    select * from {{ source("jaffle_shop", "customers") }}
),

select
    source_orders.*,
    source_customers.*
from
    source_orders.



transform as (
    select
        id as customer_id,
        first_name as customer_first_name,
        last_name as customer_last_name
    from source
)

select * from transform



transform as (
    select
        id as order_id,
        user_id as customer_id,
        order_date as order_placed_at,
        status as order_status
    from source
)

select * from transform