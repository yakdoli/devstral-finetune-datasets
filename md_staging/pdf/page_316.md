```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_316.jpeg
document_name: pdf
page_number: 316
page_id: pdf#page_316
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:13Z
fidelity: lossless
--> 

## Essential PDF

### TryGetValue Method

```vb
If field.TryGetValue("fl-2", fieldValue) AndAlso fieldValue = "" Then
    TryCast(form.Fields("fl-2"), PdfLoadedTextBoxField).Text = "2"
End If
```

## 4.4 PDF Convertor

### Overview

This section contains detailed descriptions of various Essential PDF conversion capabilities under the following topics:

- **4.4.1 HTML To PDF**

### 4.4.1 HTML To PDF

Web pages and HTML pages can be imported to PDF using the `HtmlConverter`. The `HtmlConverter` converts the HTML web page to a `Bitmap` or `Metafile` image using `MSHTML`.

**Note:** MSHTML is a rendering library used to render HTML documents. The MSHTML library is like an engine that is used to drive Internet Explorer.

Essential PDF renders the converted image into the PDF. You can convert a web page to PDF either as Bitmap or Metafile types.

- Rendering web pages as Bitmap provides reasonable performance.
- Rendering web pages as Metafile provides high resolution.

### Table of Contents

This section covers the following:

- Converting Methods
- HtmlConverter Options

### Converting Methods

HTML documents can be converted to PDF through the following methods:

- **ConvertToImage**
- **FromString**

#### 1. ConvertToImage

## Page-Level Navigation/TOC (if applicable)

- **Further Details on Converting Methods**
  - ConvertToImage
  - FromString

## Cross References

### Keywords and Tags

<!-- tags: [Syncfusion Winforms, Essential PDF, HTML to PDF, HtmlConverter, MSHTML, Bitmap, Metafile] keywords: [HtmlConverter, MSHTML, web page conversion, PDF conversion, web page to PDF, performance, high resolution] -->
```