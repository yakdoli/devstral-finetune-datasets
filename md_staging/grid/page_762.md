```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_762.jpeg
document_name: grid
page_number: 762
page_id: grid#page_762
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Further topics in this section discuss these concepts in detail with suitable examples.

## Expression Fields

### Overview
- **Expression Fields** allow adding a calculated column based on other fields in the same record.
- These columns can be visible or invisible, used in grouping, sorting, or as summary fields.
- Collection editors are used similar to Summary Rows and Summary Columns.

### Expression Fields Collection
- The Expression Fields collection in a TableDescriptor defines expression fields.
- Managed by ExpressonFieldDescriptor collection, each entry (`ExpressionFieldDescriptor`) defines one expression field.
- Expression field data is computed at runtime based on the `ExpressionFieldDescriptor.Expression` formula and may depend on other fields in the same record.

### Adding Expression Fields Through Designer
- **Property Window of Grouping Grid**: Open the `TableDescriptor` section and click the `ExpressionFields` collection property to open the `ExpressionFieldDescriptor Collection Editor`.
- The editor displays properties necessary for setting up expression fields.
- The table below describes some important properties.

| Property Name                    | Description                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| **Name**                         | Specifies the name of the expression field.                                                      |
| **Expression**                   | Specifies the formula expression.                                                                |
| **ResultType**                   | Lets you specify the result type to which the expression should be converted to.                |
| **ForceImmediateSaveValue**      | Indicates whether changes to the field in a record should trigger the SaveValue event. <br> Make it `False` to avoid triggering ListChanged events when the expression field is modified. |

## References
- **See Also**: [ExpressionFields Collection](#), [ExpressionFieldDescriptor Collection Editor](#)

<!-- tags: [Windows Forms, Expression Fields, Syncfusion.Grid.Windows, version] keywords: [ExpressionFields, TableDescriptor, expression formula, collection editor, runtime computation, grouping, sorting, summary fields] -->
```