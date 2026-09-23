# -*- coding: utf-8 -*-
"""
Content of the Summer Internship Project report of Jayasubha S (OSI2511007),
MBA (Human Resources), ISSM Business School, Chennai.

Internship: Ashok Leyland Limited, Guindy, Chennai
Department: Human Resources and Industrial Relations
Period: 09.06.2026 to 31.07.2026 (as recorded on the internship certificate)
Mentor: Mr. Venkatesan Raman, Lead - IR Center of Excellence, Human Resources

Rebuilt from the author's own draft (Jayasubha_S_SIP_Report.pdf) into the house
format used by the other reports in this repository. Industry and company
figures have been updated to FY 2025-26, the financial year that closed
immediately before the internship began.

Block vocabulary is documented in report_content.py.
"""

STUDENT = 'JAYASUBHA S'
REG_NO = 'OSI2511007'
FIRM = 'Ashok Leyland Limited'
FIRM_SHORT = 'Ashok Leyland'
MENTOR = 'Mr. Venkatesan Raman'
MENTOR_ROLE = 'Lead – IR Center of Excellence, Human Resources'
PERIOD = '9th June 2026 to 31st July 2026'

EMBED_CERTIFICATE = False

# ---------------------------------------------------------------------------
# FRONT MATTER
# ---------------------------------------------------------------------------
FRONT = [
    # ---- title page ----
    ('gap', 2),
    ('big', 'SUMMER INTERNSHIP PROJECT (SIP) – 2026', 16),
    ('gap', 2),
    ('cbi', 'Summer Internship Project Report submitted to the Malaysia '
            'University of Science and Technology, in partial fulfilment of '
            'the requirements to award the degree of', 14),
    ('gap', 2),
    ('cbold', 'MASTER OF BUSINESS ADMINISTRATION', 14),
    ('gap', 2),
    ('center', 'SUBMITTED BY'),
    ('gap', 1),
    ('cbold', STUDENT),
    ('center', REG_NO),
    ('gap', 3),
    ('logo',),
    ('gap', 2),
    ('cbold', 'Indian School of Science and Management', 14),
    ('cbold', 'Chennai', 14),
    ('pagebreak',),

    # ---- certificate ----
    ('gap', 1),
    ('big', 'CERTIFICATE'),
    ('gap', 2),
    ('p', 'This is to certify that the Summer Internship Project Report is an '
          'authentic record of Ms. Jayasubha S (OSI2511007) carried out at '
          'Ashok Leyland Limited in partial fulfilment of the requirements for '
          'the award of the MBA degree.'),
    ('gap', 1),
    ('p', 'The project was completed under the guidance of Mr. Venkatesan '
          'Raman, Lead – IR Center of Excellence, Human Resources, Ashok '
          'Leyland Limited, during the period from June 9th to July 31st, '
          '2026.'),
    ('gap', 4),
    ('p', '**Mrs.Kavitha Manikandan**', 14),
    ('p', 'Academic Head', 14),
    ('p', 'ISSM Business School'),
    ('gap', 2),
    ('p', 'Viva Voce Examination Conducted on:'),
    ('gap', 4),
    ('sign', ('Internal Examiner', 'External Examiner'), True),
    ('pagebreak',),

    # ---- internship certificate ----
    ('gap', 12),
    ('big', 'INTERNSHIP CERTIFICATE', 26),
    *([('gap', 1), ('certificate_image',)] if EMBED_CERTIFICATE else []),
    ('pagebreak',),

    # ---- declaration ----
    ('gap', 6),
    ('big', 'DECLARATION'),
    ('gap', 2),
    ('p', 'I, Ms. Jayasubha S, hereby declare that this SIP Project Report is '
          'based on my eight-week internship done at Ashok Leyland Limited, '
          'Guindy, Chennai, in the Human Resources and Industrial Relations '
          'department, during the period from June 9th to July 31st, 2026, '
          'under the guidance of Mr. Venkatesan Raman, Lead – IR Center of '
          'Excellence, Human Resources, Ashok Leyland Limited and Indian '
          'School of Science and Management, Chennai.'),
    ('gap', 1),
    ('p', 'I further declare that the work presented in this report is my own, '
          'that it has been prepared from the assignments actually handled by '
          'me during the internship, and that it has not been submitted '
          'earlier for the award of any other degree or diploma.'),
    ('gap', 6),
    ('sign', ('Place: Chennai', 'Signature')),
    ('sign', ('Date:', '')),
    ('pagebreak',),

    # ---- acknowledgement ----
    ('gap', 4),
    ('big', 'ACKNOWLEDGEMENT'),
    ('gap', 1),
    ('p', 'I have undergone extensive training to complete this internship. '
          'However, it would not have been possible without the kind support '
          'and help of many individuals. I am using this opportunity to '
          'express my gratitude to everyone who supported me throughout this '
          'internship period.'),
    ('p', 'I would like to express my sincere gratitude to our respected '
          'Chairman, **Mr. KATHIRVEL GANAPATHIAPPAN**, for providing us with '
          'the valuable opportunity to carry out and complete this project.'),
    ('p', 'I express my heartfelt thanks to our visionary, dedicated and '
          'empowering Founder and Managing Director, Dr. PARKAVI MAHALINGAM, '
          'for her continuous support and meaningful guidance, which played a '
          'key role in our progress.'),
    ('p', 'I am highly indebted to our Academic Head, **Mrs. KAVITHA '
          'MANIKANDAN**, for her guidance and constant supervision, for '
          'providing the necessary information regarding the project and for '
          'her support in completing it.'),
    ('p', 'I would also like to thank all the faculty members and staff of '
          'ISSM Business School who provided me with the facilities and the '
          'conducive conditions that were required for this project.'),
    ('p', 'My sincere gratitude to MR. VENKATESAN RAMAN, LEAD – IR CENTER OF '
          'EXCELLENCE, HUMAN RESOURCES, ASHOK LEYLAND LIMITED, for mentoring '
          'me, reviewing my work and offering immense support and knowledge '
          'throughout the internship, and to Ms. Swetha Krishnamurthy, Lead – '
          'Talent Acquisition, and the management of Ashok Leyland Limited for '
          'permitting me to undergo my Summer Internship Programme with the '
          'organisation.'),
    ('p', 'I am also thankful to the members of the Industrial Relations, '
          'recruitment, HR analytics, Learning and Development and corporate '
          'communication teams, who explained their work to me, answered my '
          'questions on statutory and documentation matters, and made it '
          'possible for me to contribute to live reporting, handbook and '
          'communication deliverables.'),
    ('pagebreak',),

    # ---- executive summary ----
    ('gap', 1),
    ('big', 'The Executive Summary', 12),
    ('gap', 1),
    ('p', 'This report presents the work carried out during my Summer '
          'Internship Programme at Ashok Leyland Limited, the flagship '
          'commercial vehicle company of the Hinduja Group and the '
          'second-largest manufacturer of commercial vehicles in India. The '
          'internship was undertaken on-site at the company’s Guindy office in '
          'Chennai from 9 June 2026 to 31 July 2026, a period of eight working '
          'weeks, in the Human Resources and Industrial Relations department, '
          'under the guidance of Mr. Venkatesan Raman, Lead – IR Center of '
          'Excellence, Human Resources.'),
    ('p', 'The internship was located in the part of Human Resources that a '
          'manufacturing company cannot function without. Ashok Leyland '
          'operates a network of plants with a large, substantially unionised '
          'workforce, which makes Industrial Relations a strategic function '
          'rather than an administrative one. Production continuity depends on '
          'workplace harmony, workplace harmony depends on consistent and '
          'procedurally fair treatment, and consistency at that scale depends '
          'on documentation and data. That chain of dependence turned out to '
          'be the organising idea of the whole eight weeks.'),
    ('p', 'The timing of the internship gave it an unusual edge. India’s four '
          'consolidated Labour Codes had come into force on 21 November 2025, '
          'replacing twenty-nine central labour laws, and the final central '
          'rules were published during 2026 (Government of India, as reported '
          'in PwC, 2025; EY, 2026). Ashok Leyland’s own results for FY 2025-26 '
          'carried a one-time charge of about INR 308 crore arising from that '
          'implementation (Economic Times, 2026a). I was therefore working in '
          'an Industrial Relations function at the precise moment when the '
          'statutory ground beneath it had shifted, which is a rare thing for '
          'a student to witness.'),
    ('p', 'The work was organised as eight week-long blocks, each covering a '
          'distinct area of the function and each closing with a deliverable. '
          'Week 1 covered organisational induction and Industrial Relations '
          'fundamentals. Week 2 covered the Recruitment Process Outsourcing '
          'model and the Darwinbox human resource management system. Week 3 '
          'covered HR analytics, in which I prepared the monthly Industrial '
          'Relations Management Information System report and contributed to '
          'an Employee Relations dashboard. Week 4 covered knowledge '
          'management, through an Industrial Relations reference handbook for '
          'new employees and HR professionals.'),
    ('p', 'Week 5 covered internal communication and event coordination, for '
          'which I designed the flyer and agenda for a conference of the '
          'Employers’ Federation of Southern India. Week 6 covered Learning '
          'and Development, through the company’s automated training '
          'dashboard. Weeks 7 and 8 were given to research and presentation: '
          'first on artificial intelligence in leadership and decision making, '
          'and then on current and future trends in industrial and automobile '
          'manufacturing, both delivered to the HR team.'),
    ('p', 'The internship therefore moved between three kinds of work within '
          'the same eight weeks: compliance-sensitive documentation, '
          'quantitative reporting, and communication addressed to audiences '
          'ranging from first-time handbook readers to experienced HR '
          'professionals. It also moved me from observation under close '
          'supervision in the first fortnight to independent research and '
          'delivery by the last, which is a progression I can now describe '
          'precisely rather than in general terms.'),
    ('p', 'Professionally, the internship gave me three things a classroom '
          'cannot. First, an understanding that in Industrial Relations the '
          'document is the practice: a grievance record or an escalation note '
          'is not the paperwork that follows a decision but the thing that '
          'makes the decision defensible. Second, the discipline of data '
          'accuracy, because plant-level figures arrive in inconsistent forms '
          'and a consolidated report is only as trustworthy as the '
          'cross-checking behind it. Third, practical experience of writing '
          'for a defined reader, since a handbook for a new employee, a report '
          'for HR leadership and a conference flyer are three different '
          'disciplines. In summary, the internship converted my MBA coursework '
          'in industrial relations, human resource information systems, HR '
          'analytics, training and development and organisational behaviour '
          'into work I can now perform, and it settled my interest in Human '
          'Resources and Industrial Relations as a career.'),
    ('pagebreak',),

    # ---- table of contents ----
    ('gap', 1),
    ('big', 'TABLE OF CONTENTS'),
    ('gap', 1),
    ('toc',),
]


