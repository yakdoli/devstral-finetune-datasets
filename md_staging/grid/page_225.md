```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: grid
page_number: 225
page_id: grid#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:03Z
fidelity: lossless
-->

## Drop-Down Form and User Control Cell

### Overview
- A custom control cell that displays a drop-down form or a user control in a grid cell can be created.
- A drop-down form in a grid cell can be created by deriving GridStaticCellModel/GridStaticCellRenderer classes.
- A drop-down user control in a grid cell can be created by deriving GridDropDownCellModel/GridDropDownCellRender classes.
- The actions mentioned can be performed using code examples in C# and VB.NET.

### Content

#### Creating a Drop-Down Form in a Grid Cell
To create a drop-down form in a grid cell, you will need to register the custom cell type and set the `CellType` property to specify which cells will use this drop-down form.

#### Using C#

```csharp
// Register your custom cell type.
this.gridControl1.CellModels.Add("DropDownForm", new DropDownFormCellModel(this.gridControl1.Model, new DropDownForm()));

// Set the style.CellType for the cells.
this.gridControl1[2, 2].CellType = "DropDownForm";
```

#### Using VB.NET

```vb.net
' Register your custom cell type.
Me.gridControl1.CellModels.Add("DropDownForm", New DropDownFormCellModel(Me.gridControl1.Model, New DropDownForm()))

' Set the style.CellType for the cells.
Me.gridControl1(2, 2).CellType = "DropDownForm"
```

#### Creating a Drop-Down User Control in a Grid Cell
To create a drop-down user control in a grid cell, you will need to register the custom cell type and set the `CellType` property to specify which cells will use this drop-down user control.

#### Using C#

```csharp
// Register your custom cell type.
this.gridControl1.CellModels.Add("DropDownUserControl", new DropDownUserCellModel(this.gridControl1.Model, new DropDownUser()));

// Set the style.CellType for the cells.
this.gridControl1[6, 2].CellType = "DropDownUserControl";
```

### API Reference
The grid control provides the following methods to create custom drop-down forms and user controls:

- `GridStaticCellModel`
- `GridStaticCellRenderer`
- `GridDropDownCellModel`
- `GridDropDownCellRender`

These classes can be derived to create custom cell types that display drop-down forms or user controls.

### Code Examples

#### C# Example
```csharp
this.gridControl1.CellModels.Add("DropDownForm", new DropDownFormCellModel(this.gridControl1.Model, new DropDownForm()));
this.gridControl1[2, 2].CellType = "DropDownForm";

this.gridControl1.CellModels.Add("DropDownUserControl", new DropDownUserCellModel(this.gridControl1.Model, new DropDownUser()));
this.gridControl1[6, 2].CellType = "DropDownUserControl";
```

#### VB.NET Example
```vb.net
Me.gridControl1.CellModels.Add("DropDownForm", New DropDownFormCellModel(Me.gridControl1.Model, New DropDownForm()))
Me.gridControl1(2, 2).CellType = "DropDownForm"

Me.gridControl1.CellModels.Add("DropDownUserControl", New DropDownUserCellModel(Me.gridControl1.Model, New DropDownUser()))
Me.gridControl1(6, 2).CellType = "DropDownUserControl"
```

### RAG Annotations
<!-- tags: [Syncfusion, Winforms, Grid, Drop-down form, User control, Custom cell] keywords: [GridStaticCellModel, GridStaticCellRenderer, GridDropDownCellModel, GridDropDownCellRender, Drop-down form, User control, Custom cell] -->
```