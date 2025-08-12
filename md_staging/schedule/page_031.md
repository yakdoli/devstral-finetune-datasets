```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: schedule
page_number: 031
page_id: schedule#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:23Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

```csharp
using System.Text;
using System.Windows.Forms;
using Syncfusion.Windows.Forms.Schedule;
using GridScheduleSample;

namespace ScheduleSample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SimpleScheduleDataProvider data = new SimpleScheduleDataProvider();
            data.MasterList = new SimpleScheduleItemList();
            data.FileName = "default.schedule";
            this.scheduleControl1.ScheduleType = ScheduleViewType.Month;
            this.scheduleControl1.DataSource = data;
        }
    }
}
```

## Overview
- Demonstrates the integration of the Syncfusion Schedule control in a Windows Forms application.
- Sets up simple scheduling functionality using a data source and predefined layout.
- Configures the Schedule control to display in month view.

## Content
The code snippet above initializes a Windows Forms application with a Syncfusion Schedule control. Here's a breakdown of the steps performed:

1. **Namespace and Using Directives**: The necessary namespaces are included to provide access to System, Forms, and Syncfusion controls.
2. **Form Class Definition**: The `Form1` class inherits from `System.Windows.Forms.Form` and utilizes the Designer-generated code (`partial class`) for UI components.
3. **Constructor Initialization**: The constructor initializes the components, typically set up in the Designer.
4. **Form Load Event**: In the `Form1_Load` method, the Schedule control's data source is configured.
   - A `SimpleScheduleDataProvider` instance is created to manage the schedule data.
   - The `MasterList` property is initialized to store schedule items.
   - A file name is assigned to the data provider for persistence.
   - The `ScheduleType` is set to `Month`, indicating the default view of the Schedule control.
   - The `DataSource` for the `scheduleControl1` is linked to the `data` object.

### Explanation of Key Components
- **`SimpleScheduleDataProvider`**: Manages the data for the Schedule control. This includes scheduling items and persistence.
- **`ScheduleViewType.Month`**: Sets the Schedule control to display in month view, offering a comprehensive overview of the schedule.

## API Reference

### Classes
- **SimpleScheduleDataProvider**
  - **Properties**
    - `MasterList`: Holds the collection of scheduling items.
    - `FileName`: Specifies the file name for persistence.

- **ScheduleControl**
  - **Properties**
    - `ScheduleType`: Determines the view mode (e.g., month, week, day).

### Methods
- **Form1_Load**: Event handler for the load event of the form, configuring the Schedule control's data and view settings.

## Code Examples

The provided code illustrates how to configure a Syncfusion Schedule control in a Windows Forms application. It ensures the control displays a monthly schedule and is linked to a simple data provider.

## Page-level Navigation/TOC
- This page focuses on integrating and configuring the Schedule control in a Windows Forms application.

## Cross References
See also:
- Advanced Schedule customization
- Working with Schedule data binding

<!-- tags: Windows Forms, Schedule Control, Data Binding, Month View, SimpleScheduleDataProvider keywords: Windows Forms, Syncfusion, Schedule, Month View, Data Binding, SimpleScheduleDataProvider -->
```