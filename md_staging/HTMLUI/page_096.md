```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: HTMLUI
page_number: 096
page_id: HTMLUI#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:37Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

### 4.6.33 TR - Table Row Tag

The **Table Row** tag is used to define a row in a table. The row contains the cells (td elements) as its children in a table. HTMLUI supports the `align` attribute that aligns the contents of the row to the specified horizontal alignment.

#### Code Example

```html
[HTML]

File Location and Name:  C:\MyProjects\table\tr.html

<html>
    <body>
        <table border="1">
            <tr align="center">
                <td>Syncfusion</td>
                <td>Essential Studio</td>
            </tr>
        </table>
    </body>
</html>
```

```csharp
[C#]

this.htmluiControl.LoadHTML(@"C:\MyProjects\table\tr.html");
```

```vb
[VB.NET]

Me.htmluiControl.LoadHTML(@"C:\MyProjects\table\tr.html")
```

### 4.6.34 UL - UnOrdered List Tag

The **UnOrdered List** tag defines the start of a bulleted list. HTMLUI supports the bullets of the following shapes: **Circle**, **Square**, and **Disc**. The unordered list contains the `<li>` items as its child elements. Each `<li>` element defines a list item. The `type` attribute is used to choose the required bulleting style.

#### Code Example

```html
[HTML]

File Location and Name:  C:\MyProjects\listItem\ul.html

<html>
    <body>
        <ul type="disc">
            <li>Essential Tools</li>
            <li>Essential Chart</li>
        </ul>
    </body>
</html>
```

## Page-level Navigation/TOC (if applicable)
- **4.6.33 TR - Table Row Tag**
- **4.6.34 UL - UnOrdered List Tag**

## Cross References
See also: [TR Tag - Table Row Tag](#TR_Tag_-_Table_Row_Tag)

## RAG Annotations
<!-- tags: [syncfusion, winforms, htmlui, table, unordered list] keywords: [tr, table row, ul, unordered list, bulleting style, type attribute] -->
```