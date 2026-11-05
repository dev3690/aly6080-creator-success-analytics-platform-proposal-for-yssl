# Creator Success Analytics Platform — Proposal for YSSL

A proposal, built in stages across a semester, for a Creator Success Analytics Platform for Your Sweet Spot Life (YSSL) — from Northeastern's ALY6080 Integrated Experiential Learning course (instructor Valerie A. Atherley, Fall 2025, CRN 70242). This is one evolving project, not a set of separate assignments: an initial proposal, an annotated bibliography, a development-tracking draft, then a trademark-analysis draft, plus the team's regulatory-compliance work. Read it in order and you can watch the idea change as the evidence comes in.

## In plain language

YSSL runs "Into The Portal", a four-month creative residency where artists, writers, musicians, and designers live and work together, make original content, and share ownership of what they produce. The organisation's problem is a people problem with a data answer: how do you pick the creators who will thrive in that intense, collaborative environment — and then, once they are in, how do you know who is struggling before they quit, and how do you help creative professionals protect their work with trademarks? This project proposes a platform that answers those questions with data, in stages.

## What is in this repo

### The Initial Proposal: Picking Creators Who Will Succeed
Folder: `project-proposal-initial/` Files: `Signature_Assignment_Individual_Project_Proposal_Document_Dev.docx`, `analysis.py`, `analysisR.R` Date: 20 September 2025.
What it does: the starting proposal. YSSL's creator selection relied on application materials and subjective judgement, which may not predict success in a collaborative residency. The proposal's business question: how can YSSL develop a predictive analytics system to identify creators most likely to succeed in the Portal program while maximising content commercial viability and participant satisfaction? It proposes predictive modelling, portfolio analytics, and a match-making system for creator teams. The two code files are sketches, not a finished model: `analysis.py` shows a decision tree (`DecisionTreeClassifier(max_depth=5, min_samples_split=10)`, 70/30 train/test split) on four features — experience, portfolio diversity, collaboration score, education — and `analysisR.R` shows the same idea as logistic regression, reading `creator_applications.csv`. That CSV does not exist in the course folder, and no accuracy is reported for either sketch. Do not quote an accuracy for this model — there is not one.

### The Evidence Base: Annotated Bibliography (Modules 2–4)
Folders: `module-2-project/`, `module-3-project/`, `module-4-project/` Dates: 28 September, 5 October, 11 October 2025.
What it does: the research behind the proposal, built one article at a time. Article 1 is Ucar et al. (2022), who predicted professional musicians' success with XGBoost, decision trees, and support vector machines on Spotify and MusicBrainz data, achieving 82% accuracy — that 82% is the cited study's result, not this project's. Article 2 is Swan and Atkinson (2012), on how community arts organisations balance evaluation with creative values — the source of this project's insistence that analytics must respect artists, not surveil them. Article 3 is Susnjak et al. (2022), who reviewed 17 learning analytics dashboards and found most were descriptive only, with almost none predictive or prescriptive. Module 2's group files (`cards_data.csv` and the XN Project pros-and-cons note) sit alongside the individual bibliography.

### The Pivot: Tracking Creators During the Residency
Folder: `proposal-module-5/` Files: `Module 5 - Individual Project Proposal .docx`, `.pdf` Date: 18 October 2025.
What it does: the proposal changes angle. Selection is not the whole problem — YSSL also had no systematic way to track creator development during the residency itself, so struggling participants stayed invisible until they withdrew. This draft proposes a Creator Development Performance Analytics Platform: baseline assessments and weekly tracking across technical skills, collaboration, creative innovation, and business acumen; role-specific dashboards for creators, mentors, and administrators; and early-warning intervention. Its expected benefits (including a 40–50% attrition reduction) are the proposal's claims, drawn from the cited literature (Verma et al. 2025), not measured results from this project.

