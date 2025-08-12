```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_380.jpeg
document_name: pdf
page_number: 380
page_id: pdf#page_380
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:26Z
fidelity: lossless
-->

## 5.5.2 How to make background images centered, stretched and fitted within the PDF Grid?

### Background Image Positioning with PdfGrid

Background image positioning such as stretch, center, and fit within the PDF Grid can be done by setting the property `ImagePosition` to `PdfGridImagePosition.Stretch`, `PdfGridImagePosition.Centre`, and `PdfGridImagePosition.Fit` respectively.

```csharp
grid.Rows(1).Cells(0).ImagePosition = PdfGridImagePosition.Stretch
grid.Rows(1).Cells(1).ImagePosition = PdfGridImagePosition.Centre
grid.Rows(1).Cells(2).ImagePosition = PdfGridImagePosition.Fit
```

For more information on positioning background images, refer to the section **Background Image Positioning** in **PdfGrid Cell**.

## API Reference

### Key Enum Members

- `PdfGridImagePosition.Stretch`: The image is stretched to fill the entire cell.
- `PdfGridImagePosition.Centre`: The image is centered within the cell.
- `PdfGridImagePosition.Fit`: The image is scaled to fit within the cell dimensions while maintaining its aspect ratio.

## Code Examples

Here is an example demonstrating how to apply different image positions to cells in a Grid:

```csharp
// Assuming grid is already initialized and contains appropriate rows and cells.
grid.Rows(1).Cells(0).ImagePosition = PdfGridImagePosition.Stretch;
grid.Rows(1).Cells(1).ImagePosition = PdfGridImagePosition.Centre;
grid.Rows(1).Cells(2).ImagePosition = PdfGridImagePosition.Fit;

// Save the grid to a PDF file.
grid.Save("ExamplePdfGridImagePosition.pdf", Format.Pdf);
```

## See also

- **Background Image Positioning** in **PdfGrid Cell**
- PDF Generation and Manipulation in Syncfusion WinForms
- Grid Customization and Styling with Syncfusion

<!-- tags: [Syncfusion WinForms, PdfGrid, Background Image Positioning, Stretch, Centre, Fit] keywords: ["background images", "PdfGrid", "Grid Image Position", "Stretch", "Centre", "Fit", "PDF", "Customization"] -->
``` 
