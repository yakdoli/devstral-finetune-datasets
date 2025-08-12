```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: calculate
page_number: 097
page_id: calculate#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:42Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains how to properly set all dependencies within the underlying `CalcEngine` using `CalculateAll`.
- Details the use of `LockDependencies` and `CalculatingSuspended` properties.
- Describes the process of setting initial values for combo boxes and transferring values between controls and the ExcelRWCalcWorkbook object.

## Content

### Step 2: Dependency Management and Calculation

A call to **CalculateAll** is made so that all dependencies can be properly set within the underlying `CalcEngine`. By default, dependent management is locked in these classes. **So, you will have to toggle `LockDependencies` to allow the engine to track them.** It works this way for this sample, as you are not changing any relations among the values like adding or editing actual formulas, so the dependency relations among the values do not change. Thus, these dependencies only need to be done once and not continually updated as values change. The sample requests the calculated values to be refreshed from the beginning and does not rely on auto-calculations.

There is another property setting that is commented out, i.e., setting **CalculatingSuspended** to `True` tells the engine to skip any calculations that might be triggered by changing values. This will postpone calculations until the property is reset to `False`. At that point, you will have to do a **RecalculateAll** call or use an explicit **PullUpdatedValue** call to ensure that the computed values are current. Suspending calculations makes sense if you are updating many entries and do not need intermediate values calculated.

### Step 3: Setting Initial Values and Triggering Calculations

Sets initial values for the combo boxes on the form. This next set of code shows what will happen when you click the button. At this point, the values need to be moved from the controls on the form into the `ExcelRWCalcWorkbook` object and the newly computed result is retrieved.

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    // 1) Moves input values from the form into the calcsheet.
    SetSheetInputs();

    // 2) Calculations are not suspended, so just getting the value triggers the calculation. So these two lines are not needed.....
    // this.calcWB.Engine.UpdateCalcID();
    // this.calcWB.Engine.PullUpdatedValue(this.calcWB.GetSheetID("Outputs"), 1, 1);

    // 3) Get the value from cell 1,1 on the output sheet.
    double d;

    if (double.TryParse(this.calcWB["Outputs"][1, 1].ToString(), NumberStyles.Any, null, out d))
    {
        // Cell 1,1 on the outputs sheet has the result.
        this.labelPrice.Text = string.Format("{0:C2}", d);
    }
    else
        this.labelPrice.Text = "----";
}
```

## API Reference

### Methods and Properties Used

- **`CalculateAll`**: Refreshes all calculated values in the `CalcEngine`.
- **`LockDependencies`**: Enables or disables tracking of dependencies within the `CalcEngine`.
- **`CalculatingSuspended`**: Temporarily suspends calculations triggered by value changes.
- **`RecalculateAll`**: Manually recalculates all values in the `CalcEngine`.
- **`PullUpdatedValue`**: Fetches the updated value after calculations are complete.
- **`SetSheetInputs`**: Moves input values from the form controls to the `ExcelRWCalcWorkbook` object.

## Code Examples

The provided code snippet demonstrates how to:
1. Transfer input values from the form to the `ExcelRWCalcWorkbook`.
2. Ensure calculations are triggered and values are updated.
3. Retrieve the computed result from a specific cell and display it on the form.

<!-- tags: [CalcEngine, ExcelRWCalcWorkbook, dependency management, calculation algorithms, WinForms] keywords: [CalculateAll, LockDependencies, CalculatingSuspended, RecalculateAll, PullUpdatedValue, SetSheetInputs] -->
```