```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_091.jpeg
document_name: grid
page_number: 091
page_id: grid#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:34Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- This section explains how to bind a Grid to a dataset and update its properties to display data effectively.
- Steps include configuring the Grid Data Bound Grid, setting properties, and handling data loading events.

### Content

#### Designer with Grid Data Bound Grid and Button

**Figure 57: Designer with Grid Data Bound Grid and Button**
[![Figure 57](https://via.placeholder.com/600x400?text=Figure+57)](https://via.placeholder.com/600x400?text=Figure+57)

##### Step-by-Step Instructions

13. Click the Grid Data Bound Grid to display its properties in the **PropertyGrid**. Set these properties:

| DataSource      | DataSet11 |
|-----------------|------------|
| DisplayMember   | Products   |

14. Double-click the form on the design surface (not one of the controls, but the form itself) to add a load event handler. In this handler, add the following statement:

```csharp
// Load dataset with records.
this.sqlDataAdapter1.Fill(this.dataSet11);
```

### API Reference

None specified in this section.

### Code Examples

The following code snippet demonstrates loading a dataset in the form's load event handler:

```csharp
private void Form_Load(object sender, EventArgs e)
{
    // Load dataset with records.
    this.sqlDataAdapter1.Fill(this.dataSet11);
}
```

### Page-level Navigation/TOC
- [Overview](#overview)
- [Content](#content)

<!-- tags: [syncfusion, winforms, grid, griddata bound, dataset, load, event handler, propertygrid] keywords: [data binding, dataset11, products, sqladapter, load dataset, form load] -->
```