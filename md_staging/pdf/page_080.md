```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: pdf
page_number: 080
page_id: pdf#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:18Z
fidelity: lossless
-->

# Essential PDF

## 4.1.2.1 Text

This section deals with various types of text supported by Essential PDF. It includes the following topics:

- Draw Text - Provides brief description on rendering RTF text, unicode text and text flow mechanisms
- HTML Styled Text - Provides explanation on rendering HTML formatted text in PDF
- Automatic Field - Demonstrates how various dynamic fields such as date are inserted in PDF
- Links - Describes how text with links are inserted in a PDF document

### 4.1.2.1.1 Drawing Text

This section elaborates on various procedures for drawing the text in a PDF document.

The following are the procedures used:

- Using DrawString
- Paginating the text area
- String Formatting and
- RTF Support

#### Using DrawString

PdfGraphics class contains plenty of DrawString methods. It draws the specified text string at the specified location with the specified size, brush and font. The format of the methods is similar to the System.Drawing.Graphics.DrawString methods.

```csharp
[C#]
public DrawString( string s, PdfFont font, PdfBrush brush, PointF point );
public DrawString( string s, PdfFont font, PdfBrush brush, PointF point, PdfStringFormat format );
public DrawString( string s, PdfFont font, PdfBrush brush, float x, float y );
public DrawString( string s, PdfFont font, PdfBrush brush, float x, float y, PdfStringFormat format );
public DrawString( string s, PdfFont font, PdfPen pen, PointF point );
```

The following code example illustrates this.
```