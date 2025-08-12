```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: Olap Common
page_number: 074
page_id: Olap Common#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:25Z
fidelity: lossless
-->

# Essential OlapCommon

```md
When (
    [Measures].[Reseller Sales Amount]
    -
    (
        [Measures].[Reseller Sales Amount],
        ParallelPeriod
        (
            [Date].[Fiscal].[Fiscal Year],
            1,
            [Date].[Fiscal].CurrentMember
        )
    )
    /
    (
        [Measures].[Reseller Sales Amount],
        ParallelPeriod
        (
            [Date].[Fiscal].[Fiscal Year],
            1,
            [Date].[Fiscal].CurrentMember
        )
    ) > .02
Then 1
Else -1
End
```

## 4.4 QueryBuilderEngine

This class will generate the query from the MDXQuerySpecification. The query generation starts from invoking the `GenerateQueryEx()` static method of `QueryBuilderEngineVersion3`, the inner class of `QueryBuilderEngine` class.

<!-- tags: [OlapCommon, query generation, MDXQuerySpecification, QueryBuilderEngine,GenerateQueryEx, performance optimization] keywords: [Olap, query builder, MDX, cube, data analysis] -->
```