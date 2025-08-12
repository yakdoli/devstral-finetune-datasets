```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_307.jpeg
document_name: DocIo
page_number: 307
page_id: DocIo#page_307
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:42Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Create a new Word document instance and add text content.
- Display the SaveFile dialog to allow the user to choose a save location and file name.
- Save the document in .docx format, converting from .doc if necessary.
- The same can be achieved using VB.Net code as well.

---

### Step 1: Create a Word Document

The following example demonstrates how to create a new Word document, add a section, and insert a paragraph with text.

```csharp
WordDocument document = new WordDocument();
// Add a new section to the document.
IWSection section = document.AddSection();
// Adding a new paragraph to the section.
IWParagraph paragraph = section.AddParagraph();
// Insert Text into the paragraph
paragraph.AppendText("Hello World!");
```

---

### Step 2: Create an Instance of SaveFile Dialog

The following lines of code create an instance of SaveFile Dialog and set the properties to display the Save dialog on the screen.

```csharp
SaveFileDialog sfd = new SaveFileDialog()
{
    Filter = "Docx files (*.docx)|*.docx|All files (*.*)|*.*",
    DefaultExt = ".docx",
    FilterIndex = 1
};
if (sfd.ShowDialog() == true)
```

---

### Step 3: Save the Document as .docx Format

The following code snippet will save the Word document in .docx format.

```csharp
{
    using (Stream stream = sfd.OpenFile())
    {
        document.Save(stream, FormatType.Docx);
    }
}
```

---

### Step 4: Run the Application

The .doc file is converted to .docx file.

**Note:** The same can be achieved using the VB.NET code as well.

---

## Summary

This document provides steps to create a Word document, display a SaveFile dialog, and save the document in .docx format. The process is applicable for C# and can be replicated using VB.Net.

---

## References

- Syncfusion WinForms Documentation
- Essential DocIO API Reference

<!-- tags: [WinForms, DocIO, Word Document, SaveFile Dialog, .docx, C#, VB.Net] keywords: [Create Document, Save Dialog, Document Conversion, DocIO, Word, SaveFile, C#, VB.Net] -->
```