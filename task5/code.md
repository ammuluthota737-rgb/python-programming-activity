# Multi-Plan Telecommunications Cost Optimization

## 1. Problem Statement

Develop a Python program to compare multiple mobile plans based on usage, validity, and budget. Calculate extra charges for usage beyond plan limits and identify the most economical eligible plan.

## 2. Algorithm

1. Start.
2. Input user usage, required validity, and budget.
3. Input the number of mobile plans.
4. For each plan, input price, data limit, call limit, validity, and excess charges.
5. Calculate excess charges and total cost for each plan.
6. Check whether the plan satisfies usage, validity, and budget constraints.
7. Select the eligible plan with the lowest total cost.
8. Display plan details and the most economical plan.
9. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_ia\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_ia\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ia\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ia\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_ia\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_ia\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_ia\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_ia\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_ia\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_ia\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ia\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ia\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_ia\_ p{margin:0;}#chatgpt-mermaid-\_r_ia\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_ia\_ .label text,#chatgpt-mermaid-\_r_ia\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ .node rect,#chatgpt-mermaid-\_r_ia\_ .node circle,#chatgpt-mermaid-\_r_ia\_ .node ellipse,#chatgpt-mermaid-\_r_ia\_ .node polygon,#chatgpt-mermaid-\_r_ia\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .rough-node .label text,#chatgpt-mermaid-\_r_ia\_ .node .label text,#chatgpt-mermaid-\_r_ia\_ .image-shape .label,#chatgpt-mermaid-\_r_ia\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_ia\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .rough-node .label,#chatgpt-mermaid-\_r_ia\_ .node .label,#chatgpt-mermaid-\_r_ia\_ .image-shape .label,#chatgpt-mermaid-\_r_ia\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_ia\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_ia\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ia\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ia\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_ia\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_ia\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ia\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ia\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_ia\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_ia\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ia\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_ia\_ .icon-shape,#chatgpt-mermaid-\_r_ia\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_ia\_ .icon-shape p,#chatgpt-mermaid-\_r_ia\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_ia\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_ia\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ia\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_ia\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_ia\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_ia\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_ia\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_ia\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_ia\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ia\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_ia\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ia\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_ia\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_ia\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_ia\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_ia\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .node rect,#chatgpt-mermaid-\_r_ia\_ .node circle,#chatgpt-mermaid-\_r_ia\_ .node ellipse,#chatgpt-mermaid-\_r_ia\_ .node polygon,#chatgpt-mermaid-\_r_ia\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ia\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_ia\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_ia\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_ia\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ia\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput usage, validity andbudgetInput mobile plan detailsCalculate excess charges andtotal costUsage and validity satisfied?More plans?Total cost within budget?Compare with lowest-costeligible planAny eligible plan?Display cheapest eligible planDisplay no eligible planStopNoYesNoYesYesNoYesNo

## 4. Python Source Code

```
usage = float(input("Enter required data (GB): "))calls = int(input("Enter required call minutes: "))days = int(input("Enter required validity (days): "))budget = float(input("Enter budget (Rs): "))n = int(input("Enter number of plans: "))best_plan = ""best_cost = float("inf")for i in range(n):    print("\nPlan", i + 1)    name = input("Plan name: ")    price = float(input("Plan price: "))    data = float(input("Data limit (GB): "))    call_limit = int(input("Call limit (minutes): "))    validity = int(input("Validity (days): "))    extra_data_rate = float(input("Extra cost per GB: "))    extra_call_rate = float(input("Extra cost per minute: "))    extra_data = max(0, usage - data)    extra_calls = max(0, calls - call_limit)    cost = price + extra_data * extra_data_rate    cost += extra_calls * extra_call_rate    print("Total cost: Rs.", round(cost, 2))    if (data >= usage and call_limit >= calls            and validity >= days and cost <= budget):        if cost < best_cost:            best_cost = cost            best_plan = nameprint("\n===== RESULT =====")if best_plan:
```

## 5. Sample Input

```
Enter required data (GB): 2
Enter required call minutes: 300
Enter required validity (days): 28
Enter budget (Rs): 300
Enter number of plans: 3

Plan 1
Plan name: Basic
Plan price: 199
Data limit (GB): 2
Call limit (minutes): 300
Validity (days): 28
Extra cost per GB: 50
Extra cost per minute: 1

Plan 2
Plan name: Smart
Plan price: 249
Data limit (GB): 3
Call limit (minutes): 500
Validity (days): 28
Extra cost per GB: 40
Extra cost per minute: 1

Plan 3
Plan name: Premium
Plan price: 349
Data limit (GB): 5
Call limit (minutes): 1000
Validity (days): 56
Extra cost per GB: 20
Extra cost per minute: 1
```

## 6. Sample Output

```
Total cost: Rs. 199.0
Total cost: Rs. 249.0
Total cost: Rs. 349.0

===== RESULT =====
Most economical plan: Basic
Total cost: Rs. 199.0
```

Result: The Basic plan is the most economical eligible plan because it meets all usage and validity requirements within the ₹300 budget.
