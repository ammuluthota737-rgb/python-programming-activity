# University Scholarship Allocation System

## 1. Problem Statement

Design a system to evaluate scholarship applicants based on aggregate marks, subject-wise minimum marks, attendance percentage, and family income. Select eligible students, rank them by merit, and resolve ties using predefined rules.

## 2. Algorithm

1. Start.
2. Input the number of applicants.
3. Read each student's aggregate marks, subject marks, attendance, and family income.
4. Check all eligibility criteria:
   - Aggregate marks ≥ 75%
   - Each subject mark ≥ 60%
   - Attendance ≥ 75%
   - Family income ≤ ₹2,50,000
5. If all conditions are satisfied, mark the student as eligible.
6. Rank eligible students by aggregate marks in descending order.
7. If marks are equal, give priority to higher attendance, then lower family income.
8. Display eligible students and their ranks.
9. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_cf\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_cf\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_cf\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_cf\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_cf\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_cf\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_cf\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_cf\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_cf\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_cf\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_cf\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_cf\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_cf\_ p{margin:0;}#chatgpt-mermaid-\_r_cf\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_cf\_ .label text,#chatgpt-mermaid-\_r_cf\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ .node rect,#chatgpt-mermaid-\_r_cf\_ .node circle,#chatgpt-mermaid-\_r_cf\_ .node ellipse,#chatgpt-mermaid-\_r_cf\_ .node polygon,#chatgpt-mermaid-\_r_cf\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .rough-node .label text,#chatgpt-mermaid-\_r_cf\_ .node .label text,#chatgpt-mermaid-\_r_cf\_ .image-shape .label,#chatgpt-mermaid-\_r_cf\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_cf\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .rough-node .label,#chatgpt-mermaid-\_r_cf\_ .node .label,#chatgpt-mermaid-\_r_cf\_ .image-shape .label,#chatgpt-mermaid-\_r_cf\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_cf\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_cf\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_cf\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_cf\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_cf\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_cf\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_cf\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_cf\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_cf\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_cf\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_cf\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_cf\_ .icon-shape,#chatgpt-mermaid-\_r_cf\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_cf\_ .icon-shape p,#chatgpt-mermaid-\_r_cf\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_cf\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_cf\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_cf\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_cf\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_cf\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_cf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_cf\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_cf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_cf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cf\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_cf\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cf\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_cf\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_cf\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_cf\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_cf\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .node rect,#chatgpt-mermaid-\_r_cf\_ .node circle,#chatgpt-mermaid-\_r_cf\_ .node ellipse,#chatgpt-mermaid-\_r_cf\_ .node polygon,#chatgpt-mermaid-\_r_cf\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_cf\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_cf\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_cf\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_cf\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_cf\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput applicant detailsAggregate = 75%?Not EligibleEvery subject = 60%?Attendance = 75%?Income <= 250000?Mark as EligibleMore applicants?Sort eligible students by marksResolve ties by attendance,then incomeDisplay merit rank and resultsStopNoYesNoYesNoYesNoYesYesNo

## 4. Sample Input

```
Enter number of applicants: 3

Student 1:
Name: Ravi
Aggregate: 85
Minimum subject mark: 70
Attendance: 90
Family income: 200000

Student 2:
Name: Sita
Aggregate: 92
Minimum subject mark: 65
Attendance: 85
Family income: 180000

Student 3:
Name: Raju
Aggregate: 68
Minimum subject mark: 75
Attendance: 80
Family income: 150000
```

## 5. Sample Output

```
UNIVERSITY SCHOLARSHIP RESULTS

Rank  Name   Aggregate  Status
1     Sita      92%     Eligible
2     Ravi      85%     Eligible
-     Raju      68%     Not Eligible

Tie-breaking rules:
1. Higher aggregate marks
2. Higher attendance
3. Lower family income
```

Note: The eligibility thresholds and tie-breaking rules are illustrative. Replace them with the university's official scholarship rules when implementing the system.
