```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_653.jpeg
document_name: grid
page_number: 653
page_id: grid#page_653
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

It is very user interactive options and provides options to test the grid performance by enabling/disabling grouping, sorting, filtering in the midst of heavy updates. It also allows you to change the timer frequency that controls the throughput i.e., the number of updates per unit time. At run time, you can also vary the amount of time the changes are highlighted.

## Overview
- Provides user interactive options for testing grid performance.
- Enables/disables grouping, sorting, and filtering during heavy updates.
- Allows adjusting the timer frequency to control throughput.
- Varies the highlight time for changes at runtime.

## Implementation

This example demonstrates the frequent updates that occur in random cells across the grid grouping control, while keeping the CPU usage at a minimum level. A timer changes cells in short intervals, inserts and removes rows. When you run the sample, you also need to open up the TaskManager in order to notice the CPU usage while the sample runs. You should be able to start up multiple instances without slowing down your machine.

### Setting Up the Grid Grouping Control
1. Set up a Grid Grouping control and load it with some random data. Enable the optimizations as required.

```csharp
GridGroupingControl gridGroupingControl1 = new GridGroupingControl();
gridGroupingControl1.VerticalThumbTrack = true;
gridGroupingControl1.HorizontalThumbTrack = true;
gridGroupingControl1.TableOptions.VerticalPixelScroll = true;
gridGroupingControl1.DataSource = GetRandomDataTable();
this.gridGroupingControl1.ShowGroupDropArea = true;

// Use less memory for internal binary tree structures.
gridGroupingControl1.CounterLogic = EngineCounters.YAmount;
gridGroupingControl1.AllowedOptimizations =
    EngineOptimizations.DisableCounters |
    EngineOptimizations.RecordsAsDisplayElements;

// Use faster GDI drawing.
gridGroupingControl1.UsesDefaultsForFasterDrawing = true;

// Skip Currency Manager.
gridGroupingControl1.BindToCurrencyManager = false;

// Immediate update after each ListChanged event.
gridGroupingControl1.UpdateDisplayFrequency = 1;
```

### Notes
- For the complete code for this example, refer to the following Browser sample:
  ```plaintext
  <Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Performance\Manual Total Summary Demo
  ```

## API Reference

### Grid Grouping Control Properties
- **VerticalThumbTrack**: Enables or disables the vertical thumb tracking.
- **HorizontalThumbTrack**: Enables or disables the horizontal thumb tracking.
- **TableOptions.VerticalPixelScroll**: Enables vertical pixel scrolling.
- **DataSource**: Sets the data source for the grid.
- **ShowGroupDropArea**: Enables or disables the group drop area.
- **CounterLogic**: Specifies the counter logic to be used.
- **AllowedOptimizations**: Enables specific optimizations.
- **UsesDefaultsForFasterDrawing**: Enables faster GDI drawing.
- **BindToCurrencyManager**: Enables or disables binding to the currency manager.
- **UpdateDisplayFrequency**: Sets the frequency of display updates.

## Code Examples

### Setting Up the Grid Grouping Control
```csharp
GridGroupingControl gridGroupingControl1 = new GridGroupingControl();
// Configure the control properties as needed.
gridGroupingControl1.DataSource = GetRandomDataTable();
```

### Enabling Optimizations
```csharp
gridGroupingControl1.AllowedOptimizations = EngineOptimizations.DisableCounters | EngineOptimizations.RecordsAsDisplayElements;
```

### Adjusting Update Frequency
```csharp
gridGroupingControl1.UpdateDisplayFrequency = 1;
```

## Cross References
- **Refer to the full sample code** in the specified location for more details.
- **See also**: Performance enhancements and optimization strategies for the Grid Grouping Control.

<!-- tags: [grid, gridgroupingcontrol, performance, groupingsamples, essentialgrid, winforms, syncfusion, optimizations, randomdata] keywords: [verticalthumbtrack, horizontalthumbtrack, pixelscroll, datasourcesetting] -->
```