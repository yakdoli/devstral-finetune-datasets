```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_668.jpeg
document_name: grid
page_number: 668
page_id: grid#page_668
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### ListChanging Options

It also includes options to insert, remove, and modify the records in the data source. All the changes will be immediately updated manually by making a call to the `grid.Update` method.

### UseScrollWindow

When enabled, inserting and removing cells will be optimized by scrolling window contents and only invalidating new cells. If set to false, it results in repaint of the whole display. Affects `TableControl.OptimizeInsertRemoveCells` property.

### ExpandAll/CollapseAll

Using these options, you can track the time taken to expand / collapse all the groups and memory usage too.

After enabling the options required, click the LoadGrid button. This will then check for the options requested and apply those options before painting the grid. After loading, it also displays a log to print various performance measures like time taken to paint the grid, physical memory usage, etc. The log will continue to display these performance measures at every instant the grid options are changed.

Given below is a sample screenshot.

## Page-level Navigation/TOC (if applicable)

<!-- Placeholder for local Table of Contents if present -->

## Cross References

See also: [Essential Grid Documentation](https://www.syncfusion.com/documentation/windowsforms/documentation)

## RAG Annotations

<!-- tags: [grid, windows forms, listchanging options, usescrollwindow, expandall, collapseall, performance measures, syncfusion winforms version: 11.4.0.26] keywords: [insert, remove, modify records, data source, grid.update, use scroll window, optimizecells, expand all groups, collapse all groups, time taken, memory usage, log, log measures, painting grid, performance metrics, sample screenshot] -->
```