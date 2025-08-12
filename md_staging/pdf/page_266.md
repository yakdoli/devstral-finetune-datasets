```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: pdf
page_number: 266
page_id: pdf#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:16Z
fidelity: lossless
-->

# Essential PDF

It also displays other information of the document, which is not always evaluated at the moment of constructing the document.

## Overview
- Displaying the correct value of the field requires specifying important properties.
- Properties include Font, Brush, Bounds, Location, and Size.
- Numeric fields have an additional numbering style property.

## Field Properties

### Font
- Font used to display the value of the field.
- Exception is thrown if this property is not set.

### Brush
- Brush used to print the value of the field.
- Exception is thrown if this property is not set.

### Bounds
- Specifies the bounds of the field.

### Location
- Location of the field.
- Default point is (0, 0).

### Size
- Size of the field.
- If not set, the size is automatically calculated to display the value.

#### Note
**It is not necessary to set the Bounds and Size with Location at the same time.**  
Size and Bounds.Size have the same values.

## Numbering Styles for Numeric Fields

### Available Numbering Styles
- Arabic (1, 2, 3, 4, ...)
- Upper Roman (I, II, III, IV, ...)
- Roman (i, ii, iii, iv, ...)
- Upper Latin (A, B, C, D, ..., Z, AA, AB, ...)
- Latin (a, b, c, d, ..., z, aa, ab, ...)

### Description of Numbering Fields

- **PdfPageNumberField**: Number of the page on which the field has been drawn.
- **PdfPageCountField**: Total number of pages in the document.
- **PdfSectionPageNumberField**: Number of pages within a section.
- **PdfSectionPageCountField**: Number of sections in a document.
- **PdfSectionNumberField**: Number of sections within a document.
- **PdfCreationDateField**: Creating date of the document; the value is taken from the DocumentInformation.CreationDate property.
- **PdfDateTimeField**: Current date and time.
- **PdfDestinationPageNumberField**: Number of the specified destination page.

## Cross References
- See also: essential PDF, numeric fields, numbering styles, field properties

<!-- tags: [essential pdf, numeric fields, numbering styles, field properties, pdf] keywords: [font, brush, bounds, location, size, numbering styles, pdf page number field, pdf page count field, pdf section page number field, pdf section page count field, pdf section number field, pdf creation date field, pdf date time field, pdf destination page number field] -->
```