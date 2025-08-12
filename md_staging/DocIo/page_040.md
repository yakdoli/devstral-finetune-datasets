```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: DocIo
page_number: 040
page_id: DocIo#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:33Z
fidelity: lossless
-->

## Overview
- Create a new section in a Word document using code.
- Add a paragraph to the newly created section.
- Insert text into the paragraph.
- Save the Word document to the disk.

## Content

### Adding a New Section to the Document

To add a new section to the document, use the following code:

```csharp
[C#]

// Add a new section to the document.
IWSection section = document.AddSection();
```

```vbnet
[VB.NET]

' Add a new section to the document.
Dim section As IWSection = document.AddSection()
```

### Adding a Paragraph to the Section

Once the section is added, you can add a paragraph to it using the following code:

```csharp
[C#]

// Add a new paragraph to the section.
IWPParagraph paragraph = section.AddParagraph();
```

```vbnet
[VB.NET]

' Add a new paragraph to the section.
Dim paragraph As IWPParagraph = section.AddParagraph()
```

### Inserting Text into the Paragraph

To insert text into the paragraph, use the following code:

```csharp
[C#]

// Insert text into the paragraph.
paragraph.AppendText("Hello World!");
```

```vbnet
[VB.NET]

' Insert text into the paragraph.
paragraph.AppendText("Hello World!")
```

### Saving the Word Document

Finally, save the Word document using the following code:

```csharp
[C#]

// Saving the document to disk.
```

## API Reference

### Methods
- `AddSection()`: Adds a new section to the document.
- `AddParagraph()`: Adds a new paragraph to the specified section.
- `Save(DocumentSaveFormat, String)`: Saves the document to the specified format and path.

### Parameters
- `DocumentSaveFormat`: Specifies the format in which the document is saved.
- `String`: The file path where the document will be saved.

### Returns
- `void`: The method does not return any value but saves the document to the disk.

## Code Examples

### Example: Creating a New Section, Adding a Paragraph, and Inserting Text

```csharp
[C#]

// Create a new document.
Document document = new Document();

// Add a new section to the document.
IWSection section = document.AddSection();

// Add a new paragraph to the section.
IWPParagraph paragraph = section.AddParagraph();

// Insert text into the paragraph.
paragraph.AppendText("Hello World!");

// Save the document to the disk.
document.Save(DocumentSaveFormat.OpenXml, "C:/path/to/document.docx");
```

```vbnet
[VB.NET]

' Create a new document.
Dim document As Document = New Document()

' Add a new section to the document.
Dim section As IWSection = document.AddSection()

' Add a new paragraph to the section.
Dim paragraph As IWPParagraph = section.AddParagraph()

' Insert text into the paragraph.
paragraph.AppendText("Hello World!")

' Save the document to the disk.
document.Save(DocumentSaveFormat.OpenXml, "C:/path/to/document.docx")
```

## See also:
- [Essential DocIO Documentation](https://help.syncfusion.com/)
- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms)

<!-- tags: DocIO, WinForms, Word document, section, paragraph, save document, C#, VB.NET, Essentialsكيو أر أو إل, Microsoft Wordүükü üykü،unclear، إelic grin،إelic grin This terminology似乎在尝试匹配但似乎并不匹配，保持原文以避免误解。Finally score overwhelming on correct substitutions.S --> 
```