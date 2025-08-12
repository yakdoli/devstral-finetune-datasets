```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_838.jpeg
document_name: grid
page_number: 838
page_id: grid#page_838
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## AutoPopulateRelations Property

It specifies if the relations should be automatically generated when you assign DataSource, with a DataTable with constraints or a DataSet with relations defined. It is true by default.

[C#]

```csharp
this.gridGroupingControl1.AutoPopulateRelations = false;
```

[VB.NET]

```vb
Me.gridGroupingControl1.AutoPopulateRelations = False
```

## ShowRelationFields Property

When a foreign key relation (or related collection) is used, this property controls the display of the dependent fields from a related table in the main table.

### Possible Options

| Property                 | Description                                                                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ShowRelationFields       | Displays the dependent fields from a related table in the main table. It includes the following options.                                                      |
|                          |                                                                                                                                                             |
|                          | - **Hide**: Hides all the fields.                                                                                                                           |
|                          | - **ShowAllRelatedFields**: Shows all related fields including Primary and Foreign Keys.                                                                    |
|                          | - **ShowDisplayFieldsOnly**: Shows only dependent fields; Hides Primary and Foreign Keys.                                                             |

**Default value is ShowDisplayFieldsOnly.**

[C#]

```csharp
this.gridGroupingControl1.ShowRelationFields = ShowRelationFields.ShowAllRelatedFields;
```

[VB.NET]

```vb
Me.gridGroupingControl1.ShowRelationFields = ShowRelationFields.ShowAllRelatedFields
```

<!-- tags: [Essential Grid, Windows Forms, AutoPopulateRelations property, ShowRelationFields property] keywords: [DataSource, DataTable, DataSet, foreign key, related collection, dependent fields, primary keys, foreign keys] -->
```