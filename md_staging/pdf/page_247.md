```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_247.jpeg
document_name: pdf
page_number: 247
page_id: pdf#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:49Z
fidelity: lossless
-->

## Page Layout and Scaling

### Supported Page Sizes

- Half Letter
- Ledger
- Letter
- Legal
- Note
- Letter11x17

### Supported Page Layouts

- OneColumn
- SinglePage
- TwoColumnLeft
- TwoColumnRight
- TwoPageRight
- TwoPageLeft

### Supported Page Modes

- Full screen
- UseAttachment
- UseNone
- UseOC
- UseOutlines
- UseThumbs

### Page Scaling Options in Print Dialog

When a print dialog is displayed for a document, the values to be selected for the page scaling option are as follows:

- **None**: Indicates that the print dialog should reflect no page scaling
- **AppDefault**: Indicates that applications should use the current print scaling

#### Note
If this entry has an unrecognized value, applications should use the current print scaling. The default value is **AppDefault**.

### Page Settings Code Snippets

The following code snippets illustrate the various page settings.

#### C#
```csharp
// To set landscape page orientation.
doc.PageSettings.Orientation = PdfPageOrientation.Landscape;
```

## API Reference

### Methods
- **SetOrientation**: Sets the orientation of the page (e.g., landscape or portrait).

### Enumerations
- **PdfPageOrientation**: Represents the orientation of the page.
  - **Landscape**: Horizontal orientation.
  - **Portrait**: Vertical orientation.

### Parameters
- **doc**: The document object to which the settings are applied.
- **Orientation**: Sets the orientation property of the page settings.

## Code Examples

#### Example: Setting Page Orientation
```csharp
// Create a new document
PdfDocument doc = new PdfDocument();

// Set the page size to Letter
doc.PageSettings.Margins = new PdfMargins(20, 20, 20, 20);
doc.PageSettings.Orientation = PdfPageOrientation.Landscape;

// Add a new page
PdfPage page = doc.Pages.Add();

// Add content to the page
PdfGraphics graphics = page.Graphics;
graphics.DrawString("This is a landscape page", new PdfStandardFont(PdfFontFamily.TimesRoman, 20), PdfBrushes.Black, new RectangleF(20, 20, 300, 50));

// Save the document
doc.Save(@"C:\LandscapePage.pdf");

// Close the document
doc.Close();
```

## Cross References

See also:
- [pageNumber]: Details on working with PDF documents.
- [pageNumber]: Additional examples of PDF manipulation.

<!-- tags: [pdf, layout, scaling, print, orientation, syncfusion] keywords: [landscape, portrait, page settings, print dialog, pdf document, page modes, page layouts, full screen, useattachment, useoutlines, usethumbs] -->
```