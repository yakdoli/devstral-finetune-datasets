```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: HTMLUI
page_number: 157
page_id: HTMLUI#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:06Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## HTML Attribute Modifications

### Adding Attributes Dynamically

#### Code Snippets

[C#]
```csharp
// textBox is an INPUT element of type 'text' in the HTML document
if (this.textBox.Attributes.Contains("style") == false)
    this.textBox.Attributes.Add("style");
```

[VB.NET]
```vbnet
' textBox is an INPUT element of type 'text' in the HTML document
If Me.textBox.Attributes.Contains("style") = False Then
    Me.textBox.Attributes.Add("style")
End If
```

### Modifying Attribute Values

You can change the value of an element's attribute at run time by using the `Value` property of that particular attribute, as shown in the below code snippet.

#### Code Snippets

[C#]
```csharp
// textBox is an INPUT element of type 'text' in the HTML document
this.textBox.Attributes["style"].Value = "background-color:red";
```

[VB.NET]
```vbnet
' textBox is an INPUT element of type 'text' in the HTML document
Private Me.textBox.Attributes("style").Value = "background-color:red"
```

## 5.6 How To Change a Characteristic Of an HTML Element Before It Is Displayed?

The characteristic of an element can be easily changed in the `PreRenderDocument` event of the HTMLUI control.

The `PreRenderDocument` event is raised when the elements in the HTML document are created in the HTMLUI control, but their size and location are not calculated yet.

### Example

```html
<html>
<body bgcolor="#c4d6e9">
    <h1>Syncfusion</h1>
    <h4>.NET Essentials</h4>
    <p>
        <img id="image" src="files/oldImage.gif"/>
    </p>
    <p>
    </p>
</body>
</html>
```

## Footer

© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion-winforms, htmlui, attribute-modification, prerenderdocument-event, code-examples] keywords: [htmlui, prerenderdocument, attribute add, attribute value, syncfusion, winforms, .net, essentials, document, elements, characteristic, display] -->
```