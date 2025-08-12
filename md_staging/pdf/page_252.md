<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: pdf
page_number: 252
page_id: pdf#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:07Z
fidelity: lossless
-->

# Page 252: Footer Template Example

## Overview
- Demonstrates how to create a footer template for a PDF document.
- Includes fields for page number and total page count.
- Uses a composite field to combine these elements into a single footer.

## Content

In this section, we will create a footer template using the `PdfPageTemplateElement` and add fields for the page number and page count. These fields are combined into a composite field which is drawn in the footer.

### Footer Template Creation
1. **Create a page template**:
   ```vb
   Dim footer As PdfPageTemplateElement = New PdfPageTemplateElement(rect)
   ```

2. **Create page number field**:
   ```vb
   Dim pageNumber As PdfPageNumberField = New PdfPageNumberField(font, brush)
   ```

3. **Create page count field**:
   ```vb
   Dim count As PdfPageCountField = New PdfPageCountField(font, brush)
   ```

4. **Add the fields in composite fields**:
   ```vb
   Dim compositeField As PdfCompositeField = New PdfCompositeField(font, brush, "Page {0} of {1}", pageNumber, count)
   compositeField.Bounds = footer.Bounds
   ```

5. **Draw the composite field in footer**:
   ```vb
   compositeField.Draw(footer.Graphics, New PointF(470, 40))
   ```

6. **Add the footer template at the bottom**:
   ```vb
   doc.Template.Bottom = footer
   ```

## Code Example
```vb
' Footer.
' Create a Template that can be used as a footer.
' Create a page template
Dim footer As PdfPageTemplateElement = New PdfPageTemplateElement(rect)

' Create page number field
Dim pageNumber As PdfPageNumberField = New PdfPageNumberField(font, brush)

' Create page count field
Dim count As PdfPageCountField = New PdfPageCountField(font, brush)

' Add the fields in composite fields
Dim compositeField As PdfCompositeField = New PdfCompositeField(font, brush, "Page {0} of {1}", pageNumber, count)
compositeField.Bounds = footer.Bounds

' Draw the composite field in footer
compositeField.Draw(footer.Graphics, New PointF(470, 40))

' Add the footer template at the bottom
doc.Template.Bottom = footer
```

## API Reference
- **PdfPageTemplateElement**: Represents a page template that can be used to add repetitive content to pages.
- **PdfPageNumberField**: Represents a field that displays the current page number.
- **PdfPageCountField**: Represents a field that displays the total page count.
- **PdfCompositeField**: Represents a composite field that combines multiple fields into a single element.

### Methods
- `Draw(Graphics g, PointF position)`: Draws the field at the specified position on the graphics context.
- `SetBounds(RectangleF bounds)`: Sets the bounds for the field.

## Cross References
- Refer to the documentation for `PdfDocument` and `PdfPageTemplateElement` for more details on working with PDF templates.

<!-- tags: [Syncfusion, WinForms, PDF, Footer, Template, Page Number, Page Count, Composite Field] keywords: [footer, template, page number, page count, composite field, pdf, document, bounds, graphics, draw] -->