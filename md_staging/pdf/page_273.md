```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_273.jpeg
document_name: pdf
page_number: 273
page_id: pdf#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:23Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Describes the process of importing and replacing pages in a PDF document.
- Highlights the restriction on manipulating "old" layers in imported pages.
- Explains the process of replacing images within a PDF document.

## Content

### Importing Process
The importing is done by converting the page content to the PdfTemplate object, which means that the new page will not inherit the possibly complex layer structure, so you will see just one default layer. Obviously, you will be able to place something beneath that layer. However, you will not be able to manipulate the "old" layers, because they won't exist.

This conversion is performed in order to avoid an incomplete page, harming further user output.

### Restrictions
- **Page Layers**: All pages are appended to the host document to make easier bookmarks (outlines). Bookmarks are organized as a complex tree, as it is hard to calculate where the new items should be placed.
- **Outlines (Bookmarks)**: Outlines (Bookmarks) will be copied to the target document along with the pages. The library will try to rebuild the bookmark tree with those bookmarks that have the destination pointing to any of the imported pages.
- **Incomplete Bookmarks**: The outline tree might look a bit weird if just part of it was copied, as it is hard to recreate the tree with part of the bookmarks.
- **Content Importation**: Some of the contents are usually imported from the original document to the final document during saving process. Hence, the original document has to be closed only after the final document is saved.

### Importing Notes
>Note: To import the document asynchronously for Windows Store apps, refer to the Asynchronous Support section.

### Replacing Images

#### Overview
Essential PDF supports extracting image locations from an existing document, replacing with new images, and then saving them in the same locations.

#### Implementation
This feature is implemented using the following APIs.

##### Replacing Images
This is done using the `ReplaceImage` method.

```csharp
doc.Pages[0].ReplaceImage(1, new PdfBitmap(@"Water lilies.jpg"));
```

##### Extracting Image Location
The `ExtractImageLocation` method can be used to extract image locations.

## API Reference

### Methods
- `ReplaceImage(int index, PdfBitmap newBitmap)`
  - **Parameters**:
    - `index`: The index of the image to be replaced.
    - `newBitmap`: The new image to replace the old image.
  - **Returns**: `void`

## Code Examples

### Replacing an Image
```csharp
// Example of replacing an image within a PDF page.
doc.Pages[0].ReplaceImage(1, new PdfBitmap(@"Water lilies.jpg"));
```

### Extracting Image Location
Extract Image Location functionality allows retrieving the location of images within a PDF document.

## Cross References
See also:
- Asynchronous Support
- PdfTemplate
- PdfBitmap

<!-- tags: [pdf, document, image replacement, essential pdf, winforms, syncfusion] keywords: [replacing images, importing pages, outline tree, bookmarks, asynchronous support, image location, pdftemplate, pdfbitmap] -->
```