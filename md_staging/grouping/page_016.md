```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_016.jpeg
document_name: grouping
page_number: 016
page_id: grouping#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:34Z
fidelity: lossless
-->

# Essential Grouping

## Getting Started

This section will show you how easy it is to get started using Essential Grouping. It will give you a basic introduction to the concepts you need to know before getting started with the product and some tips and ideas on how to implement Grouping into your projects to improve customization and increase efficiency. It shows how to create an IList data source and use it with Grouping. The datasource is an ArrayList of custom objects. As part of this lesson, you will see how to iterate through the data in the GroupingEngine.

### 3.1 Creating Platform Application

This section illustrates the step-by-step procedure to create the following platform applications.

#### Creating a Windows Application

1. Open Microsoft Visual Studio. Go to File menu and click New Project. In the New Project dialog, select Windows Forms Application template, name the project and click OK.

![Creating a New Project in Microsoft Visual Studio](https://example.com/new_project_image.jpg)

---

## Overview

- Introduction to Essential Grouping and its benefits.
- Step-by-step guide to setting up a Windows Forms Application.
- Demonstrates creating an IList data source and using it with Grouping.

## Content

### 3.1 Creating Platform Application

This section provides detailed instructions for setting up a Windows Forms Application using Microsoft Visual Studio. The steps include:

1. **Open Visual Studio**: Launch Microsoft Visual Studio.
2. **Access New Project**: Go to the **File** menu and select **New Project**.
3. **Choose Template**: In the **New Project** dialog, select the **Windows Forms Application** template.
4. **Name the Project**: Enter a name for your project in the **Name** field.
5. **Confirm**: Click **OK** to create the project.

The image included above shows the **New Project** dialog box, highlighting the selection of the **Windows Forms Application** template.

## Code Examples

### Example: Creating a Data Source

```csharp
using System;
using System.Collections.Generic;

public class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    public string Category { get; set; }
}

public class DataProvider
{
    public static IList<Product> GetProductList()
    {
        List<Product> productList = new List<Product>
        {
            new Product { Name = "Laptop", Price = 1200.00, Category = "Electronics" },
            new Product { Name = "Pen", Price = 1.50, Category = "Stationery" },
            new Product { Name = "Smartphone", Price = 800.00, Category = "Electronics" },
            new Product { Name = "Pencil", Price = 1.00, Category = "Stationery" }
        };

        return productList;
    }
}
```

## RAG Annotations

<!-- tags: [Essential Grouping, Windows Forms Application, Data Source, IList, GroupingEngine, Product, ArrayList] keywords: [Microsoft Visual Studio, New Project, Windows Forms, Data Source, Essential Grouping] -->

```