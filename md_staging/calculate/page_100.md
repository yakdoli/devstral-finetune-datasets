```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_100.jpeg
document_name: calculate
page_number: 100
page_id: calculate#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:51Z
fidelity: lossless
-->

## Necessary Calculations

This section explains the process of transferring values from controls on a form to the Inputs sheet. It highlights the importance of indexing the workbook with the sheet's name and utilizing specific row and column indexes to insert the values into the Inputs sheet.

### Batch Processing with Performance Optimization

The final set of code demonstrates how to handle batch processing requirements. This involves iterating through setting Input values and retrieving corresponding Output values. Setting `CalculatingSuspended` to `True` prevents triggering intermediate calculations, which improves performance by approximately 10% in the provided example with eight inputs. For scenarios with hundreds of inputs, this optimization becomes even more significant.

### Code Example: Button Click Event

The following C# code illustrates how to accomplish this batch processing, running 1000 iterations. It sets various random values into the Inputs sheet while suspending calculations to ensure efficiency.

```csharp
[C#]

private void button2_Click(object sender, System.EventArgs e)
{
    // Runs 1000 iterations.
    int num = 1000;

    this.Cursor = Cursors.WaitCursor;
    DateTime start = DateTime.Now;
    CalcSheet inputSheet = this.calcWB["Inputs"];
    Random r = new Random();

    this.calcWB.Engine.CalculatingSuspended = true;

    for (int i = 0; i < num; ++i)
    {
        // 1) Sets random values into the Inputs sheet.
        inputSheet[ageRow, 2] = (r.Next(74) + 15).ToString();
        inputSheet[sexRow, 2] = r.Next(2) == 1 ? "M" : "F";
        inputSheet[stateRow, 2] = this.comboBoxState.Items[r.Next(50)];
        inputSheet[pointsRow, 2] = r.Next(15).ToString();
        inputSheet[modelRow, 2] = r.Next(11).ToString();
        inputSheet[modelYearRow, 2] = (33 + r.Next(1972)).ToString();
        inputSheet[multipleDiscountRow, 2] = r.Next(2) == 1 ? "Yes" : "No";
        inputSheet[3, 5] = this.textBoxBaseAmount.Text;

        // 2) Calculations are suspended so need to pull the computed value to make sure it has been calculated with the latest changes.
        this.calcWB.Engine.UpdateCalcID();

        calcWB.Engine.PullUpdatedValue(this.calcWB.GetSheetID("Outputs"), 1, 1);

        // 3) Gets the value from cell 1,1 on the output sheet.
    }
}
```

This code snippet effectively demonstrates how to manipulate and retrieve data from Excel sheets within a batch process, emphasizing performance enhancement techniques.

## Related Content

- For more information on performance optimization techniques, refer to [Performance Optimization in Excel with Syncfusion](#).
- Detailed handling of batch operations is explained in [Batch Processing in Syncfusion WinForms](#).

<!-- tags: [Syncfusion, Winforms, Excel, batch processing, performance optimization, inputs, outputs] keywords: [batch processing, random values, calculating suspended, performance improvement, worksheet manipulation, form controls, sheet indexing] -->
```