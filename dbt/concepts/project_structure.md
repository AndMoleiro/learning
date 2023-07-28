# Model Types

## Staging

### Model Types 
`base_`, `stg_`

- Typically a 1:1 reflection of the source data
- Light Transformations
- Common SQL: casting, renaming, filtering deleted records
- No joining *

### Purpose

To clean up and standardize raw data for use in downstream models


## Marts

### Model Types 
`int_`, `dim_`, `fct_`

- Apply business logic
- Hevier transformations than staging
- Common SQL: joins, unions, case whens, window functions

### Purpose

To form the data using our business perspectives in order to build our core entities


# Layering concepts

## Raw, Base and Staging

![dbt_dag](/dbt/concepts/imgages/dbt_dag.png)


In this example, if we stage the ingredients that make up italian dressing (most notably vinegar and italian seasoning, but also water and oil), it's not going to be easy to take the ingredients and make italian dressing, as they would have to be mixed every time.
- This is one of those specific use cases for doing a join in staging, because, at this stage, vinegar and italian dresing are useless until they form the italian dressing.
- In order to do this join, we'll implement a base layer. This layer takes over what staging usually does
    - We do this because we always want to have a model that standardizes our data, whether it be a base or staging model, so our downstream models can benefit from that transformation and we can start developing consistency in how our data is commonly used.

![dbt_dag_2](/dbt/concepts/imgages/dbt_dag_2.png)

Adding to this, lets consider boiling eggs in staging. Should we?
- Yes, if we only make salads
- No, if we serve breakfast
If we boiled the eggs, when prepping my ingredients, we wouldn't be able to create scrambled eggs

## Intermediate and Dimensions & Facts

Now, we're going to build the intermediate layer, where major data transformations will take place
- This layer is optional, but it's especially useful for creating reusable components or breaking up large transformations into more understandable pieces.
- Finally, we'll join in all of those steps in order to make the salad

![dbt_dag_final](/dbt/concepts/imgages/dbt_dag_3.png)

- With this structure, it's possible to get a custo salad without eggs
