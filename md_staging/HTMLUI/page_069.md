```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_069.jpeg
document_name: HTMLUI
page_number: 069
page_id: HTMLUI#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:46Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

```csharp
Private htmlElements As Hashtable =
Me.HtmluiControl1.Document.GetElementsByUserIdHash()

Private link As StyleElementImpl = CType(IIf(TypeOf htmlElements("style") Is
StyleElementImpl, htmlElements("style"), Nothing), StyleElementImpl)

Private Me.label1.Text = Constants.vbLf & "Link(IsVisible):" &
link.IsVisible.ToString()
```

### Methods

- **GetCssStream**: Returns a stream of inner CSS data of the style element

## 4.5.29 TABLE Element

The **TABLE** element is used to create tables in a document. The table element contains the **TR**, **TD** elements within it. The **TABLEElementImpl** class is used to determine the properties and methods for the table element.

### Properties

- **ColsCount**: Gets / sets the number of columns present in the table
- **RowsCount**: Gets / sets the number of rows present in the table

#### [C#]

```csharp
// Gets the number of columns and rows present in the table.
Hashtable htmlElements =
this.htmluiControl1.Document.GetElementsByUserIdHash();
TABLEElementImpl table = htmlElements["table"] as TABLEElementImpl;
this.label1.Text = "\nTable(ColsCount and RowsCount):" +
table.ColsCount.ToString() + "," + table.RowsCount.ToString();
```

#### [VB.NET]

```vb
' Gets the number of columns and rows present in the table.
Private htmlElements As Hashtable =
Me.HtmluiControl1.Document.GetElementsByUserIdHash()
Private table As TABLEElementImpl = CType(IIf(TypeOf htmlElements("table") Is
TABLEElementImpl, htmlElements("table"), Nothing), TABLEElementImpl)
Private Me.label1.Text = Constants.vbLf & "Table(ColsCount and RowsCount):" &
table.ColsCount.ToString() + "," + table.RowsCount.ToString()
```

## 4.5.30 TD - Table cell Element

The **TD** element is used to create regular cells inside a table. The **TDElementImpl** class contains the properties and methods for the table element.

## Cross References

- See also: [List of table-related properties and methods for further details.]

<!-- tags: [product, version, HTMLUI, table, element, properties, methods] keywords: [TABLE element, ColCount, RowCount, TABLEElementImpl, TDElementImpl, HTMLUI, Windows Forms, document, table] -->
```