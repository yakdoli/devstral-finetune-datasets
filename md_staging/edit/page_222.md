```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_222.jpeg
document_name: edit
page_number: 222
page_id: edit#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:36Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
this.controlFormatsList1.LanguageSelector = this.controlLanguageSelector1;
this.controlFormatsList1.FormatsSelector = this.controlFormatsSettings1;

// Shows the font customization dialog.
this.editControl1.ShowFormatsCustomizationDialog();
```

```vb
this.controlFormatsList1.EditControl = this.editControl1;
this.controlLanguageSelector1.EditControl = this.editControl1;

this.controlFormatsList1.LanguageSelector = this.controlLanguageSelector1;
this.controlFormatsSettings1.FormatsSelector = this.controlFormatsList1;

// Shows the font customization dialog.
this.editControl1.ShowFormatsCustomizationDialog();
```

Refer to the Font Customization Demo sample for more information in this regard.

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\FontCustomizationDemo
```

## 4.9.5 Single Line Mode

Edit Control can be operated in a single line mode much like a Windows Forms Text Box, by setting its **Multiline** property to **False**. This enables you to have a simple TextBox-like control, but with all the powerful features of Edit Control like syntax highlighting, selection, underlining, and so on.

You can turn on the single line mode of the Edit Control by setting the **SingleLineMode** property to **True**.

> **Note:** The **SingleLineMode** is intended for use, only when the Edit Control contains small amounts of text data in it. Using it in a scenario where the Edit Control has a huge file loaded into it, may lead to poor performance.

### WinForms-specific conventions
- **Syncfusion.Windows.Forms.Tools.TabControlAdv**
- **Syncfusion.Windows.Forms.Grid**
- **SingleLineMode**
- **Multiline**

### Code Examples

```csharp
// C#
this.editControl1.SingleLineMode = true;
this.editControl1.Multiline = false;
```

```vb
' VB
Me.editControl1.SingleLineMode = True
Me.editControl1.Multiline = False
```

### API Reference
- **Namespace:** Syncfusion.Windows.Forms.Edit
- **Class:** SyntaxEditor

### Events
- **SingleLineModeChanged**
- **MultilineChanged**

### Parameters
- **Name:** IsSingleLineModeEnabled
- **Type:** Boolean
- **Description:** Indicates whether the Edit Control is in single line mode.

### Returns
- **Type:** None
- **Description:** Sets the Edit Control to single line mode when True is passed.

### Exceptions
- **ArgumentException:** If the property is assigned an invalid value.

<!-- tags: [Syncfusion Winforms, Edit Control, SingleLineMode, Multiline, SyntaxEditor, Version: 11.4.0.26] keywords: [single line mode, multiline property, text box, control, edit control, syncfusion windows forms] -->
```