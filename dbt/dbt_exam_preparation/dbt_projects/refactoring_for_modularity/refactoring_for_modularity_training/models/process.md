## Migrating code

1. Create a legacy folder
2. Add the old script to that folder

## Implementing sources

1. Look at the hardcoded references of the sources in the refactoring file
2. Create a staging folder
3. Create a folder inside staging for each of the raw sources
4. Create a sources.yml file inside each of the created folders. Eg:
```
version: 2

sources:
  - name: stripe
    database: raw
    tables:
      - name: payment
```

## Choosing a refactoring strategy

For this exercise, we'll follow a "side-by-side" strategy
1. Create a legacy folder inside models, and place the code to be refactored in there
2. Create a marts folder inside models, make a copy of the code to be refactored and add the "fct" prefix.

## CTE Groupings and Cosmetic Cleanups

### Cosmetic CLeanups

Making the code more readable and implementing best practices (subject to company policies)
1. Implement some white spaces
2. Break long lines

### CTE Groupings


Schema:

Import CTES

1. Replace source references with a CTE instead
  - These CTES stay very simple (select * plus some filters)
2. Change all the references from sources to the CTES
  - Don't change aliases at this point

Logical CTES

1. We'll start by looking at the nested subqueries, from the innermost to the outermost

- Final CTE
- Simple Select Statement

## Centralizing Transformations & Splitting up Models

### Staging models

1. We'll take our dependencies and move them into the staging section
- small transformations
- Column renames
2. For each of the staging ctes, we'll create a model inside the staging folder
3. Replace all refferences in the fct table

### CTES or Intermediate Models

1. Understand the data
2. Move any filters to upper ctes/models
3. Remove any unused code
4. Move aggregation to a separate cte
5. Move joining logic to intermediate models, if possible

### Final Model

