<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_795.jpeg
document_name: grid
page_number: 795
page_id: grid#page_795
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:56Z
fidelity: lossless
-->

## Overview

- Describes filtering options for grid data based on column values, dates, and datetime values.
- Explains grid grouping functionality in displaying nested tables in a hierarchical structure.
- Details the relationships and hierarchy configuration between tables, including detection and setup.

## Content

### Filtering Grid Data

The table below outlines different filtering criteria for a grid:

| Criteria | Syntax | Description |
|----------|--------|-------------|
| MATCH    | `[columnname] MATCH 'value'` | Filters grid displaying records whose specified column holds whole or a part of the mentioned value (irrespective of character casing). |
| BETWEEN  | `[columnname] BETWEEN {date1,date2}` | Filters grid displaying records whose date lies between the two dates irrespective of the time. |
| BETWEETIME | `[columnname] BETWEETIME {datetime1,datetime2}` | Filters grid displaying records whose datetime value lies between the two dates and respective times. |
| IN       | `[columnname] IN 'val1,val2,..,valn'` | Filters grid displaying records whose specified column holds the values mentioned. |

### Relations and Hierarchy

#### Grid Grouping Control

Grid Grouping control can display nested tables in a hierarchy using a master-detail configuration. In a hierarchical view, all the tables in the data source are interconnected via relations. Generally, a relation between any two tables can take any of the following forms: 1:1, 1:n, n:1, or n:n.

A grouping grid can automatically detect the data relations in a dataset for display. By default, a Relation is created for each such relation found in the dataset. Hence, the data relations defined in a dataset are sufficient enough for the grid to form the relations. No additional code is required in this case.

With nested tables, each record in the parent table will have an associated set of records in the child table. Every record in the relation is provided with a +/- button called RecordPlusMinus that can be expanded (as well as collapsed) to bring the underlying records in the child table into view. The number of tables that can be nested with relations using a Grid Grouping control is unlimited.

#### Relations Collection

## References
- **See also:** [Grid Grouping Control Documentation](#), [Hierarchy in Tables](#)

<!-- tags: [grid, filtering, grid group, hierarchy, relations] keywords: [match, between, betweetime, in, master-detail, 1:1, 1:n, n:1, n:n, automatic detection] -->