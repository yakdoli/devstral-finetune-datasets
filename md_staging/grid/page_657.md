```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_657.jpeg
document_name: grid
page_number: 657
page_id: grid#page_657
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
// Application.DoEvents();
int recNum = rand.Next(table.Rows.Count - 1);
int rowNum = recNum + 1;
int col = rand.Next(16) + 1;
int colNum = col + 1;
DataRow drow = table.Rows[recNum];
if (!(drow[col] is DBNull))
{
    drow[col] = (int)(Convert.ToDouble(drow[col]) * (rand.Next(50) / 100.0f + 0.8));
}

// Insert or remove a row.
if (insertRemoveCount == 0)
    return;

if (toggleInsertRemove > 0 && (timerCount % insertRemoveModulus) == 0)
{
    icount = ++icount % (toggleInsertRemove * 2);
    shouldInsert = icount < toggleInsertRemove;

    if (shouldInsert)
    {
        for (int ri = 0; ri < insertRemoveCount; ri++)
        {
            int recNum = 5;
            int next = rand.Next(100);
            object[] row = new object[]
            {
                "H" + ti.ToString("00000"), next + 1, next + 2, next + 3, next + 4, next + 5, next + 6,
                next + 7, next + 8, next + 9, next + 10, next + 11, next + 12, next + 13, next + 14,
                next + 15, next + 16, next + 17, next + 18, next + 19, next + 20
            };

            ti++;
            DataRow drow = table.NewRow();
            drow.ItemArray = row;
            table.Rows.InsertAt(drow, recNum);
        }
    }
    else
    {
        for (int ri = 0; ri < insertRemoveCount; ri++)
        {
            int recNum = 5;
            int rowNum = recNum + 1;

            // Underlying data structure (this could be a data table or whatever structure)
            // you use behind a virtual grid)
            if (table.Rows.Count > 10)
        }
    }
}
```

<!-- tags: [Windows Forms, Grid, Essential Grid, DataTable, DataRow, InsertRow, RemoveRow, TogglingInsertRemove, RowCount, DataStructure] keywords: [Windows Forms, Grid, DAL, DataTable, DataRow, DataManipulation, InsertRow, RemoveRow, ToggleInsertRemove, VirtualGrid] -->
```