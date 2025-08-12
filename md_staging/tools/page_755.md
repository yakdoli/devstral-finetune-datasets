```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_755.jpeg
document_name: tools
page_number: 755
page_id: tools#page_755
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:36Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

### Overview
- This page explains the various properties and options for configuring the Border3DStyle, BorderColor, BorderSides, and BorderStyle of an edit control in Windows Forms.
- It provides examples in both C# and VB.NET to demonstrate how to set these properties.

### Content

#### Table: Edit Control Border Properties

| **Property**       | **Description**                                                                                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Border3DStyle      | Specifies the 3D style of the edit control. The options included are: <br> `Left,` <br> `Top,` <br> `Right,` <br> `Bottom,` <br> `Middle and` <br> `All.` |
| BorderSide         | Indicates which sides of the edit control should have a border. The options included are given below: <br> `FixedSingle,` <br> `Fixed3D and` <br> `None.` |

#### Example in C#
```csharp
this.integerTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump;
this.integerTextBox1.BorderColor = System.Drawing.Color.Red;
this.integerTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All;
this.integerTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

#### Example in VB.NET
```vb
Me.integerTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump
Me.integerTextBox1.BorderColor = System.Drawing.Color.Red
Me.integerTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All
Me.integerTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
```

#### Figure: IntegerTextBox with Border Set

![Figure 479: IntegerTextBox with Border Set](image.png)

Figure 479: IntegerTextBox with Border Set

### API Reference

- **Namespace**: `System.Windows.Forms`
- **Types**: 
  - `Border3DStyle`
  - `Border3DSide`
  - `BorderStyle`

### Code Examples

#### C#
```csharp
// Setting Border Properties
this.integerTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump;
this.integerTextBox1.BorderColor = System.Drawing.Color.Red;
this.integerTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All;
this.integerTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

#### VB.NET
```vb
' Setting Border Properties
Me.integerTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump
Me.integerTextBox1.BorderColor = System.Drawing.Color.Red
Me.integerTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All
Me.integerTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
```

### Page-level Navigation/TOC (if applicable)
- Border3DStyle and BorderSide
- BorderStyle
- Example Code in C# and VB.NET
- Figure: IntegerTextBox with Border Set

### Cross References
- Refer to the documentation on Windows Forms controls for more details on edit controls.

### RAG Annotations
- <!-- tags: [Windows Forms, Border3DStyle, Border3DSide, BorderStyle, integerTextBox, C#, VB.NET, Figure] keywords: [Border3DStyle, BorderColor, BorderSides, BorderStyle, edit control, tools] -->
```