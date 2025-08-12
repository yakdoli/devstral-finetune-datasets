```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_358.jpeg
document_name: pdf
page_number: 358
page_id: pdf#page_358
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:05Z
fidelity: lossless
-->

# Essential PDF

```vb
Dim spanMap As Integer() = New Integer(count - 1){}

' Set just spanned cells. Other values are not important
' Except negatives that are not allowed.
spanMap(0) = 2
spanMap(2) = 3

args.ColumnSpanMap = spanMap

'Sets row height.
args.MinimalHeight = 30f

End If
End Sub
```

## 5.1.2.4 How To Improve Performance?

Performance is the one of the initial requirements of Essential PDF. This section describes performance tips that help using the product in the most appropriate way.

### Text and Font

- It is good to use PdfStandardFont during text output than Unicode characters. Standard fonts take less space in the file than other fonts.
- If PdfTrueType font is used, and it is not expected to use Unicode characters, switching off the Unicode support will reduce the size of the output PDF file. Support of Unicode by PdfTrueTypeFont is specified in the constructor.
- Do not enable RightToLeft property of PdfStringFormat, if right-to-left language is not used. Setting this property to true enables a special RTL engine that decreases the text layouting speed.

### Compression and File Structure

Changing these can change the resulting file size, however it can increase the time spent on saving.

#### Compression

Compression is responsible for compressing internal data streams in PDF. You might be surprised by the number of streams in an ordinary PDF document. High quality compression involves longer file saves, but requires less space.
```