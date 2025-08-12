```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_625.jpeg
document_name: grid
page_number: 625
page_id: grid#page_625
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Setting Up a New Grid Engine

Figure 262: Loading Grid Grouping Control  

![Loading Grid Grouping Control](https://i.imgur.com/json/EngineOptimizations.png "Figure 262: Loading Grid Grouping Control")

**Figure 262:** Loading Grid Grouping Control

1. **Set up a new engine and specify the optimizations settings required.**

#### C#

```csharp
GridEngine schema = new GridEngine();
schema.InvalidateAllWhenListChanged = false;
schema.AllowedOptimizations = EngineOptimizations.All;
schema.CounterLogic = EngineCounters.YAmount;

// Also dependent on CounterLogic = EngineCounters.YAmount.
schema.TableOptions.VerticalPixelScroll = true;
schema.TableOptions.ColumnsMaxLengthStrategy = GridColumnsMaxLengthStrategy.FirstNRecords;
schema.TableOptions.ColumnsMaxLengthFirstNRecords = 100;
schema.TableOptions.AllowSortColumns = true;
schema.TableDescriptor.AllowEdit = false;
schema.DataSource = new VirtualList(100000);
schema.Reset();
schema.TableDescriptor.Columns["Index"].MaxLength = 10;
```

#### VB

```vb
' [VB]
' Code for VB implementation here
```

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridEngine
- **Properties:**
  - `InvalidateAllWhenListChanged`: Determines if the grid should invalidate all when list changed.
  - `AllowedOptimizations`: Specifies the optimizations settings.
  - `CounterLogic`: Specifies the counter logic to use.
  - `TableOptions`: Provides access to various grid table options.
  - `TableDescriptor`: Provides access to table descriptor properties.
  - `DataSource`: Specifies the data source for the grid.
- **Methods:**
  - `Reset()`: Resets the grid engine settings.
- **Enums:**
  - `EngineOptimizations`: Collection of optimization options for the grid engine.
  - `EngineCounters`: Enumeration of possible counter logics.
  - `GridColumnsMaxLengthStrategy`: Strategy for setting maximum column lengths.

## Code Examples

### Example: Setting Grid Engine Optimizations

```csharp
GridEngine schema = new GridEngine();
schema.InvalidateAllWhenListChanged = false;
schema.AllowedOptimizations = EngineOptimizations.All;
schema.CounterLogic = EngineCounters.YAmount;
schema.TableOptions.VerticalPixelScroll = true;
schema.TableOptions.ColumnsMaxLengthStrategy = GridColumnsMaxLengthStrategy.FirstNRecords;
schema.TableOptions.ColumnsMaxLengthFirstNRecords = 100;
schema.TableOptions.AllowSortColumns = true;
schema.TableDescriptor.AllowEdit = false;
schema.DataSource = new VirtualList(100000);
schema.Reset();
schema.TableDescriptor.Columns["Index"].MaxLength = 10;
```

## See also

- [Grid Engine Overview](#grid-engine-overview)
- [Optimizations in Grid Engine](#optimizations-in-grid-engine)
- [Table Options and Settings](#table-options-and-settings)

<!-- tags: grid, grid engine, optimizations, data binding, virtual list, windows forms, syncfusion sdk, 11.4.0.26 keywords: GridEngine, EngineOptimizations, EngineCounters, TableOptions, TableDescriptor, DataSource -->
```