### The Second Pivot: Canadian Trademark Challenges
Folders: `proposal-module-8/`, `proposal-module-10/`, `proposal-module-12/` Dates: 9 November, 22 November, 4 December 2025.
What it does: three successive drafts of the same proposal stage. YSSL supports Canadian creative professionals, who face real barriers protecting their brand identities with trademarks — expensive legal help, complex filing, long waits, and applications abandoned or rejected. The drafts propose analysing the Canada Trademarks Dataset (Sheff, 2023: 1.9+ million applications, 1865–2023) to quantify success, failure, and abandonment rates for creative industries, compare subsectors (film, music, design, digital arts), measure processing times, and build classification models (logistic regression, Random Forest, XGBoost) to predict outcomes. The proposal targets 75%+ accuracy for those models — a target in the proposal, not an achieved result.

### Canada Trademarks Analysis: The Notebook
Folder: `canada-trademarks-analysis/` Files: `Untitled.ipynb`, `CA_TM_main.csv` (27 trademark applications) Charts: `images/viz1_status_distribution.png` through `viz5_subsector_breakdown.png`
What it does: the working analysis behind the trademark drafts — and it must be read honestly. The notebook loads 27 trademark applications, filters to 2000–2023, and finds 0 applications in that window, so its success rates come out as 0.0% — and then it errors (`ValueError: cannot convert float NaN to integer`). Its second cell is labelled "REALISTIC PROJECTIONS": the charts it produces are projections for a presentation, not measured results. This repo includes the notebook and its charts exactly as they are, because the honest story is that the analysis ran into a data-filtering problem, not that it produced a finding. Do not quote 0% success, and do not present the projection charts as measured trademark outcomes.

### The Team Project: Regulatory Compliance for YSSL
Folder: `xn-individual-contribution/` File: `Dev_Panchal_XN_Individual_Contribution.docx` Date: 7 December 2025.
What it does: alongside the individual proposal, Dev's team built a regulatory compliance framework for YSSL, integrating Canadian government regulatory data — occupational health and safety, environmental, and labour regulations — into YSSL's CRM so it could help clients stay compliant. Dev's own contributions were finding and preparing the dataset, creating visualisations in Power BI, and writing the research sections. The large team datasets behind this (Canadian environmental, OHS, NAICS, and business registry data) are not in this repo — several are tens of megabytes — but they are named here so the work is not mistaken for the individual proposal above.

## How to use it

1. Start with the Module 1 proposal in `project-proposal-initial/`, then read Modules 2–4 for the evidence, Module 5 for the development-tracking pivot, and Modules 8, 10, and 12 in order for the trademark drafts — they repeat material as drafts do, and the changes between them are the point.
2. Open `canada-trademarks-analysis/Untitled.ipynb` in Jupyter to see the trademark analysis, including where it breaks. It reads `CA_TM_main.csv` from its own folder.
3. Read the XN individual contribution in `xn-individual-contribution/` for the team compliance work, which is a separate thread from the individual proposal.

## Tools

Python (pandas, scikit-learn, matplotlib, seaborn), R (caret, dplyr, glm), Jupyter, Tableau / Power BI, proposal and literature-review writing, predictive modelling design (decision trees, logistic regression, Random Forest, XGBoost), dashboard design principles.

## What was left out, and why

Only the submitted proposal stages and the working analysis are included. A Week 5 Spotify analysis (mode and danceability charts from `spotify2023.csv`) is a separate class discussion exercise, not part of the YSSL proposal, so it is not in this repo. The large Week 7 team datasets, duplicate copies of the same notebook and proposal files, team member evaluations, and professor material are not included. Where a file is a sketch, a projection, or a proposal target rather than a measured result, this README says so — see the notes in each section above.

## Conclusion

This project is honest about what it is: a proposal that grew up in public. It starts with a selection problem, gathers evidence, realises the harder problem is tracking people once they are in, then follows the evidence again into trademark barriers that Canadian creatives actually face — and its one working notebook shows, plainly, where the analysis itself hit a wall. That arc — propose, research, pivot, test, and report the failure as well as the plan — is exactly what a client project looks like before it becomes a product. A recruiter reading this repo will see not a finished platform, but someone who can scope a real client problem, ground it in literature, design the analytics, and tell the truth about what the data did and did not show.
