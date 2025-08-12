```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_837.jpeg
document_name: tools
page_number: 837
page_id: tools#page_837
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Create an instance of the MaskedEditBox control.
- Set MaskedEditBox.Mask property.
- Add the MaskedEditBox control to the form.

## Content

### Step 1: Create an instance of the MaskedEditBox control.

```csharp
private Syncfusion.Windows.Forms.Tools.MaskedEditBox maskedEditBox1;
this.maskedEditBox1 = new MaskedEditBox();
```

```vb.net
Private maskedEditBox1 As Syncfusion.Windows.Forms.Tools.MaskedEditBox
Me.maskedEditBox1 = New MaskedEditBox()
```

### Step 2: Set MaskedEditBox.Mask property.

```csharp
// The mask string.
this.maskedEditBox1.Mask = ">?<????????????";
this.maskedEditBox1.Location = new System.Drawing.Point(70, 29);
```

```vb.net
' The mask string.
Me.maskedEditBox1.Mask = ">?<????????????"
Me.maskedEditBox1.Location = New System.Drawing.Point(70, 29)
```

### Step 3: Add the MaskedEditBox control to the form.

```csharp
this.Controls.Add(this.maskedEditBox1);
```

```vb.net
Me.Controls.Add(Me.maskedEditBox1)
```

## Code Examples

### C#

```csharp
private Syncfusion.Windows.Forms.Tools.MaskedEditBox maskedEditBox1;

this.maskedEditBox1 = new MaskedEditBox();
this.maskedEditBox1.Mask = ">?<????????????";
this.maskedEditBox1.Location = new System.Drawing.Point(70, 29);
this.Controls.Add(this.maskedEditBox1);
```

### VB.NET

```vb.net
Private maskedEditBox1 As Syncfusion.Windows.Forms.Tools.MaskedEditBox

Me.maskedEditBox1 = New MaskedEditBox()
Me.maskedEditBox1.Mask = ">?<????????????"
Me.maskedEditBox1.Location = New System.Drawing.Point(70, 29)
Me.Controls.Add(Me.maskedEditBox1)
```

<!-- tags: Syncfusion Winforms, MaskedEditBox, control, MaskedEditBox.Mask, version: 11.4.0.26 -->
```