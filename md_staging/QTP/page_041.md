```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: QTP
page_number: 041
page_id: QTP#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:47Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Steps to open saved tests using the Open Test dialog.
- Details on displaying the saved test name and path upon opening.

## Content

### Opening a Saved Test

#### Note:
The Open Test dialog box is displayed with a list of saved tests.

**Figure 27: Open Test Dialog**

![Open Test Dialog](https://i.imgur.com/figure27.png)

**Steps:**
1. The Open Test dialog box is displayed with a list of saved tests.
   - **Look in:** ishekmumsl.Documents/Hp/QuickTest Professional/Tests
   - **File name:** A file browser view is displayed showing Test 1.
   - **Files of type:** QuickTest Tests

2. Select the required test and click Open.

#### Note:
The saved test is opened with its name and the complete path as the name of the window. By default, Expert View of the Test is opened.

The following image shows the mouse pointer pointing towards the path and file displayed as the window name.

## API Reference
- **Open Test Dialog:** Displays a list of saved tests.
- **Expert View:** Opens the test in a detailed mode for editing.

## Code Examples
```csharp
// Example of opening a test file
void OpenTest()
{
    string filePath = @"C:\ishkumar\Documents\HP\QuickTest Professional\Tests\Test1";
    if (System.IO.File.Exists(filePath))
    {
        // Open the test file
        OpenTestDialog(filePath);
    }
    else
    {
        MessageBox.Show("The specified test file does not exist.");
    }
}
```

## Cross References
See also: "Working with Test Files" for more information on test file management.

<!-- tags: [QuickTest Professional, Open Test, Test Files, Expert View, Windows Forms] keywords: [Test Management, UI Testing, Test Automation, UI Test Framework, File Operations] -->
```