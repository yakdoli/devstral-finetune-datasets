```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: HTMLUI
page_number: 072
page_id: HTMLUI#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:56Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- The `<a>` tag is used for creating links to other files or in creating bookmarks.
- The `<abbr>` tag is used to indicate the abbreviated forms of long and important texts.

## Content

### 4.6.1 A - Anchor Tag

The Anchor tag is used for creating links to other files or in creating bookmarks. This tag ends with `</A>`. It includes the following attributes.

- `href`: Specifies the URL of the page to which the link is to be made
- `rel`: Specifies the relationship between the current document and the target URL

The following example illustrates how the Anchor tag is rendered in HTMLUI.

```csharp
[C#]
string htmlCode="<html><head><title>A Tag support</title></head><body><A href=\"link.htm\">Link</A></body></html>";
this.htmluiControl.LoadFromString(htmlCode);
```

```vb
[VB.NET]
Private htmlCode As String = "<html><head><title>A Tag support</title></head><body><A href=\"link.htm\">Link</A></body></html>"
Me.HtmluiControl1.LoadFromString(htmlCode)
```

### 4.6.2 ABBR - Abbreviation Tag

The Abbreviation tag is used to indicate the abbreviated forms of long and important texts. The `title` attribute is used to display a tooltip text when the cursor is moved over the abbreviated text. The support for `<abbr>` tag is shown in the following code snippet.

```html
[HTML]
File Location and Name: C:\MyProjects\Anchor\abbr.html

<html>
    <body>
        <abbr title="United Nations">UN</abbr>
    </body>
</html>
```

```csharp
[C#]
this.htmluiControl.LoadHTML(@"C:\MyProjects\Anchor\abbr.html");
```

```vb
[VB.NET]
```

```


## API Reference (if applicable)
- None applicable in this section.

## Code Examples (multi-language supported)
- Examples are provided for both C# and VB.NET for both the `<a>` and `<abbr>` tags.

## Cross References
- None mentioned in this section.

### RAG Annotations
```html
<!-- tags: [HTMLUI, Windows Forms, Syncfusion Winforms, Anchor Tag, Abbreviation Tag] keywords: [href, rel, title attribute, tooltip, HTMLUI, Windows Forms, C#, VB.NET] -->
```
```html
<!-- Page-level Navigation/TOC: none applicable. -->
```