```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: grouping
page_number: 028
page_id: grouping#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:24Z
fidelity: lossless
-->

# Essential Grouping

```vb
Imports Syncfusion.Grouping
```

Then create a `Grouping.Engine` object and set the `ArrayList` we created to be its data source.

**Note:** For more details on creating array list, refer to the **Creating an ArrayList Of Objects** topic.

### Creating a Grouping Engine Object

#### C#

```csharp
// Put this code in the Main function after Console.ReadLine().
// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its data source.
groupingEngine.SetSourceList(list);
```

#### VB.NET

```vb
Imports Syncfusion.Grouping

' Put this code in the Main function after Console.ReadLine().
' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its data source.
groupingEngine.SetSourceList(list)
```

ArrayList of Objects is set as the datasource for the Grouping engine.

### 4.1.3 Iterating Through the Data

Now, we have set a datasource in the Grouping Engine. Let's see how to iterate through the data.

This section will show you how to access the data through the `Grouping.Engine` object by using the `Engine.Table.Records` collection.

### Summary

- Created a `Grouping.Engine` object and set its data source to an `ArrayList`.
- Demonstrated how to iterate through the data using the `Engine.Table.Records` collection.

### Next Steps

Explore how to manipulate and display the grouped data in a grid or similar UI component.

<!-- tags: [grouping, datasource, ArrayList, Grouping.Engine, iteration, records, WinForms] keywords: [grouping engine, arraylist, iterating through data, engine.table.records, syncfusion group, syncfusion data engine] -->
```