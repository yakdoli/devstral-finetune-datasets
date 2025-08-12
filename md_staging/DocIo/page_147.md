```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_147.jpeg
document_name: DocIo
page_number: 147
page_id: DocIo#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:13Z
fidelity: lossless
-->

## Overview
- This page explains how to use the `WCheckBox` class in the Syncfusion Winforms library. It demonstrates properties like `EntityType`, `SizeType`, and various attributes of checkboxes such as `Enabled`, `StatusHelp`, and `DefaultCheckBoxValue`.

## Content

### Checkbox Properties and Usage

| Property     | Description                         |
|--------------|-------------------------------------|
| `EntityType` | Gets the type of the entity.          |
| `SizeType`   | Gets or sets check box size type.    |

The following example illustrates how to use the `WCheckBox` class.

#### Code Examples

##### C#

```csharp
IWordDocument doc = new WordDocument();
doc.EnsureMinimal();
IWParagraph par = doc.LastParagraph;
WCheckBox checkBox = par.AppendCheckBox();
checkBox.Enabled = false;
checkBox.StatusBarHelp = "Help1";
checkBox.Help = "Help2";
checkBox.DefaultCheckBoxValue = true;
checkBox.SizeType = CheckBoxSizeType.Auto;
checkBox.CalculateOnExit = true;
par.AppendText("CheckBox2: ");
WCheckBox checkBox1 = par.AppendCheckBox();
checkBox1.CheckBoxSize = 30;
checkBox1.SizeType = CheckBoxSizeType.Exactly;
checkBox1.CalculateOnExit = false;
checkBox1.Checked = true;
doc.Save("TestDoc.doc");
```

##### VB.NET

```vb
Dim doc As IWordDocument = New WordDocument()
doc.EnsureMinimal()
Dim par As IWParagraph = doc.LastParagraph
Dim checkBox As WCheckBox = par.AppendCheckBox()
checkBox.Enabled = False
checkBox.StatusBarHelp = "Help1"
checkBox.Help = "Help2"
checkBox.DefaultCheckBoxValue = True
checkBox.SizeType = CheckBoxSizeType.Auto
checkBox.CalculateOnExit = True
par.AppendText("CheckBox2: ")
checkBox1 As WCheckBox = par.AppendCheckBox()
checkBox1.CheckBoxSize = 30
checkBox1.SizeType = CheckBoxSizeType.Exactly
checkBox1.CalculateOnExit = False
```

## Page-level Navigation/TOC (if applicable)
- The page provides an example of implementing checkboxes in a Winforms document using the `WCheckBox` class.

## Cross References
- Related documentation or examples on checkbox properties and document handling in Syncfusion Winforms.

<!-- tags: [Syncfusion, Winforms, WCheckBox, C#, VB.NET, DocIO] keywords: [Checkbox, Properties, Document, Example, Winforms, Syncfusion, Design-Time, Runtime, C#, VB.NET, DocIO] -->
```