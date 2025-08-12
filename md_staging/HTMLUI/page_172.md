```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: HTMLUI
page_number: 172
page_id: HTMLUI#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:31Z
fidelity: lossless
-->

## Overview

- Explanation of how to access HTML elements using the `htmlRadioButton` object.
- Steps to load an HTML document as a startup document, either through the Properties window or by coding.

---

### Essential HTMLUI for Windows Forms

```vb
' Getting the Control from the html element and assigning it to the required object
' The html element hereafter can be accessed with the help of the htmlRadioButton object
htmlRadioButton = CType(Me.htmluiControl.Document.GetControlByElement(radioElem), RadioButton)
End Sub
```

---

### 5.13.1 Loading As Startup Document

An HTML document can be loaded at startup by two ways:

- Using the Properties window
- By coding

**Using the Properties window:**
Involves specifying the location of the startup HTML file by using the `StartupDocument` property of the HTMLUI control. The link shown at the bottom of the Properties window can also be used for the same purpose.

![Figure 57: HTMLUI control Property Grid](https://example.com/image-url)

**While using code for the Startup Document:**
It should be written in the `Form_Load` event that occurs before the form is displayed for the first time.

---

<!-- tags: [Winforms, HTMLUI, StartupDocument, Properties window, Programming, Syncfusion, Version: 11.4.0.26] keywords: [HTMLUI, StartupDocument, Properties window, Form_Load, document loading, HTML document, Syncfusion Winforms, programming guide] -->
```