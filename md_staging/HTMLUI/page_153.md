```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: HTMLUI
page_number: 153
page_id: HTMLUI#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:54Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```vb
If elem.Attributes("src").Value = "sync.jpg" Then
    elem.Attributes("src").Value = "syncfusion.gif"
Else
    elem.Attributes("src").Value = "sync.jpg"
End If
Me.HtmluiControl1.ScrollToElement(elem)
End If
End Sub
```

## 5.2 How To Access the HTML Elements Loaded Into the Control?

The HTML elements are accessed in HTMLUI for developing advanced UIs. The HTML elements are collected in a collection class. When the **Hashtable** is used as a collection class, it stores the HTML elements with a key, specific for each element.

These elements are then assigned to the code variables. The **Code Variables** are the objects of the classes that are responsible for the functionality of the tag elements. These classes contain the definitions for the properties, methods, and events for the tag elements. These variables will be used in accessing the HTML elements inside the code.

The following HTML document shows an input tag textbox element with an id as the key for accessing it in the Hashtable.

```html
<html>
<body>
    <input type="text" id="txt" />
</body>
</html>
```

The following code snippet illustrates accessing the HTML elements from the above document.

```html
<!-- tags: [product, module, control, api, version?] keywords: [HTMLUI, Windows Forms, HTML elements, access, Hashtable, Code Variables, input tag, textbox, id, Accessing HTML, Syncfusion Winforms] -->
```
```