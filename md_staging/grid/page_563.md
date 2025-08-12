```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_563.jpeg
document_name: grid
page_number: 563
page_id: grid#page_563
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.sqlDataAdapter1.Fill(this.dataSet11.Customers);
this.sqlDataAdapter2.Fill(this.dataSet11.Orders);

// Add a Data Relation to the Data Set.
DataRelation dr = new DataRelation("CustomersToOrders",
    this.dataSet11.Customers.Columns["CustomerID"],
    this.dataSet11.Orders.Columns["CustomerID"]);
this.dataSet11.Relations.Add(dr);

// Set up the data sources.
this.masterGrid.DataSource = this.dataSet11.Tables["Customers"];
this.detailsGrid.DataSource = this.dataSet11.Tables["Customers"];
this.detailsGrid.DataMember = "CustomersToOrders";
}
```

### [VB.NET]

```vb
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    ' Fill the Data Set with two tables.
    Me.SqlDataAdapter1.Fill(Me.dataSet11.Customers)
    Me.SqlDataAdapter2.Fill(Me.dataSet11.Orders)

    ' Add a Data Relation to the Data Set.
    Dim dr As DataRelation = New DataRelation("CustomersToOrders",
        Me.dataSet11.Customers.Columns("CustomerID"),
        Me.dataSet11.Orders.Columns("CustomerID"))
    Me.dataSet11.Relations.Add(dr)

    ' Set up the data sources.
    Me.masterGrid.DataSource = Me.dataSet11.Tables("Customers")
    Me.detailsGrid.DataSource = Me.dataSet11.Tables("Customers")
    Me.detailsGrid.DataMember = "CustomersToOrders"
End Sub
```

## 4.2.2.9 Foreign Key Columns: Showing One Value but Saving Another

Very often a table will have a column that displays an ID key defined in another table. In your grid, you may like to have this foreign key mapped to some meaningful value, which is referenced from a different column in this other table. The key column in the foreign table is referred to as the **ValueMember** and the meaningful column is referred to as the **DisplayMember**.

<!-- tags: [Syncfusion Winforms, DataGrid, foreignkey, displaymember, valuemember] keywords: [Windows Forms, Essential Grid, foreign key, data relations, CustomerID, Customer, Orders, dataset, grid, value member, display member, synchronization, meaningful value, table, columns] -->
```