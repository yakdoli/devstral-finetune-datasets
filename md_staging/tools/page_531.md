```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_531.jpeg
document_name: tools
page_number: 531
page_id: tools#page_531
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to add and customize color groups in a Windows Forms application using Syncfusion controls.
- Illustrates the process of adding a custom `ColorGroup` and modifying its properties such as name, depth, and color items.
- Provides guidance on customizing both default and custom color groups.

## Content

### Figure 317: Custom ColorGroup added Through Designer

```csharp
[C#]

Syncfusion.Windows.Forms.Tools.GroupColorItem groupColorItem1 = new
Syncfusion.Windows.Forms.Tools.GroupColorItem(colorUIAdvGroup1, 
System.Drawing.Color.Crimson);
groupColorItem1.Color = System.Drawing.Color.Crimson;
groupColorItem1.Index = 0;
groupColorItem1.SubItems.Add(new
Syncfusion.Windows.Forms.Tools.ColorItem(groupColorItem1, 
System.Drawing.Color.LightPink));
colorUIAdvGroup1.Items.Add(groupColorItem1);
colorUIAdvGroup1.Name = "Custom User Colors";
colorUIAdvGroup1.SubItemsDepth = 1;
this.colorPickerUIAdv1.CustomGroups.Add(colorUIAdvGroup1);
```

```vb
[VB.NET]

Dim groupColorItem1 As New
Syncfusion.Windows.Forms.Tools.GroupColorItem(colorUIAdvGroup1, 
System.Drawing.Color.Crimson)
groupColorItem1.Color = System.Drawing.Color.Crimson
groupColorItem1.Index = 0
groupColorItem1.SubItems.Add(New
Syncfusion.Windows.Forms.Tools.ColorItem(groupColorItem1, 
System.Drawing.Color.LightPink))
colorUIAdvGroup1.Items.Add(groupColorItem1)
colorUIAdvGroup1.Name = "Custom User Colors"
colorUIAdvGroup1.SubItemsDepth = 1
Me.colorPickerUIAdv1.CustomGroups.Add(colorUIAdvGroup1)
```

![Custom User Colors Group](attachment://image.png)
*Figure 318: Custom ColorGroup= "Custom User Colors"*

#### Note: The properties to customize the color groups are similar to default color groups. See how to Custom the Color Groups in *Customizing the Color Groups* topic.

#### 3.5.4.5.3.1.2 Customizing the Color Groups

## API Reference (if applicable)

### WinForms-specific Conventions
- API elements are listed under relevant sections with their exact namespace and type (e.g., `Syncfusion.Windows.Forms.Tools.ColorPickerUIAdv`, `Syncfusion.Windows.Forms.Grid`).
- Parameters, returns, and exceptions are documented exactly as shown.

## Code Examples (multi-language supported)

### C#
```csharp
// Example of adding a custom ColorGroup
Syncfusion.Windows.Forms.Tools.GroupColorItem groupColorItem1 = new
Syncfusion.Windows.Forms.Tools.GroupColorItem(colorUIAdvGroup1, 
System.Drawing.Color.Crimson);
groupColorItem1.Color = System.Drawing.Color.Crimson;
groupColorItem1.Index = 0;
groupColorItem1.SubItems.Add(new
Syncfusion.Windows.Forms.Tools.ColorItem(groupColorItem1, 
System.Drawing.Color.LightPink));
colorUIAdvGroup1.Items.Add(groupColorItem1);
colorUIAdvGroup1.Name = "Custom User Colors";
colorUIAdvGroup1.SubItemsDepth = 1;
this.colorPickerUIAdv1.CustomGroups.Add(colorUIAdvGroup1);
```

### VB.NET
```vb
' Example of adding a custom ColorGroup
Dim groupColorItem1 As New
Syncfusion.Windows.Forms.Tools.GroupColorItem(colorUIAdvGroup1, 
System.Drawing.Color.Crimson)
groupColorItem1.Color = System.Drawing.Color.Crimson
groupColorItem1.Index = 0
groupColorItem1.SubItems.Add(New
Syncfusion.Windows.Forms.Tools.ColorItem(groupColorItem1, 
System.Drawing.Color.LightPink))
colorUIAdvGroup1.Items.Add(groupColorItem1)
colorUIAdvGroup1.Name = "Custom User Colors"
colorUIAdvGroup1.SubItemsDepth = 1
Me.colorPickerUIAdv1.CustomGroups.Add(colorUIAdvGroup1)
```

## Cross References
- For additional details on customizing color groups, refer to the *Customizing the Color Groups* topic.

<!-- tags: [Syncfusion, WindowsForms, ColorPickerUIAdv, CustomColorGroup, ColorGroupItem, Version:11.4.0.26] keywords: [Syncfusion, Windows Forms, Custom Color Group, Designer, ColorGroupItem, Custom Groups, ColorPickerUIAdv] -->
```