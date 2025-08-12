```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: edit
page_number: 021
page_id: edit#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:07Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Set an appropriate size for the Edit Control.
- Configure the Dock property to desired DockStyle values.
- Assign an appropriate BorderStyle to the Edit Control.
- Add the Edit Control instance to the Host Form or UserControl.
- Run the application to test the settings.

## Content

### Step 3: Set an appropriate size for the Edit Control.

#### C#
```csharp
editControl1.Size = new Size(50, 50);
```

#### VB.NET
```vb
editControl1.Size = New Size(50, 50)
```

### Step 4: Set the Dock property to the appropriate DockStyle enumeration value if desired.

#### C#
```csharp
editControl1.Dock = DockStyle.Fill;
```

#### VB.NET
```vb
editControl1.Dock = DockStyle.Fill
```

### Step 5: Set an appropriate BorderStyle to the Edit Control instance.

#### C#
```csharp
editControl1.BorderStyle = BorderStyle.Fixed3D;
```

#### VB.NET
```vb
editControl1.BorderStyle = BorderStyle.Fixed3D
```

### Step 6: Add this instance of the Edit Control to the Host Form or an UserControl.

#### C#
```csharp
// Adding instance of the EditControl to the Host Form.
this.Controls.Add(editControl1);
```

#### VB.NET
```vb
' Adding instance of the EditControl to the Host Form.
Me.Controls.Add(editControl1)
```

### Step 7: Run the application.

---
© 2013 Syncfusion. All rights reserved. 21 | Page
<!-- tags: [essential edit, windows forms, c#, vb.net, dockstyle, borderstyle, editcontrol, windowsforms, application] keywords: [edit control size, docking properties, border style settings, adding controls, host form, usercontrol, run application] -->
```