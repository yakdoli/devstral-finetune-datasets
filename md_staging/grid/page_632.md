```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_632.jpeg
document_name: grid
page_number: 632
page_id: grid#page_632
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:31Z
fidelity: lossless
--> 

## EngineOptimizations

### Content

#### VirtualList: 100000 Items

| Index | Name                | SomeValue       | OtherValue |
|-------|---------------------|------------------|------------|
| 0     | Name00000000       | 0               | 36627879   |
| 1     | Name000000001      | 0.87333202362060547 | 36627879   |
| 2     | Name000000002      | 1.7466640472412109 | 36627878   |
| 3     | Name000000003      | 2.6199960708618164 | 36627878   |
| 4     | Name000000004      | 3.4933280944824219 | 36627878   |
| 5     | Name000000005      | 4.3666601181030273 | 36627878   |
| 6     | Name000000006      | 5.2399921417236328 | 36627878   |
| 7     | Name000000007      | 6.1133241653442383 | 36627878   |
| 8     | Name000000008      | 6.9866561889648438 | 36627878   |

**Process’s physical memory usage: 33992 kb**

**DescriptorPropertyChangedEventArgs { PropertyName="TableDescriptor", Inner=DescriptorProp**

#### Optimizations for VirtualList:
- VirtualMode: False,
- WithoutCounter: True,
- RecordsAsDisplayElements: True,
- Process’s physical memory usage: 81936 kb

**Figure 265: Log displays optimizations after Sorting the Grid**  
(Virtual Mode disabled)

## Additional Information

- **Log displays optimizations after sorting the grid when Virtual Mode is disabled.**

### Observations
- The grid displays 100,000 items in the VirtualList.
- Performance metrics, such as physical memory usage, are shown before and after sorting.
- The disablement of VirtualMode, WithoutCounter, and RecordsAsDisplayElements is highlighted, impacting memory usage.

## Related Documentation
- Further details on sorting optimizations and Virtual Mode configurations can be found in the Syncfusion Winforms documentation.

<!-- tags: [Product, Control, VirtualMode, Sorting, MemoryOptimization] keywords: [EngineOptimizations, VirtualList, PerformanceMetrics, MemoryUsage, SortingGrid, VirtualModeDisabled] -->
```