# Progressive Electricity Billing – Python Project

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on monthly electricity consumption. The program should apply multiple consumption slabs, fixed charges, surcharges, and rebates to calculate the final bill. It should compare electricity bills for several months and identify unusual increases in billing amounts.

## 2. Algorithm

1. Start.
2. Enter the number of months.
3. For each month, input the month name and electricity units consumed.
4. Calculate the energy charge using progressive slabs:
   - First 100 units: ₹2 per unit
   - Next 100 units: ₹3 per unit
   - Above 200 units: ₹5 per unit
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge on the energy charge.
7. Apply a 10% rebate on the energy charge if consumption is below 100 units.
8. Calculate and display the final bill.
9. Compare each month's bill with the previous month's bill.
10. If the bill increases by more than 30%, flag it as an unusual increase.
11. Display all monthly bills and stop.

Note: These slab rates and charges are illustrative values for this project, not official electricity tariffs.

## 3. Flowchart

\#chatgpt-mermaid-\_r_f6\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_f6\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_f6\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_f6\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_f6\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_f6\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_f6\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_f6\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_f6\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_f6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_f6\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_f6\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_f6\_ p{margin:0;}#chatgpt-mermaid-\_r_f6\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_f6\_ .label text,#chatgpt-mermaid-\_r_f6\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ .node rect,#chatgpt-mermaid-\_r_f6\_ .node circle,#chatgpt-mermaid-\_r_f6\_ .node ellipse,#chatgpt-mermaid-\_r_f6\_ .node polygon,#chatgpt-mermaid-\_r_f6\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .rough-node .label text,#chatgpt-mermaid-\_r_f6\_ .node .label text,#chatgpt-mermaid-\_r_f6\_ .image-shape .label,#chatgpt-mermaid-\_r_f6\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_f6\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .rough-node .label,#chatgpt-mermaid-\_r_f6\_ .node .label,#chatgpt-mermaid-\_r_f6\_ .image-shape .label,#chatgpt-mermaid-\_r_f6\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_f6\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_f6\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_f6\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_f6\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_f6\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_f6\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_f6\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_f6\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_f6\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_f6\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_f6\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_f6\_ .icon-shape,#chatgpt-mermaid-\_r_f6\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_f6\_ .icon-shape p,#chatgpt-mermaid-\_r_f6\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_f6\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_f6\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_f6\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_f6\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_f6\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_f6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_f6\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_f6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_f6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_f6\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_f6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_f6\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_f6\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_f6\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_f6\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_f6\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .node rect,#chatgpt-mermaid-\_r_f6\_ .node circle,#chatgpt-mermaid-\_r_f6\_ .node ellipse,#chatgpt-mermaid-\_r_f6\_ .node polygon,#chatgpt-mermaid-\_r_f6\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_f6\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_f6\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_f6\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_f6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_f6\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of monthsEnter month and unitsconsumedCalculate energy charge usingslabsCalculate surcharge and rebateAdd fixed charge and calculatefinal billDisplay monthly billMore months?Compare bills of consecutivemonthsIncrease greater than 30%?Flag unusual increaseDisplay normal increaseStopYesNoYesNo

## 4. Python Source Code

```
# Progressive Electricity Billingmonths = int(input("Enter number of months: "))month_names = []bills = []for i in range(months):    name = input("\nEnter month name: ")    units = float(input("Enter units consumed: "))    # Calculate progressive energy charges    if units <= 100:        energy = units * 2    elif units <= 200:        energy = 100 * 2 + (units - 100) * 3    else:        energy = 100 * 2 + 100 * 3 + (units - 200) * 5    fixed = 50    surcharge = energy * 0.05    if units < 100:        rebate = energy * 0.10    else:        rebate = 0    bill = energy + fixed + surcharge - rebate    month_names.append(name)    bills.append(bill)    print("Energy charge: Rs.", round(energy, 2))    print("Fixed charge: Rs.", fixed)    print("Surcharge: Rs.", round(surcharge, 2))    print("Rebate: Rs.", round(rebate, 2))    print("Final bill: Rs.", round(bill, 2))# Compare consecutive monthly billsprint("\n--- Monthly Bill Comparison ---")for i in range(months):    print(month_names[i], ": Rs.", round(bills[i], 2))    if i > 0:        increase = bills[i] - bills[i - 1]        if bills[i - 1] > 0:            percent = increase / bills[i - 1] * 100            if percent > 30:                print("Unusual increase:", round(percent, 2), "%")            elif increase > 0:                print("Normal increase:", round(percent, 2), "%")            else:                print("No increase in bill.")
```

## 5. Sample Input

```
Enter number of months: 3

Enter month name: January
Enter units consumed: 80

Enter month name: February
Enter units consumed: 120

Enter month name: March
Enter units consumed: 250
```

## 6. Sample Output

```
Energy charge: Rs. 160.0
Fixed charge: Rs. 50
Surcharge: Rs. 8.0
Rebate: Rs. 16.0
Final bill: Rs. 202.0

Energy charge: Rs. 260.0
Fixed charge: Rs. 50
Surcharge: Rs. 13.0
Rebate: Rs. 0
Final bill: Rs. 323.0

Energy charge: Rs. 750.0
Fixed charge: Rs. 50
Surcharge: Rs. 37.5
Rebate: Rs. 0
Final bill: Rs. 837.5

--- Monthly Bill Comparison ---
January : Rs. 202.0
February : Rs. 323.0
Unusual increase: 59.9 %
March : Rs. 837.5
Unusual increase: 159.29 %
```

## 7. Result

The Python program calculates electricity bills using progressive consumption slabs, fixed charges, surcharges, and rebates. It compares monthly bills and identifies increases greater than 30% as unusual.
