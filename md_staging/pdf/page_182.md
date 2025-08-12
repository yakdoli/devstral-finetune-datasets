```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_182.jpeg
document_name: pdf
page_number: 182
page_id: pdf#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:59Z
fidelity: lossless
-->

# Essential PDF

## Annotation Properties

### Property Details

| Property         | Type          | Value It Accepts                 | Description                                             |
|------------------|---------------|-----------------------------------|---------------------------------------------------------|
| Border           | float         | PdfAnnotationBorder              | Allows you to set the border type of the Annotation box. |
| LineEndingStyle  | lineStyle     | PdfLineEndingStyle              | Allows you to set the line ending style for the callout line. |
| AnnotationFlags  | PdfAnnotationFlag | PdfAnnotationFlags            | Allows you to set annotation flags. |
| Opacity          | opacity       | Float                           | Allows you to set the opacity of the Annotation box. |
| CalloutLines     | Points        | PointF[]                        | Allows you to set the starting and ending coordinates of the callout line. |

## List of Methods

The following table lists the methods available.

### Methods

| Method                      | Parameters of the Method                        | Return Type | Purpose                                      |
|-----------------------------|-------------------------------------------------|--------------|----------------------------------------------|
| PdfFreeTextAnnotation       | PdfFreeTextAnnotation(System.Drawing.RectangleF) | Annotations   | Creates annotation to be added to the PDF document. |

## Creating a Free Text Annotation

### Overview
- 1. Illustrates the creation of Free Text Annotation in PDF.
- 2. Demonstrates setting text properties, font styles, and colors.
- 3. Explains how to create and configure a free text annotation using API methods.

### Creating a Free Text Annotation

The following code snippet illustrates the creation of Free Text Annotation in PDF.

#### Code Example

```csharp
[C#]

PdfFreeTextAnnotation annot = new PdfFreeTextAnnotation(new RectangleF(50, 100, 100, 50));

annot.MarkupText = "Free Text with Callouts";

annot.TextMarkupColor = new PdfColor(Color.Black);
annot.Font = new PdfStandardFont(PdfFontFamily.Helvetica, 7f);
annot.Color = new PdfColor(Color.Yellow);
```

## Page-level Navigation/TOC

- **List of Methods**
- **Creating a Free Text Annotation**

## Cross References

See also:
- PdfAnnotationBorder
- PdfLineEndingStyle
- PdfAnnotationFlags
- PdfFreeTextAnnotation
- System.Drawing.RectangleF
- PdfColor
- PdfStandardFont
- PdfFontFamily

<!-- tags: [Essential PDF, Annotation, Free Text Annotation, WinForms, version 11.4.0.26] keywords: [PdfFreeTextAnnotation, AnnotationFlags, LineEndingStyle, Border, Opacity, CalloutLines] -->
```