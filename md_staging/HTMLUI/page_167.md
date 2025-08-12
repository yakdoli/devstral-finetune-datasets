```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: HTMLUI
page_number: 167
page_id: HTMLUI#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:16Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- HTMLUI provides a powerful control for creating interactive and rich interfaces with minimal coding.
- Enabling user interaction with HTML elements is demonstrated through code samples.
- Instructions on retrieving control objects from HTML elements in the HTMLUI control are detailed.

## Content

### Section: HTMLUI Element Interactivity

#### Figure 56: Enabling User Interaction with the HTML Elements in the HTMLUI Control

```csharp
this.liteHtml.Cursor = System.Windows.Forms.Cursors.WaitCursor;
this.liteHtml.Location = new System.Drawing.Point(8, 8);
this.liteHtml.Name = "liteHtml";
this.liteHtml.Size = new System.Drawing.Size(640, 224);
this.liteHtml.StartupDocument = @"D:\work\syncfusion\suitevss\Products\Devel";
```

#### 5.11 How To Get an Object For the Control Present In an HTML Element In the HTMLUI Control?
You can make use of the `GetControlByElement()` method of the `InputHTML` interface to get an object for the control present in an HTML element in the HTMLUI control. If the HTML element does not contain any control in it, it returns a null value, by default.

```html
[HTML]
<html>
  <body>
    <input type="text" id="txt" />
  </body>
</html>
```

## API Reference
- **InputHTML Interface**
  - `GetControlByElement()`: Retrieves the control object present in an HTML element.

## Code Examples
- Example of using `GetControlByElement()` to retrieve a control from an HTML element.

### WinForms-specific conventions
- Using the HTMLUI control in Windows Forms applications to create dynamic and interactive forms.

### Cross References
- Refer to the documentation on HTMLUI’s features and usage for more detailed information.

<!-- tags: [HTMLUI, control, Windows Forms, Syncfusion, programming, interface, inputHTML] keywords: [GetControlByElement, HTML elements, user interaction, interface methods, control objects, HTMLUI] -->
```