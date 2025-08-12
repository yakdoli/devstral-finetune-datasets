```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_591.jpeg
document_name: grid
page_number: 591
page_id: grid#page_591
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes methods `WireGrid` and `UnWireGrid` used to wire and unwire `FieldChooser` in Windows Forms.
- Provides examples of using these methods in C# and VB.
- Details steps to add `FieldChooser` for grid data bound grids.

## Content

| Method       | Description                              | Parameters         | Type                | Return Type                                                                                   | Reference links |
|--------------|------------------------------------------|---------------------|---------------------|-----------------------------------------------------------------------------------------------|------------------|
| WireGrid     | Used to wire the FieldChooser.         | Overloads: (Arg1)   | In GridWindowsForm | Example: GridDataBoundGrid1.WireGrid(GridDataBoundGrid).                                   | NA               |
| UnWireGrid   | Used to unwire the FieldChooser.       | NA                  | In GridWindowsForm | Example: GridDataBoundGrid1.Unwired().                                                       | NA               |

### Sample Link

You can find a sample for this feature in the following location:

```plaintext
..../AppData/Local/Syncfusion/EssentialStudio/9.4.0.49/Windows/Grid.Windows/Samples/2.
0/Data Bound/GDBG FieldChooser Demo
```

### Adding Field Chooser for Grid Data Bound Grid

1. **To add field chooser, pass data bound grid as the parameter of the `WireGrid` method.**  
   The following code illustrates this:

#### C#

```csharp
GridDataBoundFieldChooser fChooser = new GridDataBoundFieldChooser();
fChooser.WireGrid(this.GridDataBoundGrid1);
```

#### VB

```vb
Dim fchooser As GridDataBoundFieldChooser = New GridDataBoundFieldChooser()
fchooser.WireGrid(Me.GridDataBoundGrid1)
```

2. **When the code runs, the entire grid will open.**
3. **Right click on a column header and select the `Field Chooser` menu item to view the `Field Chooser` dialog.**

---

## API Reference

### Methods

#### WireGrid

- **Description**: Used to wire the `FieldChooser`.
- **Parameters**: Overloads: (Arg1)
- **Type**: In GridWindowsForm
- **Return Type**: Example: GridDataBoundGrid1.WireGrid(GridDataBoundGrid).

#### UnWireGrid

- **Description**: Used to unwire the `FieldChooser`.
- **Parameters**: NA
- **Type**: In GridWindowsForm
- **Return Type**: Example: GridDataBoundGrid1.Unwired().

---

## Code Examples

### C#

```csharp
GridDataBoundFieldChooser fChooser = new GridDataBoundFieldChooser();
fChooser.WireGrid(this.GridDataBoundGrid1);
```

### VB

```vb
Dim fchooser As GridDataBoundFieldChooser = New GridDataBoundFieldChooser()
fchooser.WireGrid(Me.GridDataBoundGrid1)
```

---

<!-- tags: [product, sdk, syncfusion, winforms, grid, data bound grid, field chooser] keywords: [WireGrid, UnWireGrid, GridDataBoundFieldChooser, field chooser dialog, grid windows form, data bound grid, c#, vb] -->
```