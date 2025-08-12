```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: DocIo
page_number: 155
page_id: DocIo#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:40Z
fidelity: lossless
-->

# Essential DocIO

```csharp
textField.CharacterFormat.FontSize = 20.0F
```

Setting text of text form field and its character format.  
If `textField.TextRange.Text` value is not equal to `string.Empty`,  
form field's text will be `textField.TextRange.Text`, otherwise `textField.DefaultText`.

```csharp
textField.TextRange.Text = String.Empty
textField.TextRange.CharacterFormat.FontName = "Comic Sans MS"
textField.TextRange.CharacterFormat.Shadow = True
textField.TextRange.CharacterFormat.FontSize = 20.0F
textField.TextRange.CharacterFormat.TextColor = Color.Blue

Case Else
End Select
Next ffield
Next body
Next sec
```

DocIO also provides the option to add or remove form field shading. It specifies whether to turn on the gray shading on form fields using the below code snippet.

```csharp
[C#]

document.Properties.FormFieldShading = false;
```

```vb
[VB.NET]

document.Properties.FormFieldShading = False
```

## Hyperlink

A hyperlink is a colored and underlined text or a graphic, which when clicked, directs to a file, or a location in a file, or an HTML page on the World Wide Web, or an HTML page on an Intranet. It includes the path information to another object. The object can be a target on the same document, a file on the same computer, or a uniform resource locator, giving the location of a web page halfway around the world. The process is exactly the same in all cases. Some point on the document is turned into an active spot, which includes the path information.

<!-- tags: [DocIO, form field shading, hyperlinks, document properties] keywords: [form field, gray shading, text formatting, hyperlink, document, path information, text fields, character format] -->
```