```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: grid
page_number: 227
page_id: grid#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:06Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Integer Text Box Usage

RegisterCellModel.GridCellType(`Me.gridControl1`, `CustomCellTypes.IntegerTextBox`)

```csharp
Me.gridControl1(4, 2).CellType = CustomCellTypes.IntegerTextBox.ToString()
```

#### Figure 121: Integer Text Box

![Integer Text Box](https://example.com/image.png)

### 4.1.4.4.16 Double Text Box

**Double text box** is used to display double data-type values in the grid cells. This cell type can be added to the grid cells by registering its cell model using the **RegisterCellModel** class.

The following code example illustrates how to add the double text box to grid cells using the **RegisterCellModel** class.

```csharp
RegisterCellModel.GridCellType(this.gridControl, CustomCellTypes.DoubleTextBox);
this.gridControl[4, 2].CellType = CustomCellTypes.DoubleTextBox.ToString();
```

## Page-level Navigation/TOC

- **4.1.4.4.16 Double Text Box**

## Cross References

- **RegisterCellModel**
- **CustomCellTypes**
- **DoubleTextBox**

## RAG Annotations

<!-- tags: [Grid, Windows Forms, Custom Cell Types] keywords: [IntegerTextBox, DoubleTextBox, RegisterCellModel, CustomCellTypes, CellModel] -->
```