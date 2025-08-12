```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_796.jpeg
document_name: grid
page_number: 796
page_id: grid#page_796
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:03Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

The `TableDescriptor.Relations` collection defines relations for the table. By default, a relation (`RelatedMasterDetails`) is created for each `DataRelation` found in a `DataSet`. Relations can either be related foreign key tables or nested child tables that can be expanded and collapsed. Each entry in this collection is owned by a RelationDescriptor that stores the details of a relation. All the RelationDescriptors for a given table is managed by the RelationDescriptor Collection which is returned by the TableDescriptor.Relations property.

The `TableDescriptor.RelationChildColumns` collection is internally initialized and contains the child key fields of the RelationDescriptor.RelationKeys collection of a `RelationKind.RelatedMasterDetails` relation. You should not modify this collection.

The `TableDescriptor.PrimaryKeyColumns` collection defines fields that form a unique primary key for the table. By default, the `PrimaryKeyColumns` collection is initialized from the child key fields of the RelationDescriptor.RelationKeys collection of a `RelationKind.ForeignKeyReference` relation. If the table is not a foreign table and a `UniqueConstraint` for a `DataTable` is present, the collection is initialized with fields from that `UniqueConstraint`. Users can also manually modify the collection. If the table is the foreign table of a `RelationKind.ForeignKeyReference` relation, the parent table uses the fields that are defined in the `PrimaryKeyColumns` collection to lookup and identify records in the foreign table.

### Setting Up Relations Through Designer

After binding an hierarchical dataset to the grouping grid, you could find the `TableDescriptor.Relations` collection populated with values. These values represent the relationship between the parent and child tables.
```