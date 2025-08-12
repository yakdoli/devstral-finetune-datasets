<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_806.jpeg
document_name: grid
page_number: 806
page_id: grid#page_806
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the concept of foreign-key relationships in databases.
- Demonstrates setting up a ForeignKeyReference relation between a data table and a collection.
- Provides steps to create and configure a USStates collection.

## Content

### 4.3.4.3.5.2 Foreign Key Reference Relation

**ForeignKeyReference** is a foreign-key relation for looking up values where an id column in the main table can be used to look up a record in a related table. This is an n:1 relation where multiple records in the parent table can reference the same record in the related table. Fields in the related table can be referenced using a '.' dot in the `FieldDescriptor.MappingName` of the main table.

#### Steps to setup ForeignKeyReference relation

This section sets up a foreignkeyreference relation between a data table and the collection `USStates`. The data table represents the Parent Table of the relation and the `USStates` collection serves as the related child list where in the values can be looked up using a key. The collection derives from `ArrayList` in which every item is an `USState` object having two properties named `Key` and `Name`. It also defines a method named `CreateDefaultCollection()` that returns an instance of itself populated with a set of values.

A foreignkeyreference relation can be set up between the lists by defining a relation descriptor with its attributes carrying the relation details and adding this descriptor to the Relations collection of the main table.

The following steps demonstrate this process.

1. Create a collection named `USStates` in which each entry stores a `USState` object.

```csharp
// US States Collection.
[Serializable]
public class USStatesCollection : ArrayList
{
    public new USState this[int index]
    {
        get
        {
            return (USState) base[index];
        }
        set
        {
            base[index] = value;
        }
    }

    public static USStatesCollection CreateDefaultCollection()
}
```

## API Reference (if applicable)

## Code Examples (multi-language supported)
- The code snippet above demonstrates how to create a custom collection (`USStatesCollection`) that derives from `ArrayList` and stores `USState` objects.

## Cross References
- Refer to the Syncfusion documentation for more details on relation descriptors and how to configure them in the grid.

<!-- tags: [database, foreign key, relation, Windows Forms, USStates, collection] keywords: [ForeignKeyReference, relation descriptor, ArrayList, USState, CreateDefaultCollection] -->