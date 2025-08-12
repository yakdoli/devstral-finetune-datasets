```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: DocIo
page_number: 050
page_id: DocIo#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:49Z
fidelity: lossless
-->

## Overview

- HelloWorld method creates and exports a simple Word document.
- Demonstrates adding text to a paragraph in a Word document.
- Allows launching or downloading the generated Word file.

## Content

### HelloWorld Method Implementation

```csharp
public ActionResult HelloWorld(string SaveOption, string Browser)
{
    // A new document is created.
    IWordDocument document = new WordDocument();

    // Add a new section to the document.
    ISection section = document.AddSection();

    // Adding a new paragraph to the section.
    IParagraph paragraph = section.AddParagraph();

    // Insert text into the paragraph.
    paragraph.AppendText("Hello World!");

    return document.ExportAsActionResult("Sample.doc", FormatType.Doc,
        HttpContext.ApplicationInstance.Response,
        HttpContentDisposition.InBrowser);
}
```

### Step 4: Run the Application

**Run the application.** The following dialog box appears. It provides options to download and launch the generated file.

![Figure 21: Word document being opened by using MVC Application](https://i.imgur.com/placeholder.png)

**Figure 21: Word document being opened by using MVC Application**

A Word document is created in the ASP.NET MVC application.

## API Reference

### Methods

- `ExportAsActionResult(string file, FormatType formatType, HttpResponseBase response, HttpContentDisposition disposition)`
  - **Parameters:**
    - `file`: string
    - `formatType`: FormatType
    - `response`: HttpResponseBase
    - `disposition`: HttpContentDisposition
  - **Returns:** ActionResult

### Classes

- `WordDocument`
- `Section`
- `Paragraph`

## Code Examples

Example of exporting a Word document:

```csharp
public ActionResult ExportWord()
{
    IWordDocument document = new WordDocument();
    ISection section = document.AddSection();
    IParagraph paragraph = section.AddParagraph();
    paragraph.AppendText("Hello World!");

    return document.ExportAsActionResult("output.doc", FormatType.Doc,
        HttpContext.ApplicationInstance.Response,
        HttpContentDisposition.InBrowser);
}
```

## Cross References

- See also: [DocIO Tutorials](#docio-tutorials)
- [Exporting Documents](#exporting-documents)

<!-- tags: DocIo, WordDocument, MVC_Application, ExportAsActionResult keywords: Word document, paragraph, ASP.NET MVC, dialog box -->
```