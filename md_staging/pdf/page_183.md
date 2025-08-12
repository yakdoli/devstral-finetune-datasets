```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_183.jpeg
document_name: pdf
page_number: 183
page_id: pdf#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:29Z
fidelity: lossless
-->

# Essential PDF

## Content

```csharp
annot.BorderColor = new PdfColor(Color.Red);
annot.Border = new PdfAnnotationBorder(.5f);
annot.LineEndingStyle = PdfLineEndingStyle.OpenArrow;
annot.AnnotationFlags = PdfAnnotationFlags.Default;
annot.Text = "Free Text";
annot.Opacity = 0.5f;
PointF[] points = { new PointF(100, 400), new PointF(100, 450) };

annot.CalloutLines = points;

page.Annotations.Add(annot);
```

Run the code. You have successfully created a Free Text Annotation box.

![Free Text Annotation](https://via.placeholder.com/200x100.png?text=Free%20Text%20with%20Callouts)
*Figure 29: Free Text Annotation*

### 4.1.3.3 Attachments

PDF document can contain any number of attached files. They are displayed on the Attachments navigation panel. All the data of the attached file is embedded into the document. To add a new attachment to the document, you can use the `PdfAttachment` class.

## API Reference (if applicable)
- **Namespace**: Pdf
- **Class**: PdfAnnotation
- **Properties**:
  - `BorderColor`: Specifies the border color of the annotation.
  - `Border`: Specifies the border style of the annotation.
  - `LineEndingStyle`: Specifies the ending style of the line.
  - `AnnotationFlags`: Specifies the flags for the annotation.
  - `Text`: Specifies the text content of the annotation.
  - `Opacity`: Specifies the opacity of the annotation.
  - `CalloutLines`: Specifies the callout lines for the annotation.

## Code Examples

### Creating a Free Text Annotation with Callouts
```csharp
// Create a new Free Text Annotation
PdfAnnotation annot = new PdfAnnotation();

// Set the border color to red
annot.BorderColor = new PdfColor(Color.Red);

// Set the border width to 0.5
annot.Border = new PdfAnnotationBorder(.5f);

// Set the line ending style to open arrow
annot.LineEndingStyle = PdfLineEndingStyle.OpenArrow;

// Set the annotation flags to default
annot.AnnotationFlags = PdfAnnotationFlags.Default;

// Set the text content
annot.Text = "Free Text";

// Set the opacity
annot.Opacity = 0.5f;

// Define callout lines
PointF[] points = { new PointF(100, 400), new PointF(100, 450) };
annot.CalloutLines = points;

// Add the annotation to the page
page.Annotations.Add(annot);
```

## Cross References
- For more information on annotations, refer to the earlier sections in the document.

<!-- tags: [pdf, annotation, free text, callouts, attachments, winforms, syncfusion-sdk] keywords: [free text annotation, callout lines, opacity, border color, line ending style, annotation flags, pdf attachment] -->
```