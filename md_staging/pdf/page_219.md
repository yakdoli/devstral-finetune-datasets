```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_219.jpeg
document_name: pdf
page_number: 219
page_id: pdf#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:43Z
fidelity: lossless
-->

## Chapter: Working with Right-to-Left (RTL) Strings in PDF Documents

### Overview
- Demonstrates how to set up and draw RTL text in PDF documents using Syncfusion's PDF library.
- Includes both C# and VB.NET examples to configure font settings, alignment, and string formatting for RTL text.

### Content

#### Setting Up and Drawing RTL Text in PDF
This section explains how to configure and render text in a right-to-left (RTL) format in PDF documents.

```csharp
// Create a TrueType font
PdfFont font = new PdfTrueTypeFont(f, true);

// Set the format for the string
PdfStringFormat format = new PdfStringFormat();

// Set the text direction as RTL
format.RightToLeft = true;

// Set the alignment to right
format.Alignment = PdfTextAlignment.Right;

// Draw the RTL text
page.Graphics.DrawString(text, font, brush, rect, format);
```

#### VB.NET Example
Below is the equivalent implementation in VB.NET for setting up and drawing RTL text in PDF documents.

```vb
' Create a TrueType font
Dim f As Font = New Font("Arial", 14)
Dim font As PdfFont = New PdfTrueTypeFont(f, True)

' Set the format for the string
Dim format As PdfStringFormat = New PdfStringFormat()

' Set the text direction as RTL
format.RightToLeft = True

' Set the alignment to right
format.Alignment = PdfTextAlignment.Right

' Draw the RTL text
page.Graphics.DrawString(text, font, brush, rect, format)
```

#### Key Points
- **Font Creation**: A `PdfTrueTypeFont` object is created with the specified font settings.
- **String Formatting**: The `PdfStringFormat` object is configured to handle RTL text by setting the `RightToLeft` property to `true`.
- **Alignment**: The text is aligned to the right using the `PdfTextAlignment.Right` property.
- **Drawing the Text**: The `DrawString` method is used to render the text with the specified font, brush, and formatting.

### API Reference

#### PdfStringFormat Class
- **Properties**
  - **RightToLeft**: A boolean property to set the text direction.
  - **Alignment**: Enum to specify the alignment of the text.
- **Methods**
  - **DrawString**: Renders text with the specified font, brush, and formatting.

#### PdfTrueTypeFont Class
- **Constructor**
  - `PdfTrueTypeFont(Font font, bool isUnicode)`: Creates a PDF TrueType font.

### Code Examples
The examples above demonstrate how to integrate RTL text rendering into a PDF document using Syncfusion's PDF library. The examples cover both C# and VB.NET, providing flexibility for developers using different languages.

#### Cross References
- Refer to the documentation on string formatting and font handling for more advanced configurations.
- For further details on rendering text in PDF documents, check the relevant sections in the Syncfusion PDF library documentation.

### Notes
- Ensure that the font used supports RTL languages if you're working with text in languages like Arabic or Hebrew.
- Always verify the compatibility of TrueType fonts for proper rendering in PDFs.

<!-- tags: [Syncfusion Windows Forms, PDF library, Text handling, RTL support, C#, VB.NET, Font configuration, Code examples] keywords: [PDF, font, text, right-to-left, alignment, format, draw, C#, VB.NET, RTL, StringFormat, TrueTypeFont] -->
```