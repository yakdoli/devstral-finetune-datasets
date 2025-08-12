```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_770.jpeg
document_name: grid
page_number: 770
page_id: grid#page_770
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:11Z
fidelity: lossless
-->

## Overview

- Explains conditions and syntax for using the `between` and `betweentime` operators in a grid to filter records based on date and time intervals.
- Demonstrates examples of using these operators to filter records with specific values or intervals from the current date.

## Content

### Between

| **Concept** | **Operator** | **Description** | **Example** |
|-------------|--------------|-----------------|-------------|
| Between     | between      | Checks if a date field value between the two values is listed in the right-hand operand. For example, `[date] between {2/25/2004, 3/2/2004}` returns 1 for any record whose date field is greater or equal 2/25/2004 and less than 3/2/2004. To represent the current date, use the token `TODAY`. To represent `DateTime.MinValue`, leave the first argument empty. To represent `DateTime.MaxValue`, leave the second argument empty. | `[OrderDate] between {2/25/2007, TODAY}` |

### Between Time

| **Concept**     | **Operator** | **Description**                     | **Example**                                                                 |
|------------------|--------------|-------------------------------------|------------------------------------------------------------------------------|
| Between time     | betweentime  | Checks if a time in the date field value between the two values is listed in the right-hand operand. For example, `[time] between {04:00:00 PM, 05:00:00 PM}` returns 1 for any record whose date field is greater than or equal to 04:00 and less than 05:00. The time will be calculated along with the date for betweentime. | `[OrderDate] between {“04/17/2008 9:00:00 PM”, “04/21/2008 07:00:00 AM”}` |

## API Reference (if applicable)

### Methods and Properties

- **between**: Used for filtering records based on a date range.
- **betweentime**: Used for filtering records based on a time range within a date field.

## Code Examples

### Example 1: Filter Records Based on Date Between Specific Dates

```csharp
string filterExpression = "[OrderDate] between {2/25/2007, TODAY}";
grid.View.info.SetFilter(filterExpression);
```

### Example 2: Filter Records Based on Time Between Specific Times

```csharp
string filterExpression = "[OrderDate] between {“04/17/2008 9:00:00 PM”, “04/21/2008 07:00:00 AM”}";
grid.View.info.SetFilter(filterExpression);
```

## RAG Annotations
<!-- tags: [WinForms, Grid, Filtering, DateTime, DateRange, TimeRange, BETWEEN Operator, BETWEENTIME Operator] keywords: [between, betweentime, filter expressions, date filtering, time filtering, using tokens, date range, time range, current date] -->
```