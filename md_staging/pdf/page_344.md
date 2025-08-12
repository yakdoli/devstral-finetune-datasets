```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_344.jpeg
document_name: pdf
page_number: 344
page_id: pdf#page_344
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:58Z
fidelity: lossless
-->

# Essential PDF

```vb
[VB.NET]

' Creating Border with transparent color.
Dim borderPen As PdfPen = New PdfPen(Color.Transparent)
borderPen.Width = 1.0F

' Assigning the border pen to table cell.
Dim defStyle As PdfCellStyle = New PdfCellStyle()
defStyle.Font = font
defStyle.BorderPen = borderPen
table.Style.DefaultStyle = defStyle
```

## Overview
- Describes how to create borders with transparent colors in a PDF table cell using VB.NET.
- Explains the process of assigning specific border styles to a table cell using the `PdfPen` and `PdfCellStyle` classes.
- Introduces the concept of managing borders for table cells programmatically.

### Content

#### 5.1.1.4 How To Create Page Labels?

You will be able to find a Pages tab in Adobe Reader which contains small page images. Also, you will be able to find text underneath each image. You can edit that text by using the `PdfPageLabel` class. This class allows specifying the prefix, numbering style, and starting number for a page group, which is a section. You can create and initialize an instance of this class and assign it to the `Section` property.

```csharp
[C#]

// Create a new document class object.
PdfDocument doc = new PdfDocument();

// Create few sections with few pages in each.
for (int i = 0; i < 3; ++i)
{
    PdfSection section = doc.Sections.Add();
    PdfPageLabel label = new PdfPageLabel();
    label.Prefix = "Sec" + i + "-";
    section.PageLabel = label;

    PdfPage page;
    for (int j = 0; j < 10; ++j)
    {
        page = section.Pages.Add();
    }
}
doc.Save(filename);
```

```vb
[VB.NET]
```

### Related

## WinForms-specific Conventions
- Demonstrates the use of `PdfSection`, `PdfPageLabel`, and `PdfDocument` in creating sections with page labels in a PDF.
- Focuses on the customization of page labeling in a document, especially in sections with multiple pages.

### Code Examples

- **C# Example**: Uses a loop to create sections, each containing 10 pages, with a page label prefix reflecting the section number.
- **VB.NET Example**: Similar functionality can be achieved by translating the C# example to VB.NET, though the exact code is not provided here.

## Page-level Navigation/TOC
- This section is part of a detailed guide on managing PDF elements programmatically, focusing on advanced customization options like borders and page labels.

<!-- tags: [pdf, labels, page customization, vb.net, c#, document, sections, border styles] keywords: [PdfPen, PdfCellStyle, PdfPageLabel, PdfDocument, PdfSection, page labels, transparent borders, section management, programmatically] -->
```