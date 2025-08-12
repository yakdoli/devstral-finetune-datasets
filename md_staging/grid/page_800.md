```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_800.jpeg
document_name: grid
page_number: 800
page_id: grid#page_800
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Explains the concept of RelatedMasterDetails in the context of Master-Detail relations.
- Demonstrates how to manually specify master-detail relations between three independent tables with primary and foreign key columns in common.
- Provides steps for setting up RelatedMasterDetails relations.

## Content

### RelatedMasterDetails

**Definition:**

- **RelatedMasterDetails** is a Master-Detail relationship where matching keys in columns in the parent and child tables define a relationship between two tables.
- This is a 1:n relationship where each record in the child table can only belong to one parent record.

**Goal:**
This section demonstrates how to manually specify the master-detail relations between three independent tables that have the primary key and foreign key column in common.

### Steps to setup RelatedMasterDetails relation

1. **Setup three datatables that have primary and foreign key columns in common.**

#### Code Example: Creating Parent Table

```csharp
[C#]

private int numberParentRows = 5;
private int numberChildRows = 20;
private int numberGrandChildRows = 50;

// Create Parent Table.
private DataTable GetParentTable()
{
    DataTable dt = new DataTable("ParentTable");

    dt.Columns.Add(new DataColumn("parentID"));
    dt.Columns.Add(new DataColumn("ParentName"));
    dt.Columns.Add(new DataColumn("ParentDec"));

    for (int i = 0; i < numberParentRows; i++)
    {
        DataRow dr = dt.NewRow();

        dr[0] = i;
        dr[1] = string.Format("parentName{0}", i);
        dr[1] = string.Format("parentName{0}", i);
        dt.Rows.Add(dr);
    }
    return dt;
}
```

#### Code Example: Creating Child Table

```csharp
// Create Child Table.
private DataTable GetChildTable()
{
    DataTable dt = new DataTable("ChildTable");
}
```

<!-- tags: [Master-Detail Relation, RelatedMasterDetails, DataTable, ParentTable, ChildTable, PrimaryKey, ForeignKey, 1:n Relationship, C#] keywords: [Master-Detail, Table Setup, Data Relation, Primary Key, Foreign Key, Database Design] -->
```