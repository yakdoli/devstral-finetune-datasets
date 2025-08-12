```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: HTMLUI
page_number: 060
page_id: HTMLUI#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:11Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Properties

- **IsVisited**: Gets a bool value (either true/false) indicating whether the link is visited or not. This may be used in changing the color of the links visited.
- **HoverFormat**: Gets the format of the A element when the user hovers the mouse pointer over the link.
- **VisitedFormat**: Gets the format of the A element visited recently.

### [C#]

```csharp
// IsVisited property gets the Boolean value indicating whether the link is
// visited or not
// VisitedFormat property get the format of the A element visited recently.
Hashtable hmlelements = this.htmluiControl1.Document.GetElementsByUserIdHash();
AElementImpl a = hmlelements["a"] as AElementImpl;
this.label1.Text = "\nA(IsVisited and VisitedFormat):" +
this.a.IsVisited.ToString() + "," +
this.a.VisitedFormat.BackgroundColor.Name.ToString();
```

### [VB.NET]

```vb
' IsVisited property gets the Boolean value indicating whether the link is
' visited or not
' VisitedFormat property get the format of the A element visited recently.
Private hmlelements As Hashtable = Me.HtmluiControl1.Document.GetElementsByUserIdHash()

Private a As AElementImpl = CType(IIf(TypeOf hmlelements("a") Is AElementImpl, hmlelements("a"), Nothing), AElementImpl)

Private Me.label1.Text = Constants.vbLf & "A(IsVisited and VisitedFormat):" & Me.a.IsVisited.ToString() + "," + Me.a.VisitedFormat.BackgroundColor.Name.ToString()
```

## Methods

- **ResetVisited**: Excludes the element from the list containing the visited links.

### 4.5.3 B - Bold Element

The B element is responsible for formatting the specified text in bold style. The BElementImpl class contains the properties and methods of this element. The SUBElementImpl and SUPElementImpl classes are also responsible for bolding elements. They also contain the properties and methods for the element's behavior.

### 4.5.4 BODY Element

## Footer

© 2013 Syncfusion. All rights reserved.  
Page 60

<!-- tags: [Essential HTMLUI, Windows Forms, WinForms, properties, methods, hyperlink, styles, bold, BODY] keywords: [IsVisited, HoverFormat, VisitedFormat, ResetVisited, BElementImpl, SUBElementImpl, SUPElementImpl] -->
```