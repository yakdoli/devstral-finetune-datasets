```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: HTMLUI
page_number: 113
page_id: HTMLUI#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:17Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

External style sheets are linked to the file through the `Link` tag. While the internal style sheets are applied with the help of the `Style` tag inside the head section, inline style sheets are applied as the values of the style attributes of the specific HTML element.

The following HTML code illustrates the above concepts.

```html
[HTML]

<html>
  <head>
    <link type="text/css" rel="stylesheet" href="ExternalCSS.CSS"></link>
    <style>.div{background-color: #dae5f5;}</style>
  </head>
  <body>
    <p style="background-color: #ffffff;"> This is an inline styled element </p>
    <div class="div"> The Internal style sheet is applied for this element </div>
  </body>
</html>
```

HTMLUI also supports updation of styles to the HTML document at run time. This can be done in two modes, either by changing the value of the style attribute for internal style or the class attribute for the inline style sheet.

```csharp
[C#]

if (this.textBox.Attributes.Contains("style") == false)
    this.textBox.Attributes.Add("style");
this.textBox.Attributes["style"].Value = "background-color:red;";
```

```vb
[VB.NET]

If Me.textBox.Attributes.Contains("style") = False Then
    Me.textBox.Attributes.Add("style")
End If
Private Me.textBox.Attributes("style").Value = "background-color:red;"
```

### 4.13.1 Cascading Style Sheets

Cascading style sheets contain the style definitions for various HTML tags that are defined in the document. Style sheets are included in a HTML document to make the document more clearer so that the actual contents will be inside the document while the styles for these contents will be applied from an external resource. This is to improve the readability of the document and also to apply style changes to the existing document at different times when required.
HTMLUI supports the following style sheets for adding styles to the HTML document:

<!-- tags: HTMLUI, Syncfusion Winforms, Cascading Style Sheets, CSS, Version: 11.4.0.26 -->
```