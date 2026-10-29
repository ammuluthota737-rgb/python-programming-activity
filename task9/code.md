# Multi-Currency Travel Budget Analysis

## 1. Problem Statement

Develop a Python program to calculate travel expenses in different currencies using supplied exchange rates. Include currency conversion fees, compare total spending against a budget, and identify the largest expense category.

## 2. Algorithm

1. Start.
2. Input the travel budget in Indian rupees.
3. Input the number of expense categories.
4. For each category, enter the expense amount, currency, exchange rate, and conversion fee percentage.
5. Convert the expense into INR.
6. Calculate the conversion fee and total expense.
7. Add all expenses to calculate total spending.
8. Identify the largest expense category.
9. Compare total spending with the budget.
10. Display the expense report and stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_t1\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_t1\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_t1\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_t1\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_t1\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_t1\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_t1\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_t1\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_t1\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_t1\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_t1\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_t1\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_t1\_ p{margin:0;}#chatgpt-mermaid-\_r_t1\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_t1\_ .label text,#chatgpt-mermaid-\_r_t1\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ .node rect,#chatgpt-mermaid-\_r_t1\_ .node circle,#chatgpt-mermaid-\_r_t1\_ .node ellipse,#chatgpt-mermaid-\_r_t1\_ .node polygon,#chatgpt-mermaid-\_r_t1\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .rough-node .label text,#chatgpt-mermaid-\_r_t1\_ .node .label text,#chatgpt-mermaid-\_r_t1\_ .image-shape .label,#chatgpt-mermaid-\_r_t1\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_t1\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .rough-node .label,#chatgpt-mermaid-\_r_t1\_ .node .label,#chatgpt-mermaid-\_r_t1\_ .image-shape .label,#chatgpt-mermaid-\_r_t1\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_t1\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_t1\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_t1\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_t1\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_t1\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_t1\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_t1\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_t1\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_t1\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_t1\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_t1\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_t1\_ .icon-shape,#chatgpt-mermaid-\_r_t1\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_t1\_ .icon-shape p,#chatgpt-mermaid-\_r_t1\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_t1\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_t1\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_t1\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_t1\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_t1\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_t1\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_t1\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_t1\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_t1\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_t1\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_t1\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_t1\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_t1\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_t1\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_t1\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_t1\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .node rect,#chatgpt-mermaid-\_r_t1\_ .node circle,#chatgpt-mermaid-\_r_t1\_ .node ellipse,#chatgpt-mermaid-\_r_t1\_ .node polygon,#chatgpt-mermaid-\_r_t1\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_t1\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_t1\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_t1\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_t1\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_t1\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput budget in INRInput expense details andexchange ratesConvert expense into INRCalculate conversion feeCalculate total expenseMore categories?Calculate total spendingFind largest expense categorySpending <= Budget?Within BudgetOver BudgetDisplay expense reportStopYesNoYesNo

## 4. Python Source Code

```
budget = float(input("Enter travel budget in INR: "))n = int(input("Enter number of expense categories: "))expenses = []total_spending = 0for i in range(n):    print("\nExpense", i + 1)    category = input("Category: ")    amount = float(input("Amount in foreign currency: "))    rate = float(input("Exchange rate (INR per unit): "))    fee_percent = float(input("Conversion fee (%): "))    converted = amount * rate    fee = converted * fee_percent / 100    total = converted + fee    expenses.append((category, converted, fee, total))    total_spending += totallargest = max(expenses, key=lambda x: x[3])print("\n===== TRAVEL BUDGET REPORT =====")for category, converted, fee, total in expenses:    print(f"\nCategory: {category}")    print(f"Converted Amount: Rs. {converted:.2f}")    print(f"Conversion Fee: Rs. {fee:.2f}")    print(f"Total Expense: Rs. {total:.2f}")print("\nTotal Spending: Rs.", round(total_spending, 2))print("Budget: Rs.", round(budget, 2))print("Largest Expense Category:", largest[0])if total_spending <= budget:
```

## 5. Sample Input

```
Enter travel budget in INR: 50000
Enter number of expense categories: 3

Expense 1
Category: Hotel
Amount in foreign currency: 100
Exchange rate (INR per unit): 90
Conversion fee (%): 2

Expense 2
Category: Food
Amount in foreign currency: 100
Exchange rate (INR per unit): 90
Conversion fee (%): 1

Expense 3
Category: Transport
Amount in foreign currency: 200
Exchange rate (INR per unit): 90
Conversion fee (%): 2
```

## 6. Sample Output

```
===== TRAVEL BUDGET REPORT =====

Category: Hotel
Converted Amount: Rs. 9000.00
Conversion Fee: Rs. 180.00
Total Expense: Rs. 9180.00

Category: Food
Converted Amount: Rs. 9000.00
Conversion Fee: Rs. 90.00
Total Expense: Rs. 9090.00

Category: Transport
Converted Amount: Rs. 18000.00
Conversion Fee: Rs. 360.00
Total Expense: Rs. 18360.00

Total Spending: Rs. 36630.0
Budget: Rs. 50000.0
Largest Expense Category: Transport
Status: Within Budget
Remaining: Rs. 13370.0
```

## 7. Result

The program converts foreign expenses into INR, adds conversion fees, calculates total spending, identifies the largest expense category, and checks whether the travel budget is sufficient.

Note: Exchange rates and conversion fees are entered by the user; the sample values are illustrative.
