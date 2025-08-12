```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_618.jpeg
document_name: grid
page_number: 618
page_id: grid#page_618
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:15Z
fidelity: lossless
-->

## Overview
- Explains how records without nested child tables are handled and returned as Record elements instead of RecordRow elements.
- Highlights optimizations for handling schema-based optimizations such as DisableCounters, VirtualMode, and RecordsAsDisplayElements.
- Describes various counter logic options and their memory footprints.

## Content

When the engine detects that records do not have nested child tables, no record preview rows are being used, and each record only has one row (no ColumnSets are used), records do not have to be split into RecordParts. Instead, when querying the DisplayElements collection for a specific row, the engine can simply return a Record element instead of a RecordRow element. The same applies to CaptionSection, ColumnHeaderSection, and FilterBarSection. Instead of returning a CaptionRow, ColumnHeaderRow, or FilterBarRow element, the DisplayElements collection returns the section element. If you use this optimization, you need to be careful in your own code and be aware that when you query the DisplayElements collection instead of a RecordRow element, a Record element can be returned. The same issue is also with ColumnHeader, FilterBase, and Caption.

### All
Enables the optimizations - DisableCounters, VirtualMode, and RecordsAsDisplayElements.

Based on the schema that you specify, the engine will determine if certain optimizations can be applied. If you do have a flat table and do not sort the records, VirtualMode will be applied, and the records don't have to be touched at all (only when drawing). If you sort records, then TreeTables will be built so that the grid can sort the records, but the logic for filtering and grouping is turned off (DisableCounters optimization). In the case of pass-through sorting, the table is sorted by using the DataView.Sort routine, and records will be accessed with VirtualMode. If you group records or if you have nested tables, then full grouping logic will be needed.

### CounterLogic
In addition to being able to specify VirtualMode or WithoutCounter mode, you can also specify which counters you need. Most of the times, you only want to count visible elements and filtered records and you can leave out custom counters, hidden element counter, and others. This can save you a few bytes per record (40-80 bytes). The engine will also determine whether records actually need to be broken into pieces or if a record can be returned as leave elements (RecordsAsDisplayElements option). This again saves a few bytes per record.

#### EngineCounters Enumeration
Specifies the values for CounterLogic.

##### All
All counters are supported: visible elements, filtered records, YAmount, hidden elements, hidden records, CustomCount, and VisibleCustomCount. Highest memory footprint.

##### FilteredRecords
Counts only visible elements and filtered records. Smallest memory footprint.

##### YAmount

## Page-level Navigation/TOC (if applicable)
- [All]
- [CounterLogic]
  - [EngineCounters Enumeration]
    - [All]
    - [FilteredRecords]
    - [YAmount]

## Cross References
- See also: Schema-based optimizations, DisableCounters, VirtualMode, RecordsAsDisplayElements, TreeTables, DataView.Sort, Full grouping logic.

<!-- tags: [Syncfusion Winforms, Essential Grid, counter logic, schema-based optimizations, memory footprint, grid] keywords: [Disabling Counters, VirtualMode, RecordsAsDisplayElements, EngineCounters, Filtering, Grouping, Records, TreeTables, DataView.Sort, YAmount] -->
```