```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_771.jpeg
document_name: grid
page_number: 771
page_id: grid#page_771
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:18Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the use of RecordFilters (RowFilters) to restrict displayed records based on specified logical conditions.
- Describes the RecordFilters collection and its components, including RecordFilterDescriptor, FilterRowDescriptor, and FilterCondition.
- Guides how to use the designer to add RecordFilters for specific fields.

## Content

### 4.3.4.3.4.2 RecordFilters

**RecordFilters** otherwise called as **RowFilters** will allow you to restrict displayed records to those that will satisfy the logical condition that you specify with a FilterRowDescriptor. You have the option of typing an expression (similar to an Expression Field) or entering a condition using an editor dialog.

#### RecordFilters Collection

The RecordFilters collection defines filter criteria for showing or hiding records. Each filter in this collection is internally maintained by a **RecordFilterDescriptor**. All the RecordFilterDescriptors for a given filter are managed by the **RecordFilterDescriptorCollection** which is returned by the **RecordFilters** property of the TableDescriptor. Filters can be specified through text formulas similar to expression fields or through the entries of **FilterConditionCollection**.

**FilterConditionCollection** is a set of conditions each with a **CompareOperator** and a **CompareValue** to compare with the value retrieved from the record. A condition can also have a custom **ICustomFilter** object if you want to provide your own logic for evaluating filter criteria.

#### Adding Filters Through Designer

Record Filters can easily be added through the designer. Opening the TableDescriptor.RecordFilters property in the property window will display the RecordFilterDescriptor Collection Editor that allows you to define record filters. The designer settings shown in the below image will setup a record filter for the field 'wins', to display only the records with **wins > 20**.

## Code Examples (if any)
<!-- Add any relevant code examples from the page here -->

## Page-level Navigation/TOC (if any)
<!-- Add any page-level TOC or local references here -->

## Cross References
- Refer to the syncfusion-sdk documentation for more detailed information on table descriptors and filter expressions.

<!-- tags: [syncfusion-sdk, windowsforms, grid, recordfilters, filters, filtercondition, compareoperator, icustomfilter, designertool] keywords: [recordfilters, rowfilters, tabledescriptor, filtercondition, compareoperator, icustomfilter, designer] -->
```