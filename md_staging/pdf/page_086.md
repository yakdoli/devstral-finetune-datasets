```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: pdf
page_number: 086
page_id: pdf#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:19Z
fidelity: lossless
-->

# Numeric Fields and Page Information in PDF

## Overview
- Explores the usage of numeric fields and page-related fields in PDF documents.
- Describes the various numbering styles and page information fields available in Syncfusion Winforms.
- Demonstrates how to programmatically display and manage page numbers in PDF documents.

## Content

### Note
**It is not necessary to set the Bounds and Size with Location at the same time. Size and Bounds.Size have the same values.**

#### Numeric Fields
Numeric fields have an additional **NumberingStyle** property. There are five possible numbering styles supported by the automatic fields. They are as follows:

- Arabic (1, 2, 3, 4, ...)
- Upper Roman (I, II, III, IV, ...)
- Roman (i, ii, iii, iv, ...)
- Upper Latin (A, B, C, D, ..., Z, AA, AB, ...)
- Latin (a, b, c, d, ..., z, aa, ab, ...)

**Brief descriptions on the various numbering fields are given below:**

- **PdfPageNumberField** - Specifies the number of the page on which the field has been drawn.
- **PdfPageCountField** - Specifies the total number of pages in the document.
- **PdfSectionPageNumberField** - Specifies the number of pages within a section.
- **PdfSectionPageCountField** - Specifies the number of sections in a document.
- **PdfSectionNumberField** - Specifies the number of sections within a document.
- **PdfCreationDateField** - Specifies the creation date of the document.  
  <!--
  The value is taken from the **DocumentInformation.CreationDate** property.
  -->

- **PdfDateTimeField** - Specifies the current date and time.
- **PdfDestinationPageNumberField** - Specifies the number of the specified destination page.
- **PdfCompositeField** - Specifies the value of the field that is composed of any number of other automatic fields.

**PdfCreationDateField** and **PdfDateTimeField** have the **DateFormatString** property, which defines the formatting string for the value of the field. This property uses the same formatting rules and specifiers as DateTime type of .NET. For detailed information on formatting specifiers, see [http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx](http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx).

#### Drawing Automatic Fields
You can draw the Automatic Fields on the **PdfTemplate** and set them as the document template or manually draw them on the necessary pages. The values of the fields will be automatically populated on each copy of the template.

### Code Example: Displaying Page Numbers

The following code example illustrates how to display page numbers.

```csharp
[C#]
```

## Summary
This page provides detailed information about the various numeric fields and the different ways to display page-related information in PDF documents using Syncfusion Winforms. The example demonstrates programmatically displaying page numbers, ensuring flexibility and control over the appearance and content of PDF documents.

<!-- tags: Syncfusion Winforms, numeric fields, PDF, page numbering, AutoFields, DateFormatter, .NET -->
```