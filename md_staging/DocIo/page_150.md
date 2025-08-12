```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: DocIo
page_number: 150
page_id: DocIo#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:23Z
fidelity: lossless
-->

# EssentiaDocIO

## Overview
- Demonstrates creating dropdown form fields in a Word document.
- Explains how to set dropdown options, selected index, and help texts.
- Shows saving and ensuring minimal states for the Word document.

### C#

```csharp
dropDown.Help = "Help2";
dropDown.StatusBarHelp = "Help1";

doc.Save("TestDoc.doc");
```

### VB.NET

```vb
Dim doc As IWordDocument = New WordDocument()
doc.EnsureMinimal()

Dim par As IWParagraph = doc.LastParagraph
Dim dropDown As WDropDownFormField = par.AppendDropDownFormField()
dropDown.DropDownItems.Add("One")
dropDown.DropDownItems.Add("Two")
dropDown.DropDownSelectedIndex = 1
dropDown.CalculateOnExit = True
dropDown.Enabled = False
dropDown.Help = "Help2"
dropDown.StatusBarHelp = "Help1"

doc.Save("TestDoc.doc")
```

## Text

The **WTextFormField** class represents a text form field in a Word document. To add a text form field to the Word document, click **Text Form Field** on the Forms toolbar.

![Forms Panel](https://example.com/forms-panel.png)
*Figure 52: Forms Panel*
<!-- tags: [Syncfusion SDK, WinForms], keyword: [WTextFormField, Word document, text field, form, Forms toolbar] -->
```