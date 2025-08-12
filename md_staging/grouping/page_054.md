```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: grouping
page_number: 054
page_id: grouping#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:56Z
fidelity: lossless
-->

## Essential Grouping

### Overview
- This page demonstrates the use of `Grouping.Engine` in Syncfusion Winforms for handling data grouping and custom sorting.
- The example showcases how to create an `ArrayList` of `MyObject` instances and use the `Grouping.Engine` to display and sort the data.

### Content

The following code example illustrates how to create an `ArrayList` of random `MyObject` instances, set up the `Grouping.Engine`, display the data before sorting, and implement a custom sort for a specific column.

```csharp
// Create an arraylist of random MyObjects.
ArrayList list = new ArrayList();
Random r = new Random();

for(int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(20)));
}

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its datasource.
groupingEngine.SetSourceList(list);

// Display the data before sorting.
foreach(Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if(obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();

// Custom sort column A.
// Get an IComparer object to handle the custom sorting.
AComparer comparer = new AComparer();
groupingEngine.TableDescriptor.SortedColumns.Add("A");
groupingEngine.TableDescriptor.SortedColumns["A"].Comparer = comparer;

// Display the data before sorting.
foreach(Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if(obj != null)
    {
        Console.WriteLine(obj);
    }
}
```

#### Explanation
- **Creating Random Data**: The code starts by creating an `ArrayList` filled with instances of `MyObject`, using a `Random` object to assign values.
- **Initializing Grouping Engine**: A new instance of `Grouping.Engine` is created, and its data source is set to the `ArrayList`.
- **Displaying Data Before Sorting**: The `foreach` loop iterates through the `Records` collection, displaying the data before any sorting is applied.
- **Custom Sorting**: An `IComparer` object is created to handle custom sorting for column "A". This is applied to the `TableDescriptor.SortedColumns`.
- **Displaying Sorted Data**: After applying the custom sorting, the data is displayed again to show the sorted order.

## API Reference

### Namespaces and Types
- **System.Collections.ArrayList**
  - Represents a variable-size list that can grow and shrink dynamically.
- **System.Random**
  - Generates a sequence of random numbers.
- **Syncfusion.Grouping.Engine**
  - The class responsible for handling the grouping functionality.
- **Syncfusion.Grouping.Record**
  - Represents a single record in the grouping engine.
- **Syncfusion.Grouping.TableDescriptor**
  - Provides information about the columns and their sorting options.

### Methods and Properties
- **SetSourceList**
  - Sets the data source for the grouping engine.
- **Table.Records**
  - Accesses the collection of records in the table.
- **TableDescriptor.SortedColumns**
  - Allows specifying and configuring sorted columns in the table.

### Parameters
- **ArrayList**
  - The `ArrayList` object containing the dataset.
- **IComparer**
  - The custom comparer object used for sorting.

## Code Examples

The code example provided demonstrates:
1. Creating and populating an `ArrayList` with `MyObject` instances.
2. Setting up the `Grouping.Engine` with the populated `ArrayList`.
3. Displaying the data before and after custom sorting of column "A".

## Cross References
- Refer to the `MyObject` class documentation for more details on the object type used in this example.
- For more information on `IComparer` and custom sorting, refer to the appropriate documentation.

<!-- tags: [syncfusion winforms, grouping, group engine, sorting, custom comparer] keywords: [ArrayList, Random, Grouping.Engine, TableDescriptor, IComparer, sorting, filtering, records] -->
```