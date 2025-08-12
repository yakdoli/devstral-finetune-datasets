```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: HTMLUI
page_number: 092
page_id: HTMLUI#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:07Z
fidelity: lossless
-->


# Essential HTMLUI for Windows Forms

- [VB.NET]

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\table\table.html")
```

## 4.6.29 TD - Table Cell Tag

The Table Cell tag defines a cell inside a table. The `<td>` tag has a parent `<tr>` tag to define the row and a `<table>` tag to define the table in which it is present. The `td` tag in HTMLUI supports the following attributes that help the user in designing custom structures for their documents easily.

- **align**: Specifies the alignment of the text inside the table cell
- **bgcolor**: Specifies a background color for the specified cell
- **colspan**: Spans the cell to the specified number of columns. This is used in merging the columns in the table.
- **height**: Specifies custom height for the cells
- **nowrap**: Extends the text inside a particular cell into a single line. This display extends the width of the cell according to the contents inside it.
- **rowspan**: Extends the height of the cell to the specified number of rows. This is helpful in custom merging the rows of the given cell
- **valign**: Determines the vertical alignment of the text inside the table cell
- **width**: Specifies user-defined width for the specified cells

- **[HTML]**

### File Location and Name:
C:\MyProjects\table\td.html

```html
<html>
<body>
    <table border="1">
        <tr>
            <td>Sample</td>
            <td align="center">Text Aligned Cell</td>
        </tr>
        <tr>
            <td bgcolor="Blue">bgcolor cell</td>
            <td>Cell</td>
        </tr>
        <tr>
            <td colspan="2">Colspan cell</td>
        </tr>
        <tr>
            <td height="50">Custom height cell</td>
            <td nowrap>nowrap cell</td>
        </tr>
    </table>
</body>
</html>
```

## API Reference (if applicable)

- **Namespace**: HTMLUI
- **Class**: Table Cell Tag
- **Members**:
  - **align**: Specifies the alignment of the text inside the table cell
  - **bgcolor**: Specifies a background color for the specified cell
  - **colspan**: Spans the cell to the specified number of columns.
  - **height**: Specifies custom height for the cells
  - **nowrap**: Extends the text inside a particular cell into a single line.
  - **rowspan**: Extends the height of the cell to the specified number of rows.
  - **valign**: Determines the vertical alignment of the text inside the table cell
  - **width**: Specifies user-defined width for the specified cells

### Parameters

| Name     | Type     | Description                                                                                                                                                                                 | Default | Required |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------|
| align    | string   | Specifies the horizontal alignment of the content within the cell (left, center, right).                                                                                                     | left    | No       |
| bgcolor  | string   | Specifies the background color of the cell in CSS color format (hex, RGB, etc.)                                                                                                             | None    | No       |
| colspan  | integer  | Defines the number of columns the cell should span.                                                                                                                                          | 1       | No       |
| height   | integer  | Sets the height of the cell in pixels.                                                                                                                                                      | None    | No       |
| nowrap   | bool     | Indicates whether the content of the cell should be displayed on a single line, extending the cell width.                                                                                 | False   | No       |
| rowspan  | integer  | Defines the number of rows the cell should span.                                                                                                                                            | 1       | No       |
| valign   | string   | Specifies the vertical alignment of the content within the cell (top, middle, bottom).                                                                                                      | top     | No       |
| width    | integer  | Sets the width of the cell in pixels.                                                                                                                                                       | None    | No       |

### Returns
- Type: void
- Description: Updates the table cell with the specified attributes.

### Exceptions
- No exceptions are typically thrown for this specific operation. However, invalid values or formats for specific attributes may lead to rendering errors or warnings in the HTML document.

## Code Examples (multi-language supported)

### VB.NET Example

```vb
' Loading HTML content with a table
Me.htmluiControl.LoadHTML(@"C:\MyProjects\table\td.html")
```

### HTML Example

```html
<table border="1">
    <tr>
        <td>Sample</td>
        <td align="center">Text Aligned Cell</td>
    </tr>
    <tr>
        <td bgcolor="Blue">bgcolor cell</td>
        <td>Cell</td>
    </tr>
    <tr>
        <td colspan="2">Colspan cell</td>
    </tr>
    <tr>
        <td height="50">Custom height cell</td>
        <td nowrap>nowrap cell</td>
    </tr>
</table>
```

## Cross References

See also:
- 4.6.29 TD - Table Cell Tag
- HTMLUI Table Structures

<!-- tags: [HTMLUI, Table Cell, TD, attributes, alignment, rowspan, colspan, height, width, background color] keywords: [table Rendering, HTML structures, cell property ] -->
```