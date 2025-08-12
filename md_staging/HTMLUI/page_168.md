```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_168.jpeg
document_name: HTMLUI
page_number: 168
page_id: HTMLUI#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:12Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates the process of loading custom controls as part of the HTML layout in Syncfusion Winforms.
- Explains how to integrate custom controls into the HTMLUI framework using C# and VB.NET.

## Content

### `htmluiControl1_LoadFinished` Event Implementation

#### C#

```csharp
// Initializing the respective control's object
private System.Windows.Forms.RadioButton htmlRadioButton;

private void htmluiControl1_LoadFinished(object sender, System.EventArgs e)
{
    // Collecting the html elements in a hashtable with their key as id
    Hashtable elements = this.htmluiControl1.Document.GetElementsByUserIdHash();
    BaseElement radioElem = (BaseElement)elements["radiol"];

    // Getting the Control from the html element and assigning it to the required object
    // The html element hereafter can be accessed with the help of the htmlRadioButton object
    htmlRadioButton = (RadioButton)
        this.htmluiControl1.Document.GetControlByElement(radioElem);
}
```

#### VB.NET

```vb.net
' Initializing the respective control's object
Private htmlRadioButton As System.Windows.Forms.RadioButton

Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Collecting the html elements in a hashtable with their key as id
    Dim elements As Hashtable = Me.htmluiControl1.Document.GetElementsByUserIdHash()
    Dim radioElem As BaseElement = CType(elements("radiol"), BaseElement)

    ' Getting the Control from the html element and assigning it to the required object
    ' The html element hereafter can be accessed with the help of the htmlRadioButton object
    htmlRadioButton = CType(Me.htmluiControl1.Document.GetControlByElement(radioElem), RadioButton)
End Sub
```

### 5.12 How To Load Custom Controls As Part Of the HTML Layout?

An HTML document containing custom controls is shown below.

#### HTML

```html
<HTML>
```

## API Reference

### Methods
- `GetElementsByUserIdHash()`
  - **Description:** Collects HTML elements and stores them in a hashtable with their keys as IDs.
  - **Returns:** `Hashtable` containing HTML elements.

- `GetControlByElement(BaseElement element)`
  - **Description:** Retrieves a Control object from a specified HTML element.
  - **Parameters:**
    - `element`: The `BaseElement` representing the HTML element.
  - **Returns:** The corresponding `Control` object.

## Code Examples

### Example: Loading a Custom RadioButton
```csharp
// C# Example
private void htmluiControl1_LoadFinished(object sender, EventArgs e)
{
    Hashtable elements = this.htmluiControl1.Document.GetElementsByUserIdHash();
    BaseElement radioElem = (BaseElement)elements["radiol"];
    htmlRadioButton = (RadioButton)this.htmluiControl1.Document.GetControlByElement(radioElem);
}
```

### Example: Loading a Custom RadioButton in VB.NET
```vb.net
' VB.NET Example
Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As EventArgs)
    Dim elements As Hashtable = Me.htmluiControl1.Document.GetElementsByUserIdHash()
    Dim radioElem As BaseElement = CType(elements("radiol"), BaseElement)
    htmlRadioButton = CType(Me.htmluiControl1.Document.GetControlByElement(radioElem), RadioButton)
End Sub
```

## Tags and Keywords
<!-- tags: [Syncfusion, Winforms, HTMLUI, custom controls, HTML layout, event handling] keywords: [htmlRadioButton, GetElementsByUserIdHash, GetControlByElement, C#, VB.NET, document object model] -->
```