```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: HTMLUI
page_number: 041
page_id: HTMLUI#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:03Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
Private uri As Uri = New Uri("http://www.syncfusion.com")
HtmluiControl1.LoadHTML(uri)
```

A new URI has to be declared in the code with the path from which the URI has to be loaded, as shown in the above example. The `URI` class provides an object representation of a URI and also provides easy access to the parts of the URI.

## 4.1.2.4 Loading HTML Which Is in the Form of Text

The HTML code sometimes can be directly written and stored as a string. The HTML code available in the form of string is loaded into the HTMLUI Control by using the `LoadFromString` method and the HTML contents will be displayed in the HTMLUI control.

### C#

```csharp
// Load HTML Document from String.
string htmlCode = "<HTML>
<HEAD>
<TITLE>HI</TITLE>
</HEAD>
<BODY bgcolor='#ffffff'>
<INPUT type='button' id='btn'/></INPUT>
</BODY>
</HTML>";
this.htmluiControl1.LoadFromString(htmlCode);
```

### VB.NET

```vb
' Load HTML Document from String.
Private htmlCode As String = "<HTML>
<HEAD>
<TITLE>HI</TITLE>
</HEAD>
<BODY bgcolor='#ffffff'>
<INPUT type='button' id='btn'/></INPUT>
</BODY>
</HTML>"
Me.HtmluiControl1.LoadFromString(htmlCode)
```

## 4.1.2.5 Load the File from Resource

The HTML file can be loaded as an Embedded Resource in the HTMLUI control. The procedure to be followed for making an HTML file as an embedded resource is discussed below.

1. Open the **Solution Explorer** from the **View** menu of the Menu Bar.

<!-- tags: [Syncfusion Winforms, HTMLUI, URI, LoadFromString, Embedded Resource] keywords: [HTMLUI Control, URI Representation, Load HTML from String, Embedded Resource, Solution Explorer, Menu Bar] -->
```