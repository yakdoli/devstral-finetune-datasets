```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: HTMLUI
page_number: 137
page_id: HTMLUI#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:58Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates the usage of HTMLUI controls for formatting user input and converting it into a different format.
- Explores the functionality of exporting HTML documents as images using the HTMLUI control.

## Content

### ElementFormat Sample

#### Figure 46: ElementFormat Sample
The figure below shows a sample interface demonstrating how user input can be intercepted and changed to appear with a different format. In this case, smiley descriptions are substituted with smiley images.

![](images/placeholder.png)

#### Explanation
This sample showcases the process of intercepting user input and changing it to appear with a different format (in this case, smiley descriptions are substituted with smiley images).

---

### 4.17 Exporting

Essential HTMLUI supports the export of HTML documents. These documents that are available in the HTMLUI control can be exported as images. The HTMLUI control uses the `InputHTML` class to render the HTML document and then converts the available document to Bitmaps. The following code snippet illustrates this.

#### Code Example
```csharp
[C#]
private void button1_Click(object sender, System.EventArgs e)
{
    Bitmap bmp = CreateBitmap();
    bmp.Save(@"C:\Myprojects\Bitmap.bmp");
    bmp.Dispose();
}
```

## API Reference (if applicable)
- `InputHTML`: Class used for rendering HTML documents.
- `CreateBitmap()`: Method responsible for converting the HTML document to a Bitmap.

## Code Examples
The provided C# code snippet demonstrates how to export an HTML document as an image using the HTMLUI control.

## Page-level Navigation/TOC (if applicable)
- ElementFormat Sample
- Exporting

## Cross References
- Refer to the `InputHTML` class for more details on rendering HTML documents.
- Review documentation on converting documents to Bitmaps for additional context.

## RAG Annotations
<!-- tags: [HTMLUI, Exporting, Bitmap, InputHTML] keywords: [Essential HTMLUI, ElementFormat, Smileys, Export, Images, Bitmap, HTMLUI control, InputHTML class, Code examples] -->
```