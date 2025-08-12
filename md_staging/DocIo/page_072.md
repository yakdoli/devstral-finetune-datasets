```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: DocIo
page_number: 072
page_id: DocIo#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:42Z
fidelity: lossless
-->

# Essential DocIO

```vb
Dim doc As WordDocument = New WordDocument()
doc.Open("DocumentProperties.doc")

' Getting custom property value
Dim phoneNumber As Integer = doc.CustomDocumentProperties("Telephone number").ToBit()

' Setting existent custom property value
doc.CustomDocumentProperties("Check by").Value = "user name"

' Adding new custom property
Dim completedDate As DateTime = DateTime.Now
doc.CustomDocumentProperties.Add("Date completed", completedDate)
```

## 4.2.2 Document Background

### Overview
- Background and Watermark classes represent the background effects in the Word document.
- To set the background effects in Word, open the Format menu and click Background. The following are the background effects available in Word.

### Content

#### Background and Watermark Classes
- **Fill Color**
- **Fill Effects (Gradient, Texture, Pattern, Picture)**
- **Printed Watermark**

![Background and Watermark classes in the Word document](https://via.placeholder.com/300x200?text=Figure+27)

**Note:** A document can also have a printed watermark and background effect (fill color or one of fill effects) at the same time.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [DocIo, WordDocument, CustomDocumentProperties, Watermark, Fill Color, Fill Effects, Print, Watermark, Background] -->
```