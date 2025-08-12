```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_815.jpeg
document_name: grid
page_number: 815
page_id: grid#page_815
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:13Z
fidelity: lossless
-->

## Example

### Overview
- Creates two data tables: Customers and Items.
- Demonstrates the use of `ForeignKeyKeyWords` relation to display both parent and child records in a single row.

### Content

#### Explanation
Say you have a Customers table. Each customer can have a list of purchased items. With MasterDetails, for a given customer, the underlying child list (the list of items purchased by that customer) will be displayed in a separate table once the RecordPlusMinus button is clicked. Instead if you want to view the entire record along with the related child records in a single row, then ForeignKeyKeyWords would be the right choice to use.

The following example illustrates creation of ForeignKeyKeyWords relation.

1. Create two data tables Customers and Items and add a list of records into them.

#### Code Example
```csharp
private int numberParentRows = 6;
private int numberChildRows = 20;

private DataTable GetParentTable()
{
    DataTable dt = new DataTable("Customers");

    dt.Columns.Add(new DataColumn("customerID"));
    dt.Columns.Add(new DataColumn("CustomerName"));
    dt.Columns.Add(new DataColumn("Address"));

    for (int i = 0; i < numberParentRows; ++i)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i;
        dr[1] = string.Format("CustomerName{0}", i);
        dr[2] = string.Format("Address{0}", i);
        dt.Rows.Add(dr);
    }

    return dt;
}

private DataTable GetChildTable()
{
    DataTable dt = new DataTable("Items");

    dt.Columns.Add(new DataColumn("ItemID"));
    dt.Columns.Add(new DataColumn("ItemName"));
    ...
}
```

### Footer
© 2013 Syncfusion. All rights reserved.
```