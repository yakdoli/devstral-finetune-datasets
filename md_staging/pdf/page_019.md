```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: pdf
page_number: 019
page_id: pdf#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:24:45Z
fidelity: lossless
-->

# Essential DocIO in ASP.NET MVC

## Overview
- Features server-side .NET library to handle Microsoft Word files.
- Fully integrated into ASP.NET MVC with a full-fledged object model.

## Content

### Overview of Essential DocIO

**Essential DocIO**
- High performance server-side .NET library for reading, writing, and manipulating Microsoft Word files.
- Full-fledged object model similar to the Microsoft Office COM libraries.
- Does not require Microsoft Office and is built entirely in C#.
- Fully integrated into ASP.NET MVC.

#### Featured Samples

1. **Employee Report**  
   ![Employee Report](attachment:Employee_Report)

2. **Table of Content**  
   ![Table of Content](attachment:Table_of_Content)

3. **Clone and Merge**  
   ![Clone and Merge](attachment:Clone_and_Merge)

4. **Forms**  
   ![Forms](attachment:Forms)

5. **Update Fields**  
   ![Update Fields](attachment:Update_Fields)

### Navigating the Sample Browser

**Note**: By default, the samples of Essential DocIO are displayed.

#### Steps to Access

3. Click **Pdf** from the bottom-left pane.

## API Reference
- For detailed API reference, refer to the Essential DocIO documentation.

## Code Examples

### C# Example

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Dls;
using Syncfusion.Compression;
using System;
using System.Collections.Generic;
using System.Drawing;

public class DocIOExample
{
    public void CreateWordDocument()
    {
        // Create a new Word document.
        WordDocument document = new WordDocument();

        // Add a section to the document.
        WSection section = document.AddSection();
        section.PageSetup.MarginLeft = 72;
        section.PageSetup.MarginTop = 72;
        section.PageSetup.MarginRight = 72;
        section.PageSetup.MarginBottom = 72;
        section.PageSetup.HeaderDistance = 36;
        section.PageSetup.FooterDistance = 36;

        // Add a paragraph to the section.
        WParagraph paragraph = section.AddParagraph();
        paragraph.AppendText("Welcome to Essential DocIO!");

        // Save the document to a file.
        document.Save("Sample.docx");
    }
}
```

## Cross References
- See also: "Introduction to ASP.NET MVC," "PDF Viewer Integration."

## Navigation
Use the navigation pane on the left to explore all available samples.

<!-- tags: [Essential DocIO, ASP.NET MVC, Word Files, Server-side Library, Object Model, C#] keywords: [Essential DocIO, Microsoft Word, C#, ASP.NET MVC, Word Document, CreateWordDocument, navigation pane, features samples, integrated, high-performance, object model] -->
```