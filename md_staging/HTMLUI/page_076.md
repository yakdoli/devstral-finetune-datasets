```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: HTMLUI
page_number: 076
page_id: HTMLUI#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:11Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

### DIV - Division Tag

**Overview**

- The `DIV` tag is used to define a division or a section in the document that is rendered in the HTMLUI control.
- The `align` attribute of the `div` tag is used to align the text displayed inside the `div` tag.
- The `align` attribute uses the following values to specify the position of the text display:

  - left
  - right
  - center
  - justify

```html
<html>
  <body>
    <div align="left">Essential Studio</div>
    <div align="right">Tools</div>
    <div align="center">Grid</div>
    <div align="justify">HTMLUI</div>
  </body>
</html>
```

#### Code Example

[C#]
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\divide\div.html");
```

[VB.NET]
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\divide\div.html")
```

### FORM - Form Tag

**Overview**

- The `FORM` tag is used to create a form-based dialog for the users to give their inputs.
- The form elements may be a text box, button, radio button, check box, and so on, based on the necessity of the user.

#### Code Example

```html
[HTML]
```

## API Reference

None.

## Code Examples

See the code examples above for VB.NET, C#, and HTML samples.

## Page-level Navigation/TOC

- 4.6.8 Division Tag
- 4.6.9 Form Tag

## Cross References

None.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Essential HTMLUI, DIV, Form, Tag, align, attribute, align attribute values, text display, VB.NET, C#, HTML] keywords: [div tag, alignment, essential studio, tools, grid, htmlui, form tag, form-based dialog, user inputs, text box, button, radio button, check box] -->
```