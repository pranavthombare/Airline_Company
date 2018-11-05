**Documentation for Airline management system**

This documentation will go through the steps required to simulate a database for any airline company. Before that here are some basic commands to get through MongoDB:

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

3. The next step will be to save the data entered in the collections. This can be done by using the following command.

```
    db.collection_name.save();
```
**Note**
*In order to delete any document, use the following command with the correct parameters. In this example the document is deleted with their unique id.*

```
    db.collection_name.deleteOne({
      <field_name>: <parameter>
      });
```

*More parameters can be added in this query. Records will be deleted if the document matches the condition*

4. Follow steps 2-3 for every new collections and their respective documents. After you're done with populating the database, you can view them all with the **find()** function. The usage of it given below:

```
    db.collection_name.find();
```

This will give out all the documents present in the current collection. If you want to fetch the data with some constraints, you can specify them in the **find()** function like this:

```
    db.collection_name.find({<field_name>: <parameter>});
```

**Note**
*Another way of showing the data is by giving the output in JSON format. We can do that by using the pretty() function*

```
   db.collection_name.find().pretty();
```
