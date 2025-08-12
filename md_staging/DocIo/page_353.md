```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_353.jpeg
document_name: DocIo
page_number: 353
page_id: DocIo#page_353
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:35Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This section provides an example of how to add headers and footers to sections in a Word document using the Microsoft Office Interop library.
- The code demonstrates opening an existing document, iterating through its sections, adding header and footer fields, and saving the modified document.

## Content

```csharp
[C#]

using word = Microsoft.Office.Interop.Word;
---------

// Initialize objects
object nullobject = Missing.Value;
object filePath = GetPath("original.doc");
object newFilePath = GetPath("HeaderFooterOffice.doc");

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document
word.Document document = wordApp.Documents.Open(ref filePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;

// Add header and footer for each section in the document
foreach (word.Section section in document.Sections)
{
    object fieldEmpty = word.WdFieldType.wdFieldPage;
    object autoText = "AUTOTEXT   \"Page X of Y\" ";
    object preserveFormatting = true;

    // Footer
    section.Footers[word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range.Text = "Internal";

    section.Footers[word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range.ParagraphFormat.Alignment =
    word.WdParagraphAlignment.wdAlignParagraphLeft;

    // Header
    section.Headers[word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range.Fields.Add(section.Headers[word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range, ref fieldEmpty, ref autoText, ref preserveFormatting);

    section.Headers[word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range.ParagraphFormat.Alignment =
    word.WdParagraphAlignment.wdAlignParagraphRight;
}

// Save the document
document.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);
```

### Explanation:
- **Initialization**: The necessary objects and file paths are initialized. The `nullobject` variable is used to represent missing parameters in the method calls.
- **Application Setup**: A new instance of the Word application is created, and visibility is set to false to prevent the application from opening in the foreground.
- **Document Opening**: The original Word document is opened using the `Open` method, with numerous `nullobject` parameters that correspond to optional arguments.
- **Iterating Through Sections**: Each section in the document is processed to add a header and footer. The footer text is set to "Internal," and both header and footer alignments are configured.
- **Fields in Headers**: An "AUTOTEXT" field is added to the header, which can be used to insert custom text or fields like "Page X of Y."
- **Saving and Closing**: The modified document is saved under a new file path, and the document is closed properly to free up resources.

### Dependencies:
- **Microsoft.Office.Interop.Word**: This library is required for interacting with Microsoft Word documents programmatically.
- **GetPath Method**: This method is assumed to return the file path for the specified file names.

## Tags and Keywords
<!-- tags: [essential docio, syncfusion winforms, header footer, word document, microsoft office interop, document manipulation] keywords: [headers, footers, document sections, word application, page numbering, text alignment, document saving] -->
```