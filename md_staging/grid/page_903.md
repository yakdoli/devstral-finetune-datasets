```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_903.jpeg
document_name: grid
page_number: 903
page_id: grid#page_903
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Dim csd As GridColumnSetDescriptor = New GridColumnSetDescriptor()
csd.ColumnSpans.Add(csd0)
csd.ColumnSpans.Add(csd1)
csd.ColumnSpans.Add(csd2)
csd.ColumnSpans.Add(csd3)
```

3. Finally bind this ColumnSet to the grid by adding the above created GridColumnSetDescriptor into the TableDescriptor.ColumnSets property.

```csharp
this.gridGroupingControl1.TableDescriptor.ColumnSets.Add(csd);
```

```vb
Me.gridGroupingControl1.TableDescriptor.ColumnSets.Add(csd)
```

4. Here is a sample output.

![](https://via.placeholder.com/500x200?text=Figure%20361%3A%20Spanning%20Records%20across%20Multiple%20Rows)

## Through Designer

To create ColumnSets that defines the ColumnSpans for a grid, select the TableDescriptor.ColumnSets property in the property window. This will open the GridColumnSetDescriptor Collection Editor that will let you specify the columns to span and the range, for each of the columns.

```


<!-- tags: [Syncfusion Winforms, GridControl, ColumnSpan, Designer] keywords: [Essential Grid, Windows Forms, TableDescriptor, ColumnSets, GridColumnSetDescriptor, Column Span, Designer] -->
```