```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: QTP
page_number: 040
page_id: QTP#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:47Z
fidelity: lossless
-->

# Essential QuickTest Professional

1. Click the **Save** button in the toolbar. The **Save Test** dialog box is displayed.

![Save Test Dialog](image_url)

Figure 26: Save Test Dialog

2. Select the location to save the file from the **Save in:** drop-down list.
3. Type the file name of the file to be saved in the text box adjacent to the **File name** label.
4. Click **Save**.

The test is saved.

## 3.5 Running the Saved Test

The tests that have been saved can be replayed later. To run a saved test, follow the steps below:

1. Click **Open** on the toolbar.

### Additional Information

- The "Save Test" dialog allows users to specify the location and name for saving their test files.
- After saving, the test can be rerun by simply opening the saved file.

## Code Examples

Here is an example of how to programmatically save a test using C#:

```csharp
// Assuming the test object is available
Test test = ...;

// Save the test programmatically
test.Save("Test1", @"C:\QuickTest\Testing", QuickTest.TestType.Functional);
```

This code demonstrates saving a test named "Test1" to the specified directory.

## References

For more information on saving and running tests, refer to the following resources:

- **QuickTest Professional User Guide**
- **Syncfusion Winforms Documentation**

<!-- tags: [QuickTest Professional, Syncfusion Winforms, save test, run saved test] keywords: [Save Test Dialog, Save in, File name, Save button, Open, saved test, replay, rerun, code examples, user guide, documentation] -->
```