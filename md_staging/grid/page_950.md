```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_950.jpeg
document_name: grid
page_number: 950
page_id: grid#page_950
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
return dt;
}
```

## Code Example (VB.NET)

```vb
Private numberParentRows As Integer = 50
Private numberChildRows As Integer = 200
Private numberGrandChildRows As Integer = 500

Private Function GetParentTable() As DataTable
    Dim dt As DataTable = New DataTable("ParentTable")

    dt.Columns.Add(New DataColumn("parentID"))
    dt.Columns.Add(New DataColumn("ParentName"))
    dt.Columns.Add(New DataColumn("GroupID"))

    Dim r As Random = New Random()
    Dim i As Integer = 0
    Do While i < numberParentRows
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i
        dr(1) = String.Format("parentName{0}", i)
        dr(2) = r.Next(99, 111)
        dt.Rows.Add(dr)
        i += 1
    Loop
    Return dt
End Function

Private Function GetChildTable() As DataTable
    Dim dt As DataTable = New DataTable("ChildTable")

    dt.Columns.Add(New DataColumn("childID"))
    dt.Columns.Add(New DataColumn("Name"))
    dt.Columns.Add(New DataColumn("ParentID"))
    dt.Columns.Add(New DataColumn("ChildGroupID"))

    Dim r As Random = New Random()
    Dim i As Integer = 0

    Do While i < numberChildRows
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i.ToString()
        dr(1) = String.Format("ChildName{0}", i)
        dr(2) = (i Mod numberParentRows).ToString()
    ' ... (code continues)
```

--- 

© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, winforms, essential grid, code examples, vb.net, data table, parent-child relationship, random data generation, api reference] keywords: [numberParentRows, numberChildRows, numberGrandChildRows, GetParentTable, GetChildTable, DataTable, DataRow, Random, String.Format, mod operator] -->
```