```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_549.jpeg
document_name: tools
page_number: 549
page_id: tools#page_549
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- This page explains how to create and configure a `ComboDropDown` control in Windows Forms.
- It includes code snippets for both C# and VB.NET.
- Describes adding a `TreeView` in the drop-down portion of `ComboDropDown`.

## Content

### Creating a ComboDropDown Control

1. **Create an instance of the ComboDropDown control class.**

   **[C#]**
   ```csharp
   private Syncfusion.Windows.Forms.Tools.ComboDropDown comboDropDown1;
   this.comboDropDown1 = new Syncfusion.Windows.Forms.Tools.ComboDropDown();
   ```

   **[VB.NET]**
   ```vb
   Private comboDropDown1 As Syncfusion.Windows.Forms.Tools.ComboDropDown
   Me.comboDropDown1 = New Syncfusion.Windows.Forms.Tools.ComboDropDown()
   ```

2. **Add TreeView in the drop-down portion of ComboDropDown. Finally add ComboDropDown to the Form.**

   **[C#]**
   ```csharp
   this.comboDropDown1.PopupControl = this.treeView1;
   this.Controls.Add(this.comboDropDown1);
   ```

   **[VB.NET]**
   ```vb
   Me.comboDropDown1.PopupControl = Me.treeView1
   Me.Controls.Add(Me.comboDropDown1)
   ```

   **Note:** Refer to *Setting Interaction between ComboDropDown and TreeView* to set the interaction between the `ComboDropDown` and `TreeView`.

### See also

- **Concepts and Features**
- **3.5.5.1.3 Concepts and Features**

The following topics will help you become more familiar in using the ComboDropDown control.

### 3.5.5.1.3.1 ComboDropDown Text

The `ComboDropDown` control supports the properties which can change the appearance and behavior of the control's edit portion.

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

See also:
- **3.5.5.1.3 Concepts and Features**

<!-- tags: [WindowsForms, Tools, ComboDropDown, TreeView, Syncfusion, Winforms] keywords: [ComboDropDown, TreeView, pop-up control, edit portion, appearance, behavior] -->
```