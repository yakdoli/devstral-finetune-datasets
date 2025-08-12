```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: HTMLUI
page_number: 094
page_id: HTMLUI#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:43Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```vb
[VB.NET]
Me.htmluiControl.LoadHTML(@"C:\MyProjects\textArea\textarea.html")
```

## 4.6.31 TH - Table Header Tag

The Table Header tag is used to define header cells for the cells in a table. The `<th>` tag renders the text content in the particular cell in a bold face. The `<th>` tag supports the following attributes:

- **align**: Specifies the alignment of the text inside the table cell
- **bgcolor**: Specifies a background color for the specified cell
- **colspan**: Spans the cell to the specified number of columns. This is used in merging the columns in the table.
- **height**: Specifies custom height for the cells
- **nowrap**: Extends the text inside a particular cell into a single line. This display extends the width of the cell according to the contents inside it.
- **rowspan**: Extends the height of the cell to the specified number of rows. This is helpful in custom merging the rows of the given cell.
- **valign**: Determines the vertical alignment of the text inside the table cell
- **width**: Specifies user-defined width for the specified cells

```html
[HTML]
File Location and Name: C:\MyProjects\table\th.html

<html>
<body>
    <table border="1">
        <tr>
            <th colspan="2">Essential Studio</th>
        </tr>
        <tr>
            <td>Essential</td>
            <td>Tools</td>
        </tr>
        <tr>
            <td>Essential</td>
            <td>Grid</td>
        </tr>
        <tr>
            <td>Essential</td>
            <td>Chart</td>
        </tr>
        <tr>
            <td>Essential</td>
            <td>HTMLUI</td>
        </tr>
    </table>
</body>
</html>
```

<!-- tags: [syncfusion, htmlui, table header tag, essential studio, table attributes] keywords: [th, table header, colspan, rowspan, height, width, align, valign, bgcolor, nowrap, essential studio, htmlui components] -->
```