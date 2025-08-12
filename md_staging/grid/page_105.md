```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: grid
page_number: 105
page_id: grid#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:25:59Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Demonstrates setting the background color of cells in a Virtual Grid.
- Explains handling events to retrieve data for the Virtual Grid.

### Content

#### 3.1.5.5 Handling Events to Retrieve Data for Virtual Grid

To retrieve data for the Virtual Grid from the external data source:

1. **Add event handlers for the `QueryRowCount` and `QueryColCount` events.** Use the following code in your event handlers.
   
   The `GridQueryRowCount` and `GridQueryColCount` provide the numbers of rows and columns from the external data source. Thus, the implementation code will access the public properties of our external data object to get these values.

```csharp
[C#]

// Set number of rows from external data source.
void GridQueryRowCount(object sender, GridRowColCountEventArgs e)
{
    e.Count = this._extData.RowCount;
}
```

**Figure 65: Virtual Grid with Back Color set for Cells**

![Virtual Grid with Back Color set for Cells](image.png)

### API Reference

#### Events
- **GridQueryColCount**: Provides the number of columns from the external data source.
- **GridQueryRowCount**: Provides the number of rows from the external data source.

### Code Examples

#### VB.NET Code
```vb
If ((Me._extData(e.RowIndex - 1, e.ColIndex - 1) Mod 3) = 0) Then
    e.Style.BackColor = Color.LightPink
End If
e.Handled = True
End If
End Sub
```

#### C# Code
```csharp
[C#]

// Set number of rows from external data source.
void GridQueryRowCount(object sender, GridRowColCountEventArgs e)
{
    e.Count = this._extData.RowCount;
}
```

### RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Virtual Grid, Event Handling, Data Retrieval, GridQueryRowCount, GridQueryColCount, Cell Background Color, External Data Source] -->
```