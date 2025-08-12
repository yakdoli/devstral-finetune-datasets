```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_596.jpeg
document_name: grid
page_number: 596
page_id: grid#page_596
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Steps to bind the grid grouping control to a data source.
- Adding the grid grouping control to the form.
- Visual representation of the grid bound to an MDB file.

## Content

### Setting the Data Source

[C#]

```csharp
this.gridGroupingControl.DataSource = dtSet.Tables[0];
```

[VB.NET]

```vb
Me.GridGroupingControl.DataSource = dtSet.Tables(0)
```

#### Adding the Grid Grouping Control to the Form

[C#]

```csharp
this.Controls.Add(this.gridGroupingControl1);
```

[VB.NET]

```vb
Me.Controls.Add(Me.GridGroupingControl1)
```

### Visual Output

6. When you run the application, the grid will look like the one in the following image.

![Figure 240: Binding a Grid Grouping control to an MDB File](https://syncfusion.com/documentation/images/figure240.png)

**Figure 240: Binding a Grid Grouping control to an MDB File**

### Section on Manual Data Source

### 4.3.1.2.2 Bind a Grid Grouping Control to a Manual Data Source

This section explains how to bind a Grid Grouping Control to a manual data source.

```html
<!-- tags: [syncfusion, grid, windows forms, data binding, grid grouping control, manual data source] keywords: [binding, grid, windows forms, grid grouping control, manual data source] -->
```
```