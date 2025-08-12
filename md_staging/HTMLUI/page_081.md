```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_081.jpeg
document_name: HTMLUI
page_number: 081
page_id: HTMLUI#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:33Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

| Button | Button |
| --- | --- |
| CheckBox | Check Box |
| Radio | Radio Button |
| Password | Password Box |
| Reset | Reset Button |
| Submit | Submit Button |

### Input Controls Attributes

- **value**: Specifies the default text that will appear on the control after being rendered on the document.
- **size**: Specifies the size of the input document.
- **name**: Specifies a unique name to the control. In HTMLUI, the `Control.Name` property will access the name given to the control in code and not the value of this name attribute. The user has to access this value with the help of the `Control.Attributes["name"].Value` property. This will return the value of this attribute.
- **maxlength**: Specifies the maximum number of characters that can be displayed inside the text fields.
- **disabled**: Disables the control. Any change that the user makes in the control will not be updated in the control.
- **checked**: Displays the checkbox or the radio button selected by default in the document.

### HTML Code Example

```html
[HTML]

File Location and Name: C:\MyProjects\input\input.html

<html>
  <body>
    <input type="text" value="textbox" size="20" maxlength="5" /><br/>
    <input type="button" value="button element" /><br/>
    <input type="checkbox" value="checkbox" checked /><br/>
    <input type="password" value="password" size="20" /><br/>
    <input type="radio" value="radio" /><br/>
    <input type="reset" value="reset" /><br/>
    <input type="submit" value="submit" size="50" /><br/>
  </body>
</html>
```

### C# Code Example

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\input\input.html");
```

### VB.NET Code Example

```vb
[VB.NET]
```

---

<!-- tags: [Syncfusion, WinForms, HTMLUI, input controls, attributes] keywords: [Button, CheckBox, Radio, Password, Reset, Submit, value, size, name, maxlength, disabled, checked, file location, HTML, C#, VB.NET] -->
```