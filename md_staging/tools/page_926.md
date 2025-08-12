```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_926.jpeg
document_name: tools
page_number: 926
page_id: tools#page_926
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:21Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### FontComboBox Programmatically Created

The following C# and VB.NET code snippets demonstrate how to create a `FontComboBox` control programmatically.

```csharp
this.fontComboBox1 = new Syncfusion.Windows.Forms.Tools.FontComboBox();
this.fontComboBox1.Size = new System.Drawing.Size(152, 21);

this.Controls.Add(this.fontComboBox1);
```

```vb
Private fontComboBox1 As Syncfusion.Windows.Forms.Tools.FontComboBox

Me.fontComboBox1 = New Syncfusion.Windows.Forms.Tools.FontComboBox()
Me.fontComboBox1.Size = New System.Drawing.Size(152, 21)

Me.Controls.Add(Me.fontComboBox1)
```

#### Figure 591: FontComboBox Control Created Programmatically
![FontComboBox Demo](https://via.placeholder.com/300x200?text=FontComboBox+Demo)

### 3.5.9.2.3 Concepts and Features

The below topics are discussed in this section.

#### 3.5.9.2.3.1 AutoComplete

The AutoComplete feature of the FontComboBox can be turned on/off depending upon the type of behavior required for the FontComboBox control. The following properties enable the auto complete feature.

| Properties         | Description                                                                   |
|--------------------|-------------------------------------------------------------------------------|
| UseAutoComplete    | Specifies whether the auto complete feature is implemented in the control. |

## API Reference

### Properties

- **UseAutoComplete**
  - Specifies whether the auto complete feature is implemented in the control.

## Code Examples

The C# and VB.NET code snippets above demonstrate how to create and configure a FontComboBox control programmatically.

## Page-level Navigation/TOC

- **3.5.9.2.3 Concepts and Features**
  - **3.5.9.2.3.1 AutoComplete**

## Cross References

See also:
- [FontComboBox Control Overview](#fontcombobox-control-overview)
- [Customizing FontComboBox](#customizing-fontcombobox)

## RAG Annotations

<!-- tags: fontcombobox, winforms, syncfusion, auto-complete, programmatically created, essential tools, control features, windows forms keywords: windows forms, font combo box, auto complete, programmatically, features, control, syncfusion, essential tools -->
```