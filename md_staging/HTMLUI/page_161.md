```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: HTMLUI
page_number: 161
page_id: HTMLUI#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:20Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```vb
Private htmluiControl1 = New Syncfusion.Windows.Forms.HTMLUI.HTMLUIControl()
Private htmluiControl.DefaultFormat.Font = New Font("Pristina", 16)
```

## Overview
- Demonstrates how to delete an HTML element from a document loaded into the HTMLUI Control at runtime.
- Utilizes the `Remove` method of the `IHTMLElementsCollection` interface.
- Explains the `Refresh` method to redraw the HTMLUI control with updated changes.

## Content

### 5.8 How To Delete an HTML Element From a Document Loaded Into the HTMLUI Control At Run-time?

The HTML elements loaded in the HTMLUI control are collected in the `IHTMLElementsCollection`. You can make use of the **Remove** method of the `IHTMLElementsCollection` interface to remove an element from the current collection, and the **Refresh** method to redraw the HTMLUI control with changes updated in the current document.

The following HTML document contains a textbox and a button element. The following code snippet shows how the textbox and the button are removed from the HTMLUI control's display at run time.

#### HTML Document

```html
[HTML]

<!DOCTYPE html>
<html>
    <body>
        <p>
            <input type="text" id="txt1"></input>
        </p>
        <p>
            <input type="button" id="btn1" value="Button1"></input>
        </p>
    </body>
</html>
```

#### C# Code Example

```csharp
[IHTMLelement txt1;
IHTMLelement btn1;
private System.Windows.Forms.Button button1;
button1.Click += new System.EventHandler(this.button1_Click);
htmluiControl.LoadFinished += new System.EventHandler(this.htmluiControl_LoadFinished);

private void htmluiControl_LoadFinished(object sender, System.EventArgs e)
{
    this.txt1 = this.htmluiControl.Document.GetElementByUserId("txt1");
    this.btn1 = this.htmluiControl.Document.GetElementByUserId("btn1");
}
```

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.HTMLUI
- **Class:** HTMLUIControl
- **Methods:** 
  - `Remove()`: Removes an element from the `IHTMLElementsCollection`.
  - `Refresh()`: Redraws the HTMLUI control to reflect updates.

## Code Examples

The provided C# code shows how to access and manipulate HTML elements using the `GetElementByUserId` method. This allows for targeting specific elements by their unique IDs and performing operations such as deletion at runtime.

## Page-level Navigation/TOC (if applicable)

- **5.8 How To Delete an HTML Element From a Document Loaded Into the HTMLUI Control At Run-time?**
  - Overview of the `IHTMLElementsCollection`
  - Example HTML document
  - C# implementation for removing elements

## Cross References

- Refer to documentation on manipulating HTML elements and handling event handlers for more detailed information.

<!-- tags: [HTMLUI, WinForms, VB.NET, C#, document manipulation, run-time changes, IHTMLElementsCollection, Refresh, Remove] keywords: [HTML document, textbox, button, textbox, element deletion, event handling, run-time updates] -->
```