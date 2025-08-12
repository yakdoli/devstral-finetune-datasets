```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: HTMLUI
page_number: 154
page_id: HTMLUI#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:16Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Declaring and accessing HTML elements within Windows Forms using `InputElementImpl`.
- Collection-based access to HTML elements using their `userId` as a key.
- Assigning and utilizing code variables for HTML elements in a project.
- Accessing and modifying the inner HTML text of HTML elements in the HTMLUI control.

## Content

### Code Examples

#### C#
```csharp
//declaring the code variable of the tag element
//InputElementImpl is responsible for the INPUT tag in HTMLUI
InputElementImpl text;

//Collection class accessing the HTML document with the userID as the key
Hashtable htmllements = 
this.htmluiControl.Document.GetElementsByUserIdHash();

//Code variable assigned to the html element with the help of the element's id 
//as //the key
this.text = htmllements["txt"] as InputElementImpl;

//usage of the code variable inside the project
this.text.UserControl.CustomControl.Text = "HTML Elements in HTMLUI";
```

#### VB.NET
```vb
' declaring the code variable of the tag element
' InputElementImpl is responsible for the INPUT tag in HTMLUI
Private text As InputElementImpl

' Collection class accessing the HTML document with the userID as the key
Private htmllements As Hashtable = 
Me.HtmluiControl.Document.GetElementsByUserIdHash()

' Code variable assigned to the html element with the help of the element's id 
' as 'the key
Me.Text = CType(IIf(TypeOf htmllements("txt") Is InputElementImpl, 
htmllements("txt"), Nothing), InputElementImpl)

' usage of the code variable inside the project
Me.Text.UserControl.CustomControl.Text = "HTML Elements in HTMLUI"
```

### 5.3 How To Access the Inner HTML Text Of the Current HTML Element In the HTMLUI Control?

You can access the inner HTML text of the current HTML element in the HTMLUI control by using the `InnerHTML` property of the HTMLUI control. This property also allows access to the child elements of the HTML elements.

The following HTML document contains a `div` element. The code snippet shows how the inner text of the element is accessed and displayed in the output at run time.

---

```markdown
© 2013 Syncfusion. All rights reserved. | Page 154
```

<!-- tags: [product, module, control, api, version?] keywords: [HTMLUI, Windows Forms, InputElementImpl, User ID, InnerHTML, Nested controls, Syncfusion, HTML elements] -->
```