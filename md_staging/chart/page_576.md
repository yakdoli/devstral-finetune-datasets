<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_576.jpeg
document_name: chart
page_number: 576
page_id: chart#page_576
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:48Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to export a chart image to a Word document.
- Includes code snippets for both C# and VB.NET to generate and save the document.

## Content

### Code Example

Here is the code snippet provided for adding chart functionality to your form:

#### [C#]

```csharp
string fileName = Application.StartupPath + "\\chartexport";
string exportFileName = fileName + ".doc";
string file = fileName + ".gif";

this.chartControl1.SaveImage(file);

// Create a new document.
WordDocument document = new WordDocument();

// Adding a new section to the document.
IWSection section = document.AddSection();
// Adding a paragraph to the section.
IWParagraph paragraph = section.AddParagraph();

// Writing text.
paragraph.AppendText("Essential Chart");

// Adding a new paragraph.
paragraph = section.AddParagraph();
paragraph.ParagraphFormat.HorizontalAlignment = Syncfusion.DLS.HorizontalAlignment.Center;

// Inserting chart.
paragraph.AppendPicture(Image.FromFile(file));
// Save the Document to disk.
document.Save(exportFileName, Syncfusion.DocIO.FormatType.Doc);

// Launches the file.
System.Diagnostics.Process.Start(exportFileName);
```

#### [VB.NET]

```vb
Dim fileName As String = Application.StartupPath & "\chartexport"
Dim exportFileName As String = fileName & ".doc"
Dim file As String = fileName & ".gif"

Me.chartControl1.SaveImage(file)

' Create a new document.
Dim document As WordDocument = New WordDocument()
' Adding a new section to the document.
Dim section As IWSection = document.AddSection()
Dim paragraph As IWParagraph = section.AddParagraph()

' Writing text.
paragraph.AppendText("Essential Chart")

' Adding a new paragraph.
paragraph = section.AddParagraph()
paragraph.ParagraphFormat.HorizontalAlignment = Syncfusion.DLS.HorizontalAlignment.Center

' Inserting chart.
paragraph.AppendPicture(Image.FromFile(file))
' Save the Document to disk.
document.Save(exportFileName, Syncfusion.DocIO.FormatType.Doc)

' Launches the file.
System.Diagnostics.Process.Start(exportFileName)
```

## API Reference

### Methods
- **SaveImage(string filePath)**: Saves the chart image to the specified file path.
- **AddSection()**: Adds a new section to the document.
- **AddParagraph()**: Adds a new paragraph to the section.
- **AppendText(string text)**: Appends the specified text to the paragraph.
- **AppendPicture(Image image)**: Inserts an image into the paragraph.
- **Save(string filePath, FormatType formatType)**: Saves the document to the specified file with the given format type.

<!-- tags: [syncfusion, windows forms, chart, word document, essential chart] keywords: [export image, save document, document section, paragraph alignment, append picture] -->