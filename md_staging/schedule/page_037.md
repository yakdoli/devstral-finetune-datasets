```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: schedule
page_number: 037
page_id: schedule#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:50Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- A prompt is displayed when closing a modified form.
- Instructions to modify Form_Load code for conditionally reloading saved data.
- New code to implement the conditional reloading logic.

## Content

### Prompt for Closing Modified Form

**Figure 26: A Prompt is displayed as you try to close the Modified Form**

![Image description](#)

The screenshot shows a prompt being displayed when the user attempts to close the modified form. The calendar displayed is for November and December 2006, with the focus on "Wednesday, 08 November 2006". There is a scheduled event labeled "Dr Appt 10:00" for 10:00 AM.

### Modify Form_Load Code

1. Next, modify our Form_Load code to conditionally reload the saved data if the file is present on the disk. Here is the new code. Copy this code to your Form1.cs file. Notice that you have added a "using" statement to reference the System.IO namespace in addition to the new code in the Form1_Load. (If you are not using the 2.0 Framework, remove the partial keyword).

### Code Example

```csharp
using System.IO; // Added this line to reference the System.IO namespace

private void Form1_Load(object sender, EventArgs e)
{
    // Conditional code to reload saved data if the file exists
}
```

Note that you will need to implement the logic inside the `Form1_Load` method to check if the file is present on the disk and reload the saved data accordingly.

## Page-level Navigation/TOC (if applicable)
- Prompt for Closing Modified Form
- Modify Form_Load Code
- Code Example

## Cross References
- See also: Related sections on handling file operations and event-based logic.

<!-- tags: [product, module, control, api, version?] keywords: [form_load, conditional_reloading, file_operations, event_handling, schedule] -->
```