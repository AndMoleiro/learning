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