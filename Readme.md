**Documentation for Airline management system**

This documentation will go through the steps required to simulate a database for any airline company.

1. The first step is to create a database which can done by using this command

```
    use database_name;
```

**Note**
*If there is no database with same name, it will create a new database with the same name.*

2. After creating a new database, we'll create collections where the data will be stored. In order to create collections, at least one document should be inserted. It can be done by the following command:

```
    db.collection_name.insert({
        ...
        field_1: "string",
        field_2: value,
        ...
      });
```

3.
