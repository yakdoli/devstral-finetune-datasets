```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_988.jpeg
document_name: tools
page_number: 988
page_id: tools#page_988
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:34Z
fidelity: lossless
--> 

# Essential Tools for Windows Forms

## Overview
- RadioButtonAdv can be aligned using the `CheckAlign` property.
- Lista of alignment options: TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight.
- Sample code provided for both C# and VB.NET.

## Content

### Alignment of RadioButtonAdv

The `RadioButton` itself can be aligned to any desired location that can be chosen from the options given in the following property.

| **RadioButtonAdv Properties** | **Description** |
| --- | --- |
| **CheckAlign** | Indicates the alignment of the `RadioButton`. The default value is set to `'MiddleLeft'`. <br> <br> The options included are as follows: <br> <br> `TopLeft,` <br> `TopCenter,` <br> `TopRight,` <br> `MiddleLeft,` <br> `MiddleCenter,` <br> `MiddleRight,` <br> `BottomLeft,` <br> `BottomCenter and` <br> `BottomRight.` |

### Code Examples

#### C#

```csharp
this.radioButtonAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
```

#### VB.NET

```vb
Me.radioButtonAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight
```

### Visual Representation

The following figure demonstrates the alignment of a `RadioButton` to `"MiddleRight"`:

![Figure 638: RadioButton aligned to "MiddleRight"](https://i.imgur.com/1234567.png)

**Figure 638:** RadioButton aligned to "MiddleRight"

### Sample Implementation

A Sample which demonstrates the Text and `RadioButton` Alignment features of `CheckBoxAdv` is available in the below sample installation path.

## Page-level Navigation/TOC
- **Alignment of RadioButtonAdv**
  - Description
  - Code Examples
  - Visual Representation

## Cross References
See also:
- Other alignment properties for `RadioButtonAdv`
- Documentation for `CheckBoxAdv`

## API Reference

### Properties

| Name | Type | Description |
| --- | --- | --- |
| **CheckAlign** | `System.Drawing.ContentAlignment` | Indicates the alignment of the `RadioButton`. |

## Code Examples (continued)

### Using C# to Align a `RadioButtonAdv` to `MiddleRight`

```csharp
using Syncfusion.Windows.Forms.Tools;
using System.Drawing;

// Example usage
this.radioButtonAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
```

### Using VB.NET to Align a `RadioButtonAdv` to `MiddleRight`

```vb
Imports Syncfusion.Windows.Forms.Tools
Imports System.Drawing

' Example usage
Me.radioButtonAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight
```

<!-- tags: [product: Winforms, module: Tools, control: RadioButtonAdv, api: CheckAlign, version: 11.4.0.26] keywords: [RadioButtonAdv, alignment, CheckAlign, C#, VB.NET, example, documentation, sample, figure] -->
```