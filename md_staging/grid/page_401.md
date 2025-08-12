```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_401.jpeg
document_name: grid
page_number: 401
page_id: grid#page_401
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### [C#]

```csharp
GridWordConverter converter = new GridWordConverter();
converter.GridToWord("Grid.doc", this.gridControl1);
```

### [VB.NET]

```vb
Dim converter As GridWordConverter = New GridWordConverter()
converter.GridToWord("Grid.doc", Me.gridControl1)
```

#### Events

DrawHeader and DrawFooter are the events offered by the GridWordConverter that aids in adding as well as customizing the header and footer in the destination word document.

#### Sample Output

Below images depict the conversion of grid content to a word file.

![Figure 145: Grid to be Exported](attachment://export_grid.png)
*Figure 145: Grid to be Exported*

<!-- tags: [grid, windows forms, export, word document, header, footer, events] keywords: [grid control, essential grid, grid to word exporter] -->
```