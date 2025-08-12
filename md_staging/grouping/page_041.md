```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: grouping
page_number: 041
page_id: grouping#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:27Z
fidelity: lossless
-->

# Essential Grouping

```vb
Sub Main()
    ' Create an ArrayList of random MyObjects.
    Dim list As New ArrayList()
    Dim r As New Random()

    Dim i As Integer
    For i = 0 To 10
        list.Add(New MyObject(r.Next(5)))
    Next

    ' Create a Grouping.Engine object.
    Dim groupingEngine As New Engine()

    ' Set its data source.
    groupingEngine.SetSourceList(list)
End Sub
```

10. You are now ready to apply a filter to the data. Say for example you want to see only those items whose property D has the value d1. You must observe that D is a string that has non-numeric values. So, in this case you will need to use one of the string comparison operators (LIKE or MATCH) in your filter condition.

11. To add a filter condition, you will need to add a `RecordFilterDescriptor` to the `Engine.TableDescriptor.RecordFilters` collection.

### Do the following steps:

1. List the data before the filter.
2. Apply the filter by creating a `RecordFilterDescriptor`.
3. Add it to the `RecordFilters` collection.
4. List the filtered data.

**Note:** To list the data, instead of accessing the `Table.Records` collections, you were using the `Table.FilteredRecords` collections. The `FilteredRecords` collection only includes the records that satisfy all filters in the `RecordFilters` collection. Add this code at the end of the Main method.

12. Note that the constructor on the `RecordFilterDescription` takes an expression, `[D] LIKE 'd1'`. This expression will be `True` only for those items in the list where property D has the value d1.

```csharp
// Display the data before filtering.
```

## API Reference

- **Namespace:** `Syncfusion.Windows.Forms.Grouping`
- **Class:** `RecordFilterDescriptor`

### Methods and Properties
- `SetSourceList`: Method to set the data source for the grouping engine.

## Code Examples

Extracting all code exactly:

```csharp
// Display the data before filtering.
```

### Using the RecordFilterDescriptor

```csharp
// Example of using RecordFilterDescriptor to filter records.
```

## Page-level Navigation/TOC

- Creating and setting up a grouping engine.
- Applying filters using `RecordFilterDescriptor`.

<!-- tags: [grouping, filter, recordfilterdescriptor, data filtering, syncfusion winforms, version 11.4.0.26] keywords: [essentials, grouping engine, recordfilterdescriptor, filtering data, syncfusion, winforms] -->
```