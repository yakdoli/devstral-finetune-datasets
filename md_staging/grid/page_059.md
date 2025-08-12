```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: grid
page_number: 059
page_id: grid#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

---

## Overview

- Designer setup and configuration of the `GridGroupingControl` in Windows Forms.
- Step-by-step guide to loading data into the Grid control and setting properties.
- Implementation instructions for handling `Load` events to populate the dataset.
- Detailed instructions on setting the `Anchor` property for dynamic sizing.

---

## Content

### Designer with Grid Grouping Control

Figure 22 shows the designer interface with a `GridGroupingControl` and the setup for setting the `DataSource` property.

![](attachment:gridGroupingControl.png)

#### Setting Up the Load Event Handler

1. Double-click the form on the design surface to add a Load event handler. In this handler, add the following code.

##### C#
```csharp
this.oleDbDataAdapter.Fill(this.dataSet11);
```

##### VB.NET
```vb
Me.oleDbDataAdapter.Fill(Me.dataSet11)
```

The preceding code is used to load the data from the `DataTable`. Without this code, you will see an empty `GridGroupingControl` at runtime.

### Setting the Anchor Property

Finally, set the `Anchor` property of the `GridGroupingControl` to `All`, so that the Grid Grouping control can be easily sized with the form. This is depicted in the following screenshot.

---

## Code Examples

### C#
```csharp
private void Form_Load(object sender, EventArgs e)
{
    this.oleDbDataAdapter.Fill(this.dataSet11);
}
```

### VB.NET
```vb
Private Sub Form_Load(sender As Object, e As EventArgs)
    Me.oleDbDataAdapter.Fill(Me.dataSet11)
End Sub
```

---

## RAG Annotations
<!-- tags: [GridGroupingControl, DataSourceProperty, LoadEvent, AnchorProperty, WindowsForms, Syncfusion] keywords: [Designer, Form, DataAdapter, DataSet, Grid Control, Data Binding, Event Handler, Property, Size] -->
```