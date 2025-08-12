```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: Olap Common
page_number: 072
page_id: Olap Common#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:40Z
fidelity: lossless
-->

## Essential OlapCommon

### Sample of Value, Goal, Status, and Trend expressions

#### Value Expression
```csharp
[Measures].[Reseller Sales Amount]
```

#### Goal Expression
```csharp
[Measures].[Sales Amount Quota]
```

#### Status Expression
```csharp
Case
    When [Measures].[Reseller Sales Amount] / [Measures].[Sales Amount Quota] > 1
        Then 1
    When [Measures].[Reseller Sales Amount] / [Measures].[Sales Amount Quota] <= 1
        And
            [Measures].[Reseller Sales Amount] / [Measures].[Sales Amount Quota] >= .85
            Then 0
    Else -1
End
```

#### Trend Expression
```csharp
Case
    When IsEmpty
        (
            ParallelPeriod
            (
                [Date].[Fiscal].[Fiscal Year],
```

---

© 2013 Syncfusion. All rights reserved.
```