```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_963.jpeg
document_name: tools
page_number: 963
page_id: tools#page_963
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![](./checkbox.png)

**Figure 619: Text aligned to "MiddleCenter"**

## CheckBox Alignment

The CheckBox itself can be aligned to any desired location that can be chosen from the options given in the following property.

| CheckBoxAdv Properties | Description |
| --- | --- |
| CheckAlign | Indicates the alignment of the CheckBox. The default value is set to 'MiddleLeft'. The options included are as follows.<br><br>**TopLeft**, <br>**TopCenter**, <br>**TopRight**, <br>**MiddleLeft**, <br>**MiddleCenter**, <br>**MiddleRight**, <br>**BottomLeft**, <br>**BottomCenter** and <br>**BottomRight**. |

### C#

```csharp
this.checkBoxAdv1.CheckAlign = 
System.Drawing.ContentAlignment.MiddleRight;
```

### VB.NET

```vb
Me.checkBoxAdv1.CheckAlign = 
System.Drawing.ContentAlignment.MiddleRight
```

## API Reference

### CheckBoxAdv Class

#### Properties
| Name | Type | Description | Default | Required |
| --- | --- | --- | --- | --- |
| CheckAlign | `System.Drawing.ContentAlignment` | Indicates the alignment of the CheckBox. | `MiddleLeft` | No |

## Code Examples

### Setting CheckBox Alignment in C#

```csharp
this.checkBoxAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
```

### Setting CheckBox Alignment in VB.NET

```vb
Me.checkBoxAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight
```

<!-- tags: [syncfusion, winforms, checkboxadv, alignment, version: 11.4.0.26] -->
``` 
