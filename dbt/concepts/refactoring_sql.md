# Implementing sources

Models should have a marts and staging folder

- In the staging folder, there should be a folder for each source schema that our queries pull from
    - In each of those subfolders, there should be a sources.yml file. Eg:  
    
    ```
    version: 2

    sources:
    - name: jaffle_shop
        database: raw
        tables:
        - name: customers
        - name: orders
    ```

- After configuring the source.yml files, we replace any hardcoded reverences with a source function referencing the sources we set up

# Choosing a refactoring strategy

Refactor along-side
- We leave the refactoring files untouched and create copies of those files
- Won't affect production in any way

# CTE Groupings and Cosmetic Cleanups

## Cosmetic Cleanups

- Implement white lines
- Break long lines
- Have lower case consistency accross the project

## CTE Groupings

### Order of CTES

1. Import CTEs -> Components (sources), etc..
2. Logical CTEs -> Subqueries, things that are happening in a certain order, etc...
3. Final CTE
4. Simple Select Statement

# Centralized Transformations & Splitting up models 

## Staging Models

1. Ignoring the import CTEs, identify where the staging CTEs are. These CTEs don't conduct any joins - notate above this section of CTEs with a comment that says -- staging.

2. Identify where the marts CTEs are. These CTEs conduct joins - notate above this section of CTEs with a comment that says -- marts.

3. Remove any redundant CTEs that conduct the same transformations on the same data sets. Replace all references to any removed CTEs with the proper references.

4. In the marts area, look at each field and identify the transformations that answer Yes to both of these questions:

- Can this transformation be done using one data set?
Is this transformation done on a field whose value is not due to a join?
For example: case when data_set.status is null looks like it can be done using one data set, but if the status is null because the row wasn't joined with other data, then doing this earlier than where the join occurs will result in incorrect calculations.
Move these transformations to the appropriate CTE under the -- staging section of code. Ensure that when you move these, you are:

- Removing redundant transformations
Re-referencing the CTE and field names correctly
Giving good names to fields that don't have a good name established

5. There was not a subquery that operated only on the payments table. Create a new CTE under the -- staging area that selects from the payments CTE, and continue moving transformations that belong to payment data following the rules in step 4.

Once you're done with the above, It's time to split out the code under -- staging and create models!

## CTEs or Intermediate Models

-  Big logical ctes should be moved to an intermediate model.

## Final model

- Link every model into a final one


# Audit

- Navigate to hub.getdbt.com and click on the audit_helper package.
- Check the diffs