```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_187.jpeg
document_name: edit
page_number: 187
page_id: edit#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:11Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Exporting Edit Control content into XML, RTF, and HTML formats.
- Generating source code for XML, RTF, and HTML documents using Edit Control methods.

## Content

### Saving Edit Control Contents

```vb
[VB.NET]

' Export the Edit Control's contents into XML format and save it into a XML file.
Me.editControl1.SaveAsXML("testXML.xml")

' Export the Edit Control's contents into RTF format and save it into a RTF file.
Me.editControl1.SaveAsRTF("testRTF.rtf")

' Export the Edit Control's contents into HTML format and save it into a HTML file.
Me.editControl1.SaveAsHTML("testHTML.html")
```

### Generating Source Code

Edit Control is also capable of providing XML, RTF, and HTML source code for generating documents in the corresponding formats by using the following methods.

| Edit Control Method | Description |
|---------------------|-------------|
| GetTextAsRTF       | Gets the source code to generate XML document for the text in the Edit Control. |
| GetTextAsXML       | Gets the source code to generate RTF document for the text in the Edit Control. |
| GetTextAsHTML      | Gets the source code to generate HTML document for the text in the Edit Control. |

#### Example in C#

```csharp
[C#]

// Gets the source code to generate XML document.
this.editControl1.GetTextAsXML();

// Gets the source code to generate XML document for the text range specified.
this.editControl1.GetTextAsXML(coordinatePoint1, coordinatePoint2);
```

#### Example in VB.NET

```vb
[VB.NET]

' Gets the source code to generate XML document.
Me.editControl1.GetTextAsXML()

' Gets the source code to generate XML document for the text range specified.
Me.editControl1.GetTextAsXML(coordinatePoint1, coordinatePoint2)
```

## API Reference

### Methods

- **GetTextAsRTF()**
  - Generates the source code for an RTF document from the text in the Edit Control.

- **GetTextAsXML()**
  - Generates the source code for an XML document from the text in the Edit Control.

- **GetTextAsHTML()**
  - Generates the source code for an HTML document from the text in the Edit Control.

## Code Examples
- C# and VB.NET examples demonstrate how to use the `GetTextAsRTF`, `GetTextAsXML`, and `GetTextAsHTML` methods to generate source code for various document formats.

### Cross References
See also:
- Related methods for saving to files: `SaveAsXML`, `SaveAsRTF`, `SaveAsHTML`.
- Document generation and formatting techniques in Syncfusion WinForms documentation.

<!-- tags: [edit control, document generation, xml, rtf, html, source code, syncfusion.winforms] keywords: [export, getxml, getrtf, gethtml, text, document, format, method, edit control, component one, synchronization, .NET framework, programming, document generation, text formatting, xml, rtf, html, VB.NET, C#, .NET, Syncfusion WinForms] -->
```