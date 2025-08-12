```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_132.jpeg
document_name: diagram
page_number: 132
page_id: diagram#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:56Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page describes how to set the orientation of a label to horizontal using the Orientation property in the Syncfusion Windows Forms Diagram control.
- Includes C# and VB.NET code examples demonstrating the configuration.
- Features a figure illustrating the Label with Horizontal orientation.

## Content

### Properties

Properties describes how to set or configure the properties of the label control.

| **Property**   | **Description**                                                                 | **Data Type** |
|----------------|---------------------------------------------------------------------------------|---------------|
| Orientation    | Gets or sets the orientation of the label.                                     | Enum          |

The following code shows how to set the orientation of the label to horizontal:

#### C#

```csharp
Syncfusion.Windows.Forms.Diagram.Label label = new Syncfusion.Windows.Forms.Diagram.Label(node, "Orientation");
//Sets the orientation of the label as horizontal.
label.Orientation = LabelOrientation.Horizontal;
node.Labels.Add(label);
```

#### VB.NET

```vb
Dim label As New Syncfusion.Windows.Forms.Diagram.Label(node, "Orientation")
' Sets the orientation of the label as horizontal.
label.Orientation = LabelOrientation.Horizontal
node.Labels.Add(label)
```

### Figure: Label with Horizontal Orientation

```markdown
Figure 73: Label with Horizontal orientation
```

![](image.png)

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```