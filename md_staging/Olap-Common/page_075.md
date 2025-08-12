```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_075.jpeg
document_name: Olap Common
page_number: 075
page_id: Olap Common#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:13Z
fidelity: lossless
-->

# Essential OlapCommon

## 4.4.1 MDXQuerySpecification

### Overview
- MDXQuerySpecification is the foundational element for query creation in OlapCommon.
- Categorizes query elements into three main clauses: `With`, `Select`, and `Where`.
- Iterates through report elements and stores them according to the specified categorization.
  
### Content

#### MDXQuerySpecification
MDXQuerySpecification is the base for query creation. The MDXQuerySpecification will categorize the element into three clauses namely:
- `With`
- `Select`
- `Where`

The elements in the given report are iterated and stored according to the specification.
- The calculated member element in the given report will be added under the `With` clause.
- The categorical and series items in the given report's categorical elements and series element will come in the `Select` category.
- The `Slicer` and `Filter` items will come under the `Where` category.

Based on the current report, the `TogglePivot` value and the axis position of each item will be assigned before it is stored in the appropriate clauses.

#### Query Specification Diagram

![MDXQuerySpecification](https://i.imgur.com/placeholder_image_link.png)
**Figure 8: MDXQuerySpecification**

#### Query Generation
Once the query specification is created, the `GenerateQueryEx()` method of `QueryBuilderEngine` was called by passing the created `MDXQuerySpecification` to generate the query.

---

## 4.4.2 Steps in Query Generation

### Overview
- Describes the process of generating a query using the MDXQuerySpecification.

### Content

#### Steps to Generate a Query
To generate a query:
1. Get the query specification and iterate through the items in each category (`With`, `Select`, and `Where`) of specification and separately store the column elements, row elements, filter elements, and slice elements.
2. The filter, slicer, and sort elements are moved to the appropriate axis based on their axis property.
3. Once the initial level categorizing of elements is completed, it starts creating a query string by writing using `With` or `Select`.
4. Now it starts writing the query by checking each and every property.

---

### Page-level Navigation/TOC
- [MDXQuerySpecification](#4.4.1-mdxqueryspecification)
- [Steps in Query Generation](#4.4.2-steps-in-query-generation)

### Cross References
- See also: [Olap Common: QueryBuilderEngine](#)

<!-- tags: [olapcommon, mdxqueryspecification, querygeneration, syncfusion, windowsforms, sfpivot] keywords: [query creation, mdx, with clause, select clause, where clause, calculated member, category, series, filter, slicer, axis, query string, togglepivot, QueryBuilderEngine] -->
```