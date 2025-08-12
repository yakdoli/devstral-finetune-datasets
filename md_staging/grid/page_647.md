<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_647.jpeg
document_name: grid
page_number: 647
page_id: grid#page_647
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

- Making a call to `gridGroupingControl.Update` method.
- Timer Interval is set to 100, meaning there would be an update every 100 ms.
- Implementation pushes pending updates every 100 ms and updates 1000 records each time.

## Code Example: Handling Timer Tick Event

```csharp
[C#]

void timer_tick(object sender, EventArgs e)
{
    GridTableDescriptor td = this.gridGroupingControl1.TableDescriptor;
    ManualTotalSummaryTable tb =
        (ManualTotalSummaryTable)this.gridGroupingControl1.Table;
    int i = 0;
    using (MeasureTime.Measure("Form1.timer_tick"))
    {
        int count = 1000;

        if (this.gridGroupingControl1.SortPositionChangedBehavior ==
            GridListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate)
        {
            if (sortedByFreight || gridGroupingControl.TestDeleteRecords ||
                gridGroupingControl1.TestInsertRecords ||
                gridGroupingControl1.TestChangeGroup)
            {
                // When sort position is changed, this is much more demanding,
                // let's do less records then.
                count = 200;
            }

            if (sortedByEmployeeID)
            {
                // Each update will cause records being shifted around,
                // so let's do even less records. You can also check out
                // InvalidateAll option instead above.
                count = 50;
            }
        }

        for (i = 0; i < count; i++)
        {
            ManualTotalSummaries.DataSet1.OrdersRow dr;

            // Insert Records.
            if (gridGroupingControl1.TestInsertRecords)
            {
                if (i % 10 == 0)
                {
                    dr = northwindDataSet1.Orders.NewOrdersRow();
                    dr.CustomerID = i.ToString() + (j++).ToString();
                    dr.EmployeeID = i;
                    dr.Freight = i / 10;
                    dr.ShipVia = 0;
                }
            }

            // ... (rest of the code continues here)
        }
    }
}
```

## Page-level Navigation/TOC (if applicable)
- Timer-based Update Mechanism
- Handling Sort Position Change
- Adjusting Record Counts based on Operations

## Cross References
- See also: [gridGroupingControl.Update], [Timer.Interval], [ManualTotalSummaryTable]

<!-- tags: [winforms, gridgroupingcontrol, timer, dataset, records, synchronization] keywords: [grid, windows forms, updating, sorting, records, performance] -->