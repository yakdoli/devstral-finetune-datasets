```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_360.jpeg
document_name: XlsIO
page_number: 360
page_id: XlsIO#page_360
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:30Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
//Creates the data sorter
IDataSort sorter = book.CreateDataSorter();

//Range to sort
sorter.SortRange = range;

//Adds the sort field with the column index, sort based on and order by attribute
ISortField sortField = sorter.SortFields.Add(0, SortOn.Values, OrderBy.Ascending);

//Adds another sort field
ISortField sortField2 = sorter.SortFields.Add(1, SortOn.Values, OrderBy.Ascending);

//Sort based on the sort Field attribute
sorter.Sort();
```

```vb
'Creates the Data sorter
Dim sorter As IDataSort = book.CreateDataSorter()
'Specifies the sort range
sorter.SortRange = range
Dim field As ISortField
' Adds the sort field with column index, sort based on and order by attribute
field = sorter.SortFields.Add(2, SortOn.Values, OrderBy.OnTop)
' Adds the second sort field
field = sorter.SortFields.Add(2, SortOn.Values, OrderBy.OnTop)
' Sorts the data with the sort field attribute
sorter.Sort()
```

## 4.5.3.3 Sorting by Font Color

With this feature, MS Excel moves the text that is applied with the selected color to the specified location (bottom or top) of the sorting range.
```