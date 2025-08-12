```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_070.jpeg
document_name: HTMLUI
page_number: 070
page_id: HTMLUI#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:14Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## 4.5.31 TEXTAREA Element

The `TEXTAREA` element is used to define a multiline textbox, allowing the user to enter an unlimited number of characters. The `TEXTAREAELEMENTIMPL` class is invoked to define the properties and methods of the element.

### Properties

- **UserControl**: Gets / sets the user control instance for the particular input element declared by the user

#### Code Example (C#)
```csharp
[C#]

// UserControl property gets the user control instance for the particular input
// element declared by the user.
Hashtable htmlElements = 
this.htmlUiControl.Document.GetElementsByIdHash();
TEXTAREAELEMENTIMPL txt = htmlElements["txt"] as TEXTAREAELEMENTIMPL;
this.txt.UserControl.CustomControl.Text = "This is a multiline textBox";
```

#### Code Example (VB.NET)
```vb
[VB.NET]

' UserControl property gets the user control instance for the particular input
' element declared by the user.
Private htmlElements As Hashtable = 
Me.HtmlUiControl.Document.GetElementsByIdHash()
Private txt As TEXTAREAELEMENTIMPL = CType(IIf(TypeOf htmlElements("txt") Is 
TEXTAREAELEMENTIMPL, htmlElements("txt"), Nothing), TEXTAREAELEMENTIMPL)
Private Me.txt.UserControl.CustomControl.Text = "This is a multiline textBox"
```

## 4.5.32 TH - Table Head Element

The `TH` element is used to create header cells inside a table. The `THELEMENTIMPL` class contains the properties and methods for the table header element. The text inside this element is formatted in bold by default.

## 4.5.33 TR - Table Row Element

The `TR` element is used to create rows inside a table. The `TRLEMENTIMPL` class contains the properties and methods for the table cell coding.

### Properties

## Footer Details
© 2013 Syncfusion. All rights reserved.
```