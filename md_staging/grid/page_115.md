<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: grid
page_number: 115
page_id: grid#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:33:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Conversion of GridControl to Excel is detailed, covering cell-by-cell conversion.
- Focus on the GridCellToExcel() method of the GridExcelConverterControl class for handling cell styles, formats, and background colors.
- Explains the handling of Currency and Number cell types during conversion.

## GridControl to Excel Conversion Process

### Conversion Mechanism
The conversion of Grid to Excel is done cell by cell. Each cell is converted with respect to its style, including its format and background color. This is done by using the **GridCellToExcel()** method of the **GridExcelConverterControl** class.

#### Currency Cell Conversion

##### If format specified
The cell is checked whether it is a Currency cell type by using the CellType property. If it is a Currency Cell type then the CellValue will be converted into Double and saved in Range's Number property. NumberFormatInformation is extracted from the NumberFormatInfoObject and the number is converted to string by using the extracted format. FormatString is created and saved in Range's NumberFormat property.

The following is a sample code to set the format of the Currency cell:

```csharp
[C#]
this.gridControl1[row,col].Format = "C";
```

```vb
[VB]
Me.gridControl1(row,col).Format = "C"
```

##### If format not specified
The cell is checked whether it is a Currency cell type by using the CellType property. If the CellType is not given then it switches to the default CellType and the CellValue is stored in Range's “Value2” property, where the value2 is converted into the given CellValueType(Except Date Time and Currency). Hence, in this case the CellValue will be converted to General format.

#### Number Cell Conversion

##### If format specified
The cell is checked whether it is a Number cell type by using the CellType property. If it is a Number Cell type then the cell value is assigned to Range's Value2 property. Since the format is specified, the Value2's value is converted to its respective type and set to Number format.

The following is a sample code to set the format of Currency cell:

```csharp
[C#]
this.gridControl1[row,col].Format = "N";
```

```vb
[VB]
Me.gridControl1(row,col).Format = "N"
```

## API Reference (if applicable)
- **GridCellToExcel()**: Method in **GridExcelConverterControl** class for converting GridControl cells to Excel.
- **CellType**: Property to identify the type of cell (e.g., Currency, Number).
- **CellValue**: Represents the value of a cell.
- **NumberProperty**: Property in Range to store converted number values.

### Code Examples
```csharp
this.gridControl1[row,col].Format = "C";
```

```vb
Me.gridControl1(row,col).Format = "C"
```

## Cross References
- See also: Data grid handling, Excel export functionalities, and grid-to-Excel conversion best practices.

<!-- tags: [Syncfusion-winforms, gridcontrol, excelconversion, currencycells, numbercells] keywords: [GridCellToExcel, CellType, CellValue, NumberProperty, Format, Currency, Number] -->