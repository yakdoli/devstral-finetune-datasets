```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_613.jpeg
document_name: grid
page_number: 613
page_id: grid#page_613
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:11Z
fidelity: lossless
-->

## Overview

This page discusses the optimization properties of the Grid Grouping Control, specifically focusing on the settings available under the "Optimization" section in the Properties window. The properties listed provide control over how the grid behaves during data loading, rendering, and interaction, aiming to improve performance and user experience.

### Key Points

- **Optimization Properties**: Various properties related to grid optimization.
- **AllowedOptimizations**: Specifies the optimizations the grid engine is allowed to use.
- **AllowOptimizeLoadTime**: Property to reduce flickering at startup by pre-rendering the grid.

---

## Content

### Figure 261: Optimization options in the Grid Grouping Control

#### Optimization Properties - A Glance

Below is a brief overview of the properties listed in the figure.

- **AllowedOptimizations**: Specifies the optimizations the engine is allowed to use when applicable. These optimizations can be used in combination with the EngineCounter setting. The EngineOptimizations enum defines the values for this property, which will be discussed further in the next chapter.

- **AllowOptimizeLoadTime**: This property might help in reducing the flickering issue at startup. When enabled, the grid will be rendered once into an offline bitmap before the form is shown for the first time.

#### Detailed Overview of Properties

- **AllowedOptimizations**: Defines which optimizations the grid engine can utilize. The optimizations are based on the EngineOptimizations enum.

- **AllowOptimizeLoadTime**: This property is designed to mitigate flickering issues during the initial display of the grid by performing an offline bitmap render in advance.

The upcoming chapters will provide deeper insights into these properties with suitable examples.

---

## API Reference

The following are the properties related to grid optimization:

- **AllowedOptimizations**: 
  - **Type**: `EngineOptimizations`
  - **Default**: `None`
  - **Description**: Specifies optimizations for the grid engine. Available values can be found in the `EngineOptimizations` enum.

- **AllowOptimizeLoadTime**: 
  - **Type**: `bool`
  - **Default**: `True`
  - **Description**: Enables or disables optimizations during the grid's loading phase to reduce flickering.

---

## Code Examples

Below is a sample code snippet demonstrating how to configure the optimization properties:

```csharp
// Accessing the Grid Grouping Control properties
gridGroupingControl1.AllowedOptimizations = EngineOptimizations.CacheStringIndexes | EngineOptimizations.CacheRecordValues;
gridGroupingControl1.AllowOptimizeLoadTime = true;
```

---

## Cross References

For more detailed discussions on EngineOptimizations and optimization strategies:

- **Next Chapter**: For explanations on various EngineOptimizations and their impact on performance.
- **Chapter on Performance Tips**: For general advice on optimizing grid performance.

---

<!-- tags: [grid, optimization, performance, flickering, cache, engine] keywords: [AllowedOptimizations, AllowOptimizeLoadTime, EngineCounter, EngineOptimizations] -->
```