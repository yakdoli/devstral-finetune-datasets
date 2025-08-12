```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_196.jpeg
document_name: grid
page_number: 196
page_id: grid#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:12Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Custom Borders

![Figure: Custom Borders](#)

Figure 103: Custom Borders

A sample demonstrating this feature is available under the following sample installation path:

```
C:\Syncfusion\EssentialStudio\[VersionNumber]\Windows\Grid.Windows\Samples\2.0\Appearance\Custom Border Demo
```

### Number Formats

The formats of a numeric field (cell value) can be masked by using the `Format` object. You can specify numeric format string as a mask. Format mask objects are assigned to date and numeric fields, and are used to define how the data returned for that field is displayed.

#### Note

Format masks object cannot be deleted once assigned to a field.

The following code examples illustrate masking numeric fields by using the `Format` object:

---

## API Reference

### Format Object

#### Properties

- `FormatString`: Specifies the numeric format string to be used as a mask.
- `Alignment`: Defines the alignment of the formatted text within the field.

#### Methods

- `SetFormat(String formatString)`: Sets the numeric format string for the field.

#### Events

- `FormatChanged`: Raised when the format of the field is changed.

## Code Examples

### Example 1: Setting a Numeric Format Mask

```csharp
// Set a numeric format mask for a specific column
GridColumn col = gridModel.Columns["AmountColumn"];
col.Format = new GridDataFormat("c2");
```

### Example 2: Using Format Mask for Date Fields

```csharp
// Set a date format mask for a specific column
GridColumn dateCol = gridModel.Columns["DateColumn"];
dateCol.Format = new GridDataFormat("dd/MM/yyyy");
```

---

## Page-level Navigation/TOC (if applicable)

- Custom Borders
- Number Formats

## Cross References

See also: [GridColumn](#), [GridDataFormat](#)

---

<!-- tags: [syncfusion-grid, custom-borders, numeric-formats, format-object, gridcolumn, griddataformat] keywords: [custom borders, numeric formats, format object, date formats, alignment, masking, grid column, grid data format] -->
```