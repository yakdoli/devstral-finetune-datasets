```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_091.jpeg
document_name: HTMLUI
page_number: 091
page_id: HTMLUI#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:56Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
<html>
<head>
</head>
<body>
    Pythagoras theorem:<br />
    In a right angled triangle,<br />
    <code>
        hypotenuse<sup>2</sup> = opposite<sup>2</sup> + adjacent<sup>2</sup>
    </code>
</body>
</html>
```

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\sup\sup.html");
```

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\sup\sup.html")
```

## 4.6.28 TABLE - Table Tag

### Overview
- The `TABLE` tag defines a table in an HTML document.
- The table tag uses the `<tr>` tag to define a row and the `<td>` tag to define a cell element.
- The HTMLUI control supports the table with attributes that help in rendering and displaying complex HTML pages.

### Attributes
- **bgcolor**: Specifies the background color of the table.
- **border**: Specifies the thickness of the table border.

### Example

#### [HTML]
```html
File Location and Name: C:\MyProjects\table\table.html

<html>
<body>
    <table bgcolor="#dae5f5" border="1">
        <tr>
            <td>Sample</td><td>Sample</td>
        </tr>
    </table>
</body>
</html>
```

#### [C#]
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\table\table.html");
```

### Footer
© 2013 Syncfusion. All rights reserved.
```html
<!-- tags: [Syncfusion Winforms, HTMLUI, Table Tag, Attributes, Rendering, Display, C#, VB.NET] keywords: [HTML tables, HTMLUI control, bgcolor, border, rendering complex HTML pages, Syncfusion Winforms, HTMLPageLoad, Table attributes] -->
``` 
```