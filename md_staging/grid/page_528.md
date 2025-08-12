```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_528.jpeg
document_name: grid
page_number: 528
page_id: grid#page_528
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:06Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Content

The `PopulateValues` method is used to move values from a given data source into the specified grid range. The first parameter specifies the range of destination cells where the data is to be copied, and the second parameter specifies the data source for the destination cells.

#### a. Using C#

```csharp
[C#]

gridControl1.Model.PopulateValues(GridRangeInfo.Cells(top, left, bottom, right), this.intArray);
```

#### b. Using VB.NET

```vb
[VB.NET]

gridControl1.Model.PopulateValues(GridRangeInfo.Cells(top, left, bottom, right), Me.intArray)
```

---

### 3. Implementing Virtual Mode

Three events need to be handled in order to implement a virtual mode. They perform the following actions:

- Determine the number of rows
- Determine the number of columns
- Pass a value to a cell from a data source.

#### a. Using C#

```csharp
[C#]

// Determine number of rows.
this.gridControl1.QueryRowCount += new GridRowColCountEventHandler(GridQueryRowCount);
private void GridQueryRowCount(object sender, GridRowColCountEventArgs e)
{
    e.Count = this.numArrayRows;
    e.Handled = true;
}

// Determine the number of columns.
this.gridControl1.QueryColCount += new GridRowColCountEventHandler(GridQueryColCount);
private void GridQueryColCount(object sender, GridRowColCountEventArgs e)
{
    // implement your logic here
}
```

## API Reference (if applicable)
- Namespace: Syncfusion.Windows.Forms.Grid
- Members:
  - `PopulateValues`: Moves the values from a data source into a specified grid range.

### Code Examples (multi-language supported)

```csharp
[C#]
// Example: PopulateValues Usage
GridRangeInfo range = GridRangeInfo.Cells(top, left, bottom, right);
gridControl1.Model.PopulateValues(range, this.intArray);
```

```vb
[VB.NET]
' Example: PopulateValues Usage
Dim range As GridRangeInfo = GridRangeInfo.Cells(top, left, bottom, right)
gridControl1.Model.PopulateValues(range, Me.intArray)
```

### Cross References
- Refer to the `GridRowColCountEventHandler` API for more details on event handling.

#### RAG Annotations
<!-- tags: [grid, windows forms, populatevalues, virtual mode, c#, vb.net, api, events] keywords: [PopulateValues, GridRangeInfo, GridRowColCountEventHandler, virtual mode, data source, grid control, event handling] -->
```