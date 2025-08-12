```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_080.jpeg
document_name: HTMLUI
page_number: 080
page_id: HTMLUI#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:24Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
Me.htmluiControl.LoadHTML(@"C:\MyProjects\HTML\htmlElement.html")
```

## 4.6.14 IMG - Image Tag

The **IMG** tag is used to display an image in the HTMLUI control. The HTMLUI control supports the following attributes for the image element, which can be used in developing advanced HTMLUI applications.

- **src**: Source attribute is used to access the location of the image file. The image may be located in the local folder or in the URI.
- **alt**: Alternate Text tag provides a tooltip text when the mouse is moved over the image. In case the image is not rendered in the control, this text is displayed in place of the image.

### Example Code

**[HTML]**

File Location and Name: C:\MyProjects\img\imageElement.html

```html
<html>
<body>
    <img src="htmlui.jpg" alt="Syncfusion Essential HTMLUI" />
</body>
</html>
```

**[C#]**

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\img\imageElement.html");
```

**[VB.NET]**

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\img\imageElement.html")
```

## 4.6.15 INPUT - Input Tag

The **Input** tag is used to receive some inputs from the user. The input tag uses the following attributes to provide a value for the specified input elements from the user.

- **type**: Specifies the type of input control to be placed in the document. HTMLUI control supports the following input elements:

| Attribute Value | Control that will be Displayed |
|------------------|-----------------------------|
| Text            | Text Box                    |

### Summary

The HTMLUI control provides flexibility through its versatile attributes, allowing for the inclusion of images and user input mechanisms. The example code snippets demonstrate how to load HTML documents containing image and input elements into an HTMLUI control in both C# and VB.NET.

## API Reference

### Supported Input Element Types

- **Text**: Displays a text box for user input.

## Code Examples

### Loading HTML with Image and Input Elements

#### C#

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\inputElement.html");
```

#### VB.NET

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\inputElement.html")
```

## See also

- [Essential HTMLUI Documentation](#)
- [Input Tag Reference](#)
- [Image Tag Reference](#)

<!-- tags: Syncfusion WinForms, HTMLUI, IMG, INPUT, Image Tag, Input Tag keywords: HTMLUI, IMG, Input, Attributes, User Input, Control -->
```