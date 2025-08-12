```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_334.jpeg
document_name: pdf
page_number: 334
page_id: pdf#page_334
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:26Z
fidelity: lossless
-->

## Overview
- Lists various PDF features and their availability in the Syncfusion Winforms PDF API.
- Indicates support status for different PDF components, such as `ArcSegment`, `Canva`, and `Glyphs`.
- Highlights restrictive features marked as `No`, indicating limitations in functionality.

## Content

The following table summarizes the availability and support status of various PDF features:

| Feature | Available |
|---------|-----------|
| ArcSegment | Yes |
| Canva | Yes |
| DocumentOutline | No |
| DocumentReference | No |
| FigureStructure | No |
| FixedPageResources | Yes |
| Glyphs | Yes |
| Gradient | Yes |
| ImageBrush | Yes |
| Intent | Yes |
| LinkTarget | Yes |
| ListitemStructure | Yes |
| ListStructure | Yes |
| MatrixTransform | Yes |
| NamedElement | No |
| OutlineEntry | No |
| PageContent | Yes |
| PageContentLinkTargets | No |
| ParagraphStructure | No |
| Path | Yes |
| PolyBezierSegment | Yes |
| PolyLineSegment | Yes |
| PolyQuadraticBezierSegment | Yes |
| ResourceDictionary | Yes |
| SectionStructure | No |
| SignBy | No |
| SignatureDefinition | No |

### Notes
- Features marked as `Yes` are supported and can be utilized in the PDF API.
- Features marked as `No` are either not supported or restricted in the current version.

## API Reference

### Methods/Properties
- `ArcSegment`: Available for usage.
- `Canva`: Available for usage.
- `FixedPageResources`: Available for usage.
- `PolyBezierSegment`: Available for usage.
- `PolyLineSegment`: Available for usage.
- `PolyQuadraticBezierSegment`: Available for usage.
- `ResourceDictionary`: Available for usage.

### Restricted Features
- `DocumentOutline`: Not supported.
- `DocumentReference`: Not supported.
- `FigureStructure`: Not supported.
- `NamedElement`: Not supported.
- `OutlineEntry`: Not supported.
- `PageContentLinkTargets`: Not supported.
- `ParagraphStructure`: Not supported.
- `SectionStructure`: Not supported.
- `SignBy`: Not supported.
- `SignatureDefinition`: Not supported.

## Code Examples

```csharp
// Example: Using ArcSegment in PDF generation
PdfGraphics graphics = new PdfGraphics();
PdfBrush brush = new PdfSolidBrush(PdfColor.Blue);
PdfArcSegment arcSegment = new PdfArcSegment(new PointF(100, 100), new SizeF(50, 50), 0, 90);
graphics.DrawPath(brush, new PdfPath().Add(arcSegment));
```

## Cross References

- **See also:**
  - [Syncfusion PDF API Documentation](https://help.syncfusion.com/windowsforms/pdf)
  - [PDF Features in WinForms](https://www.syncfusion.com/products/windowsforms/pdf)

## RAG Annotations
<!-- tags: [product, pdf, features, availability, restrictons] keywords: [ArcSegment, Canva, DocumentOutline, FixedPageResources, Glyphs, Gradient, ImageBrush, Intent, LinkTarget, ListitemStructure, ListStructure, MatrixTransform, NamedElement, OutlineEntry, PageContent, PageContentLinkTargets, ParagraphStructure, Path, PolyBezierSegment, PolyLineSegment, PolyQuadraticBezierSegment, ResourceDictionary, SectionStructure, SignBy, SignatureDefinition, Syncfusion Winforms, PDF API, version 11.4.0.26] -->
```