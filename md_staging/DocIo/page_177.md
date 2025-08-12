```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_177.jpeg
document_name: DocIo
page_number: 177
page_id: DocIo#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:38Z
fidelity: lossless
-->

## Picture Properties and Methods

| Property                | Description                                               |
|-------------------------|-----------------------------------------------------------|
| VerticalPosition        | Gets or sets text wrapping style of the picture.         |
| Width                   | Gets or sets picture width (in points).                  |
| WidthScale              | Gets or sets picture width scale factor in percent.     |

### Public Methods

| Name         | Description                          |
|--------------|--------------------------------------|
| AddCaption   | Add Caption for current Picture.     |
| LoadImage    | Loads image.                        |

## Layout Formats in MS Word

The following screenshot illustrates the various layout formats available in MS Word.

![Layout Formats in MS Word](image.png)

**Figure 62: Layout Formats in MS Word**

## API Reference

### Picture Layout Methods

- **AddCaption()**: Adds a caption to the current picture.
- **LoadImage()**: Loads an image into the document.

### Picture Positioning

- **Horizontal Positioning**: 
  - **Alignment**: Set the alignment relative to a column (e.g., left).
  - **Book layout**: Inside margins of the page.
  - **Absolute position**: Specify the exact position relative to the column.

- **Vertical Positioning**:
  - **Alignment**: Set the alignment relative to the page (e.g., top).
  - **Absolute position**: Specify the exact position relative to the paragraph.

### Layout Options

- **Move object with text**: Toggle to move the image along with the text.
- **Allow overlap**: Enable overlapping of the image with other content.
- **Lock anchor**: Lock the image's position within the document.
- **Layout in table cell**: Enable layout within table cells.

## Code Example (C#)

```csharp
private void ConfigurePicture()
{
    // Initialize the picture object
    Picture picture = document.AddPicture();
    
    // Load the image
    picture.LoadImage("path_to_image.jpg");
    
    // Set the caption
    picture.AddCaption("Example Caption");
    
    // Set horizontal alignment
    picture.VerticalPosition = PictureAlignment.Left;
    picture.HorizontalPosition = PicturePosition.Inside;
    
    // Additional layout options
    picture.MoveObjectWithText = true;
    picture.AllowOverlap = false;
}
```

## Page-level Navigation/TOC
- Public Methods
- Layout Formats in MS Word
- API Reference
- Code Example

<!-- tags: [syncfusion, winforms, ms-word, picture, layout] keywords: [ms-word, layoutformats, api, codeexample, picturealignment] -->
```