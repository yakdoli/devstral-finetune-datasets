```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: HTMLUI
page_number: 093
page_id: HTMLUI#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:13Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
<td rowspan=2>Rowspan cell</td>
<td valign="bottom" height="80">V align cell</td>
</tr>
<tr>
    <td width="300">custom width cell</td>
</tr>
<tr>
    <td>Cell</td>
    <td>Cell</td>
</tr>
</table>
</body>
</html>
```

## Code: C#

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\table\td.html");
```

## Code: VB.NET

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\table\td.html")
```

## 4.6.30 TEXTAREA - Text Area Tag

The **Text Area** tag is used to define a multiline text box. The HTMLUI control supports the following attributes with the `<textarea>` tag for receiving inputs from the user effectively.

- **rows**: Specifies the number of rows for the text area
- **cols**: Specifies the number of columns for the text area

### [HTML]

**File Location and Name:** C:\MyProjects\textArea\textarea.html

```html
<html>
<body>
    <textarea rows="5" cols="20">
        Essential Studio features "Just-In-Time" source level debugging. Switch between debug and release versions with a single click.
    </textarea>
</body>
</html>
```

### [C#]

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\textArea\textarea.html");
```

---

## Page-level Navigation/TOC
- **4.6.30 TEXTAREA - Text Area Tag**
  - Attributes and Usage
  - Code Examples (HTML, C#, VB.NET)

## Cross References
- Refer to related sections on HTMLUI controls and attributes for further details.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```