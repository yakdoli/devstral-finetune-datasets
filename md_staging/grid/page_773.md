```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_773.jpeg
document_name: grid
page_number: 773
page_id: grid#page_773
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:01Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

| Conditions                           | A collection of conditions each with a CompareOperator and a CompareValue. |
| ------------------------------------- | ----------------------------------------------------------------------------- |
| Expression                            | A formula expression similar to expression fields.                         |
| LogicalOperator                       | Indicates the logical operator used if multiple conditions are given.      |

### Programmatically

To add a record filter, you must create a RecordFilterDescriptor by specifying the field name with which the filter should be compared and a filter condition that contains a CompareOperator and a CompareValue. The possible options for a CompareOperator are Equals, NotEquals, LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, Like, Match and Custom (for Custom Filter). A filter criteria can also be specified as an expression text similar to the one used in expression fields. A LogicalOperator will be used when you specify more than one condition for a given filter. Finally, add the record filter descriptor to the RecordFilters collection of the Table Descriptor.

Following code example illustrates how to add a record filter for the column "wins" to display only the records with wins > 20.

#### [C#]

```csharp
FilterCondition cond = new FilterCondition(FilterCompareOperator.GreaterThan, 20);
RecordFilterDescriptor filter = new RecordFilterDescriptor("wins", cond);
this.gridGroupingControl.TableDescriptor.RecordFilters.Add(filter);
```

#### [VB.NET]

```vb
Dim cond As FilterCondition = New FilterCondition(FilterCompareOperator.GreaterThan, 20)
Dim filter As RecordFilterDescriptor = New RecordFilterDescriptor("wins", cond)
Me.gridGroupingControl.TableDescriptor.RecordFilters.Add(filter)
```

Given below is a sample screenshot showing the grid filtered with wins > 20.
<!-- tags: [grid, windows forms, record filter, essential grid, synchronization, compare operator, custom filter, logical operator, filter expression, filter condition, table descriptor, record filters, wins, wins > 20, record filter descriptor, condition, expression field, field name, compare value, logical operator] keywords: [grid, windows forms, record filter, essential grid, synchronization, compare operator, custom filter, logical operator, filter expression, filter condition, table descriptor, record filters, wins, wins > 20, record filter descriptor, condition, expression field, field name, compare value, logical operator] -->
```