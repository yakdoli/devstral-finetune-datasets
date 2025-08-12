```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: QTP
page_number: 042
page_id: QTP#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:39Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- Opens a test file in **QuickTest Professional** and prepares it for execution.
- Describes the process of running a saved test using the toolbar.

## Content

### Steps to Run a Test

1. **Open the Test:**
   - The test file `Test1` is open, as shown in Figure 28.

   ![Figure 28: Test Opened](#)

   The test contains multiple actions targeting a grid control, including:
   - Moving the grid window to specified positions.
   - Setting current cells, cell data, radio buttons, checkboxes, and entering text.
   - Using the `SwfWindow` and `SwfObject` methods to interact with the grid control.

2. **Review the Expert View:**
   - In the **Expert View**, detailed lines of the test script are visible. These lines include commands such as:
     ```
     SwfWindow("GridControl").Move 456,247
     SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 11,4
     SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 13,1,"456.00"
     SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 13,2,"-739.00"
     SwfWindow("GridControl").SwfObject("gridControl1").SetColumnWidth 1,200
     SwfWindow("GridControl").SwfObject("gridControl1").SetCellContents 16,2,"new_value"
     ```
     and so on.

3. **Run the Test:**
   - Click the **Run** button on the toolbar to execute the test.

4. **For More Details:**
   - Additional information on running the test can be found in the **Running a Test** topic in this document.

### Completion of the Process

The process of running a saved test is now complete.

## Cross References

- **Refer to the Running a Test topic** in this document for more details on executing the test.

<!-- tags: [syncfusion-sdk, essential-quicktest-professional, test-execution, test-running, gridcontrol] keywords: [test, grid, swfwindow, swfobject, move, setcurrentcell, setcelldata, setcolumnwidth, syncfusion winforms, qtp] -->
```