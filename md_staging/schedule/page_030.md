```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_030.jpeg
document_name: schedule
page_number: 030
page_id: schedule#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:30Z
fidelity: lossless
-->

## Overview
- Steps to add the SimpleScheduleDataProvider.cs file to a Windows Forms project.
- Explains integrating the ScheduleDataProvider to provide data support for the ScheduleControl.
- Provides code examples to set up a data source and configure ScheduleViewType.

## Content

### Adding the SimpleScheduleDataProvider.cs File

Figure 20 illustrates how to add the SimpleScheduleDataProvider.cs file to the project.

![Figure 20: Adding the SimpleScheduleDataProvider.cs file to the Project](image.png)

### Steps to Integrate Schedule Data Support

1. **After adding the SimpleScheduleDataProvider.cs file:**
   - Enhance your project by adding code to `Form.cs` to provide data support to your ScheduleControl.

   - **i. Add a using statement:**
     - Include a using statement to reference the class names in the SimpleScheduleDataProvider.cs file without specifying the namespace directly.

   - **ii. Set up in Form_Load:**
     - In the `Form_Load` event, create an instance of the DataProvider and a MasterList to hold the data.

   - **iii. Configure properties:**
     - Set properties to provide a filename, the `ScheduleViewType` for the initial display, and the `DataSource` property for your ScheduleControl.

   - **iv. Copy the code to Form1.cs:**
     - Transfer the provided code block to your `Form1.cs` file. If you are not using the 2.0 Framework, remove the `partial` keyword.

### Code Examples

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
```

## API Reference

### Namespaces
- **System**
- **System.Collections.Generic**
- **System.ComponentModel**
- **System.Data**
- **System.Drawing**

This reference encompasses the essential namespaces required for integrating the ScheduleControl with the ScheduleDataProvider.

### See also:
- [ScheduleControl Documentation](#schedule-control-documentation)

<!-- tags: [schedule, windowsforms, namespace, data provider, schedule control, schedule viewtype, framework] keywords: [SimpleScheduleDataProvider, Form.cs, data source, ScheduleControl, ScheduleViewType, dataSource] -->
```