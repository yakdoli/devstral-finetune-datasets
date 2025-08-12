```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_813.jpeg
document_name: grid
page_number: 813
page_id: grid#page_813
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

The following section illustrates how to configure and use the Foreign Key Reference feature in the Essential Grid control for Windows Forms.

```vb
' Disallow users to modify states.
usStatesRd.ChildTableDescriptor.AllowNew = False

mainTd.Relations.Add(usStatesRd)

' Assign data source.
Me.gridGroupingControl1.DataSource = table
mainTd.Name = "ForeignKeyReference"
```

### Explanation
- **Disallow users to modify states**: The `AllowNew` property of the `ChildTableDescriptor` is set to `False` to prevent modifying the states.
- **Add relations**: The `usStatesRd` object is added to the `mainTd.Relations` collection to establish a foreign key relationship.
- **Assign data source**: The `gridGroupingControl1`'s `DataSource` is set to the `table` object.
- **Name the main table descriptor**: The `mainTd.Name` is set to `"ForeignKeyReference"`.

### Sample Output
Here is a sample output that displays a look-up child list for the data column `State` with value `Georgia`.

![ForeignKeyReference Relation](https://example.com/figure322.png)
*Figure 322: ForeignKeyReference Relation*

## Page-level Navigation/TOC (if applicable)
- [Essential Grid for Windows Forms]
  - [Disallow users to modify states]
  - [Assign data source]
  - [Sample Output]

<!-- tags: [syncfusion, winforms, essentialgrid, foreignkeyreference] keywords: [disallow, states, look-up, child list, data column, value, georgia] -->
```