```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: XlsIO
page_number: 125
page_id: XlsIO#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:45Z
fidelity: lossless
-->

# Essential XlsIO

## Number Formatting Examples

### Applying Number Format

Both C# and VB.NET code examples demonstrate how to apply a percentage format to a cell.

#### C#

```csharp
// Applying Number Format.
sheet.Range["C8"].Number = 1.20;
sheet.Range["B8"].Text = "0.00%";
sheet.Range["C8"].NumberFormat = "0.00%";
```

#### VB.NET

```vb
' Applying Number Format.
sheet.Range("C8").Number = 1.2
sheet.Range("B8").Text = "0.00%"
sheet.Range("C8").NumberFormat = "0.00%"
```

### Setting DateTime Format

The following code examples show how to set the format for a DateTime value.

#### C#

```csharp
sheet.Range["B2"].NumberFormat = "m/d/yyyy";
sheet.Range["B2"].DateTime = new DateTime(2005, 12, 25);
```

#### VB.NET

```vb
sheet.Range("B2").NumberFormat = "m/d/yyyy"
sheet.Range("B2").DateTime = New DateTime(2005, 12, 25)
```

### Setting Currency Format

The following code examples demonstrate how to set the format for a Currency value.

#### C#

```csharp
// Applying Number Format.
sheet.Range["C4"].Number = 1.20;
sheet.Range["B4"].Text = "$#,##0.00";
sheet.Range["C4"].NumberFormat = "$#,##0.00";
```

#### VB.NET

```vb
' Applying Number Format.
sheet.Range("C4").Number = 1.2
sheet.Range("B4").Text = "$#,##0.00"
```

## API Reference

### Methods and Properties

- `Number`: Sets or gets the numeric value of a cell.
- `Text`: Sets or gets the text value of a cell.
- `NumberFormat`: Sets or gets the number formatting applied to a cell.
- `DateTime`: Sets or gets the DateTime value of a cell.

## Code Examples

### C# Example

```csharp
// Demonstrating Number, Text, and NumberFormat properties.
sheet.Range["C8"].Number = 1.20;
sheet.Range["B8"].Text = "0.00%";
sheet.Range["C8"].NumberFormat = "0.00%";
```

### VB.NET Example

```vb
' Demonstrating Number, Text, and NumberFormat properties.
sheet.Range("C8").Number = 1.2
sheet.Range("B8").Text = "0.00%"
sheet.Range("C8").NumberFormat = "0.00%"
```

### Conclusion

The examples provided illustrate how to apply formatting to cells in an XlsIO worksheet using both C# and VB.NET, covering Number, DateTime, and Currency formats.

<!-- tags: XlsIO, Syncfusion, Winforms, C#, VB.NET, Number Formatting, DateTime, Currency, API Reference, Code Examples keywords: XlsIO, Syncfusion, Winforms, C#, VB.NET, Number Formatting, DateTime, Currency, Cell Formatting, API, Code Examples -->
```