```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: HTMLUI
page_number: 156
page_id: HTMLUI#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:19Z
fidelity: lossless
-->


# Essential HTMLUI for Windows Forms

```html
</p>
</body>
</html>
```

## Accessing Elements and Attributes

### C#

```csharp
INPUTElementImpl textBox1;
Hashtable htmlElements = this.htmluiControl1.Document.GetElementsByUserIdHash();

// accessing the input element
textBox1 = htmlElements["txt1"] as INPUTElementImpl;

// accessing the tag name of the element
Console.WriteLine("Tag Name of TextBox1:\n" + textBox1.Name.ToString());

// accessing the attribute name of the element
Console.WriteLine("Name given for TextBox1:\n" + textBox1.Attributes["name"].Value);
```

### VB.NET

```vb
Private textBox1 As INPUTElementImpl
Private htmlElements As Hashtable = Me.htmluiControl1.Document.GetElementsByUserIdHash()

' accessing the input element
Private textBox1 = CType(IIf(TypeOf htmlElements("txt1") Is INPUTElementImpl, htmlElements("txt1"), Nothing), INPUTElementImpl)

' accessing the tag name of the element
Console.WriteLine("Tag Name of TextBox1:" & Constants.vbLf & textBox1.Name.ToString())

' accessing the attribute name of the element
Console.WriteLine("Name given for TextBox1:" & Constants.vbLf & textBox1.Attributes("name").Value)
```

## 5.5 How To Add an Attribute To an HTML Element And Change Its Value At Run-time?

You can add an attribute to an HTML element using the `Add` method of the `Attributes` property, as shown in the following code snippet.

```md
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [product, module, control, api, version?] keywords: [HTMLUI, Windows Forms, Syncfusion Winforms, attributes, runtime, HTML elements, C#, VB.NET] -->
```