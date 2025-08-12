```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_777.jpeg
document_name: grid
page_number: 777
page_id: grid#page_777
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
Return pattern
End Function
```

**Note:** The 'Like' operator here is implemented similar to the 'Like' operator in VB.NET, where `"#"` character is considered as a character in patterns. Refer [http://msdn.microsoft.com/en-us/library/swf8kaxw.aspx](http://msdn.microsoft.com/en-us/library/swf8kaxw.aspx) for detailed information.

## Clearing Filters

Row Filters that are added for a table can be cleared by calling the `Clear()` method of the `RecordFilters` property.

### C#

```csharp
this.gridGroupingControl1.TableDescriptor.RecordFilters.Clear();
```

### VB.NET

```vb
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
```

**Note:** For more details, refer the following browser sample:

`<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Filters and Expressions\Filtering Tutorial`

### 4.3.4.3.4.2.1 Filter Bar

Grouping Grid provides in-built support for displaying a **Filter Bar** across the columns. It can be used to filter and unfilter the records at run time. It is very user interactive and more advantageous than using the `RecordFilters` collection. The main reason for its wide usage is that it could display various filter options for the columns. You can be able to add your own filter criteria too.

When the filter bar is applied, a new row (Filter Row) will be added at the top of the table displaying the filter options for the columns in a drop down. Each cell in the filter bar row is a simple `ComboBox` cell whose items are the filter options. The filter options for a given column includes one entry for each value in that column.

---

``` 
© 2013 Syncfusion. All rights reserved.          777 | Page
```

<!-- tags: [Syncfusion Winforms, Filter Bar, RecordFilters, TableDescriptor, Filters and Expressions] keywords: [FilterBar, ClearMethod, TableDescriptor, Recordfilters, FilterRow, ComboBox] -->
``` 
