```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_260.jpeg
document_name: tools
page_number: 260
page_id: tools#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
MessageBox.Show(siblingcontrol.Name);
Next tabpage
End If
```

## Overview
- Explains how to avoid flickering while creating MDI child forms.
- Instructions for determining if a control is in MDI mode.

## Content

### 3.4.4.4 MDIChild

This section covers the following topics:

#### 3.4.4.4.1 How to avoid flickering while creating MDI child form?

Flickering can be avoided by calling the following methods:

LockHostFormUpdate and UnlockHostFormUpdate Methods - The LockHostFormUpdate and UnlockHostFormUpdate methods are used to lock and unlock the host form's updates respectively. These methods help in avoiding flickering while creating an MDI child form, and they can be used in the following way.

#### Code Examples

##### C#

```csharp
// To avoid flickering
this.dockingManager1.LockHostFormUpdate();
this.dockingManager1.DockControl(form, this, Syncfusion.Windows.Forms.Tools.DockStyle.Right, 0);
this.dockingManager1.SetAsMDIChild(form, true);
this.dockingManager1.SetControlSize(form, size);
this.dockingManager1.UnlockHostFormUpdate();
```

##### VB.NET

```vb
' To avoid flickering
Me.dockingManager1.LockHostFormUpdate()
Me.dockingManager1.DockControl(form, Me, Syncfusion.Windows.Forms.Tools.DockStyle.Right, 0)
Me.dockingManager1.SetAsMDIChild(form, True)
Me.dockingManager1.SetControlSize(form, size)
Me.dockingManager1.UnlockHostFormUpdate()
```

#### 3.4.4.4.2 How to detect whether a particular control is in MDI mode or not?

To know whether the control is in MDI mode or not, the following method can be called.

---

## API Reference

- Members related to MDIChild functionality in the Syncfusion.Winforms library.

## Code Examples (multi-language supported)

- Examples demonstrate the use of `LockHostFormUpdate` and `UnlockHostFormUpdate` methods in both C# and VB.NET.

## Page-level Navigation/TOC (if applicable)

- This section provides a detailed explanation of the steps to avoid flickering and check MDI mode.

## Cross References

- Refer to related topics on MDI functionality in the Syncfusion.Winforms documentation.

---

<!-- tags: [Syncfusion Winforms, MDIChild, LockHostFormUpdate, UnlockHostFormUpdate, MDI mode, C#, VB.NET, flickering, essential tools] keywords: [MDIChild, flickering, LockHostFormUpdate, UnlockHostFormUpdate, MDI mode, essential tools] -->
```