```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_967.jpeg
document_name: grid
page_number: 967
page_id: grid#page_967
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:04Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Stock Exchange View – Displays the details with respect to the individual stock exchange.

### Content

#### Portfolio Manager-Dashboard
![Portfolio Manager-Dashboard](#)

The screenshot shows the **Portfolio Manager-Dashboard** interface. It highlights several components:

- **Tabs:** Dashboard, PerformanceAnalyzer, ContributionAnalyzer.
- **Tabs (Detail View):** DataView, Industry/SectorView, StockExchangeView.
- **Stock Details Table:** Displays columns for Delete, Symbol, Name, PricePaid, Quantity, and Change. Each row represents a stock or fund with corresponding details.
  - Example entries:
    - **AmericanFunds**: $-6595.22, "ChildrenCollegeSavings"
    - **SchwabFunds**: $-4357.70, "RetirementSavings", etc.

#### Contribution Analyzer
**Contribution Analyzer:** This module illustrates the contributions of different stocks for every portfolio account in a graphical representation by using chart controls. Click the desired portfolio account on the left side chart to view its contributions.

### API Reference

#### Methods
- **Add to portfolio:** Adds a new stock to the portfolio by setting Symbol Name, Symbol, Quantity, Price, and selecting the Account and StockExchange.

### Code Examples

#### Example of Adding Stocks to a Portfolio
```csharp
// Example of adding stocks to a portfolio
public void AddStockToPortfolio(string symbolName, string symbol, int quantity, decimal price)
{
    // Logic to add the stock to the portfolio
    // Update the portfolio grid with the new stock details
}
```

### Cross References
- For more information on the **Portfolio Manager-Dashboard**, refer to the Syncfusion documentation.
- The **Contribution Analyzer** section provides a graphical breakdown of portfolio contributions.

### RAG Annotations
<!-- tags: grid, windows forms, stock exchange view, portfolio manager, contribution analyzer, essential grid keywords: stock details, price paid, quantity, change, dashboard, performance analyzer, contribution analyzer -->
```