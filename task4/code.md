# Employee Payroll and Deduction Analysis

## 1. Problem Statement

Design a Python program to calculate an employee's gross salary using basic pay, allowances, overtime, and incentives. Apply progressive deductions, calculate net salary, and display a formatted salary statement.

## 2. Algorithm

1. Start.
2. Input employee name and basic pay.
3. Calculate allowances, overtime pay, and incentives.
4. Calculate gross salary.
5. Apply progressive deductions:
   - 0% for the first ₹10,000
   - 10% for the next ₹10,000
   - 20% for the amount above ₹20,000
6. Calculate net salary = gross salary − deductions.
7. Display the formatted salary statement.
8. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_gh\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_gh\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gh\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_gh\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_gh\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_gh\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_gh\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_gh\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_gh\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_gh\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_gh\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_gh\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_gh\_ p{margin:0;}#chatgpt-mermaid-\_r_gh\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_gh\_ .label text,#chatgpt-mermaid-\_r_gh\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ .node rect,#chatgpt-mermaid-\_r_gh\_ .node circle,#chatgpt-mermaid-\_r_gh\_ .node ellipse,#chatgpt-mermaid-\_r_gh\_ .node polygon,#chatgpt-mermaid-\_r_gh\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .rough-node .label text,#chatgpt-mermaid-\_r_gh\_ .node .label text,#chatgpt-mermaid-\_r_gh\_ .image-shape .label,#chatgpt-mermaid-\_r_gh\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_gh\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .rough-node .label,#chatgpt-mermaid-\_r_gh\_ .node .label,#chatgpt-mermaid-\_r_gh\_ .image-shape .label,#chatgpt-mermaid-\_r_gh\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_gh\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_gh\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_gh\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_gh\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_gh\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_gh\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_gh\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_gh\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_gh\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_gh\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_gh\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_gh\_ .icon-shape,#chatgpt-mermaid-\_r_gh\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_gh\_ .icon-shape p,#chatgpt-mermaid-\_r_gh\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_gh\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_gh\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_gh\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_gh\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_gh\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_gh\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_gh\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_gh\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_gh\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gh\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_gh\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_gh\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_gh\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_gh\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_gh\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_gh\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .node rect,#chatgpt-mermaid-\_r_gh\_ .node circle,#chatgpt-mermaid-\_r_gh\_ .node ellipse,#chatgpt-mermaid-\_r_gh\_ .node polygon,#chatgpt-mermaid-\_r_gh\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_gh\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_gh\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_gh\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_gh\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_gh\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput employee details andbasic payCalculate allowances, overtimeand incentivesCalculate gross salaryCalculate progressivedeductionsNet salary = Gross salary -DeductionsDisplay salary statementStop

## 4. Python Source Code

```
name = input("Enter employee name: ")basic = float(input("Enter basic pay: "))allowances = float(input("Enter allowances: "))overtime = float(input("Enter overtime pay: "))incentives = float(input("Enter incentives: "))gross = basic + allowances + overtime + incentivesif gross <= 10000:    deduction = 0elif gross <= 20000:    deduction = (gross - 10000) * 0.10else:    deduction = 1000 + (gross - 20000) * 0.20net = gross - deductionprint("\n===== SALARY STATEMENT =====")print("Employee Name :", name)print("Basic Pay     : ₹", basic)print("Allowances    : ₹", allowances)print("Overtime Pay  : ₹", overtime)print("Incentives    : ₹", incentives)print("----------------------------")print("Gross Salary  : ₹", round(gross, 2))print("Deductions    : ₹", round(deduction, 2))print("Net Salary    : ₹", round(net, 2))
```

## 5. Sample Input

```
Enter employee name: Ravi
Enter basic pay: 25000
Enter allowances: 5000
Enter overtime pay: 2000
Enter incentives: 3000
```

## 6. Sample Output

```
===== SALARY STATEMENT =====
Employee Name : Ravi
Basic Pay     : ₹ 25000.0
Allowances    : ₹ 5000.0
Overtime Pay  : ₹ 2000.0
Incentives    : ₹ 3000.0
----------------------------
Gross Salary  : ₹ 35000.0
Deductions    : ₹ 4000.0
Net Salary    : ₹ 31000.0
```

Note: The deduction slabs are illustrative. The program applies 10% to the portion between ₹10,000 and ₹20,000 and 20% only to the portion above ₹20,000.
