```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_911.jpeg
document_name: grid
page_number: 911
page_id: grid#page_911
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:17Z
fidelity: lossless
-->

# **Essential Grid for Windows Forms**

## Overview

- Explains how to wire the GridGroupingControl with the Field Chooser.
- Demonstrates disabling the `EnableColumnsInView` property.
- Describes the steps to view the Field Chooser dialog.

## Content

### Wiring the GridGroupingControl with the Field Chooser

Here is the code snippet used to wire the `GridGroupingControl` with the field chooser.

```csharp
// wire the GridGroupingControl with the field chooser.
FieldChooser fchooser = new FieldChooser(this.gridGroupingControl1);
```

#### Disabling the `EnableColumnsInView` Property

Here is the code snippet used to disable the `EnableColumnsInView` property:

```csharp
//disable the EnableColumnsInView property
fchooser.EnableColumnsInView = false;
```

#### VB Implementation

```vb
'Wire the GridGroupingControl with the field chooser.
Dim fchooser As FieldChooser = New FieldChooser(Me.gridGroupingControl1)
'Disable the EnableColumnsInView property
fchooser.EnableColumnsInView = False
```

### Steps to View the Field Chooser Dialog

1. **Open the Grid:** When the code runs, the entire grid will open.
2. **Access the Field Chooser Menu:**
   - Right-click on a column header and select the **Field Chooser** menu item to view the Field Chooser dialog.

#### Figure 328: Field Chooser

![Field Chooser](image.png)

_This image shows the Field Chooser dialog, listing all column names with check boxes adjacent to them._

3. **Field Chooser Dialog:** This dialog will list all the column names with check boxes adjacent to them.

---

## Code Examples

### C# Example

```csharp
FieldChooser fchooser = new FieldChooser(this.gridGroupingControl1);
fchooser.EnableColumnsInView = false;
```

### VB Example

```vb
Dim fchooser As FieldChooser = New FieldChooser(Me.gridGroupingControl1)
fchooser.EnableColumnsInView = False
```

## Cross References

- See also: `GridGroupingControl`, `FieldChooser`, `EnableColumnsInView`.

<!-- tags: [Syncfusion, Winforms, GridGroupingControl, FieldChooser, EnableColumnsInView] keywords: [Field Chooser, GridGroupingControl, EnableColumnsInView, Windows Forms] -->
```