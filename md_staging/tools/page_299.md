```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_299.jpeg
document_name: tools
page_number: 299
page_id: tools#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the functionality of text completion modes in the Textbox control.
- Demonstrates different auto-complete options: Suggest, Append, and SuggestAppend.
- Includes code examples in both C# and VB.NET for configuring auto-complete modes.

## Content

This section describes how to configure the AutoCompleteMode property of the Textbox control in Windows Forms to support various auto-complete behaviors.

### AutoCompleteMode Property

The AutoCompleteMode property of the Textbox control allows you to specify how the control should respond when matching entries are found in the auto-complete source.

#### Examples in Code

**C#**:
```csharp
this.textBox1.AutoCompleteMode =
System.Windows.Forms.AutoCompleteMode.SuggestAppend;
```

**VB.NET**:
```vb
Me.textBox1.AutoCompleteMode =
System.Windows.Forms.AutoCompleteMode.SuggestAppend
```

#### Visual Demonstration

Figure 128 illustrates the different modes of text completion available in the Textbox control:

- **Suggest**: Displays a drop-down list of matching items based on the entered text.
- **Append**: Automatically completes the text in the control without showing a drop-down list.
- **SuggestAppend**: Combines both Suggest and Append behaviors, displaying matching items and completing the text with the closest match.

![Figure 128: Textbox control with Suggest, Append, and SuggestAppend Options](image_for_Figure_128.png)

### See Also
- [Multiple Columns, External Datasource](#)
- [3.5.1.1.3.2.3 External Datasource](#)

## API Reference

- **Namespace**: System.Windows.Forms
- **AutoCompleteMode Enum**:
  - Suggest
  - Append
  - SuggestAppend

### Parameters
- **AutoCompleteMode**: Specifies the auto-complete behavior of the Textbox control.
  - Type: `AutoCompleteMode`
  - Description: Determines how matching items are displayed or applied in the control.
  - Default: `None`
  - Required: Yes

### Returns
- None

## Code Examples

#### C#
```csharp
this.textBox1.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.SuggestAppend;
this.textBox1.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.CustomSource;
this.textBox1.AutoCompleteCustomSource = new System.Collections.Specialized.StringCollection();
this.textBox1.AutoCompleteCustomSource.Add("Custom Collections");
this.textBox1.AutoCompleteCustomSource.Add("Customization Properties");
```

#### VB.NET
```vb
Me.textBox1.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.SuggestAppend
Me.textBox1.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.CustomSource
Me.textBox1.AutoCompleteCustomSource = New System.Collections.Specialized.StringCollection()
Me.textBox1.AutoCompleteCustomSource.Add("Custom Collections")
Me.textBox1.AutoCompleteCustomSource.Add("Customization Properties")
```

## Page-level Navigation/TOC

- Overview
- Content
  - AutoCompleteMode Property
  - Visual Demonstration
- API Reference
- Code Examples

## Cross References
- [External Datasource](#)

<!-- tags: [windows forms, textbox, auto-complete, suggest, append, suggestappend, tool] keywords: [syncfusion, winforms, text completion, autocompletemode, suggest, append, suggestappend, custom source] -->
```