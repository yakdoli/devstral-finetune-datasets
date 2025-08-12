```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: HTMLUI
page_number: 155
page_id: HTMLUI#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:20Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

```html
[HTML]

<!DOCTYPE html>
<html>
<body>
    <div id="div1">
        Have an issue you need to contact Syncfusion about? Use our state-of-the-art incident management system - Direct-Trac.
    </div>
</body>
</html>
```

```csharp
[C#]

Hashtable htmlElements = this.htmluiControl.Document.GetElementsByUserIdHash();
DIVELEMENTImpl div1 = this.htmlElements["div1"] as DIVELEMENTImpl;
MessageBox.Show(div1.InnerHTML.ToString());
```

```vbnet
[VB.NET]

Private htmlElements As Hashtable = Me.htmluiControl.Document.GetElementsByUserIdHash()
Private div1 As DIVELEMENTImpl = CType(IIf(TypeOf Me.htmlElements("div1") Is DIVELEMENTImpl, Me.htmlElements("div1"), Nothing), DIVELEMENTImpl)
MessageBox.Show(div1.InnerHTML.ToString())
```

### 5.4 How To Access the Name Of an HTML Element At Run-time?

The **element.Name** property gets the name of the tag that defines the element as an attribute, and not the name of the element defined by the user. You can access the name of the element with the help of the **element.Attributes** property.

The following HTML document illustrates how an input element with a name is declared and accessed in HTMLUI.

```html
[HTML]

<html>
<body>
    <p>
        <input type="text" id="txt1" name="textboxOne" size="20"/>
    </p>
</body>
</html>
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.HTMLUI
- **Class**: HTMLUIControl
  - **Method**: `GetElementsByUserIdHash()`
    - Returns a Hashtable containing all the HTML elements indexed by their ID.
- **Property**: `Document`
    - Type: HTMLDocument
    - Represents the document structure of the HTML control.

- **Property**: `InnerHTML`
    - Type: string
    - Gets or sets the HTML content of the element.

## Code Examples

### Input Element with Name

```html
<input type="text" id="txt1" name="textboxOne" size="20"/>
```

### Accessing Attributes in C#

```csharp
Hashtable htmlElements = htmluiControl.Document.GetElementsByUserIdHash();
DIVELEMENTImpl inputElement = htmlElements["txt1"] as DIVELEMENTImpl;
string inputName = inputElement.Attributes["name"]?.Value;
MessageBox.Show($"Element Name: {inputName}");
```

### Accessing Attributes in VB.NET

```vbnet
Private htmlElements As Hashtable = Me.htmluiControl.Document.GetElementsByUserIdHash()
Private inputElement As DIVELEMENTImpl = CType(IIf(TypeOf Me.htmlElements("txt1") Is DIVELEMENTImpl, Me.htmlElements("txt1"), Nothing), DIVELEMENTImpl)
Dim inputName As String = inputElement.Attributes("name").Value
MessageBox.Show($"Element Name: {inputName}")
```

<!-- tags: [Syncfusion Winforms, HTMLUI, element attributes, runtime access, HTML DOM] keywords: [element.Name, element.Attributes, HTMLUIControl, GetElementsByUserIdHash, InnerHTML, Attributes, input element, declarative ID, run-time access, VB.NET, C#] -->
```