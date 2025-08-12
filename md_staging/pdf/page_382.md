```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_382.jpeg
document_name: pdf
page_number: 382
page_id: pdf#page_382
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:37Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Working with Fonts
- Form Fields management
- Form Filling process
- Free Text Annotation guidelines
- Answers to Frequently Asked Questions

### Fonts
- Fonts 77

### Form Fields
- Form Fields 297

### Form Filling
- Form Filling 308

### Free Text Annotation
- Free Text Annotation 180

### Frequently Asked Questions
- Frequently Asked Questions 342

### G
- How To Improve Performance? 358
- How To Insert a Table In The Header? 359
- How to make background images centered, stretched and fitted within the PDF Grid? 380
- How To Measure the String Whose End Position Is Not Known? 360
- How to open the generated PDF document into the browser instead of displaying the Open/Save dialog in browser? 352
- How to position the background image as a tile? 379
- How To Read Conformance Level From PDF? 361
- How To Render Unicode Text [CJK Fonts] In a PDF Document? 350
- How To Set Graphic Units? 351
- How to set margins for the PDF pages? 361
- How to set the default view of Navigation Pane in Viewer? 353
- How to set width for Table? 362
- How to specify bounds for Table during pagination? 363
- How To Store And Retrieve a PDF Document From the Database? 365
- Html Styled Text 83
- HTML To PDF 316
- HTML to PDF Conversion using Gecko Rendering Engine 322
- Hyperlinks for other external files 179

### H
- Header 139, 156
- Headers and Footers 250
  - How can we make IE9 to render metafile? 379
  - How To Access Pages In an Existing Document? 363
  - How To Add Sections And Pages? 342
  - How To Add the Tables One After Another? 355
  - How To Add Watermarks Or Stamps In an Existing Document? 364
  - How To Compress a PDF Document? 343
  - How To Convert Secure Webpages? 375
  - How To Convert Units In PDF / What Are the Units Of the Elements In PDF? 365
  - How To Create a Borderless Table? 343
  - How To Create a Form Which Transfers Data To the Server? 367
  - How To Create Page Labels? 344
  - How To Dispose The Pdf document Object? 352
  - How To Draw a SoftMask Image Into a PDF Document? 345
  - How To Draw an Image In a Table Cell? 355
  - How to edit header in PdfGrid? 362
  - How To Embed 3D Files In a PDF Document? 345
  - How To Embed Fonts? 348
  - How To Enable and Disable PDF Layers In a PDF document? 366

### Graphics
- Drawing Images From an Existing PDF Document? 377
- Extracting Text From an Existing PDF Document? 378
- Finding the End Position Of a Table? 349
- Implementing Column Span In PdfLightTable? 356

### I
- IEnumerable 132
- ImageExtraction 327
- Images 103

## API Reference
- Namespace: `Essential PDF`
- Methods:
  - `ExtractImages()`
  - `ExtractText()`
  - `FindTableEndPosition()`
  - `InsertTableInHeader()`
  - `SetGraphicUnits()`

## Code Examples
```csharp
// Example of extracting text from a PDF
using (PdfDocument document = new PdfDocument("existing_pdf.pdf"))
{
    PdfTextExtraction textExtraction = new PdfTextExtraction(document.Pages[0]);
    string extractedText = textExtraction.Text;
}
```

## Page-level Navigation/TOC
- Fonts
- Form Fields
- Form Filling
- Free Text Annotation
- Frequently Asked Questions
- G
- H
- Graphics
- I

## Cross References
- See Also: `PdfLightTable`, `PdfGrid`, `PdfDocument`

<!-- tags: [Essential PDF, Syncfusion Winforms, fonts, form fields, form filling, free text annotation, frequently asked questions, graphics, images, text extraction] keywords: [fonts, form fields, form filling, free text annotation, frequently asked questions, graphics, images, text extraction, pdfgrid, pdflighttable, pdf document] -->
```