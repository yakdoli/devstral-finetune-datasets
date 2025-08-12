```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_917.jpeg
document_name: grid
page_number: 917
page_id: grid#page_917
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:29Z
fidelity: lossless
-->

## SelectionMode Configuration in Essential Grid for Windows Forms

### Overview

This section details the configuration of selection modes in the Essential Grid for Windows Forms, specifically focusing on the `SelectionMode.One` and `SelectionMode.MultiSimple` options. These selection modes dictate the behavior of item selection in the grid's list box.

### SelectionMode - One

The `SelectionMode.One` configuration allows selection of a single item at a time in the grid's list box.

#### Code Examples

**C#:**
```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.One;
```

**VB.NET:**
```vb
Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.One
```

#### Visual Representation

![Figure 333: Selection Mode set to "One"](images/2025-08-09T06:48:29Z.png)

**Figure 333:** Selection Mode set to "One"

### SelectionMode - MultiSimple

The `SelectionMode.MultiSimple` configuration allows multiple items to be selected individually. Unlike `SelectionMode.One`, it does not support the use of SHIFT, CTRL, and ARROW keys to extend the selection.

#### Explanation

You would be able to select multiple items individually. It does not support the use of SHIFT, CTRL, and ARROW keys to extend the selection.

#### Code Examples

**C#:**
```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiSimple;
```

**VB.NET:**
```vb
Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiSimple
```

---
<!-- tags: [winforms, gridgroupingcontrol, selectionmode, oneselectmode, multisimpleselectmode, syncfusion] keywords: [selectionmode, listboxselectionmode, gridgroupingcontrol, windowsforms, csharp, vb.net, singleitem, multipleitems] -->
```