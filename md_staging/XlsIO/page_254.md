```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: XlsIO
page_number: 254
page_id: XlsIO#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:32Z
fidelity: lossless
-->

## XlsIO

### Overview
- Demonstrates how to insert images into headers and use formatting strings for page numbering.
- Explains the use of placeholders (`&T`, `&F`, `&A`, etc.) for printing different document details.
- Describes the limitation of XlsIO regarding page count retrieval.

## Content

### Code Example: Inserting Images in Headers

The following code example illustrates how to insert images in the header using different programming languages.

#### Step 1: Inserting Images in Headers

**C# Example:**

```csharp
[C#]
// Insert image in right header.
Image img = Image.FromFile(@"logo.jpg");

// Right Header Image.
sheet.PageSetup.RightHeaderImage = img;
sheet.PageSetup.RightHeader = "&G";
```

**VB.NET Example:**

```vb
[VB.NET]
' Insert image in right header.
Dim img As Image = Image.FromFile("logo.jpg")

' Right Header Image.
sheet.PageSetup.RightHeaderImage = img
sheet.PageSetup.RightHeader = "&G"
```

### Note: Page Count Limitation

Note: XlsIO does not provide any option to get the page count. You can only insert the page count by using the format string, as illustrated in the following code sample.

## Code Examples

**C# Example: Inserting the Page Count**

```csharp
[C#]
``` 

### References
- Together with the code examples, you can explore more deeply into XlsIO functionalities through the Syncfusion documentation or specific API references.
``` 

<!-- tags: [XlsIO, winforms, headers, images, page setup, page count, placeholders, C#, VB.NET] keywords: [insert image, header, page numbering, document details, page count, Syncfusion] -->
```