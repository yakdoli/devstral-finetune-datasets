```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: HTMLUI
page_number: 086
page_id: HTMLUI#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:17Z
fidelity: lossless
-->

## HTMLUI for Windows Forms

### Code Example

```html
</pre>
</body>
</html>
```

### Loading HTML Content

#### C#

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\paragraph\p.html");
```

#### VB.NET

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\paragraph\p.html")
```

## 4.6.22 SCRIPT - Script Tag

### Overview
- The `Script` tag allows inclusion of executable user-defined code snippets within the HTML document.
- It enhances the document's self-contained nature and reduces dependency on external means for executing actions.
- HTMLUI supports C#, Visual Basic, and Jscript. The `language` attribute specifies the selected scripting language.

### HTML Example

#### File Details
- **Location**: `C:\MyProjects\scripting\scripting.html`

```html
<html>
<head>
    <title>Scripting</title>
</head>
<body>
    <p><input type="button" id="btn"></p>
    <p><img id="img" src=""></p>
    <script language="C#">
        
        using System;
        using System.Windows.Forms;
        using System.Collections;
        using Syncfusion.Windows.Forms.HTMLUI;

        namespace Syncfusion
        {
            public class Script
            {
                IHTMLElement button = null;
                IHTMLElement img = null;
                Hashtable htmlElements = new Hashtable();
                /* Initializes script. */
                public static Script OnScriptStart()
                {
```

## Page-Level Navigation/TOC
- This section provides detailed guidance on utilizing the `Script` tag within HTML documents for embedding executable code snippets in Windows Forms applications. It highlights the use of `language` attributes and supported scripting languages for enhanced functionality.

## Cross References
- Refer to previous sections for information on loading and displaying HTML content in HTMLUI controls.

## RAG Annotations
<!-- tags: [HTMLUI, Windows Forms, Scripting, C#, VB.NET, Jscript, Script Tag] keywords: [executable code snippets, self-contained HTML documents, scripting languages, HTMLUI controls, Syncfusion] -->
```