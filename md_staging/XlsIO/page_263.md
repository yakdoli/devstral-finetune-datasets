```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_263.jpeg
document_name: XlsIO
page_number: 263
page_id: XlsIO#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:44Z
fidelity: lossless
-->

Essential XlsIO

The following properties of the IPivotTableOption interface are used to customize the settings of the pivot table.

## IPivotTableOption Properties

### Overview
- IPivotTableOption interface properties allow for customization of pivot table settings.
- Properties include options for displaying asterisks, managing headers, enabling custom sorting, and controlling data editing.
- Each property has a detailed description outlining its functionality and usage.

### Content

#### IPivotTableOption Properties Table

| **Property**            | **Description**                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------------------|
| ShowAsteriskTotals      | True, if an asterisk (*) is displayed next to each subtotal and grand total value in the specified PivotTable report. |
| ColumnHeaderCaption     | Specifies the string to be displayed in the column header of the pivot table when in compact layout mode. |
| RowHeaderCaption        | Specifies the string to be displayed in the Row header of the pivot table when in compact layout mode. |
| ShowCustomSortList      | Specifies a boolean value that indicates whether the "custom lists" option is offered when sorting this PivotTable. |
| ShowFieldList           | False, to disable the ability to display the field list for the PivotTable. If the field list was already being displayed, it disappears. |
| IsDataEditable          | True, to disable the alert for when the user overwrites values in the data area of the PivotTable. |
| EnableFieldProperties   | True, if the PivotTable Field dialog box is available when you double-click the PivotTable field. |
| Indent                  | Specifies the indentation increment for compact axis and can be used to set the Report Layout to Compact Form. |
| ErrorString             | Returns or sets the string displayed in cells that contain errors when the DisplayErrorString property is True. |
| DisplayErrorString      | True, if the PivotTable report displays a custom error string in cells that contain errors. The default value is False. |
| MergeLabels             | True, if the specified PivotTable report's outer-row item, column item, subtotal, and grand total labels use merged cells. |
| PageFieldWrapCount      | Returns or sets the number of page fields in each column or row in the PivotTable report. |

## Page-level Navigation/TOC

This page focuses on the properties of the IPivotTableOption interface used to customize pivot table settings in Syncfusion Winforms XlsIO.

## Cross References

See also:
- [IPivotTableOption Interface](#ipivottableoption-interface)
- [Pivot Table Customization](#pivot-table-customization)

<!-- tags: [Syncfusion Winforms, XlsIO, IPivotTableOption, pivot table customization, data editing, field lists, error handling, layout options] -->
```