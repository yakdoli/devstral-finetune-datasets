```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_320.jpeg
document_name: pdf
page_number: 320
page_id: pdf#page_320
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:25Z
fidelity: lossless
-->

# EnableJavaScript

You can control the JavaScript by using the `EnableJavaScript` property of the `HtmlConverter` class library. By default, this property is set to `False`. So the JavaScript code is disabled during conversion. Set the `EnableJavaScript` property to `True` to activate the JavaScript code during conversion.

The following code example illustrates this:

### [C#]

```csharp
HtmlConverter html = new HtmlConverter();

// Activating JavaScript
html.EnableJavaScript = true;
```

### [VB.NET]

```vb
Dim html As HtmlConverter = New HtmlConverter()

' Activating JavaScript
html.EnableJavaScript = True
```

> **Note:** If JavaScript code is not executed by setting the `EnableJavaScript` property, it means the Internet Security Settings on the server do not allow the JavaScript execution.

## Enable Hyperlink

Essential PDF supports enabling/disabling live hyperlinks in PDF while converting web pages to PDF. The following code example illustrates this:

### [C#]

```csharp
HtmlConverter html = new HtmlConverter();

// Enabling Hyperlink
html.EnableHyperlinks = true;
```

### [VB.NET]

```vb
Dim html As New HtmlConverter()

' Enabling Hyperlink
html.EnableHyperlinks = True
```
```html

<!-- tags: [Syncfusion Winforms, Essential PDF, HtmlConverter, EnableJavaScript, EnableHyperlinks] keywords: [JavaScript, web page conversion, PDF, Hyperlinks, Internet Security Settings] -->
```