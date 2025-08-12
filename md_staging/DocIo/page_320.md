```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_320.jpeg
document_name: DocIo
page_number: 320
page_id: DocIo#page_320
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:26Z
fidelity: lossless
-->

## Essential DocIO

### Code Example in C#

```csharp
WTable table = doc.LastSection.AddTable() as WTable;
RowFormat rowFormat = new RowFormat();
rowFormat.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.Double;
rowFormat.LeftIndent = 20;
table.ResetCells(3, 3, rowFormat, 100);
```

### Code Example in VB

```vb
Dim table As ITable = sec.body.AddTable()
Dim rowFormat As New RowFormat()
rowFormat.BackColor = Color.Purple
rowFormat.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.[Double]
rowFormat.LeftIndent = 20
table.ResetCells(3, 3, rowFormat, 100)
```

### Modifying Built-in Styles

#### Overview
- This section explains how to modify built-in styles in documents.
- It demonstrates the use of the `CreateBuiltinStyle` method to customize styles.

### 5.6 How to modify the Built-in styles?

#### Introduction
You can use the `CreateBuiltinStyle` method of the Style class to override the built-in styles.

#### Example: Modifying the Heading1 Style
The following code illustrates how to modify the Heading1 style.

#### C# Code Example
```csharp
Style style = Style.CreateBuiltinStyle(BuiltinStyle.Heading1, doc) as Style;
style.CharacterFormat.Italic = true;
style.CharacterFormat.UnderlineStyle = UnderlineStyle.DotDash;
doc.Styles.Add(style);
para.ApplyStyle(style.Name);
```

#### VB Code Example
```vb
Dim style As Style = TryCast(Style.CreateBuiltinStyle(BuiltinStyle.Heading1, doc), Style)
style.CharacterFormat.Italic = True
style.CharacterFormat.UnderlineStyle = UnderlineStyle.DotDash
doc.Styles.Add(style)
para.ApplyStyle(style.Name)
```

---

<!-- tags: [docio, style, heading1, built-in styles, document formatting, syncfusion, winforms, csharp, vb] keywords: [createbuiltinstyle, style, override, italics, underlinestyle, dotdash, paragraph, text formatting] -->
```