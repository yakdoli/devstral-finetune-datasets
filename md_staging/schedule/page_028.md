```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: schedule
page_number: 028
page_id: schedule#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:18Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

```csharp
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

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
        }
    }
}
```

## Content

Figure 18: Empty Form1_Load method added by double-clicking the Form in the Designer

5. Now add an existing file to this project, SimpleScheduleDataProvider.cs (or SimpleScheduleDataProvider.vb if you are using VB.NET).  
This file defines several classes that implement the interfaces that the ScheduleControl needs to manage the data associated with the appointments that will appear in the calendar.  
These interfaces are discussed in detail later in this UserGuide.  
For now, just use the implementation provided in the SimpleScheduleDataProvider.cs file.  
This file ships as part of the \SyncfusionEssentialStudio\5.x.x\Windows\Schedule.Windows\Sample.2.0\SampleSchedule sample.  
Drill down to this folder, and add this file to your project by using the Solution Explorer window as shown here.

## Cross References
- See also: SimpleScheduleDataProvider.cs, VB.NET

<!-- tags: product, module, control, api, version? keywords: syncfusion, winforms, schedule, form1, eventhandler, simpleScheduleDataProvider.cs -->
``` 
