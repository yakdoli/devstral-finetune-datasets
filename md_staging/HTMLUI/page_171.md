```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: HTMLUI
page_number: 171
page_id: HTMLUI#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:30Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
Dim oTemp3 As CustomControlBase = New CustomControlBase(dataGridElement1, 
                                                        Me.dataGrid1) 
End Sub 
```

## 5.13 How To Load HTML Into the HTMLUI Control?

You can make use of the `GetControlByElement()` method of the `InputHTML` Interface to get an object for the control present in an HTML element in the HTMLUI control. If the HTML element does not contain any control in it, it returns a null value, by default.

### HTML

```html
<html>
  <body>
    <input type="text" id="txt" />
  </body>
</html>
```

### C#

```csharp
//Initializing the respective control's object
private System.Windows.Forms.RadioButton htmlRadioButton;

private void htmluiControl1_LoadFinished(object sender, System.EventArgs e)
{
    //Collecting the html elements in a hashtable with their key as id
    Hashtable elements = this.htmluiControl1.Document.GetElementsByUserIdHash();
    BaseElement radioElem = (BaseElement)elements["radiol"];

    //Getting the Control from the html element and assigning it to the required object
    //The html element hereafter can be accessed with the help of the htmlRadioButton object
    htmlRadioButton = (RadioButton)
    this.htmluiControl1.Document.GetControlByElement(radioElem);
}
```

### VB.NET

```vb.net
'Initializing the respective control's object
Private htmlRadioButton As System.Windows.Forms.RadioButton

Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    'Collecting the html elements in a hashtable with their key as id
    Dim elements As Hashtable = Me.htmluiControl1.Document.GetElementsByUserIdHash()
    Dim radioElem As BaseElement = CTYPE(elements("radiol"), BaseElement)
End Sub
```

## API Reference

- `GetControlByElement()`: Method of the `InputHTML` Interface to retrieve an object for the control present in an HTML element.

## Code Examples

### C#

```csharp
private void htmluiControl1_LoadFinished(object sender, System.EventArgs e)
{
    Hashtable elements = this.htmluiControl1.Document.GetElementsByUserIdHash();
    BaseElement radioElem = (BaseElement)elements["radiol"];
    htmlRadioButton = (RadioButton)
    this.htmluiControl1.Document.GetControlByElement(radioElem);
}
```

### VB.NET

```vb.net
Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim elements As Hashtable = Me.htmluiControl1.Document.GetElementsByUserIdHash()
    Dim radioElem As BaseElement = CTYPE(elements("radiol"), BaseElement)
End Sub
```

<!-- tags: [WinForms, HTMLUI, Control, InputHTML, Interface] keywords: [HTMLUI, ControlByElement, InputHTML, GetElementsByUserIdHash, RadioButton, hashtable, object retrieval, Visual Basic.NET, C#] -->
```