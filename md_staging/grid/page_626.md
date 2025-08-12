```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_626.jpeg
document_name: grid
page_number: 626
page_id: grid#page_626
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:48Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Configuring the Grid Engine

The following example demonstrates configuring the GridEngine and setting various properties:

```vb
Dim schema As GridEngine = New GridEngine()
schema.InvalidateAllWhenListChanged = False
schema.AllowedOptimizations = EngineOptimizations.All
schema.CounterLogic = EngineCounters.YAmount

' Also dependent on CounterLogic = EngineCounters.YAmount.
schema.TableOptions.VerticalPixelScroll = True
schema.TableOptions.ColumnsMaxLengthStrategy = GridColumnsMaxLengthStrategy.FirstNRecords
schema.TableOptions.ColumnsMaxLengthFirstNRecords = 100
schema.TableOptions.AllowSortColumns = True
schema.TableDescriptor.AllowEdit = False
schema.DataSource = New VirtualList(100000)
schema.Reset()
schema.TableDescriptor.Columns["Index"].MaxLength = 10
```

### Displaying Memory Usage Log

Define a method `LogMemoryUsage` that calculates and displays the amount of memory consumed along with various optimizations applied to the grouping engine.

```csharp
[C#]

void LogMemoryUsage()
{
    // Force garbage collection and get used memory size.
    GC.Collect();
    System.Threading.Thread.Sleep(10);
    GC.Collect();
    System.Threading.Thread.Sleep(100);
    GC.Collect();

    LogWindow.Items.Add(string.Format("Optimizations for {0}: ", this.gridGroupingControl.TableDescriptor.Name));
    LogWindow.Items.Add(string.Format("VirtualMode: {0}, ", this.gridGroupingControl.Table.VirtualMode));
    LogWindow.Items.Add(string.Format("WithoutCounter: {0}, ", this.gridGroupingControl.Table.WithoutCounter));
    LogWindow.Items.Add(string.Format("RecordsAsDisplayElements: {0}, ", gridGroupingControl.Table.RecordsAsDisplayElements));

    Process myProcess = Process.GetCurrentProcess();
    double workingSetSizeInKiloBytes = myProcess.WorkingSet64 / 1000;
    string s = "Process's physical memory usage: " + workingSetSizeInKiloBytes.ToString() + " kb";
    LogWindow.Items.Add(s);
    LogWindow.Items.Add("");
}
```

## API Reference

### Properties Used in Example

- **GridEngine**: Represents the engine for handling grid operations.
  - **InvalidateAllWhenListChanged**: A property to control whether the grid is invalidated when the list changes.
  - **AllowedOptimizations**: Specifies the optimiziations allowed for the grid engine.
  - **CounterLogic**: Specifies the logic for handling counters in the grid.
  - **TableOptions**: Defines the options related to the grid's table.
    - **VerticalPixelScroll**: Enable vertical pixel-based scrolling.
    - **ColumnsMaxLengthStrategy**: Strategy for determining the maximum length of columns.
    - **ColumnsMaxLengthFirstNRecords**: Number of records used for first-time column length determination.
    - **AllowSortColumns**: Allow sorting of columns.
  - **TableDescriptor**: Descriptor for the grid's table structure.
    - **AllowEdit**: Enable or disable editing.
  - **DataSource**: Specifies the data source for the grid.
  - **Reset**: Resets the grid engine.

- **VirtualList**: Represents a virtual list for efficient data handling.

### Methods Used in Example

- **LogMemoryUsage**: A custom method to log memory usage.
  - Forces garbage collection using `GC.Collect()` to get an accurate memory usage.
  - Records various optimization settings related to the grid's table structure.
  - Retrieves and displays the current working set size of the process to show physical memory usage.

## Code Examples

The example demonstrates configuring a `GridEngine` and logging its memory usage along with the applied optimizations. The code ensures efficient memory management and optimal grid performance by setting various properties related to virtual mode, counter logic, and sorting capabilities.

<!-- tags: [Syncfusion, GridEngine, Windows Forms, VirtualList, LogMemoryUsage] keywords: [GridEngine properties, memory usage logging, virtual mode, column settings, garbage collection] -->
```