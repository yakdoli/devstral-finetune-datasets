```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_350.jpeg
document_name: DocIo
page_number: 350
page_id: DocIo#page_350
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:28Z
fidelity: lossless
-->

## Overview
- This page provides a C# code example demonstrating how to insert a text watermark into a Word document. The example includes creating a new Word document, adding a watermark, customizing its properties, and saving the document.

## Content

### Code Example for Inserting a Text Watermark

To insert a text watermark into a Word document using C#, you can use the following code:

```csharp
[C#]

// Create a new word document
WordDocument doc = new WordDocument();

doc.EnsureMinimal();

// Add text watermark to the document
TextWatermark textWatermark = new TextWatermark();
doc.Watermark = textWatermark;

textWatermark.Size = 48;
textWatermark.Layout = WatermarkLayout.Horizontal;
textWatermark.Semitransparent = false;
textWatermark.Color = Color.Black;
textWatermark.Text = "Watermark";

// Save the document
doc.Save("Watermark.doc", FormatType.Doc);

// Close the document
doc.Close();
```

### Explanation
- **WordDocument**: The `WordDocument` class is used to create a new Word document.
- **EnsureMinimal()**: Ensures that the document only contains the necessary elements.
- **TextWatermark**: The `TextWatermark` class is used to create and configure the watermark.
- **Size**: Sets the font size of the watermark text.
- **Layout**: Defines the orientation of the watermark (in this case, horizontal).
- **Semitransparent**: Determines whether the watermark should be semitransparent.
- **Color**: Sets the color of the watermark text.
- **Text**: Specifies the text content of the watermark.
- **Save**: Saves the document with the specified filename and format.
- **Close**: Closes the document after it has been saved.

## API Reference

The code example uses the following classes and methods:

- **WordDocument**
  - **EnsureMinimal()**: Simplifies the document structure to only include what is necessary.
  - **Watermark (property)**: Sets the watermark for the document.
  - **Save(String, FormatType)**: Saves the document to a file with the specified format.
  - **Close()**: Closes the document.

- **TextWatermark**
  - **Size**: Sets the font size.
  - **Layout**: Determines the layout (e.g., horizontal, vertical).
  - **Semitransparent**: Sets the transparency mode.
  - **Color**: Sets the color of the text.
  - **Text**: Sets the text content.

## Code Examples

The provided C# code illustrates the complete process of inserting a text watermark into a Word document, including creating and configuring the watermark and saving the document.

### Description
The example demonstrates how to:
1. Initialize a new `WordDocument`.
2. Add a `TextWatermark` to the document with specific properties such as size, layout, transparency, color, and text.
3. Save the document to a file.
4. Close the document after saving.

## Cross References

- **See also**: Documentation on creating and modifying Word documents, customizing document elements, and saving files in various formats.

<!-- tags: DocIO, Winforms, WordDocument, TextWatermark, Syncfusion.Windows.Forms, C# examples, watermark insertion keywords: text watermark, Word document, C#, document format, document properties, watermark layout, document save, document close -->
```