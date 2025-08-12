```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: ProjIO
page_number: 042
page_id: ProjIO#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:19Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Properties and descriptions related to resource management.
- Includes details on NTAccount, MaterialLabel, Code, Group, and WorkGroup.
- Focuses on resource allocation, hyperlink settings, and scheduling dates.

## Content

### Resource Properties Table

| Property              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| name. For use with Japanese only. |          |
| NTAccount             | Gets or sets the NT account associated with the resource.               |
| MaterialLabel         | Gets or sets the unit of measure for the material resource.             |
| Code                  | Gets or sets the code or other information about the resource.          |
| Group                 | Gets or sets the group to which the resource belongs.                   |
| WorkGroup             | Gets or sets the type of workgroup to which the resource belongs.       |
| EmailAddress          | Gets or sets the email address of the resource.                         |
| Hyperlink             | Gets or sets the title of the hyperlink associated with the resource.   |
| HyperlinkAddress      | Gets or sets the hyperlink associated with the resource.               |
| HyperlinkSubAddress   | Gets or sets the document bookmark of the hyperlink associated with the resource. |
| MaxUnits              | Gets or sets the maximum number of units that the resource is available. |
| PeakUnits             | Gets or sets the largest number of units assigned to the resource at any time. |
| OverAllocated         | True if the resource is over allocated.                                  |
| AvailableFrom         | Gets or sets the first date that the resource is available.             |
| AvailableTo           | Gets or sets the last date the resource is available.                   |
| Start                 | Gets or sets the scheduled start date of the resource.                  |
| Finish                | Gets or sets the scheduled finish date of the resource.                 |
| CanLevel              | True if the resource can be leveled.                                     |

## API Reference

### Namespace: Syncfusion.Windows.Forms.Utilities.ResourceComponents

#### Properties

- **name**: For use with Japanese only.
- **NTAccount**: Gets or sets the NT account associated with the resource.
- **MaterialLabel**: Gets or sets the unit of measure for the material resource.
- **Code**: Gets or sets the code or other information about the resource.
- **Group**: Gets or sets the group to which the resource belongs.
- **WorkGroup**: Gets or sets the type of workgroup to which the resource belongs.
- **EmailAddress**: Gets or sets the email address of the resource.
- **Hyperlink**: Gets or sets the title of the hyperlink associated with the resource.
- **HyperlinkAddress**: Gets or sets the hyperlink associated with the resource.
- **HyperlinkSubAddress**: Gets or sets the document bookmark of the hyperlink associated with the resource.
- **MaxUnits**: Gets or sets the maximum number of units that the resource is available.
- **PeakUnits**: Gets or sets the largest number of units assigned to the resource at any time.
- **OverAllocated**: True if the resource is over allocated.
- **AvailableFrom**: Gets or sets the first date that the resource is available.
- **AvailableTo**: Gets or sets the last date the resource is available.
- **Start**: Gets or sets the scheduled start date of the resource.
- **Finish**: Gets or sets the scheduled finish date of the resource.
- **CanLevel**: True if the resource can be leveled.

## Code Examples

```csharp
// Example: Setting resource properties
using Syncfusion.Windows.Forms.Utilities;

Syncfusion.Windows.Forms.Utilities.ResourceComponent resource = new Syncfusion.Windows.Forms.Utilities.ResourceComponent();
resource.NTAccount = "DOMAIN\\Username";
resource.Code = "Resource123";
resource.Group = "Engineering";
resource.MaxUnits = 10;
resource.Start = DateTime.Now;
resource.Finish = DateTime.Now.AddDays(14);
resource.CanLevel = true;
```

## Page-level Navigation/TOC
- [ ] [Resource Properties Overview](#resource-properties-table)

## Cross References
- See also: Documentation for `ResourceComponent` in the standard API reference.

<!-- tags: [resource, allocation, hyperlink, scheduling, Windows Forms] keywords: [NTAccount, MaterialLabel, Code, Group, WorkGroup, EmailAddress, Hyperlink, HyperlinkAddress, HyperlinkSubAddress, MaxUnits, PeakUnits, OverAllocated, AvailableFrom, AvailableTo, Start, Finish, CanLevel] -->
```