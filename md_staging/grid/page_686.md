```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_686.jpeg
document_name: grid
page_number: 686
page_id: grid#page_686
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

**Note:** For more details, refer the following browser sample:

```plaintext
<Install Location>\Syncfusion\EssentialStudio\​[Version
Number]\Windows\Grid.Grouping.Windows\samples\2.0\Custom Collections\Array List Demo
```

## 4.3.4.2.3.4 Strongly Typed Collections

The Grid Grouping control can be bound to a Strongly Typed Collection. A Strongly Typed Collection is a collection that stores a Known Type. It can be viewed as an array of specific object. For example, suppose your application needs to store the information about products in a factory. You could create a Strongly Typed collection of Product objects.

### Benefits
- Since the collection knows the type of the object, it does not need to type cast the items between the type you are really storing and a generic object type stored in a collection.
- If you are writing the code to manage the collection items, then you can perform any other operations on the items that are being written into and read from the collection.

In this lesson, you will learn about the following topics.

### 4.3.4.2.3.4.1 Collection Base

This section demonstrates how to build a Strongly Typed Collection using CollectionBase class. A Strongly Typed collection can be created by inheriting from the System.Collections.CollectionBase class. The CollectionBase class implements IList, IListSource, and IEnumerable. These interfaces enable the users to implement the methods and properties that support binding, enumerating and looping using ForEach construct. The result is that your strongly typed collections can be bound directly to our grid grouping control as a datasource.

1. Create a class Product whose instances represent the records and properties represent the record fields.

```csharp
class Product
{
}
```

<!-- tags: [grid, strongly typed collections, collection base, syncfusion winforms, array list demo] keywords: [grid grouping control, product objects, type casting, binding, enumeration, iteration, foreach, datasource, collectionbase] -->
```