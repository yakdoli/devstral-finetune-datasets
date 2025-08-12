```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_176.jpeg
document_name: HTMLUI
page_number: 176
page_id: HTMLUI#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:42Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
// Loads styles from the specified CSS document from a System.IO.Stream and refresh the current
// document using the styles
this.htmluiControl.LoadCSS(@"C:\MyProjects\LoadCSS\style.css");
```

```vb
' Loads styles from the specified CSS document from a System.IO.Stream and refresh the current
' document using the styles
Me.HtmluiControl.LoadCSS("C:\MyProjects\LoadCSS\style.css")
```

## 5.16 How To Toggle the Visibility Of an HTML Element In the HTMLUI control At Run-time?

Each HTML element in the HTMLUI has an `xVisible` attribute by default that helps the user to toggle the visibility of a particular element. Since the `xVisible` is a bool property, the value to be set is either `True` or `False`, as string.

The following code snippet shows how the visibility of an element is toggled on the execution of an event.

```html
[HTML]
<html>
    <body>
        <table>
            <tr>
                <td id="tdpopup">Cell Toggle</td>
                <td id="tdpopup">Cell Toggle</td>
            </tr>
            <tr>
                <td colspan="2">
                    <img src="sync.gif" id="img"/>
                </td>
            </tr>
        </table>
    </body>
</html>
```

---

<!-- tags: [Syncfusion Winforms, HTMLUI, Visibility] keywords: [HTMLUI, xVisible, toggle visibility, runtime, visibility control] -->
```