# ---------------------------------------------------------------------------
# CHAPTER 1
# ---------------------------------------------------------------------------
CH1 = {
    'num': 1,
    'title': 'INDUSTRY AND COMPANY OVERVIEW',
    'header_left': 'CHAPTER 1',
    'header_right': 'INDUSTRY AND COMPANY OVERVIEW',
    'blocks': [
        ('h1', '1. INDUSTRY AND COMPANY OVERVIEW'),

        ('h2', '1.1  GLOBAL AUTOMOTIVE AND COMMERCIAL VEHICLE LANDSCAPE'),
        ('p_indent', 'The global automotive industry, and the commercial vehicle '
                     'segment in particular, is passing through a period of '
                     'substantial transformation driven by electrification, '
                     'digitalisation, tightening emission norms and changing '
                     'customer expectations around total cost of ownership. '
                     'Commercial vehicles, meaning trucks, buses and light '
                     'commercial vehicles, form the backbone of freight '
                     'movement and public transport worldwide. Manufacturers '
                     'are increasingly expected to deliver not merely vehicles '
                     'but complete mobility solutions encompassing financing, '
                     'telematics, fleet management and after-sales support.'),
        ('p', 'Alongside the shift in products, the people-management practices '
              'of large manufacturing organisations are themselves being '
              'reshaped. Human Resource functions in global automotive '
              'companies are moving from transactional administration towards '
              'strategic workforce planning, skills-based hiring, data-driven '
              'employee relations and continuous learning. At the same time '
              'Industrial Relations continues to occupy a central place in '
              'manufacturing-heavy organisations, where large unionised '
              'workforces, shop-floor productivity and statutory compliance '
              'intersect. Effective practice is no longer limited to grievance '
              'handling and wage settlements; it now includes proactive '
              'engagement, structured communication and data-backed monitoring '
              'of workplace harmony.'),
        ('h2', '1.2  THE INDIAN COMMERCIAL VEHICLE AND REGULATORY CONTEXT'),
        ('p', 'India is among the largest commercial vehicle markets in the '
              'world, and the financial year that closed immediately before my '
              'internship was a record one. Commercial vehicle sales rose 12.6 '
              'per cent in FY 2025-26 to an all-time high of about 10,79,871 '
              'units, part of a wider automotive recovery in which total '
              'wholesales reached a record 2.83 crore units, the highest in '
              'seven years, with every vehicle category posting its best ever '
              'annual figure (SIAM, as reported in Economic Times, 2026b; The '
              'Hindu, 2026). A reduction in the goods and services tax rate on '
              'commercial vehicles from 28 per cent to 18 per cent in '
              'September 2025 improved purchase economics and released '
              'deferred replacement demand (Crisil Ratings, as reported in '
              'Economic Times, 2026c).'),
        ('p', 'The outlook moderates from that high base. Crisil Ratings '
              'expects volumes to reach a record 12.4 lakh units in FY 2026-27, '
              'surpassing the previous peak of FY 2018-19, but with growth '
              'easing to about 5 to 6 per cent after the roughly 13 per cent '
              'rebound of the preceding year (Crisil Ratings, as reported in '
              'Economic Times, 2026c). ICRA similarly forecasts 4 to 6 per '
              'cent wholesale growth in FY 2026-27 (ICRA, 2026). Measured by '
              'value, the Indian commercial vehicle market has been estimated '
              'at about USD 55.91 billion in 2026, rising to roughly USD 84.12 '
              'billion by 2034 at a compound annual growth rate near 5 per '
              'cent (IMARC Group, n.d.).'),
        ('p', 'The regulatory position changed fundamentally shortly before my '
              'internship, and this is the single most important piece of '
              'context for the work described in this report. Indian '
              'employer-employee relations had historically been governed by a '
              'dense set of separate statutes, principally the Industrial '
              'Disputes Act, 1947, the Factories Act, 1948 and the Trade '
              'Unions Act, 1926. On 21 November 2025 the Government of India '
              'brought into force four consolidated Labour Codes, namely the '
              'Code on Wages, 2019, the Industrial Relations Code, 2020, the '
              'Code on Social Security, 2020 and the Occupational Safety, '
              'Health and Working Conditions Code, 2020, replacing twenty-nine '
              'central labour laws in a single notification (Government of '
              'India, as reported in PwC, 2025; Economic Times, 2025). The '
              'final central rules under the codes were published during 2026 '
              '(EY, 2026).'),
        ('p', 'The practical consequence for an Industrial Relations team is '
              'considerable. Definitions, thresholds, documentation '
              'requirements and escalation procedures that had been settled '
              'for decades required review, and internal policy templates and '
              'reference material had to be brought into line with the new '
              'framework. The financial consequence was visible in the '
              'company’s own accounts: Ashok Leyland’s FY 2025-26 results '
              'included a one-time charge of approximately INR 308 crore '
              'arising from implementation of the new Labour Code (Economic '
              'Times, 2026a). For a student, the timing was instructive. It '
              'demonstrated that statutory change is not an abstraction '
              'discussed in a labour law paper but an event with a number '
              'attached to it in an audited profit and loss account, and with '
              'consequences that reach every document an Industrial Relations '
              'team produces.'),
        ('h2', '1.3  COMPANY OVERVIEW: ASHOK LEYLAND LIMITED'),
        ('h3', '1.3.1  BACKGROUND AND CORPORATE IDENTITY'),
        ('p', 'Ashok Leyland Limited was originally established as Ashok '
              'Motors in 1948 and renamed Ashok Leyland in 1955 following a '
              'technical collaboration with British Leyland, which gave the '
              'company access to British engineering expertise that shaped its '
              'early truck and bus platforms. It is headquartered at Sardar '
              'Patel Road, Guindy, Chennai, and is the flagship company of the '
              'Hinduja Group. It stands among India’s largest and most '
              'established commercial vehicle manufacturers and is the '
              'second-largest in the country by volume (Ashok Leyland Limited, '
              'n.d.).'),
        ('p', 'The company’s product portfolio spans heavy, medium and light '
              'commercial vehicles, buses including electric buses under the '
              'Switch Mobility brand, defence and military vehicles, engines '
              'and power solutions. It is also among the largest suppliers of '
              'mobility and logistics vehicles to the Indian Army, which '
              'reflects both its engineering depth and a long-standing '
              'institutional relationship. Vehicle financing is offered '
              'through Hinduja Leyland Finance, allowing the group to support '
              'customers across the ownership lifecycle. The company is '
              'chaired by Mr. Dheeraj G. Hinduja, with Mr. Shenu Agarwal '
              'serving as Managing Director and Chief Executive Officer.'),
        ('p', 'Financially, the year immediately preceding my internship was '
              'the company’s strongest on record and its fourth consecutive '
              'year of growth in both revenue and profit. Standalone revenue '
              'from operations for FY 2025-26 was INR 44,007 crore, an '
              'increase of 14 per cent over INR 38,753 crore in the previous '
              'year, with consolidated revenue of INR 56,362 crore. Profit '
              'after tax rose 8 per cent to INR 3,566 crore, and operating '
              'profit before tax rose 22 per cent to INR 5,163 crore, despite '
              'the one-time Labour Code charge of about INR 308 crore noted '
              'earlier (Economic Times, 2026a; Business World, 2026). The '
              'fourth quarter produced the highest quarterly profit in the '
              'company’s history (Livemint, 2026).'),
        ('p', 'Sustained financial strength of this kind matters directly to an '
              'HR intern, and not only as background. It is what funds the '
              'HR technology upgrades, the structured Learning and Development '
              'programmes and the employee engagement initiatives that I was '
              'able to observe. A company under financial pressure does not '
              'ordinarily invest in automated training dashboards or in '
              'modernising its human resource management system, and much of '
              'what made this internship instructive existed because the '
              'company could afford it.'),

        ('h3', '1.3.2  PRODUCTS, SEGMENTS AND MANUFACTURING FOOTPRINT'),
        ('p', 'The company reports a manufacturing footprint of nine plants, '
              'seven of them in India together with a bus manufacturing '
              'facility at Ras Al Khaimah in the United Arab Emirates and a '
              'facility at Leeds in the United Kingdom, alongside a joint '
              'venture with the Alteams Group for high-pressure die-cast '
              'aluminium components (Ashok Leyland Limited, n.d.). The Indian '
              'plants include Ennore, Hosur, Bhandara, Vijayawada, Alwar and '
              'Pantnagar. The table below summarises the principal business '
              'segments.'),
        ('table', {'rows': [
            ['Segment', 'Description', 'Relevance to the HR and IR Function'],
            ['Trucks',
             'Haulage vehicles, tippers and tractor-trailers for logistics, '
             'mining and construction, from light to heavy duty',
             'The core volume business, and the principal driver of shop-floor '
             'shift planning and manpower deployment'],
            ['Buses',
             'City buses, intercity coaches and school buses; the company '
             'pioneered India’s first double-decker bus',
             'Body-building work is labour-intensive, making workforce '
             'scheduling and safety compliance central'],
            ['Light commercial vehicles',
             'The Dost, Bada Dost, Partner and MiTR range for small business '
             'and last-mile logistics',
             'Higher-volume, faster-cycle assembly with its own productivity '
             'and staffing patterns'],
            ['Defence and military vehicles',
             'A major supplier to the Indian Army and allied establishments',
             'Security, vetting and confidentiality obligations shape HR '
             'process in this segment'],
            ['Electric and alternative fuel',
             'Electric buses and light vehicles under Switch Mobility, with '
             'CNG and LNG trucks',
             'Creates demand for reskilling in electric powertrains, battery '
             'systems and vehicle software'],
            ['Power solutions and engines',
             'Diesel and alternative-fuel engines for automotive and '
             'industrial use, including gensets and marine engines',
             'A distinct technical workforce with its own training and '
             'certification requirements'],
            ['Financial services',
             'Vehicle financing through Hinduja Leyland Finance',
             'A white-collar workforce whose HR practices differ markedly from '
             'the manufacturing plants'],
        ], 'widths': [3, 5, 4], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),
        ('p', 'The multi-plant structure is the main reason Industrial '
              'Relations occupies such a strategically important place within '
              'the company. Each plant maintains its own local workforce, '
              'union dynamics and production rhythm, while corporate HR '
              'remains responsible for consistency in policy application, '
              'statutory compliance and reporting standards across all of '
              'them. Centrally designed systems, including the Darwinbox '
              'platform and the Industrial Relations reporting framework I '
              'worked on, are what give corporate leadership a consolidated '
              'and comparable view of workforce indicators across locations '
              'that are otherwise geographically and culturally distinct.'),

        ('h2', '1.4  STRATEGIC FOCUS AND THE HR FUNCTION'),
        ('h3', '1.4.1  STRATEGIC DIRECTION AND RECENT INITIATIVES'),
        ('p', 'The company’s stated ambition is to become one of the world’s '
              'leading commercial vehicle manufacturers by responding actively '
              'to electrification, alternative fuel adoption, digitalisation '
              'of fleet management and shifting global trade patterns. The '
              'principal initiatives visible during my internship were the '
              'following.'),
        ('bullets', [
            '**Electrification and alternative fuels:** continued expansion of '
            'the electric bus portfolio under Switch Mobility, with active '
            'work on liquefied natural gas and hydrogen-powered commercial '
            'vehicles.',
            '**Export market deepening:** a strategic focus on the Middle '
            'East, Africa and the ASEAN region, supported by regional '
            'manufacturing and supply-chain arrangements.',
            '**Technology partnerships:** collaboration with global technology '
            'firms in vehicle electronics and with the Alteams Group in '
            'precision components, reflecting a push towards advanced '
            'engineering capability.',
            '**Digital HR transformation:** continuing investment in the '
            'Darwinbox human resource management system and in structured '
            'Recruitment Process Outsourcing partnerships, so that recruitment '
            'and workforce administration can scale across a multi-plant '
            'organisation.',
            '**Financial discipline:** four consecutive years of growth in '
            'revenue and profit, culminating in record FY 2025-26 results and '
            'a second interim dividend for the year (Economic Times, 2026a).',
        ]),
        ('h3', '1.4.2  THE HR AND INDUSTRIAL RELATIONS FUNCTION'),
        ('p', 'Given the scale of its manufacturing operations, the company’s '
              'HR function is organised to address two distinct domains. The '
              'first is corporate and managerial HR, covering recruitment, '
              'administration of the human resource management system, '
              'learning and development, HR analytics and internal '
              'communication. The second is plant-level Industrial Relations, '
              'covering union engagement, grievance redressal, compliance with '
              'labour statutes, wage settlements and workplace harmony '
              'initiatives. The Industrial Relations team works closely with '
              'plant leadership and employee representative bodies to sustain '
              'productive shop-floor relationships, while corporate HR '
              'concentrates on employer branding, digital platforms and '
              'organisation-wide people analytics.'),
        ('p', 'My internship gave exposure to both domains, and the contrast '
              'between them was itself part of the education. The corporate '
              'side was technology-enabled and analytical, working through the '
              'Darwinbox platform, Recruitment Process Outsourcing '
              'arrangements and management reporting. The Industrial Relations '
              'side was documentation-intensive and communication-intensive, '
              'working through the monthly reporting pack, the reference '
              'handbook and internal communication for events such as the '
              'conference of the Employers’ Federation of Southern India. The '
              'two are frequently taught as separate subjects and are in '
              'practice a single function.'),
        ('h3', '1.4.3  ORGANISATIONAL CULTURE AND EMPLOYEE VALUE PROPOSITION'),
        ('p', 'The workplace culture reflects the identity of a heritage '
              'engineering organisation that is actively modernising. A strong '
              'emphasis on safety, discipline and process rigour on the shop '
              'floor, which is essential in heavy manufacturing, sits '
              'alongside an increasingly employee-centric approach in the '
              'corporate functions, expressed through self-service HR delivery '
              'on the Darwinbox portal, structured induction for new joiners '
              'and visible leadership communication at company-wide events.'),
        ('p', 'The organisation also places considerable emphasis on driver '
              'training and community skill-building through its long-running '
              'driver training programme, which extends its skills agenda well '
              'beyond its own payroll and connects to its road safety and '
              'livelihood commitments. Internally, cross-functional exposure '
              'is encouraged, and interns and new employees are given '
              'structured opportunities to move across HR sub-functions. The '
              'design of my own internship, which moved sequentially through '
              'induction, recruitment, analytics, documentation, '
              'communication, learning and development, and strategic '
              'research, is itself an illustration of that practice.'),
        ('p', 'Employer branding matters increasingly in this sector, because '
              'competition for engineering and HR talent has intensified. A '
              'credible employer brand supports recruitment conducted through '
              'external partners and also supports retention, since employees '
              'are more likely to stay engaged where external reputation '
              'matches internal experience. The company’s participation in '
              'industry platforms such as the Employers’ Federation of '
              'Southern India, its driver training initiatives and its visible '
              'investment in HR technology together produce an employer brand '
              'that balances engineering heritage with a forward-looking '
              'workplace. Designing communication material for the federation '
              'conference gave me a direct view of how such activity is '
              'planned and executed at working level.'),
        ('h2', '1.5  SWOT ANALYSIS'),
        ('p', 'The following analysis is based on what was observable to me '
              'during an eight-week internship in the HR and Industrial '
              'Relations function, read together with publicly available '
              'information about the company and its sector. It is offered as '
              'a student’s assessment rather than an internal strategic '
              'review.'),

        ('h3', '1.5.1  STRENGTHS'),
        ('bullets', [
            '**Market position:** second-largest commercial vehicle '
            'manufacturer in India, with a diversified portfolio spanning '
            'trucks, buses, light commercial vehicles and defence mobility.',
            '**Group parentage:** the backing of the Hinduja Group provides '
            'financial stability, global reach and access to expertise across '
            'sectors.',
            '**Defence franchise:** a position among the largest suppliers of '
            'mobility solutions to the Indian Army provides a stable, '
            'high-value business segment that is less exposed to the civilian '
            'demand cycle.',
            '**Distribution, service and training network:** an established '
            'pan-India dealer and service network, together with a substantial '
            'driver training programme, strengthens customer relationships and '
            'brand loyalty.',
            '**Progressive HR technology adoption:** implementation of the '
            'Darwinbox platform and structured Recruitment Process Outsourcing '
            'partnerships reflects a forward-looking approach to workforce '
            'administration.',
        ]),

        ('h3', '1.5.2  WEAKNESSES'),
        ('bullets', [
            '**Cyclicality:** revenues remain closely tied to the domestic '
            'replacement and infrastructure cycle, which exposes the company '
            'to periodic demand slowdowns and complicates workforce planning.',
            '**Industrial Relations complexity:** a large, multi-plant, '
            'substantially unionised workforce increases the administrative '
            'and relational effort required to maintain industrial harmony.',
            '**Pace of electric transition:** relative to some global peers, '
            'the shift of the core commercial vehicle portfolio to electric '
            'and alternative-fuel platforms is still maturing.',
            '**Coordination overhead across plants:** local reporting habits '
            'differ between plants, which means consolidated reporting '
            'requires standardisation effort before it becomes reliable.',
            '**Dependence on statutory interpretation:** a compliance-heavy '
            'function carries the risk that a change in law requires '
            'simultaneous revision of policy, documentation and training '
            'across every location.',
        ]),

        ('h3', '1.5.3  OPPORTUNITIES'),
        ('bullets', [
            '**Record demand conditions:** commercial vehicle volumes reached '
            'an all-time high of about 10.8 lakh units in FY 2025-26 and are '
            'projected to rise further to roughly 12.4 lakh units in FY '
            '2026-27 (SIAM, as reported in Economic Times, 2026b; Crisil '
            'Ratings, as reported in Economic Times, 2026c).',
            '**Export market expansion:** growth potential in the Middle East, '
            'Africa and the ASEAN region through regional manufacturing '
            'partnerships.',
            '**Electrification and alternative fuels:** rising policy and '
            'customer emphasis on electric, liquefied natural gas and '
            'hydrogen-powered vehicles opens new product and skill areas.',
            '**HR analytics and digital transformation:** continued investment '
            'in the human resource management system and in dashboard-based '
            'reporting can further improve workforce planning, engagement and '
            'compliance monitoring.',
            '**Infrastructure-led demand:** sustained public investment in '
            'roads, logistics parks and public transport supports medium-term '
            'demand for commercial vehicles.',
        ]),

        ('h3', '1.5.4  THREATS'),
        ('bullets', [
            '**Intensifying competition:** sustained competitive pressure from '
            'Tata Motors, Mahindra and Mahindra, VE Commercial Vehicles and '
            'Daimler India Commercial Vehicles.',
            '**Regulatory change:** the four Labour Codes that came into force '
            'in November 2025, together with evolving emission and safety '
            'regulation, require continuous adaptation of both operations and '
            'HR process (Government of India, as reported in PwC, 2025).',
            '**Competition for newer skills:** rising demand for electric '
            'vehicle, data analytics and software talent across the automotive '
            'sector intensifies competition for a scarce pool.',
            '**Moderating growth outlook:** after the strong rebound of FY '
            '2025-26, industry growth is expected to ease to 4 to 6 per cent, '
            'which tightens the link between cost discipline and workforce '
            'planning (ICRA, 2026).',
            '**Macroeconomic sensitivity:** interest rate movements, fuel '
            'price volatility and freight rate fluctuations can all dampen '
            'commercial vehicle purchase decisions.',
        ]),

        ('h2', '1.6  KEY COMPETITORS'),
        ('p', 'The company competes across several distinct fronts, and the '
              'competitive set differs by segment. The tables below summarise '
              'the principal competitors in each group, together with the '
              'competitive effect of each.'),

        ('h3', '1.6.1  DIVERSIFIED DOMESTIC MANUFACTURERS'),
        ('table', {'rows': [
            ['Company', 'Core Segment', 'Competitive Effect'],
            ['Tata Motors', 'Commercial and passenger vehicles',
             'The largest domestic rival, with scale advantages across both '
             'vehicle types and an aggressive electric push; its research '
             'spending is spread across a wider portfolio than Ashok '
             'Leyland’s more focused commercial and defence specialisation'],
            ['Mahindra and Mahindra',
             'Light commercial vehicles, tractors and utility vehicles',
             'Competes chiefly in light commercial and rural mobility, drawing '
             'on tractor and utility strength to serve small-business and '
             'agricultural logistics adjacent to the core medium and heavy '
             'segment'],
        ], 'widths': [3, 4, 5], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),

        ('h3', '1.6.2  TECHNOLOGY-LED AND JOINT VENTURE COMPETITORS'),
        ('table', {'rows': [
            ['Company', 'Core Segment', 'Competitive Effect'],
            ['VE Commercial Vehicles',
             'Trucks and buses, as an Eicher and Volvo joint venture',
             'Competes in the premium, fuel-efficient heavy truck segment by '
             'drawing on Volvo global engineering standards'],
            ['Daimler India Commercial Vehicles',
             'Trucks under the BharatBenz brand',
             'Targets the technology-forward segment of the domestic and '
             'export truck market, positioning on build quality and total cost '
             'of ownership'],
        ], 'widths': [3, 4, 5], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),

        ('h3', '1.6.3  NICHE AND REGIONAL COMPETITORS'),
        ('table', {'rows': [
            ['Company', 'Core Segment', 'Competitive Effect'],
            ['SML Isuzu', 'Light commercial vehicles and buses',
             'Occupies a specialised niche in light commercial vehicles and '
             'school buses, competing on relationship-driven regional sales '
             'rather than on scale'],
            ['Regional body builders and assemblers',
             'Bus bodies and specialised vehicle applications',
             'Compete on price and local responsiveness in specific '
             'geographies, particularly in bus body-building work'],
        ], 'widths': [3, 4, 5], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),

        ('h2', '1.7  COMPETITIVE POSITIONING'),
        ('p', 'Ashok Leyland’s competitive positioning rests on a combination '
              'of engineering depth, an extensive service and driver training '
              'network, a diversified base spanning civilian and defence '
              'mobility, and the financial and strategic backing of the '
              'Hinduja Group. Unlike smaller regional players, it is able to '
              'invest simultaneously in electrification, alternative fuels and '
              'digital HR transformation, which allows it to modernise its '
              'workforce practices at the same time as its products. Against '
              'Tata Motors, which enjoys scale across both passenger and '
              'commercial vehicles, it differentiates through deeper '
              'specialisation in medium and heavy commercial vehicles and a '
              'distinctive defence franchise. Against VE Commercial Vehicles '
              'and Daimler India, which lean on foreign technology '
              'partnerships for premium positioning, it leverages a long '
              'domestic manufacturing heritage, cost-competitive engineering '
              'and a distribution network built over more than seven decades.'),
        ('p', 'Large commercial vehicle manufacturers face a set of '
              'people-management challenges that purely white-collar '
              'organisations do not. Manufacturing requires careful shift '
              'planning, adherence to statutory working-hour limits and '
              'continuous engagement with employee representative bodies to '
              'prevent disruption to production. Seasonal and cyclical demand '
              'creates workforce-planning difficulty, since HR teams must '
              'balance permanent, contractual and temporary staffing in a way '
              'that is both compliant and cost-effective. The shift towards '
              'electrification and connected-vehicle technology adds a further '
              'requirement, because established diesel-engine expertise must '
              'now be supplemented with knowledge of electric powertrains, '
              'battery systems and vehicle software.'),
        ('p', 'For an HR intern this environment offered a valuable vantage '
              'point. I was able to watch a large, engineering-led '
              'organisation balance the discipline required for statutory '
              'Industrial Relations compliance against the innovation required '
              'to modernise recruitment, analytics and learning systems for a '
              'workforce spread across plants and functions. The tension '
              'between those two demands, rather than either one on its own, '
              'is what the function actually manages.'),

        ('h2', '1.8  KEY MILESTONES'),
        ('p', 'The company’s history provides context for the culture observed '
              'during the internship. The milestones below are drawn from '
              'publicly available company and press sources.'),
        ('bullets', [
            '**1948, foundation:** established as Ashok Motors in Chennai, '
            'initially to assemble vehicles for the Indian market.',
            '**1955, formation of Ashok Leyland:** renamed following a '
            'technical collaboration with British Leyland, gaining engineering '
            'expertise that shaped its early truck and bus platforms.',
            '**1987 onward, international expansion:** commercial presence '
            'extended beyond India, laying the groundwork for what is today a '
            'multi-country manufacturing and distribution footprint.',
            '**2000s onward, product diversification:** expansion into light '
            'commercial vehicles through the Dost range, deepening of the '
            'defence mobility business and growth of the power solutions and '
            'engines division.',
            '**2017 onward, digital and electric transformation:** '
            'accelerated investment in electric mobility through Switch '
            'Mobility, alongside modernisation of internal HR and operational '
            'systems, which produced the technology-enabled HR environment '
            'observed during this internship.',
            '**November 2025, statutory transition:** India’s four '
            'consolidated Labour Codes came into force, replacing twenty-nine '
            'central labour laws and requiring a review of Industrial '
            'Relations policy and documentation across the organisation '
            '(Government of India, as reported in PwC, 2025).',
            '**FY 2025-26, record performance:** revenue of INR 44,007 crore '
            'and profit after tax of INR 3,566 crore, a fourth consecutive '
            'year of growth, achieved despite a one-time Labour Code charge of '
            'about INR 308 crore (Economic Times, 2026a).',
        ]),
        ('p', 'The last two milestones are the ones that framed my internship, '
              'and they pull in opposite directions in a way I found '
              'instructive. The company was performing at its historical best '
              'while simultaneously absorbing the largest change to Indian '
              'labour law since independence. That combination explains why an '
              'intern in the Industrial Relations function in mid-2026 was '
              'given documentation and reporting work rather than peripheral '
              'tasks: the function had a genuine need for reference material '
              'and management visibility at exactly that moment.'),
        ('p', 'For a student of management, the lesson in a company at this '
              'stage of its life is that stability and change are not '
              'opposites. An organisation seventy-eight years old was, during '
              'the eight weeks I spent there, rewriting the documents that '
              'govern its relationship with its own workforce. The heritage '
              'was what made the change manageable, and the documentation '
              'discipline built over decades was what made it possible to '
              'revise policy without losing consistency.'),
    ],
}


# ---------------------------------------------------------------------------
# CHAPTER 2
# ---------------------------------------------------------------------------
CH2 = {
    'num': 2,
    'title': 'JOB / TASK DESCRIPTION',
    'header_left': 'CHAPTER 2',
    'header_right': 'JOB / TASK DESCRIPTION',
    'blocks': [
        ('h1', '2. JOB / TASK DESCRIPTION'),

        ('h2', '2.1  OBJECTIVES OF THE INTERNSHIP'),
        ('p_indent', 'The purpose of the internship was to bridge the gap '
                     'between classroom learning in Human Resource Management, '
                     'Organisational Behaviour and Industrial Relations and the '
                     'practical functioning of the HR and Industrial Relations '
                     'department of a large, substantially unionised '
                     'manufacturing organisation. The internship was carried '
                     'out at Ashok Leyland Limited, Guindy, Chennai, from 9 '
                     'June 2026 to 31 July 2026, a period of eight working '
                     'weeks, under the guidance of Mr. Venkatesan Raman, Lead – '
                     'IR Center of Excellence, Human Resources.'),
        ('p', 'The internship was structured to provide exposure across the '
              'breadth of the function rather than depth in any single part of '
              'it: organisational induction, HR technology, HR analytics and '
              'reporting, Industrial Relations documentation, internal '
              'communication and event coordination, Learning and Development '
              'systems, and contemporary themes such as artificial '
              'intelligence in leadership. The specific objectives were the '
              'following.'),
        ('bullets', [
            'To understand Ashok Leyland’s organisational structure and the '
            'fundamentals of Industrial Relations in a manufacturing '
            'environment.',
            'To gain practical exposure to HR technology, including the '
            'Recruitment Process Outsourcing model and the Darwinbox human '
            'resource management system.',
            'To develop HR analytics and reporting skill through preparation of '
            'the Industrial Relations Management Information System report and '
            'an Employee Relations dashboard.',
            'To contribute to Industrial Relations knowledge management through '
            'a reference handbook for new employees and HR professionals.',
            'To build HR communication and event-coordination capability '
            'through the conference materials for the Employers’ Federation of '
            'Southern India.',
            'To explore Learning and Development systems and understand how '
            'automated training dashboards support capability building.',
            'To strengthen research, synthesis and presentation skill through '
            'two structured presentations delivered to the HR team.',
            'To develop the professional habits the function depends on: '
            'accuracy, discretion, version discipline and proactive '
            'communication of dependencies.',
        ]),
        ('p', 'It is worth stating what the scope was not. As an eight-week '
              'internship, my involvement in any single sub-function was '
              'necessarily shallower than that of a permanent team member, and '
              'this report does not claim otherwise. Exposure to live, '
              'high-stakes Industrial Relations situations was observational '
              'rather than participative, and access to certain systems and '
              'historical data was restricted under the organisation’s data '
              'governance policies. Where this report describes a deliverable, '
              'it describes my actual contribution to it rather than sole '
              'ownership of it.'),

        ('h3', '2.1.1  METHODOLOGY AND APPROACH'),
        ('p', 'The internship was structured as a task-based, week-wise '
              'programme in which each week concentrated on a distinct '
              'functional area and closed with a tangible deliverable. Work was '
              'carried out under the guidance of the HR and Industrial '
              'Relations team, combining observation in the early weeks with '
              'increasing hands-on participation and independent contribution '
              'as the internship progressed.'),
        ('p', 'A typical task followed a consistent sequence: understand the '
              'objective and the intended reader or user of the output; '
              'identify and gather the information required; check that '
              'information against a second source wherever one existed; '
              'prepare the deliverable in the format the team expected; submit '
              'it for review; and incorporate the feedback received before '
              'finalising. The review step was never optional. In a '
              'compliance-sensitive function an intern’s draft is not a '
              'finished document, and treating review as part of the task '
              'rather than as an obstacle to it was among the earliest things '
              'I learned.'),

        ('h2', '2.2  INITIAL ONBOARDING AND ORGANISATIONAL INDUCTION'),
        ('p', 'The internship opened with a structured induction designed to '
              'familiarise me with the organisation before I was asked to '
              'produce anything. This covered the company’s history, products '
              'and manufacturing footprint, its position as the flagship '
              'company of the Hinduja Group, and the core functions of the HR '
              'and Industrial Relations department. Understanding the business '
              'had to come first, because Industrial Relations documentation '
              'cannot be drafted sensibly by someone who does not understand '
              'what happens on the shop floor it governs.'),
        ('bullets', [
            'Introduction to the company’s history, product range and '
            'multi-plant manufacturing footprint.',
            'An overview of the HR department’s structure and reporting lines, '
            'and of its coordination with plant-level Industrial Relations '
            'teams.',
            'Orientation on workplace policies, the code of conduct and the '
            'importance of confidentiality in handling employee data.',
            'Guided walkthroughs of how Industrial Relations activities are '
            'documented and escalated within the organisation.',
            'Study of the organisation chart of the HR and Industrial Relations '
            'department, including the relationship between plant-level '
            'officers and the corporate team.',
            'Briefings on workplace safety norms, which in a manufacturing '
            'organisation are treated as an HR concern and not solely an '
            'operational one.',
            'An introduction to the statutory framework, including the position '
            'following the coming into force of the four Labour Codes in '
            'November 2025.',
        ]),
        ('h2', '2.3  WORK PLAN AND SCOPE'),
        ('p', 'The work fell into eight areas, one for each week of the '
              'internship. The descriptions below set out the nature of my '
              'involvement and the learning focus of each.'),

        ('h3', '2.3.1  Industrial Relations Fundamentals and Documentation'),
        ('p', 'The first area covered the fundamentals of Industrial Relations '
              'and the documentation that supports them. I assisted with '
              'routine activities including the filing and updating of records, '
              'and observed how the team engages with employee representatives '
              'on the shop floor. The central insight was that documentation '
              'is not clerical work in this function. A grievance record is the '
              'evidence that a matter was handled consistently, and its '
              'completeness is what allows a decision to be defended later.'),
        ('bullets', [
            'Assisted with the filing and updating of Industrial Relations '
            'records under supervision.',
            'Observed a routine case-file review, gaining a first-hand sense of '
            'how documentation supports fair and consistent resolution of '
            'workplace issues.',
            'Studied the reporting relationship between plant-level officers '
            'and the corporate HR team.',
            'Began building a personal glossary of Industrial Relations and '
            'labour-law terminology, which proved essential in the weeks that '
            'followed.',
        ]),

        ('h3', '2.3.2  Recruitment Process Outsourcing and HR Technology'),
        ('p', 'The second area covered how the organisation recruits and the '
              'platform on which it administers its workforce. I observed the '
              'Recruitment Process Outsourcing model, including how external '
              'partners are briefed, how candidate pipelines are managed and '
              'how quality and turnaround-time metrics are tracked, and gained '
              'hands-on exposure to the Darwinbox human resource management '
              'system, covering employee records, onboarding workflows and '
              'self-service features.'),
        ('bullets', [
            'Reviewed sample job requisitions and understood how role profiles '
            'are translated into sourcing briefs for external partners.',
            'Navigated the employee-record module to understand how master data '
            'such as designation, grade and plant location is structured and '
            'maintained.',
            'Observed how onboarding checklists are triggered automatically '
            'once an offer is accepted, reducing manual coordination between HR '
            'and the IT and administration teams.',
            'Understood how service-level agreements and periodic reviews allow '
            'the organisation to outsource recruitment activity while retaining '
            'control of quality and candidate experience.',
        ]),

        ('h3', '2.3.3  HR Analytics and MIS Reporting'),
        ('p', 'The third area was the most analytical of the internship. I '
              'prepared the monthly Industrial Relations Management Information '
              'System report, consolidating data on attendance, grievances, '
              'disciplinary matters and union engagement across plants, and '
              'contributed to the development of a data-driven Employee '
              'Relations dashboard intended to give HR leadership visibility of '
              'workforce sentiment and Industrial Relations trends.'),
        ('p', 'The reporting pack was structured to give leadership a concise, '
              'plant-wise view of the indicators that matter. Its sections '
              'were as follows.'),
        ('bullets', [
            '**Attendance summary:** plant-wise attendance percentage, '
            'absenteeism trends and overtime hours for the reporting month.',
            '**Grievance tracker:** grievances raised, resolved and pending, '
            'categorised by type and by plant.',
            '**Disciplinary matters:** a summary of ongoing and closed cases, '
            'with resolution timelines.',
            '**Union engagement log:** a record of formal and informal '
            'engagement with employee representative bodies.',
            '**Key observations:** narrative highlights and emerging themes '
            'flagged for leadership attention.',
        ]),
        ('h3', '2.3.4  Industrial Relations Knowledge Management'),
        ('p', 'The fourth area was knowledge management. I contributed to '
              'preparing an Industrial Relations reference handbook for new '
              'employees and HR professionals, consolidating key policies, '
              'escalation procedures, statutory obligations and frequently '
              'asked questions into a single accessible document. The need for '
              'such a document was sharpened by the statutory transition of '
              'November 2025, since scattered references to superseded statutes '
              'are worse than no reference at all.'),
        ('bullets', [
            'Reviewed existing policy documents and past case notes to identify '
            'the questions most commonly asked, for inclusion in the handbook.',
            'Drafted sections explaining grievance escalation procedures and '
            'the roles of the various stakeholders in the process.',
            'Incorporated review feedback from senior HR staff to simplify '
            'language and improve readability for first-time users.',
            'Maintained version control across drafts so that the revision '
            'history of a compliance-relevant document remained auditable.',
        ]),
        ('p', 'Writing for a broad, non-expert reader proved to be a different '
              'skill from writing an internal note, and a harder one. The '
              'handbook had to be accurate enough to be relied upon and plain '
              'enough to be read by someone encountering the subject for the '
              'first time, and those two requirements pull against each other '
              'on almost every sentence.'),

        ('h3', '2.3.5  HR Communication and Event Coordination'),
        ('p', 'The fifth area moved from documentation to communication. I '
              'designed the flyer and agenda for a conference of the '
              'Employers’ Federation of Southern India, coordinating with '
              'internal stakeholders to finalise content, session sequencing '
              'and branding, and supporting internal communication ahead of '
              'the event. The federation is a century-old Chennai-based body '
              'representing employer interests across southern India, with '
              'several hundred member organisations and representation on state '
              'and central tripartite committees, which makes participation in '
              'its platforms a matter of industry standing as well as of '
              'professional exchange.'),
        ('bullets', [
            'Drafted several design concepts for the conference flyer and '
            'incorporated feedback from the corporate communications team.',
            'Structured the agenda in consultation with session owners to '
            'ensure logical sequencing and appropriate time allocation, '
            'balancing keynote sessions with panel discussions.',
            'Presented the event title, theme, date, venue and registration '
            'details prominently, since logistical clarity is the first '
            'function of such material.',
            'Prepared brief speaker introductions to build credibility and '
            'audience interest ahead of the event.',
            'Coordinated logistics-related communication, including invitee '
            'lists and confirmation follow-ups.',
        ]),
        ('p', 'The week was a lesson in how much planning sits behind something '
              'that looks, from outside, like a single page. Sequencing '
              'sessions is a negotiation with the people who own them, and the '
              'flyer is the last and most visible product of a long chain of '
              'internal agreement.'),

        ('h3', '2.3.6  Learning and Development Systems'),
        ('p', 'The sixth area covered capability building. I explored the '
              'automated Learning and Development dashboard used to track '
              'training nominations, completions and effectiveness scores '
              'across the organisation, and reviewed how training needs are '
              'identified and mapped to competency frameworks. The dashboard '
              'views were organised as follows.'),
        ('bullets', [
            '**Nomination against completion:** the proportion of nominated '
            'employees completing assigned training within the target window.',
            '**Department-wise training hours:** average training hours per '
            'employee by department, supporting resource-planning decisions.',
            '**Feedback score trends:** post-training ratings tracked over time '
            'to flag programmes needing redesign.',
            '**Mandatory compliance training status:** completion status for '
            'statutory and safety-related modules, where the consequence of a '
            'gap is a compliance exposure rather than a capability one.',
        ]),
        ('h3', '2.3.7  Research and Presentation on AI in Leadership'),
        ('p', 'The seventh area shifted from operational support to research. I '
              'conducted secondary research and delivered a presentation titled '
              '"AI in Leadership and Decision Making" to the HR team, covering '
              'how artificial intelligence tools are being applied to talent '
              'analytics, sentiment analysis and decision support in '
              'contemporary HR functions.'),
        ('bullets', [
            'Researched examples of artificial intelligence applied to talent '
            'analytics, workforce sentiment analysis and predictive attrition '
            'modelling.',
            'Structured the presentation to connect global trends with '
            'practical implications for the organisation’s own HR technology '
            'direction.',
            'Framed artificial intelligence as a decision-support tool rather '
            'than a replacement for human judgement, a framing refined in '
            'response to questions from the HR team.',
            'Prepared for questions from an audience considerably more '
            'experienced than myself, which required knowing the limits of my '
            'own material.',
        ]),

        ('h3', '2.3.8  Research and Presentation on Industry Trends'),
        ('p', 'The eighth area closed the internship. I prepared and delivered '
              'a presentation titled "Current and Future Trends in Industrial '
              'and Automobile Manufacturing", covering electrification, '
              'automation, digital transformation and workforce evolution, and '
              'consolidated my learning from the eight weeks for a closing '
              'discussion with the HR team.'),
        ('bullets', [
            'Researched electrification, alternative fuels, shop-floor '
            'automation and connected-vehicle technology as they affect '
            'commercial vehicle manufacturing.',
            'Linked those trends to their implications for future workforce '
            'skilling and HR strategy at the organisation.',
            'Applied the structuring and delivery feedback received after the '
            'previous week’s presentation, which measurably improved this one.',
            'Presented a closing summary of internship learning and received '
            'structured feedback from the HR and Industrial Relations team.',
        ]),

        ('h2', '2.4  TIMELINE OF ACTIVITIES'),
        ('p', 'The internship ran for eight working weeks from 9 June 2026 to '
              '31 July 2026, the dates recorded on the internship certificate. '
              'Because 9 June fell on a Tuesday, the first week was a short '
              'one and the remaining seven ran from Monday to Friday, with the '
              'programme closing on Friday 31 July. The week-by-week record '
              'below follows that calendar.'),

        ('h3', 'Week 1 (9 June – 12 June 2026): Induction and IR Fundamentals'),
        ('bullets', [
            'Attended the induction programme covering company history, '
            'structure and manufacturing operations.',
            'Assisted with routine Industrial Relations activities and record '
            'documentation.',
            'Observed how the Industrial Relations team engages with employee '
            'representatives on the shop floor.',
            'Began compiling terminology notes, having found the labour-law '
            'vocabulary unfamiliar at first encounter.',
        ]),

        ('h3', 'Week 2 (15 June – 19 June 2026): Recruitment and HR Technology'),
        ('bullets', [
            'Observed the Recruitment Process Outsourcing model, including '
            'partner briefing and pipeline management.',
            'Gained hands-on exposure to the Darwinbox platform across '
            'employee records, onboarding workflows and self-service features.',
            'Reviewed sample requisitions and the translation of role profiles '
            'into sourcing briefs.',
            'Traced the recruitment lifecycle end to end, from requisition '
            'through to onboarding.',
        ]),

        ('h3', 'Week 3 (22 June – 26 June 2026): HR Analytics and MIS'),
        ('bullets', [
            'Collected and cleaned raw attendance and grievance data from '
            'several plant-level sources.',
            'Prepared the monthly Industrial Relations Management Information '
            'System report consolidating attendance, grievances, disciplinary '
            'matters and union engagement.',
            'Built summary tables and charts showing month-on-month movement in '
            'case volumes.',
            'Contributed to the design of the Employee Relations dashboard in '
            'discussion with the analytics lead.',
        ]),

        ('h3', 'Week 4 (29 June – 3 July 2026): IR Documentation'),
        ('bullets', [
            'Reviewed existing policy documents and past case notes to identify '
            'content for the reference handbook.',
            'Drafted handbook sections on grievance escalation procedures and '
            'stakeholder roles.',
            'Simplified language following review feedback from senior HR '
            'staff.',
            'Maintained dated version labels across drafts to preserve an '
            'auditable revision trail.',
        ]),

        ('h3', 'Week 5 (6 July – 10 July 2026): HR Communication and Events'),
        ('bullets', [
            'Designed the flyer for the conference of the Employers’ Federation '
            'of Southern India through several concept iterations.',
            'Structured the conference agenda in consultation with session '
            'owners.',
            'Coordinated invitee lists and confirmation follow-ups.',
            'Balanced this project against continuing reporting '
            'responsibilities, which made the week the most demanding of the '
            'eight for time management.',
        ]),

        ('h3', 'Week 6 (13 July – 17 July 2026): Learning and Development'),
        ('bullets', [
            'Explored the automated Learning and Development dashboard covering '
            'nominations, completions and effectiveness scores.',
            'Reviewed how training calendars are built around identified skill '
            'gaps and statutory requirements.',
            'Examined nomination-to-completion ratios and post-training '
            'feedback by department.',
            'Discussed with the team how effectiveness data informs the design '
            'of future programmes.',
        ]),

        ('h3', 'Week 7 (20 July – 24 July 2026): Presentation on AI in HR'),
        ('bullets', [
            'Conducted secondary research on artificial intelligence in talent '
            'analytics, sentiment analysis and predictive attrition modelling.',
            'Structured and delivered the presentation "AI in Leadership and '
            'Decision Making" to the HR team.',
            'Responded to questions and refined the framing of artificial '
            'intelligence as decision support rather than replacement.',
            'Received structured feedback on both content and delivery.',
        ]),

        ('h3', 'Week 8 (27 July – 31 July 2026): Industry Trends and Closure'),
        ('bullets', [
            'Researched electrification, automation, digital transformation and '
            'workforce evolution in automobile manufacturing.',
            'Delivered the presentation "Current and Future Trends in '
            'Industrial and Automobile Manufacturing", applying the previous '
            'week’s feedback.',
            'Linked industry trends to workforce skilling and HR strategy '
            'implications for the organisation.',
            'Consolidated internship learning, handed over documentation and '
            'received closing feedback from the HR and Industrial Relations '
            'team.',
        ]),

        ('h2', '2.5  TOOLS AND SYSTEMS USED'),
        ('h3', '2.5.1  Darwinbox Human Resource Management System'),
        ('p', 'Darwinbox served as the central human resource management system '
              'for employee records, onboarding workflows and self-service '
              'functions. Working with it gave me an understanding of how a '
              'modern cloud-based platform consolidates the employee '
              'lifecycle, from recruitment through onboarding to records '
              'management and reporting, into a single integrated system. The '
              'value of such consolidation is clearest in a multi-plant '
              'organisation, where the alternative is inconsistent local '
              'record-keeping.'),

        ('h3', '2.5.2  The Recruitment Process Outsourcing Model'),
        ('p', 'Exposure to the outsourcing model helped me understand how the '
              'organisation partners with external recruitment agencies to '
              'manage high-volume hiring while retaining oversight of quality, '
              'turnaround time and candidate experience through defined '
              'service-level agreements and periodic review. The model is a '
              'practical answer to a scale problem, and it shifts the internal '
              'HR role from sourcing towards specification and governance.'),

        ('h3', '2.5.3  Spreadsheets for Reporting and Dashboards'),
        ('p', 'Spreadsheet work was essential to consolidating data for the '
              'reporting pack and the Employee Relations dashboard. Pivot '
              'tables, conditional formatting and summary charts were used to '
              'convert raw workforce and Industrial Relations data into '
              'management-ready output. The technique matters less than the '
              'habit that surrounds it: checking a consolidated figure against '
              'its source before presenting it.'),

        ('h3', '2.5.4  Presentation and Document Preparation'),
        ('p', 'Presentation software was used to design the conference flyer '
              'and agenda and to build the two research presentations, while '
              'word processing was used to draft and format the Industrial '
              'Relations reference handbook and other internal documentation. '
              'Working across both taught me that document design is part of '
              'communication rather than decoration, since a handbook that is '
              'hard to navigate will not be consulted.'),

        ('h3', '2.5.5  The Learning and Development Dashboard'),
        ('p', 'The automated Learning and Development dashboard provided '
              'visibility of training nominations, completions and feedback '
              'scores, illustrating how technology supports structured, '
              'trackable employee development at scale. It also demonstrated '
              'the difference between recording that training occurred and '
              'establishing whether it worked, which are separate questions '
              'that the dashboard deliberately kept apart.'),

        ('h2', '2.6  APPLICATION OF ACADEMIC KNOWLEDGE'),
        ('h3', '2.6.1  Industrial Relations and Labour Laws'),
        ('p', 'The subject moved from statute to practice. Classroom coverage '
              'of grievance handling, union engagement and dispute resolution '
              'became concrete while assisting with documentation and preparing '
              'the reporting pack, and the statutory transition of November '
              '2025 meant I was learning the framework in its current form '
              'rather than its historical one.'),
        ('bullets', [
            'Applied grievance-handling and dispute-resolution concepts while '
            'assisting with Industrial Relations documentation.',
            'Traced how statutory obligations translate into day-to-day process '
            'on the shop floor.',
            'Understood the practical consequence of the consolidation of '
            'twenty-nine central labour laws into four Labour Codes for policy '
            'and documentation.',
        ]),

        ('h3', '2.6.2  Human Resource Information Systems'),
        ('p', 'Coursework on human resource information systems became tangible '
              'through practical use of the Darwinbox platform, and the '
              'outsourcing model showed how recruitment theory is '
              'operationalised at scale.'),
        ('bullets', [
            'Related classroom learning on information systems to practical '
            'employee data management and workflow automation.',
            'Understood how outsourcing arrangements turn recruitment theory '
            'into a scalable, governed process.',
            'Saw how master data structure determines what reporting is '
            'subsequently possible.',
        ]),

        ('h3', '2.6.3  HR Analytics'),
        ('p', 'Analytics was the subject most directly exercised. Data analysis '
              'and dashboard-design concepts were applied to build the Employee '
              'Relations dashboard and the reporting pack, and the experience '
              'clarified the difference between description and prediction.'),
        ('bullets', [
            'Applied data consolidation and dashboard-design concepts to live '
            'workforce and Industrial Relations data.',
            'Understood how descriptive analytics supports proactive Industrial '
            'Relations management rather than purely reactive case handling.',
            'Learned to validate figures across sources before presenting them '
            'to leadership.',
        ]),

        ('h3', '2.6.4  Training and Development'),
        ('p', 'Academic frameworks on training needs analysis and on the '
              'evaluation of training effectiveness connected directly to the '
              'tracking of interventions on the Learning and Development '
              'dashboard.'),
        ('bullets', [
            'Connected training needs analysis to the way training calendars '
            'are built around identified skill gaps.',
            'Related evaluation frameworks to the dashboard’s treatment of '
            'completion rates and feedback scores as distinct measures.',
            'Understood mandatory compliance training as a category with a '
            'different consequence from developmental training.',
        ]),

        ('h3', '2.6.5  Organisational Behaviour and Communication'),
        ('p', 'Principles of organisational communication and stakeholder '
              'management were applied while designing the conference materials '
              'and while researching and delivering the two presentations.'),
        ('bullets', [
            'Applied stakeholder management while reconciling inputs from '
            'session owners and the communications team.',
            'Adapted register and structure to three different audiences: '
            'handbook readers, HR leadership and a professional conference '
            'audience.',
            'Practised delivering and defending a researched position before an '
            'experienced audience.',
        ]),

        ('h3', '2.6.6  Strategic HRM and Emerging Technologies'),
        ('p', 'Research for the two presentations required me to treat HR as an '
              'enabler of business strategy rather than as a support function, '
              'which is the claim the subject makes and which the internship '
              'substantiated.'),
        ('bullets', [
            'Linked workforce capability building to the company’s '
            'electrification and digitalisation agenda.',
            'Assessed artificial intelligence in HR as a decision-support '
            'capability with identifiable limits.',
            'Understood how industry-level trends translate into workforce '
            'planning requirements at firm level.',
        ]),

        ('h2', '2.7  SKILLS DEVELOPED DURING THE INTERNSHIP'),
        ('h3', '2.7.1  Industrial Relations Documentation'),
        ('p', 'The ability to prepare and maintain records in a '
              'compliance-sensitive function, with the version discipline and '
              'completeness that such records require.'),
        ('h3', '2.7.2  Management Reporting and Data Consolidation'),
        ('p', 'The ability to consolidate data arriving in inconsistent formats '
              'from several sources into a single reliable, management-ready '
              'reporting pack.'),
        ('h3', '2.7.3  Dashboard Design and Interpretation'),
        ('p', 'Practical understanding of how workforce indicators are selected '
              'and presented so that leadership can act on them, and of the '
              'difference between activity and outcome measures.'),
        ('h3', '2.7.4  HR Systems Navigation'),
        ('p', 'Working familiarity with a cloud-based human resource management '
              'system across employee records, onboarding workflow and '
              'self-service functions.'),
        ('h3', '2.7.5  Writing for a Defined Reader'),
        ('p', 'The ability to adjust register and structure to the intended '
              'reader, having written for new employees, for HR leadership and '
              'for an external professional audience within the same eight '
              'weeks.'),
        ('h3', '2.7.6  Stakeholder Coordination'),
        ('p', 'The ability to gather, reconcile and follow up inputs from '
              'several internal parties against a fixed deadline, as the '
              'conference materials required.'),
        ('h3', '2.7.7  Research Synthesis and Presentation'),
        ('p', 'The ability to convert secondary research into a structured '
              'argument and to deliver and defend it before an audience more '
              'experienced than myself.'),
        ('h3', '2.7.8  Data Confidentiality and Professional Discretion'),
        ('p', 'The habit of aggregating or anonymising employee-identifiable '
              'information wherever the analysis does not require '
              'individual-level detail, and of treating confidentiality as a '
              'legal obligation rather than a courtesy.'),

        ('h2', '2.8  KEY OBSERVATIONS FROM THE JOB'),
        ('bullets', [
            'In Industrial Relations the document is the practice. A grievance '
            'record or escalation note is not the paperwork that follows a '
            'decision; it is what makes the decision consistent and '
            'defensible.',
            'Consistency matters more than speed. Across a multi-plant '
            'workforce, the same situation handled two different ways is a '
            'greater risk than the same situation handled slowly.',
            'Small documentation lapses have outsized consequences. In a '
            'unionised environment an inconsistency in a record can affect '
            'trust well beyond the individual case it concerns.',
            'Plant-level data arrives in inconsistent forms. Local reporting '
            'habits differ, and standardisation before consolidation is the '
            'real work in preparing a management report.',
            'Centralised consistency has to be balanced against legitimate '
            'local variation. A handbook or reporting framework that ignores '
            'genuine differences between plants will not be used.',
            'A good report begins with the question, not the data. Formatting '
            'a figure well does not make it informative; knowing why '
            'leadership needs it does.',
            'Collective and individual interests both have to be weighed. Plant '
            'decisions on scheduling, grievances or policy communication '
            'involve employee representative bodies and not only individual '
            'employees, which makes procedural fairness structural rather than '
            'discretionary.',
            'Statutory change reaches the accounts. A revision to labour law '
            'appeared in the company’s results as a one-time charge of about '
            'INR 308 crore, which settled any doubt about whether compliance '
            'work is commercially material.',
            'HR sub-functions are interconnected in practice. The same employee '
            'data feeds the human resource management system and the Industrial '
            'Relations reporting pack, and communication skill built on the '
            'handbook transferred directly to the conference materials.',
        ]),

        ('h2', '2.9  CHALLENGES ENCOUNTERED DURING THE INTERNSHIP'),
        ('h3', '2.9.1  Unfamiliar Terminology'),
        ('p', 'Industrial Relations and labour-law vocabulary encountered in '
              'the first week was genuinely unfamiliar, and imprecision in '
              'such terminology is not a cosmetic problem: terms have defined '
              'statutory meanings. The response was focused reading, a running '
              'glossary of my own, and a willingness to ask rather than infer. '
              'A brief glossary provided at induction would have shortened this '
              'curve considerably, which is a suggestion I make in Chapter 5.'),

        ('h3', '2.9.2  Data Consolidation Across Plants'),
        ('p', 'Consolidating attendance and grievance data from several '
              'plant-level sources for the reporting pack required careful '
              'cross-checking, because local recording conventions differed. '
              'Reconciling them meant following up with plant contacts and '
              'agreeing definitions before consolidation rather than adjusting '
              'figures afterwards. This was slower than expected and was the '
              'most valuable technical lesson of the internship.'),

        ('h3', '2.9.3  Balancing Concurrent Deliverables'),
        ('p', 'Coordinating the conference materials in Week 5 alongside '
              'continuing reporting responsibilities required disciplined time '
              'management. The difficulty was not the volume of work but its '
              'different rhythms: a reporting pack has a fixed monthly '
              'deadline, while event coordination generates unpredictable '
              'requests from other people. Learning to protect time for the '
              'predictable task while remaining responsive to the '
              'unpredictable one was a genuine adjustment.'),

        ('h3', '2.9.4  Presenting to a Senior Audience'),
        ('p', 'Delivering research-based presentations to experienced HR '
              'professionals in Weeks 7 and 8 required a confidence I did not '
              'initially have. The specific difficulty was anticipating '
              'questions and knowing the boundary of my own material well '
              'enough to say where it ended. Feedback after the first '
              'presentation directly improved the second, which is the clearest '
              'single example of iterative improvement during the internship.'),

        ('h3', '2.9.5  Working Within Access and Confidentiality Limits'),
        ('p', 'Access to certain systems and to historical data was restricted '
              'under the organisation’s data governance policies, which meant '
              'some analysis rested on a limited data window. Observation '
              'rather than participation was also the appropriate mode for '
              'sensitive Industrial Relations matters. Learning to produce '
              'useful work within those limits, and to state the limits plainly '
              'rather than overclaim, was itself part of the professional '
              'education.'),

        ('h2', '2.10  OVERALL JOB EXPERIENCE'),
        ('p', 'The overall experience was that HR and Industrial Relations in a '
              'manufacturing organisation is considerably more procedural and '
              'considerably more consequential than classroom treatment '
              'suggests. I had expected a function centred on people skills. '
              'What I found was a function in which people skills operate '
              'through documents, data and defined procedure, because at the '
              'scale of a multi-plant workforce nothing else scales.'),
        ('p', 'The mentorship I received shaped that experience decisively. '
              'Regular check-ins clarified expectations for each week’s task, '
              'and structured feedback after each deliverable allowed the next '
              'one to be better. Colleagues across the Industrial Relations, '
              'recruitment, analytics, Learning and Development and '
              'communication teams were consistently willing to explain '
              'unfamiliar concepts, which materially eased the early learning '
              'curve and made the progression from observation to independent '
              'delivery possible within eight weeks.'),
        ('p', 'I should also be honest about the limits of the period. Eight '
              'weeks is long enough to understand how each part of the function '
              'works and too short to see an Industrial Relations matter '
              'through from origin to resolution, or to observe whether a '
              'training intervention changed anything. I therefore left with a '
              'good understanding of process and a partial understanding of '
              'outcomes, and I would rather record that plainly than imply a '
              'depth of involvement the programme did not allow.'),
        ('h2', '2.11  SUMMARY OF RESPONSIBILITIES'),
        ('p', 'The table below consolidates the work of the internship and the '
              'nature of my contribution to each item. It reflects the areas '
              'assigned to me and does not claim sole ownership of team '
              'deliverables.'),
        ('table', {'rows': [
            ['S. No.', 'Area of Work', 'Major Responsibility and Contribution'],
            ['1', 'Organisational induction',
             'Attended induction; studied organisation structure, reporting '
             'lines, code of conduct and confidentiality expectations'],
            ['2', 'Industrial Relations documentation',
             'Assisted with filing and updating IR records; observed case-file '
             'review and shop-floor engagement with employee representatives'],
            ['3', 'Recruitment Process Outsourcing',
             'Observed partner briefing, pipeline management and the tracking '
             'of quality and turnaround-time metrics'],
            ['4', 'Human resource management system',
             'Hands-on exposure to Darwinbox across employee records, '
             'onboarding workflows and self-service features'],
            ['5', 'IR Management Information System report',
             'Collected, cleaned and consolidated plant-level attendance, '
             'grievance, disciplinary and union engagement data into the '
             'monthly reporting pack'],
            ['6', 'Employee Relations dashboard',
             'Contributed to dashboard design and indicator selection in '
             'discussion with the HR analytics lead'],
            ['7', 'IR reference handbook',
             'Drafted sections on grievance escalation and stakeholder roles; '
             'incorporated review feedback; maintained version control'],
            ['8', 'EFSI Conference communication',
             'Designed the conference flyer through several iterations and '
             'structured the agenda with session owners'],
            ['9', 'Event coordination support',
             'Coordinated invitee lists, confirmation follow-ups and related '
             'internal communication'],
            ['10', 'Learning and Development dashboard',
             'Reviewed nomination, completion, training-hour and feedback '
             'views, and how effectiveness data informs programme design'],
            ['11', 'Presentation on AI in leadership',
             'Independent secondary research, structuring and delivery to the '
             'HR team, with framing refined after questions'],
            ['12', 'Presentation on manufacturing trends',
             'Independent research and delivery, linking industry trends to '
             'workforce skilling and HR strategy implications'],
        ], 'widths': [1, 3, 6], 'col_bold': [True, True, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),

        ('h2', '2.12  CONCLUSION OF JOB / TASK DESCRIPTION'),
        ('p', 'The eight weeks gave me practical exposure to the full breadth '
              'of an HR and Industrial Relations function: induction and '
              'statutory fundamentals, recruitment and HR technology, analytics '
              'and management reporting, knowledge management, internal '
              'communication and event coordination, Learning and Development, '
              'and research-based presentation. Each week closed with a '
              'deliverable, which meant the learning was tested rather than '
              'merely received.'),
        ('p', 'The chapter has described responsibilities, method and '
              'contribution rather than claiming outcomes I was not in a '
              'position to observe or verify. No campaign-style results or '
              'performance figures are attributed to my work, because the '
              'deliverables were team products to which I contributed and '
              'because an eight-week window does not reveal the effect of an '
              'Industrial Relations or training intervention. What can be '
              'stated with confidence is the method I was taught, the '
              'standards I was held to, and the progression from supervised '
              'observation to independent delivery. The next chapter analyses '
              'how well I performed against those standards.'),
    ],
}


# ---------------------------------------------------------------------------
# CHAPTER 3
# ---------------------------------------------------------------------------
CH3 = {
    'num': 3,
    'title': 'ANALYSIS OF JOB PERFORMANCE',
    'header_left': 'CHAPTER 3',
    'header_right': 'ANALYSIS OF JOB PERFORMANCE',
    'blocks': [
        ('h1', '3. ANALYSIS OF JOB PERFORMANCE'),

        ('h2', '3.1  QUALITY OF WORK'),
        ('p_indent', 'Throughout the internship I maintained a consistent focus '
                     'on accuracy, clarity and professionalism across '
                     'deliverables that demanded quite different combinations '
                     'of skill. Industrial Relations documentation required '
                     'precision, management reporting required data discipline, '
                     'the reference handbook required plain writing, the '
                     'conference materials required design judgement, and the '
                     'two presentations required research synthesis. The '
                     'quality of my output improved progressively across the '
                     'eight weeks, moving from close supervision during '
                     'induction to independent contribution in the closing '
                     'weeks.'),
        ('bullets', [
            'The Industrial Relations reporting pack and the Employee Relations '
            'dashboard were prepared with attention to data accuracy and clear, '
            'management-ready formatting.',
            'The reference handbook was structured logically, with content '
            'reviewed and refined on the basis of feedback from the HR team.',
            'The conference flyer and agenda were designed to be visually clear '
            'and aligned with the organisation’s communication standards.',
            'Both research presentations were structured, appropriately sourced '
            'and delivered with clarity to a professional audience.',
            'Documentation standards were observed throughout, including dated '
            'version labels, consistent file naming and aggregation or '
            'anonymisation of employee-identifiable data wherever '
            'individual-level detail was not required.',
        ]),
        ('p', 'Assessing myself honestly on this dimension, the early work '
              'required more correction than it should have. Minor errors in '
              'the first fortnight, principally in terminology and in the '
              'structure of records, were identified and corrected with '
              'guidance. What changed was sequence rather than effort: I began '
              'checking details against a source before recording them rather '
              'than after, which reduced rework substantially from Week 3 '
              'onward.'),

        ('h2', '3.2  TIMELINESS AND TASK OWNERSHIP'),
        ('p', 'As the internship progressed I took increasing ownership of '
              'assigned work, completing the reporting pack, the handbook '
              'sections and the conference materials within the agreed '
              'timelines. Coordination for inputs from stakeholders within the '
              'HR team was handled proactively, and dependencies or likely '
              'delays were communicated to my reporting manager as soon as they '
              'became apparent rather than at the point they became problems.'),
        ('p', 'Task ownership for an intern has a boundary worth naming. It does '
              'not extend to decisions beyond the assigned authority, and in a '
              'compliance-sensitive function it does not extend to finalising a '
              'document without review. What it does mean is understanding the '
              'expected output, tracking progress against it, chasing the inputs '
              'one depends on and being transparent about status. I was '
              'initially more hesitant than necessary about following up with '
              'senior colleagues for inputs I genuinely needed, which is a '
              'reticence I had to get past.'),
        ('h2', '3.3  ADAPTABILITY AND LEARNING CURVE'),
        ('p', 'I began with no prior exposure to the Darwinbox platform, to '
              'outsourced recruitment models or to Industrial Relations '
              'reporting formats. Adaptation was necessary rather than '
              'optional, and it happened over roughly the first fortnight. '
              'Confidence in spreadsheet-based reporting, in the terminology of '
              'the function and in navigating the HR system improved steadily '
              'through repeated practice and guidance.'),
        ('bullets', [
            'Learned to navigate the Darwinbox platform and understand its core '
            'modules within the first two weeks.',
            'Became competent at structuring reports and dashboards using pivot '
            'tables, summary charts and conditional formatting.',
            'Adapted to unfamiliar formats for Industrial Relations '
            'documentation and handbook preparation, applying feedback from '
            'senior staff.',
            'Showed initiative in researching independently for both the '
            'artificial intelligence and industry-trends presentations.',
            'Adjusted to the statutory framework as it now stands following the '
            'Labour Codes, rather than relying on the pre-consolidation '
            'position covered in coursework.',
        ]),

        ('h2', '3.4  COMMUNICATION AND COLLABORATION'),
        ('p', 'Professional communication and collaboration were central to the '
              'internship, because HR and Industrial Relations work is '
              'cross-functional by construction. Almost every deliverable I '
              'contributed to required inputs from someone else.'),
        ('bullets', [
            'Maintained clear, respectful communication with the HR and '
            'Industrial Relations team while gathering inputs for the reporting '
            'pack and the handbook.',
            'Coordinated with internal stakeholders to finalise content and '
            'design for the conference flyer and agenda, reconciling multiple '
            'inputs under time pressure.',
            'Presented consolidated data and structured reports in formats that '
            'supervisors could review and act upon without rework.',
            'Sought clarification proactively when encountering unfamiliar '
            'terminology or system workflows, and incorporated feedback into '
            'subsequent tasks rather than defending the first attempt.',
            'Interacted regularly with peers across the Industrial Relations, '
            'recruitment, analytics, Learning and Development and communication '
            'teams, which built a working understanding of how these teams '
            'collaborate on shared priorities.',
            'Adopted the professional norms the team modelled: raising '
            'questions early, documenting agreed decisions clearly and '
            'following up without waiting to be reminded.',
        ]),

        ('h2', '3.5  STRENGTHS DEMONSTRATED'),
        ('p', 'The following are offered as qualitative reflections on the '
              'internship rather than as formal ratings, since no formal '
              'appraisal was conducted.'),
        ('bullets', [
            '**Attention to detail:** maintained accuracy in consolidating '
            'plant-level data and in handbook content, in a function where an '
            'inconsistency carries consequences.',
            '**Ownership:** took responsibility for assigned deliverables and '
            'followed up on pending inputs without requiring reminders.',
            '**Quick learning:** adapted to the Darwinbox platform, outsourced '
            'recruitment processes and Industrial Relations reporting formats '
            'with limited formal training.',
            '**Communication:** coordinated effectively across HR, Industrial '
            'Relations, communication and event stakeholders.',
            '**Presentation skill:** researched, structured and delivered two '
            'presentations to an audience of experienced professionals.',
            '**Documentation discipline:** applied version control, consistent '
            'naming and appropriate handling of confidential data without being '
            'prompted after the first week.',
            '**Willingness to state uncertainty:** became comfortable recording '
            'that a figure was unavailable or a definition unclear rather than '
            'resolving the gap by assumption.',
        ]),

        ('h2', '3.6  AREAS FOR IMPROVEMENT'),
        ('p', 'The internship was at least as informative about my gaps as '
              'about my strengths. These are stated specifically, because a '
              'general intention to improve cannot be acted upon.'),
        ('bullets', [
            '**Statutory depth:** initial unfamiliarity with Industrial '
            'Relations and labour-law terminology was overcome for working '
            'purposes, but genuine fluency in the four Labour Codes requires '
            'sustained study beyond an eight-week exposure.',
            '**Advanced dashboard technique:** confidence with more advanced '
            'spreadsheet and dashboard methods improved with practice but '
            'remains a development area, particularly in automating recurring '
            'reporting.',
            '**Presentation confidence:** comfort in presenting to senior '
            'professionals improved markedly between Weeks 7 and 8, and would '
            'benefit from further repetition.',
            '**Document structuring for end users:** I learned to organise the '
            'handbook more intuitively only after review feedback, indicating '
            'that I should think about the reader’s navigation before drafting '
            'rather than after.',
            '**Analytical interpretation:** I became competent at preparing '
            'indicators but have more to learn about interpreting them, '
            'particularly in distinguishing a genuine trend from monthly '
            'variation.',
            '**Union-facing practice:** my exposure to employee representative '
            'engagement was observational, and direct capability in that area '
            'remains to be built.',
        ]),

        ('h2', '3.7  OVERALL PERFORMANCE'),
        ('p', 'At the start and again at the end of the internship I completed '
              'a brief self-assessment across the skill areas most relevant to '
              'the function, on a five-point scale where 1 represents beginner '
              'and 5 represents confident and independent. The movement is set '
              'out below. These are my own assessments and not an evaluation by '
              'the organisation.'),
        ('bullets', [
            '**Understanding of Industrial Relations concepts:** 2 at the start, '
            '4 at the end.',
            '**Darwinbox platform navigation:** 1 at the start, 4 at the end, '
            'the largest single movement, from no prior exposure.',
            '**Spreadsheet-based reporting and dashboards:** 2 at the start, 4 '
            'at the end.',
            '**Business and HR documentation writing:** 3 at the start, 4 at '
            'the end, the highest starting point and therefore the smallest '
            'gain.',
            '**Event and communication coordination:** 2 at the start, 4 at the '
            'end.',
            '**Formal presentation and public speaking:** 2 at the start, 4 at '
            'the end.',
        ]),
        ('p', 'Read chronologically, performance across the eight weeks shows a '
              'clear arc. Weeks 1 and 2 were characterised by observation, '
              'guided learning and heavy reliance on supervisory support, '
              'particularly while becoming familiar with terminology and the HR '
              'system. By Weeks 3 and 4 I was contributing directly to '
              'analytical and documentation deliverables with moderate '
              'supervision. Weeks 5 and 6 introduced cross-functional '
              'coordination demands that required greater initiative and '
              'stakeholder management. By Weeks 7 and 8 I was working with a '
              'high degree of independence, conducting original research and '
              'delivering formal presentations with minimal guidance.'),
        ('p', 'Periodic feedback from the HR and Industrial Relations team '
              'tracked that progression. Early feedback concentrated on '
              'building familiarity with terminology and system navigation, '
              'while later feedback recognised growing independence in '
              'preparing the reporting pack, structuring the handbook and '
              'presenting research findings. The movement from guided execution '
              'to independent contribution was noted as a positive indicator of '
              'readiness for a professional role. Against the criteria the team '
              'applied informally, accuracy of documentation was consistently '
              'sound after early corrections, deliverables were completed '
              'within agreed timelines, initiative increased noticeably from '
              'Week 5 onward, and adaptation to new tools was rapid.'),
        ('p', 'Benchmarked against commonly cited practice in the field, the '
              'work I was given aligns well with how well-run functions '
              'operate. Consolidating employee data onto a single platform '
              'mirrors the direction of large Indian and global manufacturers. '
              'Preparing a dashboard-supported Industrial Relations reporting '
              'pack reflects the shift towards proactive, data-informed '
              'employee relations rather than reactive case handling. Building '
              'a reference handbook reflects recognised knowledge-management '
              'practice, reducing dependence on tacit knowledge held by '
              'individuals and building institutional memory that survives '
              'changes of personnel. The tasks were therefore not '
              'administrative filler but genuine function work at an intern '
              'level.'),
        ('p', 'If I were to summarise my performance in a sentence, it would be '
              'this: I was a reliable and increasingly independent contributor '
              'to documentation, reporting and communication deliverables, who '
              'improved most in the areas where I started weakest, and who '
              'leaves with an accurate rather than an inflated sense of what '
              'she can currently do. No numerical performance score is stated '
              'here, because no formal appraisal rubric was applied to my work, '
              'and constructing one for the sake of appearance would '
              'misrepresent the basis of this chapter.'),
    ],
}

# ---------------------------------------------------------------------------
# CHAPTER 4
# ---------------------------------------------------------------------------
CH4 = {
    'num': 4,
    'title': 'LEARNING OUTCOMES',
    'header_left': 'CHAPTER 4',
    'header_right': 'LEARNING OUTCOMES',
    'blocks': [
        ('h1', '4. LEARNING OUTCOMES'),

        ('h2', '4.1  FUNCTIONAL KNOWLEDGE ACQUIRED'),
        ('p', 'The internship converted a set of examinable topics into a '
              'working understanding of how an HR and Industrial Relations '
              'function actually operates in a large manufacturing '
              'organisation. The functional knowledge acquired is set out '
              'below.'),
        ('bullets', [
            '**Industrial Relations fundamentals:** a working understanding of '
            'grievance handling, engagement with employee representative '
            'bodies, documentation practice and the statutory context governing '
            'employer-employee relations.',
            '**The current statutory framework:** familiarity with the '
            'consolidation of twenty-nine central labour laws into four Labour '
            'Codes, and with the practical revision of policy and documentation '
            'that such a change requires.',
            '**Human resource management systems:** familiarity with the '
            'Darwinbox platform, including employee records, onboarding '
            'workflows and self-service modules.',
            '**Recruitment Process Outsourcing:** an understanding of how such '
            'partnerships are structured, briefed, monitored and evaluated for '
            'quality and turnaround time.',
            '**HR analytics and management reporting:** the ability to '
            'consolidate and present Industrial Relations and workforce data '
            'through structured reporting packs and dashboards.',
            '**Knowledge management:** an appreciation of how handbooks and '
            'reference material convert individually held knowledge into '
            'institutional memory.',
            '**Learning and Development tracking:** an understanding of how '
            'automated dashboards support structured, measurable capability '
            'building, and of the distinction between completion and '
            'effectiveness.',
            '**Internal communication:** practical experience of planning and '
            'producing communication material for an industry-facing event.',
        ]),

        ('h2', '4.2  PRACTICAL EXPOSURE TO HR BUSINESS PROCESSES'),
        ('p', 'The internship gave me insight into how a large manufacturing '
              'organisation structures its HR function and how the '
              'sub-functions interlock. The most valuable realisation was about '
              'dependency: recruitment, system records, Industrial Relations '
              'reporting and training tracking all draw on the same underlying '
              'employee data, which means an error introduced at one point '
              'surfaces at several others.'),
        ('p', 'I also saw how HR, Industrial Relations and corporate '
              'communication coordinate for organisation-wide initiatives such '
              'as the federation conference, and understood the procedural '
              'discipline required to prepare compliance-relevant documents '
              'such as the reference handbook. Observing the function from '
              'inside made clear why its process constraints exist. Review '
              'steps, version control and confidentiality rules can look like '
              'bureaucracy from outside; from inside, each is a response to a '
              'specific way that an Industrial Relations matter can go wrong at '
              'the organisation’s expense.'),

        ('h2', '4.3  IMPROVEMENT IN ANALYTICAL AND SYSTEMS THINKING'),
        ('p', 'The internship pushed me to think past task completion and to '
              'ask what a piece of analysis was for. Consolidating a figure is '
              'not useful unless the figure answers a question leadership '
              'actually has, and a dashboard indicator is not useful unless '
              'someone can act on it.'),
        ('p', 'Three habits developed specifically. The first was '
              'cross-functional validation: checking data across system records '
              'and Industrial Relations reports before finalising the pack, '
              'rather than trusting a single source. The second was pattern '
              'recognition: becoming attentive to recurring themes in the data '
              'that might signal an emerging employee-relations issue, since '
              'the value of monthly reporting lies in catching a trend before '
              'it becomes a dispute. The third was decision-support thinking: '
              'understanding that the purpose of accurate reporting is to '
              'inform leadership decisions on workforce planning and Industrial '
              'Relations strategy, which means the report should be built for '
              'the decision rather than for completeness.'),
        ('p', 'I also came to appreciate the difference between an activity '
              'measure and an outcome measure. A count of grievances logged '
              'describes work; whether workplace relations improved is a '
              'separate question requiring different evidence. The Learning and '
              'Development dashboard made the same distinction by keeping '
              'completion rates and feedback scores apart, and that design '
              'choice taught me more about measurement than any single lecture '
              'had.'),

        ('h2', '4.4  SOFT SKILLS AND PROFESSIONAL TRAITS STRENGTHENED'),
        ('p', 'Alongside the functional learning, the internship strengthened a '
              'set of professional traits that no coursework had tested.'),
        ('bullets', [
            '**Time management:** balancing a recurring monthly reporting '
            'obligation against project deliverables such as the handbook, the '
            'conference materials and two presentations.',
            '**Written communication:** adjusting register and structure across '
            'a handbook for new employees, a reporting pack for leadership and '
            'an external-facing flyer.',
            '**Verbal communication:** structuring and delivering two formal '
            'presentations, and defending a researched position under '
            'questioning.',
            '**Adaptability:** adjusting to new tools, formats and functional '
            'areas across an eight-week rotation through HR sub-functions.',
            '**Accountability:** taking ownership of assigned tasks, honouring '
            'deadlines and incorporating feedback constructively.',
            '**Discretion:** handling employee-identifiable information with '
            'the care a legal obligation requires rather than the care a '
            'courtesy would suggest.',
            '**Professional persistence:** following up with plant contacts and '
            'session owners for inputs I needed, having initially been '
            'reluctant to chase senior colleagues.',
        ]),

        ('h2', '4.5  ALIGNMENT WITH ACADEMIC LEARNING'),
        ('p', 'The internship served as a practical extension of the subjects '
              'studied in the MBA programme. The table below maps each subject '
              'to the work in which it was applied.'),
        ('table', {'rows': [
            ['Academic Subject', 'Internship Application'],
            ['Industrial Relations and Labour Laws',
             'Industrial Relations documentation, the monthly reporting pack '
             'and the reference handbook, read against the four Labour Codes '
             'now in force'],
            ['Human Resource Information Systems',
             'Hands-on exposure to the Darwinbox platform and to the '
             'Recruitment Process Outsourcing model'],
            ['HR Analytics',
             'Preparation of the Employee Relations dashboard and the '
             'Industrial Relations Management Information System report'],
            ['Training and Development',
             'Exploration of the automated Learning and Development dashboard '
             'and of training needs identification'],
            ['Organisational Behaviour and Communication',
             'Conference flyer and agenda design, stakeholder coordination and '
             'internal HR communication'],
            ['Strategic HRM and Emerging Technologies',
             'Research and presentation on artificial intelligence in '
             'leadership, and on manufacturing trends and their workforce '
             'implications'],
            ['Business Ethics and Data Governance',
             'Aggregation and anonymisation of employee data, version control '
             'and observance of confidentiality policy'],
        ], 'widths': [3, 6], 'col_bold': [True, False],
            'col_align': ['center', 'left'], 'row_height': 500}),
        ('p', 'The internship also exposed the limits of purely academic '
              'preparation. Coursework presents recruitment, Industrial '
              'Relations, analytics and Learning and Development as discrete, '
              'cleanly separated topics. In practice they proved closely '
              'interconnected: the same underlying employee data fed both the '
              'HR system and the Industrial Relations reporting pack, the '
              'writing discipline built on the handbook was reused directly in '
              'the conference materials, and the research method developed for '
              'the Week 7 presentation carried straight into Week 8. That '
              'interconnectedness was, in many ways, the most significant '
              'single learning of the internship.'),

        ('h2', '4.6  OVERALL REALISATIONS'),
        ('bullets', [
            'Industrial Relations is as much about proactive communication and '
            'disciplined documentation as it is about statutory compliance.',
            'HR technology and analytics are now central to timely, informed '
            'workforce decisions in a multi-plant organisation, not '
            'peripheral conveniences.',
            'HR functions as a strategic partner to the business, balancing '
            'compliance, culture and capability building at the same time.',
            'Consistency across locations is the hardest thing an HR function '
            'does, and the systems that deliver it are what justify their own '
            'cost.',
            'Statutory change is commercially material, as the one-time charge '
            'in the company’s FY 2025-26 accounts demonstrated.',
            'Writing is a core HR skill rather than a supporting one, because '
            'policy that cannot be understood cannot be followed.',
            'An honest account of what one did not see is part of professional '
            'reporting, and my own exposure was broad rather than deep.',
        ]),
        ('p', 'Comparing expectations with reality is instructive here. I '
              'arrived expecting HR to be predominantly people-facing and found '
              'that its people-facing work rests on a substantial base of '
              'documentation, data and procedure. I also arrived expecting '
              'Industrial Relations to be adversarial and found it to be '
              'largely preventive, concerned with maintaining conditions in '
              'which disputes do not arise. Both corrections were useful, and '
              'both changed how I read the subject.'),

        ('h2', '4.7  PROFESSIONAL INSIGHTS AND LEARNINGS'),
        ('p', 'The internship sharpened my understanding of what a career in '
              'this field requires. Effectiveness depends on a combination of '
              'statutory knowledge, analytical capability, writing skill, '
              'systems familiarity, interpersonal judgement and personal '
              'discretion. Strength in one while neglecting the others is '
              'unlikely to support progression, which is a more demanding '
              'conclusion than I expected to reach.'),
        ('p', 'I leave with a clearer sense of professional identity as well. '
              'The internship gave me an appreciation of the quieter, '
              'process-driven side of the function, meaning documentation, '
              'compliance and analytics, alongside the more visible '
              'people-facing side of communication, events and presentation. '
              'Both dimensions are essential, and I had previously understood '
              'only the second to be the substance of HR work. The progression '
              'from shadowing team members in the first week to independently '
              'researching and presenting on industry trends in the last was '
              'itself a demonstration of how quickly practical capability can '
              'be built when structured exposure is paired with consistent '
              'mentorship.'),
    ],
}

# ---------------------------------------------------------------------------
# CHAPTER 5
# ---------------------------------------------------------------------------
CH5 = {
    'num': 5,
    'title': 'SUMMARY AND CONCLUSION',
    'header_left': 'CHAPTER 5',
    'header_right': 'SUMMARY AND CONCLUSION',
    'blocks': [
        ('h1', '5. SUMMARY AND CONCLUSION'),

        ('h2', '5.1  SUMMARY OF INTERNSHIP EXPERIENCE'),
        ('p_indent', 'The Summer Internship Programme was carried out at Ashok '
                     'Leyland Limited, the flagship commercial vehicle company '
                     'of the Hinduja Group, on-site at its Guindy office in '
                     'Chennai, from 9 June 2026 to 31 July 2026, a period of '
                     'eight working weeks, in the Human Resources and '
                     'Industrial Relations department under the guidance of Mr. '
                     'Venkatesan Raman, Lead – IR Center of Excellence, Human '
                     'Resources. The programme provided practical exposure to '
                     'Industrial Relations fundamentals and documentation, '
                     'recruitment and HR technology, HR analytics and '
                     'management reporting, knowledge management, internal '
                     'communication and event coordination, Learning and '
                     'Development systems, and research-based presentation.'),
        ('p', 'The timing gave the internship a particular character. India’s '
              'four consolidated Labour Codes had come into force on 21 '
              'November 2025, replacing twenty-nine central labour laws, and '
              'the company’s FY 2025-26 results carried a one-time charge of '
              'about INR 308 crore arising from that implementation, in a year '
              'that was otherwise its strongest on record. Working in an '
              'Industrial Relations function at that moment made the '
              'relationship between statute, documentation and commercial '
              'consequence unusually visible.'),
        ('p', 'One limitation should be restated in summary, because it '
              'qualifies everything above. Eight weeks gave breadth rather than '
              'depth. My involvement in any single sub-function was shallower '
              'than a permanent team member’s, exposure to live Industrial '
              'Relations matters was observational, access to certain systems '
              'and historical data was appropriately restricted, and the period '
              'was too short to see a grievance resolved from origin to closure '
              'or a training intervention change an outcome. I have preferred '
              'to record this plainly rather than imply a depth of involvement '
              'the programme did not permit.'),

        ('h2', '5.2  KEY TAKEAWAYS'),
        ('h3', '5.2.1  Process-Level Thinking'),
        ('bullets', [
            'Understood that HR and Industrial Relations operate as '
            'interconnected processes, in which data from recruitment, the HR '
            'system and Industrial Relations reporting feed a single view used '
            'for organisation-wide decisions.',
            'Observed how recruitment, documentation, analytics, communication '
            'and Learning and Development must work in sequence to sustain a '
            'compliant and engaged workforce.',
            'Learned that an error introduced at one point in that chain '
            'surfaces at several others, which is why validation at the point '
            'of entry matters more than correction later.',
        ]),
        ('h3', '5.2.2  Decision-Making Awareness'),
        ('bullets', [
            'Recognised the importance of accurate, timely Industrial Relations '
            'data in supporting leadership decisions on employee relations and '
            'workforce planning.',
            'Understood how documentation gaps or delayed reporting can allow a '
            'minor issue to escalate into a larger dispute.',
            'Learned to build a report around the decision it supports rather '
            'than around the data that happens to be available.',
        ]),
        ('h3', '5.2.3  Workplace Discipline'),
        ('bullets', [
            'Developed habits of structured reporting, proactive follow-up and '
            'organised documentation, including dated version control on '
            'compliance-relevant drafts.',
            'Maintained punctuality and professionalism in coordinating '
            'time-bound deliverables across several internal stakeholders.',
            'Learned to treat confidentiality and data minimisation as standing '
            'obligations rather than case-by-case judgements.',
        ]),
        ('h3', '5.2.4  Industrial Relations in Practice'),
        ('bullets', [
            'Experienced how a large manufacturer manages Industrial Relations '
            'across multiple plants and several stakeholder groups, each with '
            'its own local dynamics.',
            'Understood that procedural fairness in a unionised environment is '
            'structural rather than discretionary, because collective as well '
            'as individual interests are engaged.',
            'Learned that the preventive work of maintaining conditions in '
            'which disputes do not arise is the larger part of the function, '
            'and the less visible part.',
        ]),
        ('h3', '5.2.5  Digital and Analytical Readiness'),
        ('bullets', [
            'Worked across several HR systems and tools and understood how '
            'digital platforms reduce manual effort while improving the '
            'consistency of records.',
            'Learned to translate raw workforce data into dashboard indicators '
            'that leadership can act upon.',
            'Understood the difference between an activity measure and an '
            'outcome measure, and why the easily counted is not therefore the '
            'meaningful.',
        ]),
        ('h3', '5.2.6  Collaboration and Continuous Improvement'),
        ('p', 'The points below include general process suggestions drawn from '
              'my own experience as an intern. They are offered as '
              'observations rather than as criticism, and any application would '
              'need to fit the organisation’s existing systems and priorities.'),
        ('bullets', [
            'Understood the importance of cross-departmental collaboration in '
            'Industrial Relations, analytics, Learning and Development and '
            'internal communication initiatives.',
            'Built confidence in asking the right questions, incorporating '
            'feedback and contributing within a professional team.',
            'A short glossary of Industrial Relations and HR-technology '
            'terminology, provided at induction, would reduce the initial '
            'learning curve that the first fortnight involved.',
            'A brief mid-internship review checkpoint, in addition to the final '
            'review, would let an intern recalibrate priorities and address '
            'skill gaps earlier in the programme.',
            'Continued expansion of the Employee Relations and Learning and '
            'Development dashboards would be valuable, as these were the tools '
            'that gave both leadership and a newcomer the clearest view of the '
            'function.',
            'Future interns would benefit from keeping a running weekly log of '
            'tools, terminology and processes encountered; my own proved '
            'essential both during the internship and in preparing this '
            'report.',
        ]),

        ('h2', '5.3  CONCLUSION'),
        ('p', 'The eight-week internship at Ashok Leyland Limited was the point '
              'at which my study of Human Resource Management became practical. '
              'Across eight weeks I moved from induction and Industrial '
              'Relations fundamentals, through recruitment and HR technology, '
              'analytics and management reporting, knowledge management, '
              'internal communication and Learning and Development, to '
              'independent research and presentation. In doing so I acquired '
              'skills that are directly employable: Industrial Relations '
              'documentation, management reporting and data consolidation, '
              'dashboard interpretation, HR systems navigation, writing for a '
              'defined reader, stakeholder coordination and research '
              'presentation.'),
        ('p', 'Beyond the technical content, three things changed. First, my '
              'understanding of the function: in a manufacturing organisation '
              'HR operates through documents, data and defined procedure, '
              'because at the scale of a multi-plant workforce nothing else '
              'scales, and the people-facing work rests on that base rather '
              'than replacing it. Second, my understanding of compliance: '
              'having watched an organisation absorb the largest change to '
              'Indian labour law since independence, and having seen its cost '
              'appear in an audited profit and loss account, I can no longer '
              'regard statutory work as peripheral to commercial performance. '
              'Third, my understanding of myself. I learned that I am '
              'comfortable with detailed, procedural work, that I write more '
              'carefully under a professional standard than an academic one, '
              'and that I can present a researched position to people who know '
              'more than I do.'),
        ('p', 'I am equally clear about what remains to be developed: genuine '
              'statutory fluency in the four Labour Codes, stronger analytical '
              'interpretation and automation of recurring reporting, further '
              'practice before senior audiences, and direct rather than '
              'observational experience of engagement with employee '
              'representative bodies. Knowing these gaps specifically, rather '
              'than as a general intention to improve, is itself an outcome of '
              'the internship.'),
        ('p', 'In conclusion, the internship achieved what a Summer Internship '
              'Programme is intended to achieve. It bridged the gap between '
              'theoretical understanding of Human Resource Management, '
              'Organisational Behaviour and Industrial Relations and their '
              'application within a large, substantially unionised '
              'manufacturing organisation, and it settled my career direction '
              'towards Human Resources and Industrial Relations. I am grateful '
              'to the management of Ashok Leyland Limited for the opportunity, '
              'to Mr. Venkatesan Raman for his guidance and review throughout '
              'the period, to Ms. Swetha Krishnamurthy for facilitating the '
              'programme, and to the Industrial Relations, recruitment, '
              'analytics, Learning and Development and communication teams for '
              'explaining their work to me. I leave the organisation with an '
              'accurate sense of what I can currently do, a specific agenda for '
              'what I need to learn next, and the confidence to contribute to a '
              'professional HR or Industrial Relations team.'),
    ],
}

# ---------------------------------------------------------------------------
# CHAPTER 6 - REFERENCES
# ---------------------------------------------------------------------------
CH6 = {
    'num': 6,
    'title': 'REFERENCES',
    'header_left': '',
    'header_right': 'REFERENCES',
    'divider_title': 'REFERENCES',
    'blocks': [
        ('h1', 'REFERENCES'),
        ('p', 'The sources below provide the company, industry and regulatory '
              'context used in this report. The internship-specific content is '
              'based on the work actually assigned to the author during the '
              'period recorded on the internship certificate.'),
        ('bullets', [
            'Ashok Leyland Limited. (n.d.). About us: corporate overview, '
            'manufacturing footprint and product range. Retrieved September '
            '2026, from https://www.ashokleyland.com/in/aboutus',

            'Ashok Leyland Limited. (2026). Annual report and directors’ '
            'report for the financial year ended 31 March 2026.',

            'Ashok Leyland Limited. (2026, July 30). Internship completion '
            'certificate issued to the author.',

            'Business World. (2026). Ashok Leyland FY26: consolidated revenue '
            'of INR 44,007 crore and operating profit before tax of INR 5,163 '
            'crore. Retrieved September 2026, from '
            'https://www.businessworld.in/',

            'Crisil Ratings. (2026). India’s commercial vehicle volumes to '
            'reach 12.4 lakh units in FY27, surpassing the previous peak. As '
            'reported in Economic Times. Retrieved September 2026, from '
            'https://economictimes.indiatimes.com/industry/auto/lcv-hcv/',

            'Darwinbox. (n.d.). Human resource management system: platform '
            'overview and product documentation. Retrieved September 2026, '
            'from https://darwinbox.com/',

            'Economic Times. (2025, November). India implements four Labour '
            'Codes, replacing 29 laws in the biggest labour reform since '
            'independence. Retrieved September 2026, from '
            'https://economictimes.indiatimes.com/news/economy/policy/',

            'Economic Times. (2026a, May). Ashok Leyland Q4 results: FY26 '
            'revenue up 14 per cent to INR 44,007 crore and profit up 8 per '
            'cent to INR 3,566 crore after a one-time charge of INR 308 crore '
            'for the new Labour Code. Retrieved September 2026, from '
            'https://economictimes.indiatimes.com/markets/stocks/earnings/',

            'Economic Times. (2026b, September). Auto sales hit a record high '
            'in FY26; commercial vehicle sales rise 12.6 per cent to 10.8 lakh '
            'units. Retrieved September 2026, from '
            'https://economictimes.indiatimes.com/industry/auto/auto-news/',

            'Economic Times. (2026c). India’s commercial vehicle sales surge as '
            'the GST rate cut releases deferred demand. Retrieved September '
            '2026, from '
            'https://economictimes.indiatimes.com/industry/auto/lcv-hcv/',

            'Employers’ Federation of Southern India. (n.d.). About EFSI: '
            'membership, affiliated associations and representation on '
            'tripartite committees. Retrieved September 2026, from official '
            'federation publications.',

            'EY. (2026, May). Final rules published by the central government '
            'under the new labour codes. Retrieved September 2026, from '
            'https://www.ey.com/en_in/alerts-hub',

            'Hinduja Group. (n.d.). Ashok Leyland Limited: group company '
            'profile. Retrieved September 2026, from '
            'https://hindujagroup.com/ashok-leyland-ltd.html',

            'ICRA. (2026). Indian commercial vehicle industry to register 4 to '
            '6 per cent wholesale growth in FY2027 after 12.6 per cent growth '
            'in FY2026. Retrieved September 2026, from https://www.icra.in/',

            'IMARC Group. (n.d.). India commercial vehicle market size, share '
            'and analysis to 2034. Retrieved September 2026, from '
            'https://www.imarcgroup.com/india-commercial-vehicle-market',

            'Livemint. (2026, May). Ashok Leyland posts highest-ever quarterly '
            'profit after tax; dividend declared. Retrieved September 2026, '
            'from https://www.livemint.com/market/stock-market-news/',

            'PwC India. (2025, November). New labour codes: the Code on Wages, '
            '2019, the Industrial Relations Code, 2020, the Code on Social '
            'Security, 2020 and the Occupational Safety, Health and Working '
            'Conditions Code, 2020, effective 21 November 2025. Retrieved '
            'September 2026, from '
            'https://www.pwc.in/tax-knowledge-hub/new-labour-codes.html',

            'Society of Indian Automobile Manufacturers. (2026). Automobile '
            'wholesales in India reach a record 2.83 crore units in FY26. As '
            'reported in The Hindu. Retrieved September 2026, from '
            'https://www.thehindu.com/business/Industry/',

            'The Hindu. (2026). Indian automobile industry closes FY26 with '
            'every vehicle category at its highest ever annual sales. '
            'Retrieved September 2026, from '
            'https://www.thehindu.com/business/Industry/',
        ]),
    ],
}

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]
