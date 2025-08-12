```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: DocIo
page_number: 175
page_id: DocIo#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:58Z
fidelity: lossless
-->

## Essentials for Document Formatting

### Overview
- Explains the vertical alignment options for shapes.
- Lists the variants for the HorizontalOrigin and VerticalOrigin properties.
- Describes setting picture dimensions and scaling.
- Provides details on loading and appending images.

### Content

#### Vertical Alignment Property

The VerticalAlignment property returns the object of the ShapeVerticalAlignment type. The following are the variants for the VerticalAlignment property:

- Center
- Right
- Inside
- Outside

#### ShapeVerticalAlignment Variants

The following are the variants for the VerticalAlignment property:

- Bottom
- Center
- Inline
- Inside
- None
- Outside
- Top

#### HorizontalOrigin and VerticalOrigin Properties

HorizontalOrigin and VerticalOrigin properties define the reference origin, which is used for relative positioning of a picture.

#### HorizontalOrigin Property Variants

The HorizontalOrigin property returns the value of the HorizontalOrigin type. The following are the variants for the HorizontalOrigin property:

- Margin
- Page
- Column
- Character

#### VerticalOrigin Property Variants

The VerticalOrigin property returns the value of VerticalOrigin type. The following are the variants for the VerticalOrigin property:

- Margin
- Page
- Paragraph
- Line

#### Setting Picture Dimensions and Scaling

You can set the width and height of the picture by using the Width and Height properties, and the HeightScale and WidthScale properties to get or set picture scaling.

#### Loading and Appending Images

The LoadImage function is used to set an image by loading the System.Drawing.Image object, or image bytes array. Also, you can use the AppendPicture function of the WParagraph class to append a picture to a paragraph.

### API Reference

- **Properties**
  - Width
  - Height
  - HeightScale
  - WidthScale

- **Functions**
  - LoadImage
  - AppendPicture

### Code Examples

```csharp
// Example of setting image properties
using Syncfusion.DocIO;
using System.Drawing;

// Create a new Word document
WordDocument document = new WordDocument();

// Get the first section of the document
WSection section = document.AddSection();

// Add a paragraph to the section
WParagraph paragraph = section.AddParagraph();

// Load an image
System.Drawing.Image image = System.Drawing.Image.FromFile("path_to_image.jpg");

// Append the image to the paragraph
paragraph.AppendPicture(image, "ImageCaption");

// Set image properties
paragraph.Format.ImageInfo.Height = 100;
paragraph.Format.ImageInfo.Width = 200;
paragraph.Format.ImageInfo.HeightScale = 50;
paragraph.Format.ImageInfo.WidthScale = 50;
```

### Cross References

See also:
- [Property Reference for Word Processing](property-reference-for-word-processing)
- [Image Handling in Word Documents](image-handling-in-word-documents)

<!-- tags: [syncfusion, winforms, docio, verticalalignment, horizontalorigin, verticalorigin, image, scaling] keywords: [vertical alignment, horizontal origin, vertical origin, picture dimensions, image scaling, append picture] -->
```