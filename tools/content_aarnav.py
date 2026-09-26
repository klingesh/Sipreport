# -*- coding: utf-8 -*-
"""
Content of the Summer Internship Project report of Aarnav Rupesh. K,
MBA (Marketing major, Logistics minor), ISSM Business School, Chennai.

Internship: Ecosoft Zolutions Pvt Ltd, Ambattur, Chennai
Department: Sales | Designation: Business Development Executive
Period: 20.05.2026 to 31.07.2026 (as recorded on the internship certificate)
Certificate dated 6 August 2026, signed by Mr. Santharaj Periyasamy, Director.
Certificate records the assignments as relating to Pune Market Expansion.

PLACEHOLDERS - the author asked that nothing be invented. Every unresolved
item below appears as [SQUARE-BRACKET CAPITALS] and can be found with one
search:
    [NAME OF CHAIRMAN]                    ISSM office bearers were not
    [NAME OF FOUNDER AND MANAGING DIRECTOR]   supplied; the author asked that
    [NAME OF ACADEMIC HEAD]               they not be copied from another
                                          student's report
    [NAME OF INDUSTRY GUIDE]              no individual supervisor was named
                                          apart from the corporate trainer
    [TO BE PROVIDED]                      facts the author has not yet given

NOTE ON THE REGISTER NUMBER: the internship certificate reads
"Reg No: ISSMCHNM250112"; the author's written brief gives "OSI2511003". The
certificate is used here because the author asked that it be treated as
authoritative, but the two disagree and the point needs settling.

Block vocabulary is documented in report_content.py.
"""

STUDENT = 'AARNAV RUPESH. K'
REG_NO = 'ISSMCHNM250112'
FIRM = 'Ecosoft Zolutions Pvt Ltd'
FIRM_SHORT = 'Ecosoft Zolutions'
MENTOR = '[NAME OF INDUSTRY GUIDE]'
MENTOR_ROLE = ''
PERIOD = '20th May 2026 to 31st July 2026'

EMBED_CERTIFICATE = False

# The sample reports list chapters only in the contents table, so the page is
# filled by giving those rows generous, evenly spaced heights.
TOC_ROW_HEIGHT = 1550

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
          'authentic record of **Mr. Aarnav Rupesh. K** (ISSMCHNM250112) '
          'carried out at M/s. Ecosoft Zolutions Pvt Ltd, Chennai, in partial '
          'fulfilment of the requirements for the award of the MBA degree.'),
    ('gap', 1),
    ('p', 'The internship was completed in the Sales Department of M/s. '
          'Ecosoft Zolutions Pvt Ltd during the period from May 20th to July '
          '31st, 2026, and the internship certificate was issued on 6 August '
          '2026 under the authorised signature of **Mr. Santharaj '
          'Periyasamy**, Director.'),
    ('gap', 4),
    ('p', '**[NAME OF ACADEMIC HEAD]**', 14),
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
    ('p', 'I, **Mr. Aarnav Rupesh. K**, hereby declare that this SIP Project '
          'Report is based on my three-month internship done at Ecosoft '
          'Zolutions Pvt Ltd, SP75, Sidco Industrial Estate, Ambattur, '
          'Chennai, as a Business Development Executive in the Sales '
          'Department, during the period from May 20th to July 31st, 2026, '
          'under the guidance of the Sales Department of Ecosoft Zolutions Pvt '
          'Ltd and Indian School of Science and Management, Chennai.'),
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
    ('p', 'I have undergone extensive training to complete this internship, '
          'and it would not have been possible without the kind support of '
          'many individuals. I am using this opportunity to express my '
          'gratitude to everyone who supported me throughout the period.'),
    ('p', 'I would like to express my sincere gratitude to our respected '
          'Chairman, **[NAME OF CHAIRMAN]**, for providing us with the '
          'valuable opportunity to carry out and complete this project.'),
    ('p', 'I express my heartfelt thanks to our Founder and Managing '
          'Director, **[NAME OF FOUNDER AND MANAGING DIRECTOR]**, for the '
          'continuous support and meaningful guidance which played a key role '
          'in our progress.'),
    ('p', 'I am highly indebted to our Academic Head, **[NAME OF ACADEMIC '
          'HEAD]**, for guidance and constant supervision, for providing the '
          'necessary information regarding the project and for support in '
          'completing it.'),
    ('p', 'I would also like to thank all the faculty members and staff of '
          'ISSM Business School who provided me with the facilities and the '
          'conducive conditions that were required for this project.'),
    ('p', 'My sincere gratitude to **Mr. Santharaj Periyasamy**, Director, '
          'Ecosoft Zolutions Pvt Ltd, for permitting me to undergo my Summer '
          'Internship Programme with the organisation, and to **Mr. Vester '
          'Anandaraj**, who conducted the corporate training and orientation '
          'during my first weeks at Chennai and from whose guidance my '
          'understanding of the sales function began.'),
    ('p', 'I am also thankful to the members of the Sales Department and to '
          'the colleagues who explained their work to me and made it '
          'possible for me to take part in the Pune Market Expansion '
          'assignments.'),
    ('pagebreak',),

    # ---- executive summary ----
    ('gap', 1),
    ('big', 'The Executive Summary', 12),
    ('gap', 1),
    ('p', 'This report presents the work carried out during my Summer '
          'Internship Programme at Ecosoft Zolutions Pvt Ltd, a Chennai based '
          'software and web development company at Sidco Industrial Estate, '
          'Ambattur. I worked in the Sales Department as a Business '
          'Development Executive from 20 May 2026 to 31 July 2026, and the '
          'certificate records my assignments as relating to Pune Market '
          'Expansion.'),
    ('p', 'The internship moved between two locations and two kinds of work. '
          'The first fortnight was spent at Chennai in training and '
          'orientation under **Mr. Vester Anandaraj**, covering the company, '
          'sales and business development activity, professional '
          'communication, lead generation and the relationship between a '
          'business requirement and a software solution. Two students from '
          'ISSM were then selected for the Pune assignment, and I spent about '
          'a week in the Pune and Chakan industrial belt, where I generated '
          'leads from three companies.'),
    ('p', 'Two to three weeks back at Chennai followed, given to client '
          'follow-up, telephone calls, company visits, and the requirement '
          'work I had not expected in a sales role: understanding what a '
          'client was asking for, preparing Software Requirements '
          'Specification documents and roadmaps. A second Pune and Chakan '
          'assignment of about two weeks followed, weighted towards existing '
          'client relationships and including interaction at Hyundai.'),
    ('p', 'Alongside this I prepared Month-End Review Meeting material in '
          'Microsoft PowerPoint, Figma and Microsoft Power BI. My technical '
          'exposure was introductory: I worked on requirements and '
          'documentation in a software-oriented company, and this report '
          'claims no programming or deployment work.'),
    ('p', 'Professionally, the internship gave me three things a classroom '
          'cannot: the experience of representing a company to a stranger in '
          'an unfamiliar market, an understanding that a requirement has to be '
          'heard before it can be written, and the discipline of following up '
          'without being told to. It connected my MBA study of sales '
          'management, business communication, customer relationship '
          'management and business analysis to work I can now perform.'),
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

        ('h2', '1.1  THE INDIAN SOFTWARE AND IT SERVICES INDUSTRY'),
        ('p_indent', 'Ecosoft Zolutions operates in the Indian software and '
                     'information technology services industry, and the scale '
                     'of that industry is worth establishing before describing '
                     'a single company within it. According to the annual '
                     'strategic review of the National Association of Software '
                     'and Service Companies, the Indian technology sector was '
                     'expected to record revenues of about USD 315 billion in '
                     'the 2026 financial year, a growth of 6.1 per cent over '
                     'the USD 282.6 billion of the previous year (NASSCOM, as '
                     'reported in Economic Times, 2026).'),
        ('p', 'Within that total, information technology services accounted for '
              'approximately USD 149 billion, engineering research and '
              'development for about USD 63 billion, business process '
              'management for around USD 59 billion and software products for '
              'about USD 23 billion (Times of India, 2026). Exports were '
              'expected to exceed USD 246 billion and sector headcount to '
              'reach about 5.95 million people (CNBC TV18, 2026).'),
        ('p', 'Those figures describe the industry as a whole, and it is '
              'important not to read them as a description of the company I '
              'worked for. The great majority of that revenue belongs to a '
              'small number of very large firms. The sector also contains '
              'several thousand small and medium software companies which '
              'build custom applications for Indian businesses, and it is in '
              'that part of the industry that my internship took place. The '
              'relevance of the national figures to a company of that size is '
              'indirect: they establish that demand for software services is '
              'growing, that clients across manufacturing and services are '
              'buying, and that the market a business development team calls '
              'into is expanding rather than contracting.'),
        ('p', 'One further characteristic of this industry matters for a sales '
              'role. Software is an intangible, configured product. A '
              'prospective client cannot inspect it in advance, compare it on '
              'a shelf or judge it by weight, and what is actually being sold '
              'is a promise that a described business problem will be solved. '
              'That single fact shapes everything a business development '
              'executive in this sector does, and it is the reason the work I '
              'was given moved so quickly from selling towards understanding '
              'requirements.'),

        ('h2', '1.2  CUSTOM SOFTWARE DEVELOPMENT AND THE B2B SALES ENVIRONMENT'),
        ('p', 'Custom software development is a business-to-business activity '
              'with a long and consultative sales cycle. The buyer is an '
              'organisation rather than an individual, the decision usually '
              'involves several people with different concerns, and the '
              'evaluation extends over weeks or months. A purchasing manager '
              'may be concerned with cost, an operations head with disruption '
              'during changeover, and a technical lead with whether the '
              'proposed approach will work at all. A single message cannot '
              'satisfy all three.'),
        ('p', 'The practical consequence is that business development in this '
              'setting is not order taking. The sequence runs from identifying '
              'organisations that plausibly have the problem the company '
              'solves, through establishing contact and earning a hearing, to '
              'understanding the specific business need well enough to propose '
              'something credible, and only then to commercial discussion. '
              'Each of those stages can fail, and the earlier stages consume '
              'most of the effort. This is the sequence the reader will '
              'recognise in Chapter 2, because it is the sequence my own work '
              'followed.'),
        ('h2', '1.3  COMPANY OVERVIEW: ECOSOFT ZOLUTIONS PRIVATE LIMITED'),
        ('h3', '1.3.1  BACKGROUND AND REGISTERED PARTICULARS'),
        ('p', 'Ecosoft Zolutions Pvt Ltd is a private limited company based in '
              'Chennai, Tamil Nadu. Its particulars, as recorded on the '
              'company letterhead of the internship certificate issued to me, '
              'are set out in the table below. A third-party business '
              'directory describes the organisation as working in custom web '
              'application development and software services, including web '
              'development, mobile application development and software '
              'outsourcing (CB Insights, n.d.).'),
        ('table', {'rows': [
            ['Particular', 'Detail'],
            ['Name', 'Ecosoft Zolutions Pvt Ltd'],
            ['Registered address',
             'SP75, 4th Floor, Sidco Industrial Estate, Ambattur, Chennai – '
             '600 058, Tamil Nadu'],
            ['Landmark', 'Dexterity Building'],
            ['GSTIN', '33AAFCE6509C1Z2'],
            ['PAN', 'AAFCE6509C'],
            ['Business domain',
             'Software and web application development and related services'],
            ['Department of internship', 'Sales'],
            ['Authorised signatory on the certificate',
             'Mr. Santharaj Periyasamy, Director'],
        ], 'widths': [3, 7], 'col_bold': [True, False],
            'col_align': ['center', 'left']}),
        ('p', 'I have to be explicit about the limits of what this report can '
              'say about the organisation. Detailed and independently verified '
              'public information about the company, of the kind that would '
              'support statements about its founding year, ownership history, '
              'employee numbers, client list, revenue, service lines in detail '
              'or organisational structure, was not available to me, and I was '
              'not given internal documents covering those matters. I have '
              'therefore not stated them. Where a reader of an academic report '
              'would expect such detail, the correct entry is [TO BE '
              'PROVIDED], and I would rather leave the gap visible than fill '
              'it with plausible invention.'),
        ('p', 'What I can describe is the company as it appeared to a member '
              'of its sales function over three months. It is an owner-managed '
              'organisation of a size at which a Director signs an intern’s '
              'certificate personally. It works in the software and web '
              'development domain, which means its output is bespoke rather '
              'than packaged. It maintains a Sales Department with a distinct '
              'business development function, and that function was active '
              'enough during my internship to justify sending staff to another '
              'state to open a new market. It also invests in structured '
              'induction, since my own first fortnight was given to training '
              'rather than to output.'),

        ('h3', '1.3.2  THE SALES FUNCTION AND ITS SERVICE DOMAIN'),
        ('p', 'The activities visible to me were those of the Sales '
              'Department rather than of the development teams. The table below '
              'sets out the functions I observed and the purpose each served, '
              'and it is confined to what I actually saw.'),
        ('table', {'rows': [
            ['Activity', 'Nature of Work', 'Purpose'],
            ['Prospect identification',
             'Identifying organisations that might need custom software, in '
             'Chennai and in the Pune and Chakan belt',
             'Building a pipeline of organisations worth approaching'],
            ['Lead generation',
             'Establishing contact and converting an identified organisation '
             'into a live prospect',
             'Creating opportunities the company can pursue commercially'],
            ['Client and customer follow-up',
             'Telephone calls and physical visits to keep a conversation alive '
             'and move it forward',
             'Preventing an opened opportunity from lapsing through neglect'],
            ['Requirement understanding',
             'Listening to what a client needs and discussing it with business '
             'representatives',
             'Establishing whether and how the company can help before '
             'anything is promised'],
            ['Requirement documentation',
             'Preparing Software Requirements Specification documents and '
             'project roadmaps',
             'Converting a spoken business need into a form colleagues can '
             'act on'],
            ['Client relationship management',
             'Maintaining contact with existing clients and identifying '
             'further needs',
             'Retaining and extending relationships already won'],
            ['Management reporting',
             'Preparing Month-End Review Meeting material in PowerPoint, '
             'Figma and Power BI',
             'Giving management a periodic, comparable view of sales activity'],
        ], 'widths': [3, 5, 4], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left']}),
        ('h2', '1.4  THE PUNE AND CHAKAN INDUSTRIAL MARKET'),
        ('p', 'Because my internship certificate records my assignments as '
              'relating to Pune Market Expansion, the market itself deserves '
              'description. This section draws on public sources and is '
              'separate from the account of my own work, which appears in '
              'Chapter 2.'),

        ('h3', '1.4.1  THE CHAKAN AND TALEGAON BELT'),
        ('p', 'Chakan, on the northern edge of Pune, has developed over the '
              'past two decades into one of India’s principal automobile '
              'manufacturing clusters. Bajaj Auto was the first major '
              'industrial unit to establish there, and the belt now extends '
              'over an area of roughly 4,000 hectares and hosts units of '
              'Hyundai, Mercedes-Benz, Skoda, Mahindra and Volkswagen among '
              'others, together with several hundred ancillary and '
              'component-making firms (Indian Express, 2026a). Mahindra and '
              'Mahindra announced in July 2026 that its Chakan plant had '
              'crossed three million cumulative vehicles produced (Mahindra '
              'and Mahindra, 2026).'),
        ('p', 'The belt’s advantage is its position on the corridor between '
              'Pune and Mumbai, which gives manufacturers access to a port, to '
              'a large engineering labour market and to national highways '
              '(Indian Express, 2026b). Its commercial weight is visible in '
              'logistics demand: the Chakan and Talegaon belt accounted for '
              'close to 80 per cent of Pune’s warehouse leasing activity '
              'according to a market study by Knight Frank India (Knight Frank '
              'India, as reported in Times of India, 2026).'),
        ('p', 'The belt is not without difficulty, and an honest market '
              'description should say so. During 2026 a group of about twenty '
              'automotive companies in the area wrote to the Maharashtra '
              'government seeking a dedicated cell to address infrastructure '
              'problems which they said were affecting productivity, with some '
              'indicating that they were considering relocation (The Print, '
              '2026). A market being opened by a new entrant is therefore an '
              'active market rather than a settled one.'),

        ('h3', '1.4.2  WHY AN INDUSTRIAL BELT MATTERS TO A SOFTWARE VENDOR'),
        ('p', 'A dense industrial cluster is attractive to a software services '
              'company for reasons that became clear to me only after visiting '
              'one. The first is concentration. Several hundred potential '
              'client organisations within a short travelling distance means '
              'that a single visit of a few days can support many '
              'conversations, which is not true of a dispersed market.'),
        ('p', 'The fourth reason is the one I would not have anticipated. '
              'Manufacturing clients are accustomed to dealing with vendors in '
              'person, and a supplier who travels from another state to '
              'discuss a requirement is treated differently from one who '
              'telephones. The cost of travel buys a kind of attention that no '
              'amount of electronic communication produces, and that is a '
              'commercial judgement rather than a courtesy.'),

        ('h3', '1.4.3  MARKET ENTRY CONSIDERATIONS'),
        ('p', 'Entering a market of this kind involves difficulties that a '
              'classroom discussion of market entry does not convey. An '
              'entrant has no local reputation, no reference client in the '
              'region and no existing relationships, and it is competing '
              'against vendors who have all three. Language and regional '
              'business convention differ from those of the home market. The '
              'sales cycle is lengthened by the need to establish credibility '
              'before a requirement will even be discussed.'),
        ('h2', '1.5  SWOT ANALYSIS'),
        ('p', 'The following analysis is my own assessment, based on what was '
              'observable to me during three months in the Sales Department '
              'and on the public information about the industry and the Pune '
              'market cited above. It is offered as a student’s view and not as '
              'an internal strategic review, and it deliberately avoids claims '
              'about financial or commercial matters I was not in a position '
              'to verify.'),

        ('h3', '1.5.1  STRENGTHS'),
        ('bullets', [
            '**Bespoke capability:** the company builds software to a client’s '
            'requirement rather than selling a fixed product, which allows it '
            'to pursue opportunities a packaged vendor would have to decline.',
            '**Short internal distance:** in an organisation where a Director '
            'signs an intern’s certificate, the route from a client '
            'conversation to a decision is short, and a prospect’s question '
            'can be answered quickly.',
            '**Willingness to invest in new markets:** committing staff, '
            'travel and accommodation to open the Pune and Chakan belt '
            'indicates a company prepared to pursue growth beyond its home '
            'city.',
            '**Combined sales and requirement capability:** the same person '
            'carries an opportunity from first contact through to requirement '
            'documentation, which avoids the loss of context that a handover '
            'between departments causes.',
            '**Structured induction:** a documented training and orientation '
            'period for new entrants, which is not universal in organisations '
            'of this size.',
            '**Chennai base:** a location in an established industrial and '
            'technology estate, with access to both a technical labour market '
            'and a substantial local client base.',
        ]),

        ('h3', '1.5.2  WEAKNESSES'),
        ('bullets', [
            '**Limited public visibility:** independently verifiable '
            'information about the company is scarce, which matters when a '
            'prospective client in an unfamiliar market tries to assess a new '
            'vendor.',
            '**No regional reference client at entry:** entering the Pune belt '
            'without a local reference lengthens the sales cycle, since '
            'credibility has to be built from nothing.',
            '**Dependence on individual relationships:** where one person '
            'holds a prospect from first contact to documentation, that '
            'person’s absence interrupts the opportunity.',
            '**Cost of in-person selling at distance:** travel and stay for '
            'each market visit is a real charge against a small number of '
            'conversations, which constrains how often the market can be '
            'worked.',
            '**Competition for technical attention:** in a small company the '
            'colleagues who answer a prospect’s technical question are the '
            'same colleagues delivering existing work.',
        ]),

        ('h3', '1.5.3  OPPORTUNITIES'),
        ('bullets', [
            '**A growing national market:** Indian technology sector revenues '
            'of about USD 315 billion in the 2026 financial year, growing at '
            '6.1 per cent, indicate expanding demand for software services '
            '(NASSCOM, as reported in Economic Times, 2026).',
            '**Concentration in the target market:** an industrial belt of '
            'roughly 4,000 hectares containing units of several major '
            'manufacturers and hundreds of ancillary firms offers a dense '
            'pipeline within a short travelling distance (Indian Express, '
            '2026a).',
            '**Digitisation of mid-sized manufacturing:** smaller '
            'manufacturing units that previously managed operations on '
            'spreadsheets are candidates for custom applications.',
            '**Supplier networks around anchor plants:** a relationship with '
            'one unit in a cluster creates access to the suppliers around it.',
            '**Existing clients as a source of further work:** the second Pune '
            'assignment showed that additional requirements can be identified '
            'within a relationship already established, which is cheaper than '
            'winning a new client.',
        ]),

        ('h3', '1.5.4  THREATS'),
        ('bullets', [
            '**Established regional vendors:** local software suppliers in '
            'Pune hold the relationships and references an entrant lacks.',
            '**Large services firms:** national and global providers compete '
            'for the same clients with brand recognition an owner-managed '
            'company cannot match.',
            '**Infrastructure pressure in the target belt:** the '
            'representations made by around twenty automotive companies to the '
            'Maharashtra government during 2026, and the relocation these '
            'firms indicated they were considering, introduce uncertainty into '
            'a market being entered (The Print, 2026).',
            '**Low-cost and low-code alternatives:** tools that let a client '
            'assemble a simple application without a vendor reduce demand at '
            'the straightforward end of the market.',
            '**Lengthening decision cycles:** discretionary software spending '
            'is among the first items deferred when a manufacturing client’s '
            'own market tightens.',
        ]),

        ('h2', '1.6  KEY COMPETITORS'),
        ('p', 'I was not given a competitor list, and I have not invented one. '
              'What follows describes the categories of competitor that a '
              'business development executive in this position encounters, '
              'grouped by the kind of competition each represents. No '
              'individual competing company is named, because naming one '
              'without evidence would be fabrication.'),

        ('h3', '1.6.1  REGIONAL AND LOCAL SOFTWARE COMPANIES'),
        ('table', {'rows': [
            ['Competitor Type', 'Typical Proposition', 'Competitive Effect'],
            ['Local Pune software firms',
             'Custom development with an established presence in the region '
             'and local references',
             'The most direct obstacle to a new entrant, since they hold the '
             'relationships and the reference sites a prospect asks about'],
            ['Chennai-based peers',
             'Comparable bespoke capability competing for the same home-market '
             'clients',
             'Compete on portfolio and on the personal relationships of their '
             'own sales staff'],
        ], 'widths': [3, 4, 5], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left']}),

        ('h3', '1.6.2  LARGE SERVICES AND PRODUCT VENDORS'),
        ('table', {'rows': [
            ['Competitor Type', 'Typical Proposition', 'Competitive Effect'],
            ['National IT services firms',
             'Scale delivery, recognised brand and procurement familiarity',
             'Compete for the larger clients in the belt on brand and on the '
             'ability to absorb programme risk'],
            ['Packaged software and ERP vendors',
             'A configured product with a published feature set and an '
             'implementation partner network',
             'Compete wherever a standard product can meet the need, on '
             'predictability of cost and timeline'],
        ], 'widths': [3, 4, 5], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left']}),

        ('h3', '1.6.3  LOW-COST AND INTERNAL ALTERNATIVES'),
        ('table', {'rows': [
            ['Competitor Type', 'Typical Proposition', 'Competitive Effect'],
            ['Freelance and very small developers',
             'Low-cost delivery of narrowly defined work',
             'Compete on price where the requirement is small and fully '
             'specified'],
            ['Low-code and spreadsheet alternatives',
             'Tools allowing a client to assemble a simple solution without a '
             'vendor',
             'Compete at the straightforward end of the market and postpone '
             'the decision to buy'],
            ['The client’s own staff',
             'Internal development or continuing with existing manual methods',
             'Competes as the option of not buying at all, which any '
             'proposition has to answer implicitly'],
        ], 'widths': [3, 4, 5], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left']}),

        ('h2', '1.7  COMPETITIVE POSITIONING'),
        ('p', 'The competitive logic of custom software services is that a '
              'client is not really choosing between feature lists. It is '
              'deciding which supplier appears most likely to understand its '
              'problem and to remain engaged until the problem is solved. '
              'Scale, brand and price all bear on that judgement, but none of '
              'them settles it, which is what allows a smaller company to win '
              'work against a larger one.'),
        ('p', 'The corresponding weakness is credibility at first contact, and '
              'this is exactly what a market expansion assignment exists to '
              'address. A prospect in a new region has no basis on which to '
              'trust an unfamiliar vendor, and the only available remedies are '
              'to turn up in person, to demonstrate understanding of the '
              'client’s business quickly, and to follow up reliably enough '
              'that reliability itself becomes evidence. Watching that process '
              'and taking part in it was the substance of my internship.'),

        ('h2', '1.8  KEY MILESTONES'),
        ('p', 'On the matter of company milestones I have to be direct about '
              'what this report cannot state. I was not given the company’s '
              'founding year, incorporation history, funding history, '
              'ownership changes, client acquisitions, revenue history or '
              'employee numbers at any date, and reliable independent sources '
              'for those facts were not available to me. A milestone table '
              'invented from plausible-looking dates would be worse than no '
              'table at all, and I have therefore not produced one. The '
              'correct entry for a dated company history is [TO BE PROVIDED].'),
        ('p', 'What can be recorded is the stage of development that was '
              'visible in the nature of the work being done during my three '
              'months. An organisation that commits travel and accommodation '
              'to place staff in another state, that is prepared to send '
              'students on that assignment, and that is simultaneously '
              'servicing existing clients in that region is an organisation in '
              'an expansion phase rather than a consolidation one. The '
              'presence of both first-contact prospecting and existing-client '
              'requirement work in the same market, across my two assignments, '
              'indicates a market that had been entered and was being '
              'developed rather than one being tested for the first time.'),
        ('p', 'For a student of management, the lesson in a company at this '
              'stage is that market entry is not a strategic decision followed '
              'by an outcome. It is a long series of small, unglamorous acts: '
              'identifying a company, finding the right person, earning a '
              'hearing, understanding a requirement, writing it down '
              'accurately and going back when promised. The strategy is only '
              'the instruction to begin.'),

        ('p', 'That, in the end, is the value of the industry and market '
              'material in this chapter: it explains why the company was '
              'sending people to Pune at all, and therefore why an intern '
              'spent three months doing what Chapter 2 describes.'),
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
        ('p_indent', 'The purpose of the internship was to convert the sales, '
                     'marketing and communication concepts studied in the MBA '
                     'programme into practical work inside a functioning '
                     'software company. The internship was carried out at '
                     'Ecosoft Zolutions Pvt Ltd, Ambattur, Chennai, from 20 '
                     'May 2026 to 31 July 2026, a period of three months, in '
                     'the Sales Department with the designation of Business '
                     'Development Executive. The internship certificate records '
                     'my assignments as relating to Pune Market Expansion.'),
        ('p', 'The objectives set for the period were the following.'),
        ('bullets', [
            'To understand how a software company identifies prospective '
            'clients and converts them into live business opportunities.',
            'To learn lead generation in practice, in the home market and in a '
            'market the company was entering.',
            'To develop professional communication by telephone and in person '
            'with corporate representatives.',
            'To understand how a client’s business need is heard, discussed and '
            'recorded.',
            'To gain exposure to business analysis activity, including '
            'Software Requirements Specification documents and project '
            'roadmaps.',
            'To learn how existing client relationships are maintained and how '
            'further requirements are identified within them.',
            'To prepare material for Month-End Review Meetings and so '
            'understand how sales activity is reported to management.',
            'To develop the professional habits the work depends on: '
            'punctuality, follow-up, record-keeping and adapting to an '
            'unfamiliar business environment.',
        ]),
        ('p', 'It is equally important to state what the internship was not. I '
              'was appointed to a sales role and my technical exposure was '
              'introductory throughout. I did not develop software, write '
              'production code, design a database, build an interface or deploy '
              'a system, and nothing in this report should be read as claiming '
              'otherwise. Where this report discusses requirements or software '
              'documentation, it describes work of understanding, discussion '
              'and writing, carried out by a business development trainee in a '
              'software-oriented company.'),

        ('h3', '2.1.1  METHODOLOGY AND APPROACH'),
        ('p', 'The internship was organised as a sequence of phases rather than '
              'as a single continuous assignment: training at Chennai, a first '
              'field assignment in the Pune and Chakan belt, a Chennai period '
              'of follow-up and documentation, and a second Pune assignment. '
              'Each phase built on the one before it, and the degree of '
              'independence expected of me increased at each stage.'),
        ('h2', '2.2  INITIAL TRAINING AND ORIENTATION AT CHENNAI'),
        ('p', 'The first fortnight of the internship was spent at Chennai in '
              'training and orientation, conducted with guidance from **Mr. '
              'Vester Anandaraj**, the corporate trainer. The period was given '
              'to understanding rather than to output, which in retrospect was '
              'the right allocation: I could not have approached a prospective '
              'client credibly without first understanding what the company '
              'does and how it works.'),
        ('p', 'The orientation covered the following ground.'),
        ('bullets', [
            'The company and its working environment, including how the Sales '
            'Department relates to the technical side of the business.',
            'Sales and business development activities, and the sequence by '
            'which an unknown organisation becomes a client.',
            'Professional communication, in particular how to speak to a '
            'corporate representative one has not met before.',
            'Lead generation, and the distinction between a name on a list and '
            'a live opportunity.',
            'The relationship between a business requirement and a software '
            'solution, which was the conceptual bridge between the sales role '
            'and the company’s technical work.',
            'Basic exposure to software and web development concepts, '
            'sufficient to follow a technical discussion without claiming to '
            'contribute to it.',
        ]),
        ('h2', '2.3  WORK PLAN AND SCOPE'),
        ('p', 'The work fell into eight areas, described below. The first four '
              'are the business development activities proper; the next three '
              'are the requirement and documentation work that arose from '
              'them; the last is management reporting. They were not separate '
              'jobs, and in practice a single client conversation could touch '
              'five of them.'),

        ('h3', '2.3.1  Lead Generation and Prospect Identification'),
        ('p', 'Lead generation was my principal responsibility, and it was the '
              'work that occupied most of both Pune assignments. It began with '
              'identifying organisations that plausibly needed the kind of '
              'software the company builds, which in the Chakan belt meant '
              'manufacturing and ancillary units. It continued with '
              'establishing who within such an organisation would be the right '
              'person to approach, and then with making that approach.'),
        ('p', 'During the first Pune assignment I generated leads from three '
              'companies. I have deliberately not named them in this report, '
              'because I am not in a position to publish client and prospect '
              'identities. The substantive point is not the count but what '
              'producing it taught me: that a lead is not a contact detail but '
              'a conversation in which an organisation has expressed an actual '
              'interest, and that reaching that point takes several '
              'unsuccessful approaches for each successful one.'),
        ('bullets', [
            'Identifying potential companies within the target market and '
            'assessing whether the company’s services were relevant to them.',
            'Finding new prospects through field visits, enquiry and '
            'observation of the industrial belt.',
            'Establishing contact and securing a hearing, which in an '
            'unfamiliar market is the hardest single step.',
            'Recording what had been discussed and what the agreed next step '
            'was, so that a conversation could be resumed later.',
        ]),

        ('h3', '2.3.2  Business Development and Sales Activities'),
        ('p', 'Business development extended beyond first contact into the work '
              'of turning interest into an opportunity. This meant explaining '
              'what the company does in terms that mattered to the particular '
              'organisation, judging whether a stated interest was genuine, and '
              'exploring where a commercial possibility might exist. In a new '
              'market it also meant a great deal of simply being present: '
              'walking an industrial estate, noting which units existed, and '
              'building an understanding of the market that no list could have '
              'supplied.'),
        ('h3', '2.3.3  Client and Customer Follow-Up'),
        ('p', 'Follow-up was the continuous thread of the Chennai periods, and '
              'it is the activity I most underestimated at the start. An '
              'opportunity opened in the field does not advance by itself. It '
              'requires a telephone call at an appropriate interval, a '
              'recollection of what was previously agreed, and a reason for '
              'making contact again that is useful to the recipient rather '
              'than merely convenient to me.'),
        ('p', 'The work consisted of professional telephone conversations with '
              'clients and prospects, follow-up on requirements and enquiries '
              'raised earlier, and keeping track of which conversations were '
              'awaiting a response from which side. I learned that the '
              'difference between diligent follow-up and nuisance is judged '
              'entirely by the person receiving the call, and that the '
              'judgement turns on interval, relevance and whether the previous '
              'discussion has evidently been remembered.'),

        ('h3', '2.3.4  Client and Company Visits'),
        ('p', 'I visited several companies during the internship, in Chennai '
              'and in the Pune and Chakan belt. One visit I particularly '
              'remember was to Yamaha Music. I have not described the purpose, '
              'discussion or outcome of that visit, because doing so beyond '
              'what I can actually attest would be invention; the visit is '
              'recorded here because it formed part of my exposure to '
              'corporate environments.'),
        ('h3', '2.3.5  Business Analysis and Requirement Understanding'),
        ('p', 'Although my designation was Business Development Executive, a '
              'substantial part of my work turned out to be business analysis '
              'exposure. This was not a separate assignment but a consequence '
              'of the sales work: once a prospect begins describing what it '
              'needs, somebody has to understand that need precisely enough for '
              'the company to respond, and in a small organisation that '
              'somebody is often the person who opened the conversation.'),
        ('p', 'The single most valuable distinction I learned here is between '
              'a business requirement and a technical requirement. A client '
              'says that invoices take too long to reach customers; that is a '
              'business requirement. What a system must therefore do is a '
              'technical requirement, and it is not the client’s job to state '
              'it. Confusing the two produces either a document the developer '
              'cannot use or a solution the client did not ask for. I should '
              'record clearly that my role in this was to understand and '
              'document, as a trainee gaining exposure, and not to act as an '
              'experienced business analyst.'),

        ('h3', '2.3.6  Software Requirements Specification Documentation'),
        ('p', 'One of the more substantial parts of my internship was working '
              'on Software Requirements Specification documents. An SRS is the '
              'document that records what a proposed system is required to do, '
              'written so that the client can confirm it and the development '
              'team can build from it. It typically sets out the purpose and '
              'scope of the system, the users and their needs, the functions '
              'the system must perform, the constraints under which it must '
              'operate and the criteria by which it will be accepted.'),
        ('p', 'Requirement documentation of this kind is a recognised '
              'engineering discipline rather than an administrative habit. The '
              'long-standing reference was the IEEE recommended practice for '
              'software requirements specifications, IEEE 830-1998, which set '
              'out the content and qualities of a good specification (IEEE, '
              'n.d.-a). It has since been superseded by the international '
              'standard for requirements engineering, ISO, IEC and IEEE 29148, '
              'published in 2011 and revised in 2018, which places requirements '
              'work within the wider system life cycle and defines what makes a '
              'requirement well formed (IEEE, n.d.-b). Many organisations still '
              'refer to the earlier document by name (TechTarget, n.d.).'),
        ('h3', '2.3.7  Roadmap Preparation'),
        ('p', 'I was also involved in preparing roadmaps relating to client, '
              'business and project requirements. A roadmap differs from a '
              'specification in purpose: where a specification records what is '
              'required, a roadmap records the order in which it is to be '
              'approached and how the work is expected to progress. It is a '
              'communication document, and its audience is usually the client '
              'and the management of both organisations rather than the '
              'developer.'),
        ('p', 'As with the specification work, I have not set out specific '
              'timelines, milestones, technologies or deliverables from any '
              'roadmap I worked on. Those belong to the projects concerned, and '
              'I do not have permission or documentation to publish them.'),

        ('h3', '2.3.8  Month-End Review Meeting Preparation'),
        ('p', 'I was involved in preparing presentations and visual material '
              'for Month-End Review Meetings, the periodic internal review at '
              'which activity and progress are presented to management. The '
              'tools used were Microsoft PowerPoint for the presentation '
              'itself, Figma for visual and layout work, and Microsoft Power BI '
              'for reporting and visualisation of data.'),
        ('p', 'I should be precise about my role. I prepared presentation and '
              'reporting material; I did not set the indicators being reported, '
              'nor did I take part in management decisions arising from those '
              'meetings. I have not reproduced any figures, indicators, '
              'dashboard values or decisions in this report, because those are '
              'internal to the company.'),

        ('h2', '2.4  TIMELINE OF ACTIVITIES'),
        ('p', 'The internship ran from 20 May 2026 to 31 July 2026, the dates '
              'recorded on the internship certificate. Because 20 May fell on '
              'a Wednesday, the first week was a short one and the remaining '
              'weeks ran from Monday to Friday, with the programme closing on '
              'Friday 31 July. The record below follows that calendar and '
              'reflects the phase structure described above. Where the exact '
              'week of an activity is not something I can attest precisely, the '
              'entry describes the phase rather than claiming a specific date.'),

        ('h3', 'Weeks 1 and 2 (20 May – 29 May 2026): Training at Chennai'),
        ('bullets', [
            'Induction to the company, its working environment and the Sales '
            'Department.',
            'Training and orientation with guidance from **Mr. Vester '
            'Anandaraj**, covering sales and business development activity.',
            'Learning professional communication, prospect understanding and '
            'lead generation as the company practises them.',
            'First exposure to the relationship between a business requirement '
            'and a software solution, and to basic web and software '
            'development concepts.',
        ]),

        ('h3', 'Week 3 (1 June – 5 June 2026): First Pune and Chakan '
               'Assignment'),
        ('bullets', [
            'Selected, with one other student from ISSM, for the Pune '
            'assignment; travel and stay arranged by the company.',
            'Identifying potential companies and finding new prospects in the '
            'Pune and Chakan industrial belt.',
            'Establishing contact with business representatives and '
            'understanding requirements at first hand.',
            'Generated leads from three companies during the assignment, and '
            'exploring further opportunities for market expansion.',
            'First substantial independent exposure to business analysis '
            'activity in a live market environment.',
        ]),

        ('h3', 'Weeks 4 to 6 (8 June – 26 June 2026): Chennai Follow-Up and '
               'Documentation'),
        ('bullets', [
            'Client and customer follow-up by telephone on opportunities '
            'opened during the Pune assignment.',
            'Physical company and client visits in and around Chennai, '
            'including a visit to Yamaha Music.',
            'Continued lead generation and business development in the home '
            'market.',
            'Requirement understanding and discussion with clients and '
            'business representatives.',
            'Preparing Software Requirements Specification documents and '
            'client-related documentation.',
            'Preparing project and business roadmaps connecting requirements '
            'to stages of work.',
        ]),

        ('h3', 'Weeks 7 and 8 (29 June – 10 July 2026): Second Pune and '
               'Chakan Assignment'),
        ('bullets', [
            'Second assignment to the Pune and Chakan belt, of approximately '
            'two weeks, weighted towards existing client relationships.',
            'Client visit and interaction at Hyundai in the Chakan belt in '
            'relation to business requirements.',
            'Understanding existing requirements and identifying further '
            'requirements within an established relationship.',
            'Communication with client representatives and observation of '
            'client relationship management in practice.',
            'Continued lead generation, prospect identification and follow-up '
            'on business opportunities.',
        ]),

        ('h3', 'Weeks 9 to 11 (13 July – 31 July 2026): Consolidation at '
               'Chennai'),
        ('bullets', [
            'Follow-up on requirements and opportunities arising from the '
            'second Pune assignment.',
            'Continued client communication, company visits and relationship '
            'maintenance.',
            'Preparing Month-End Review Meeting presentations and reporting '
            'material in PowerPoint, Figma and Power BI.',
            'Completing requirement documentation and roadmap work in hand.',
            'Consolidating notes and handing over open conversations at the '
            'close of the internship on 31 July 2026.',
        ]),
        ('h2', '2.5  TOOLS AND SYSTEMS USED'),
        ('h3', '2.5.1  Microsoft PowerPoint'),
        ('p', 'PowerPoint was the medium for Month-End Review Meeting '
              'presentations. Using it for a management audience taught me that '
              'a slide is a unit of argument rather than a container for '
              'information, and that the discipline lies in deciding what to '
              'leave out. I also learned the practical value of a consistent '
              'visual structure, since a reviewer moving quickly through '
              'material should not have to relearn the layout on each slide.'),

        ('h3', '2.5.2  Figma'),
        ('p', 'Figma was used for visual and layout work supporting the review '
              'material. Working in a design tool rather than a presentation '
              'tool taught me to think about alignment, spacing and visual '
              'hierarchy as deliberate choices. It also gave me an '
              'appreciation of how much design work sits behind material that '
              'appears simple, which was a recurring theme of the internship.'),

        ('h3', '2.5.3  Microsoft Power BI'),
        ('p', 'Power BI was used for reporting and visualisation of business '
              'information for review meetings. The learning here was about '
              'the relationship between a figure and its presentation: the same '
              'information can be shown in a form that prompts a question or '
              'in a form that obscures it. I used the tool to prepare '
              'reporting material and did not set the indicators being '
              'reported, and this report states no values from it.'),

        ('h3', '2.5.4  Requirement and Roadmap Documentation'),
        ('p', 'Document preparation for Software Requirements Specifications, '
              'roadmaps and client-related records was a substantial part of '
              'the work. The skill involved is less about software than about '
              'writing: recording what was agreed, distinguishing fact from '
              'assumption, marking an open question as open, and structuring a '
              'document so that a reader can find what concerns them.'),

        ('h3', '2.5.5  Telephone and In-Person Communication'),
        ('p', 'The most-used tool of the internship was the telephone, followed '
              'by the physical visit. Neither is a system, but both are '
              'instruments that reward technique. I learned to prepare before '
              'calling, to state a reason for the call within the first '
              'sentence, to listen more than I spoke, and to close by '
              'confirming what each side would do next.'),

        ('h2', '2.6  APPLICATION OF ACADEMIC KNOWLEDGE'),
        ('h3', '2.6.1  Sales Management'),
        ('p', 'The sales cycle studied in the classroom proved to be the actual '
              'structure of my work, from prospecting through approach and '
              'need identification to follow-up. What practice added was a '
              'sense of proportion: the textbook gives each stage equal weight, '
              'while in a new market prospecting and earning a hearing consume '
              'most of the effort.'),

        ('h3', '2.6.2  Business Development and Market Expansion'),
        ('p', 'Market entry, studied as a strategic choice, became a set of '
              'practical problems: no local reputation, no reference client, '
              'unfamiliar business conventions and a lengthened decision cycle. '
              'The Pune assignments were an education in the difference '
              'between deciding to enter a market and actually entering one.'),

        ('h3', '2.6.3  Customer Relationship Management'),
        ('p', 'The second Pune assignment applied relationship management '
              'directly. Maintaining contact with an existing client, '
              'understanding its current position and identifying further needs '
              'within the relationship is cheaper and more reliable than '
              'winning a new client, which is the argument the subject makes '
              'and which I was able to observe.'),

        ('h3', '2.6.4  Business Communication'),
        ('p', 'Business communication was the subject most continuously in use. '
              'Telephone follow-up, client meetings, requirement discussion and '
              'management presentation each demanded a different register, and '
              'the internship taught me to judge which one a situation called '
              'for rather than applying a single professional manner to all of '
              'them.'),

        ('h3', '2.6.5  Business Analysis and Requirement Gathering'),
        ('p', 'Requirement gathering moved from a described technique to a '
              'practised one. Eliciting a need by listening, separating a '
              'business requirement from a technical one, recording it '
              'unambiguously and confirming it with the client are the core '
              'activities of the discipline, and the internship gave me '
              'introductory practice in all four.'),

        ('h3', '2.6.6  Data Visualisation, Reporting and Information Systems'),
        ('p', 'Preparing review material applied the principles of reporting '
              'and data visualisation: choosing a form that answers the '
              'question, keeping comparisons honest and structuring '
              'information for a reader with limited time. Working inside a '
              'software company also gave me introductory exposure to '
              'information systems concepts and to how business requirements '
              'relate to technical implementation.'),

        ('h2', '2.7  SKILLS DEVELOPED DURING THE INTERNSHIP'),
        ('h3', '2.7.1  Prospect Identification'),
        ('p', 'The ability to look at a market and judge which organisations '
              'are worth approaching, rather than treating every name as an '
              'equal opportunity.'),
        ('h3', '2.7.2  Lead Generation in an Unfamiliar Market'),
        ('p', 'The ability to establish contact and earn a hearing where '
              'neither the company nor I was known, and to persist through '
              'unsuccessful approaches.'),
        ('h3', '2.7.3  Professional Telephone Communication'),
        ('p', 'The ability to prepare for a call, state a purpose immediately, '
              'listen, and close by confirming what each party will do next.'),
        ('h3', '2.7.4  Client Interaction in Person'),
        ('p', 'The ability to read an organisation’s formality and pace within '
              'the first minutes of a visit and to adjust my approach '
              'accordingly.'),
        ('h3', '2.7.5  Requirement Elicitation and Documentation'),
        ('p', 'Introductory competence in drawing out a business need, '
              'distinguishing it from a technical requirement and recording it '
              'unambiguously.'),
        ('h3', '2.7.6  Structured Written Documentation'),
        ('p', 'The discipline of preparing specifications, roadmaps and client '
              'records that another person can act on without asking me to '
              'explain them.'),
        ('h3', '2.7.7  Presentation and Visual Reporting'),
        ('p', 'Working competence in PowerPoint, Figma and Power BI, and the '
              'judgement to structure material around the decision it '
              'supports.'),
        ('h3', '2.7.8  Working Independently Away from Base'),
        ('p', 'The ability to organise my own days productively in another '
              'city, without daily supervision, and to account for what was '
              'achieved.'),

        ('h2', '2.8  KEY OBSERVATIONS FROM THE JOB'),
        ('bullets', [
            'In an intangible business, credibility precedes everything. A '
            'prospect cannot inspect software, so it is judging the people '
            'describing it, which is why turning up in person changes a '
            'conversation.',
            'A lead is a conversation, not a contact detail. An organisation '
            'that has expressed a genuine interest is worth more than a long '
            'list of names, and reaching that point takes several '
            'unsuccessful approaches for each success.',
            'Follow-up is where opportunity is won or lost. An opened '
            'conversation does not advance by itself, and the research that '
            'earned it is wasted if the follow-up lapses.',
            'A business requirement is not a technical requirement. Confusing '
            'them produces either an unusable document or an unwanted '
            'solution, and keeping them apart is the beginning of business '
            'analysis.',
            'Writing is the durable part of the work. A requirement remembered '
            'differently by two parties is a dispute waiting to happen; '
            'written and confirmed, it is an agreement.',
            'Reporting should answer the question the meeting is asking. '
            'Material organised around the work done rather than the decision '
            'to be taken wastes the reviewer’s time.',
        ]),

        ('h2', '2.9  CHALLENGES ENCOUNTERED DURING THE INTERNSHIP'),
        ('h3', '2.9.1  Adjusting to Professional Communication'),
        ('p', 'Speaking to a senior corporate representative on the telephone '
              'was genuinely difficult at the start. A student is accustomed to '
              'being asked questions rather than to opening a conversation with '
              'a stranger who has no particular reason to continue it. What '
              'helped was preparation: knowing what I wanted to establish and '
              'saying so early, rather than approaching the call hoping it '
              'would develop.'),

        ('h3', '2.9.2  Understanding Differing Client Expectations'),
        ('p', 'Organisations differ more than I expected in what they want '
              'from a conversation. Some expect a brief proposition and a '
              'prompt exit; others expect an unhurried discussion before any '
              'business is raised. Misjudging this costs the meeting. Learning '
              'to read the signals, and to accept that the client sets the '
              'pace, took most of the internship.'),

        ('h3', '2.9.3  Working Independently in an Unfamiliar City'),
        ('p', 'The Pune assignments placed me in a market I did not know, '
              'without daily supervision, and required me to make the days '
              'productive myself. The difficulty was not the travel but the '
              'self-direction: deciding which area to work, which units to '
              'approach and when an approach was not going to progress. It was '
              'the most valuable discomfort of the internship.'),

        ('h3', '2.9.4  Communicating Between Business and Technical Contexts'),
        ('p', 'Standing between a client describing an operational problem and '
              'colleagues thinking in terms of systems was harder than either '
              'conversation alone. I did not always have the technical '
              'vocabulary to ask a precise question, and I sometimes recorded '
              'a need in language that was accurate to the client and '
              'insufficient for a developer. Learning to ask the clarifying '
              'question at the time, rather than discovering the gap later, '
              'was the correction.'),

        ('h3', '2.9.5  Seeing Academic Concepts Behave Differently in Practice'),
        ('p', 'The final challenge was conceptual. The sales funnel, market '
              'entry strategy and requirement gathering all exist in '
              'coursework as orderly processes. In practice they are '
              'interrupted, repeated and conducted with incomplete '
              'information, and a stage one has supposedly completed reopens '
              'when a client changes his mind. Accepting that the models '
              'describe a direction rather than a sequence was a genuine '
              'adjustment.'),

        ('h2', '2.10  OVERALL JOB EXPERIENCE'),
        ('p', 'The overall experience was that business development in a '
              'software company is far more analytical, and far less '
              'promotional, than I had assumed. I had expected a role centred '
              'on persuasion. What I found was a role centred on '
              'understanding: which organisations have the problem, what '
              'exactly the problem is, what can honestly be promised, and what '
              'has to be written down so that the promise can be kept.'),
        ('p', 'I should be honest about the limits of the period. Three months '
              'is long enough to learn how business development is conducted '
              'and too short to see an opportunity through from first contact '
              'to a signed engagement and a delivered system. I did not '
              'negotiate commercial terms, and I had no visibility of pricing, '
              'margins or contracts. I therefore left with a good understanding '
              'of the front of the process and a limited understanding of its '
              'conclusion, and I would rather record that plainly than imply '
              'otherwise.'),

        ('h2', '2.11  SUMMARY OF RESPONSIBILITIES'),
        ('p', 'The table below consolidates the work of the internship and the '
              'nature of my contribution to each item. It reflects the areas '
              'actually assigned to me and does not claim sole ownership of '
              'team outcomes.'),
        ('table', {'rows': [
            ['S. No.', 'Area of Work', 'Major Responsibility and Contribution'],
            ['1', 'Training and orientation',
             'Completed induction and corporate training at Chennai with '
             'guidance from Mr. Vester Anandaraj'],
            ['2', 'Prospect identification',
             'Identified potential client organisations in Chennai and in the '
             'Pune and Chakan industrial belt'],
            ['3', 'Lead generation',
             'Established contact and generated live leads, including leads '
             'from three companies during the first Pune assignment'],
            ['4', 'Business development',
             'Explained the company’s services in client-relevant terms and '
             'explored commercial possibilities'],
            ['5', 'Client and customer follow-up',
             'Conducted professional telephone follow-up and tracked what each '
             'party had undertaken'],
            ['6', 'Client and company visits',
             'Visited client and prospect organisations in both markets, '
             'including a visit to Yamaha Music'],
            ['7', 'Requirement understanding',
             'Listened to and discussed business needs with clients and '
             'business representatives'],
            ['8', 'SRS documentation',
             'Worked on Software Requirements Specification documents '
             'recording agreed requirements'],
            ['9', 'Roadmap preparation',
             'Prepared project and business roadmaps connecting requirements '
             'to stages of work'],
            ['10', 'Client relationship management',
             'Maintained contact with an existing client during the second '
             'Pune assignment, including interaction at Hyundai'],
            ['11', 'Month-End Review Meeting preparation',
             'Prepared presentations and visual reporting material in '
             'PowerPoint, Figma and Power BI'],
            ['12', 'Documentation and handover',
             'Maintained client-related records and left open conversations in '
             'a state others could resume'],
        ], 'widths': [1, 3, 6], 'col_bold': [True, True, False],
            'col_align': ['center', 'left', 'left']}),

        ('h2', '2.12  CONCLUSION OF JOB / TASK DESCRIPTION'),
        ('p', 'The three months gave me practical exposure to the whole front '
              'end of a business development function: training, prospecting, '
              'lead generation, follow-up, client visits, requirement '
              'understanding, specification and roadmap documentation, '
              'relationship management and management reporting. The phase '
              'structure, alternating between the home market and the market '
              'being opened, meant each area was encountered more than once '
              'and at increasing levels of independence.'),
        ('p', 'The chapter has described responsibilities, method and learning '
              'rather than results. No conversion rates, revenue figures, deal '
              'values or client outcomes are stated, because I was not given '
              'verified figures for them and because inventing plausible '
              'numbers would defeat the purpose of an academic report. What can '
              'be stated with confidence is the work I was given, the standards '
              'I was held to and the progression from supervised training to '
              'independent fieldwork. The next chapter assesses how well I '
              'performed against those standards.'),

        ('p', 'What I carry forward from this chapter is less the list of '
              'activities than the order they belong in: understand the '
              'organisation, earn the hearing, listen to the need, write it '
              'down, and go back when promised.'),
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
        ('p_indent', 'This chapter is an honest assessment of how I performed, '
                     'and it should be read with one limitation in mind: no '
                     'formal appraisal rubric was applied to my work and I was '
                     'not given a written evaluation. What follows is therefore '
                     'my own analysis, supported by the feedback I received in '
                     'conversation and by what the internship certificate '
                     'records, namely that I completed the assigned tasks '
                     'efficiently and maintained a professional attitude '
                     'throughout.'),
        ('h2', '3.2  TIMELINESS AND TASK OWNERSHIP'),
        ('p', 'Task ownership developed over the period, and the Pune '
              'assignments accelerated it. Working in another city without '
              'daily supervision meant that nobody else was going to decide '
              'how my day was spent, and the accountability that followed was '
              'the most formative part of the internship. I learned to plan a '
              'day’s calls and visits in advance, to record what had come of '
              'them, and to be able to say what had been achieved.'),
        ('h2', '3.3  ADAPTABILITY AND LEARNING CURVE'),
        ('p', 'The internship required adaptation on four fronts at once: a '
              'new industry, a new functional role, two unfamiliar software '
              'tools and, twice, an unfamiliar city. The first fortnight of '
              'structured training made the first two manageable; the others I '
              'learned by doing.'),
        ('bullets', [
            'Learned the company’s service domain well enough to describe it '
            'credibly to a prospect within the first two weeks.',
            'Became competent in PowerPoint, Figma and Power BI for review '
            'reporting, having had no prior working use of the latter two.',
            'Adapted from the home market to the Pune and Chakan belt, where '
            'business convention and language differed from Chennai.',
            'Moved from prospecting in the first Pune assignment to existing '
            'client relationship management in the second, which required a '
            'different manner entirely.',
            'Acquired enough introductory understanding of software and web '
            'development concepts to follow a technical discussion without '
            'pretending to contribute to it.',
        ]),
        ('h2', '3.4  COMMUNICATION AND COLLABORATION'),
        ('p', 'This internship was almost entirely communication, and my '
              'performance in it is the fairest measure of the whole period. '
              'The work involved telephone conversations with strangers, '
              'face-to-face meetings at client premises, requirement '
              'discussions with business representatives, and presentation '
              'material for internal management review. Each demanded a '
              'different register.'),
        ('bullets', [
            'Conducted professional telephone follow-up with clients and '
            'prospects, and learned to open with a reason rather than a '
            'pleasantry.',
            'Represented the company in person at client and prospect '
            'premises in two states.',
            'Discussed business requirements with client representatives and '
            'asked clarifying questions at the time rather than afterwards.',
            'Communicated requirements internally in written form so that '
            'colleagues who had not attended could act on them.',
            'Prepared review material for a management audience, structured '
            'around the decision it supported.',
            'Worked alongside a fellow ISSM student on the Pune assignments, '
            'dividing ground and sharing what each of us had learned about the '
            'market.',
        ]),
        ('h2', '3.5  STRENGTHS DEMONSTRATED'),
        ('p', 'The following are offered as qualitative reflections rather than '
              'as formal ratings, since no appraisal rubric was applied to my '
              'work.'),
        ('bullets', [
            '**Willingness to work in the field:** I was comfortable '
            'approaching organisations I did not know in a city I did not '
            'know, which is the part of this work that most people find hardest.',
            '**Independence:** the Pune assignments required self-direction '
            'without daily supervision, and I was able to plan and account for '
            'my own days.',
            '**Listening:** I learned quickly that a prospect describing his '
            'operations is more useful than a prospect being presented to.',
            '**Accuracy in writing:** once corrected, I wrote requirement notes '
            'and documentation that distinguished what was said from what I '
            'had assumed.',
            '**Restraint:** I learned not to answer a question I could not '
            'answer, which in a sales role is a harder discipline than it '
            'appears.',
        ]),

        ('h2', '3.6  AREAS FOR IMPROVEMENT'),
        ('p', 'The internship was at least as informative about my limitations '
              'as about my strengths. These are stated specifically, because a '
              'general intention to improve cannot be acted on.'),
        ('bullets', [
            '**Persistence in follow-up:** I treated silence as refusal for too '
            'long, and a more confident follow-up rhythm would have kept more '
            'conversations alive.',
            '**Technical vocabulary:** I could not always frame a precise '
            'question about a requirement, which occasionally left a gap that '
            'surfaced later.',
            '**Writing for an absent reader:** my early notes assumed context '
            'the reader did not have, and this took correction rather than '
            'instinct to fix.',
            '**Commercial exposure:** I did not negotiate terms or see pricing, '
            'so my understanding of the closing end of the sales process '
              'remains theoretical.',
            '**Qualification discipline:** I spent effort on prospects that a '
            'more experienced executive would have set aside earlier, '
            'particularly during the first Pune assignment.',
        ]),

        ('h2', '3.7  OVERALL PERFORMANCE'),
        ('p', 'Taken as a whole, I consider the internship to have been '
              'performed satisfactorily, and the internship certificate records '
              'that the assigned tasks were completed efficiently and that a '
              'professional attitude was maintained throughout. The progression '
              'is the clearest evidence: I began under training at Chennai, was '
              'selected with one other student for a field assignment in an '
              'unfamiliar market, returned to follow up and document what that '
              'produced, and was sent again for a longer assignment weighted '
              'towards an existing client relationship. That sequence '
              'represents increasing trust.'),
        ('p', 'One claim requires careful handling, and I would rather address '
              'it directly than leave it implied. I had formed the impression '
              'during the internship that the leads I generated in the first '
              'Pune assignment represented a substantial share of the '
              'company’s business in that month, and I had estimated that share '
              'at around a quarter. I want to be explicit that this was my own '
              'approximate impression as a trainee. I was not shown revenue '
              'records, I had no visibility of pricing or margins, and I cannot '
              'evidence the figure. It is recorded here as a personal '
              'impression and should not be read as a verified financial fact '
              'about the company, and no conversion rate, deal value or revenue '
              'figure appears anywhere else in this report for the same reason.'),
        ('p', 'Measured against what a first-year business development '
              'executive would ordinarily be expected to handle, the comparison '
              'is reasonably close on the front end of the process. Prospect '
              'identification, lead generation, telephone and in-person '
              'follow-up, client visits, requirement discussion and '
              'documentation are all tasks such an executive performs, and by '
              'the closing weeks I was performing them with limited '
              'supervision. My exposure fell short in three respects: I did not '
              'negotiate commercial terms, I had no visibility of pricing or '
              'account profitability, and I did not carry an opportunity '
              'through to a signed engagement. Those are the areas where I have '
              'method without practice.'),
        ('p', 'If I were to summarise my performance in a sentence, it would be '
              'this: I was a reliable and increasingly independent contributor '
              'at the front end of a business development function, strongest '
              'in fieldwork and weakest in commercial judgement, who improved '
              'most in the areas where he began least confident. No numerical '
              'score is stated, because none was given to me, and constructing '
              'one for the sake of appearance would misrepresent the basis of '
              'this chapter.'),
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
              'working understanding of how a software company finds and keeps '
              'clients. The functional knowledge acquired is set out below.'),
        ('bullets', [
            '**The business development sequence:** how an unknown '
            'organisation becomes a prospect, a lead, a discussion and '
            'eventually a client, and how much of the effort sits at the front '
            'of that sequence.',
            '**Lead generation in practice:** what distinguishes a live lead '
            'from a contact detail, and how many approaches a single lead costs.',
            '**Client relationship management:** how an existing relationship '
            'is maintained and how further requirements are identified within '
            'it.',
            '**Requirement elicitation:** how a business need is drawn out in '
            'conversation, and why the client cannot be expected to state a '
            'technical requirement.',
            '**Requirement documentation:** the purpose and content of a '
            'Software Requirements Specification and why written, confirmed '
            'requirements protect both parties.',
            '**Management reporting:** how periodic review material is '
            'structured for an audience with limited time and a specific '
            'question.',
        ]),

        ('h2', '4.2  PRACTICAL EXPOSURE TO BUSINESS PROCESSES'),
        ('p', 'More importantly, I understood why the process constraints '
              'exist. Insisting that a requirement be written and confirmed, '
              'that a promise not be made without authority, and that an open '
              'question be recorded as open can look like caution from '
              'outside. From inside, each is a response to a specific way a '
              'software engagement goes wrong: a client receiving what it did '
              'not ask for, a company committed to something it cannot '
              'deliver, or an assumption discovered at the wrong stage.'),
        ('h2', '4.3  IMPROVEMENT IN ANALYTICAL AND SYSTEMS THINKING'),
        ('p', 'Analytically, the largest change was learning to ask what a '
              'piece of work was for. An approach is worth making when the '
              'organisation plausibly has the problem; a requirement note is '
              'worth writing when somebody else can act on it; a slide is worth '
              'including when it bears on the decision. Each of those is a test '
              'a piece of work can fail while still being finished.'),
        ('h2', '4.4  SOFT SKILLS AND PROFESSIONAL TRAITS STRENGTHENED'),
        ('p', 'Alongside the functional learning, the internship strengthened a '
              'set of traits that no coursework had tested.'),
        ('bullets', [
            '**Professional confidence:** speaking to senior representatives '
            'of organisations I had never met, by telephone and in person.',
            '**Self-direction:** organising productive days in an unfamiliar '
            'city without supervision, and accounting for them afterwards.',
            '**Resilience:** continuing to approach organisations after several '
            'unproductive conversations, which is the ordinary condition of '
            'field business development.',
            '**Listening:** hearing what a client actually said rather than '
            'what I expected, and asking rather than assuming.',
            '**Written clarity:** writing documentation for a reader who was '
            'not present at the conversation.',
            '**Adaptability:** adjusting register and approach to the '
            'organisation in front of me.',
            '**Restraint:** not claiming, not promising and not reporting '
            'activity as achievement.',
        ]),

        ('h2', '4.5  ALIGNMENT WITH ACADEMIC LEARNING'),
        ('p', 'The internship served as a practical extension of the subjects '
              'studied in the MBA programme, with my Marketing major and '
              'Logistics minor both finding application. The table below maps '
              'each subject area to the work in which it was applied. Where an '
              'official subject title in my academic record differs from the '
              'description used here, the official title should be substituted: '
              '[TO BE PROVIDED].'),
        ('table', {'rows': [
            ['Academic Subject Area', 'Internship Application'],
            ['Sales Management',
             'The full prospecting to follow-up cycle, in the home market and '
             'in the Pune and Chakan belt'],
            ['Business Development and Market Expansion',
             'The Pune Market Expansion assignments recorded on the internship '
             'certificate'],
            ['Customer Relationship Management',
             'Maintaining an existing client relationship and identifying '
             'further requirements during the second Pune assignment'],
            ['Business Communication',
             'Telephone follow-up, client meetings, requirement discussion and '
             'management presentation'],
            ['Business Analysis and Requirement Gathering',
             'Requirement elicitation, SRS documentation and roadmap '
             'preparation'],
            ['Marketing Research and Market Analysis',
             'Assessing the Pune and Chakan industrial belt as a target market '
             'for the company’s services'],
            ['Data Visualisation and Business Reporting',
             'Month-End Review Meeting material prepared in PowerPoint, Figma '
             'and Power BI'],
            ['Logistics and Supply Chain (minor)',
             'Understanding the operations of manufacturing and ancillary '
             'clients in an automotive cluster'],
            ['Information Systems',
             'Introductory exposure to how business requirements relate to '
             'software implementation'],
        ], 'widths': [3, 6], 'col_bold': [True, False],
            'col_align': ['center', 'left']}),
        ('p', 'The internship also exposed the limits of purely academic '
              'preparation. Coursework presents a target market as a set of '
              'attributes and a sales funnel as an orderly progression. '
              'Practice required me to stand in an industrial estate in another '
              'state, decide which gate to walk through, find a person willing '
              'to listen and hold a conversation that had no script. The gap '
              'between a described market and an entered one is, in my view, '
              'the real content of an internship.'),

        ('h2', '4.6  OVERALL REALISATIONS'),
        ('bullets', [
            'In an intangible business the seller is the evidence, which is why '
            'credibility has to be established before a requirement will even '
            'be discussed.',
            'Most of business development is preparation and follow-up; the '
            'conversation everybody imagines is the shortest part.',
            'A requirement heard and not written down is not a requirement, it '
            'is a recollection, and recollections differ.',
            'Selling and understanding are not separable in a bespoke '
            'business, because the conversation that opens an opportunity is '
            'also the one in which the need is first heard.',
            'Existing clients are the most accessible source of new work, and '
            'the second Pune assignment demonstrated this more clearly than any '
            'lecture.',
            'Reporting is a service to the reader, not a record of the writer’s '
            'effort.',
            'An honest account of what one did not see is part of professional '
            'reporting, and my own exposure stopped short of the commercial '
            'close.',
        ]),
        ('h2', '4.7  PROFESSIONAL INSIGHTS AND LEARNINGS'),
        ('p', 'Three insights from the internship seem to me to have lasting '
              'value. The first concerns trust in an intangible business. A '
              'client buying custom software is buying a promise, and every '
              'element of the vendor’s conduct, including the punctuality of a '
              'follow-up call, is read as evidence about whether the promise '
              'will be kept. That reframes ordinary professional behaviour as '
              'commercially material rather than merely polite.'),
        ('p', 'The third concerns my own career direction. I entered the '
              'internship with a general interest in marketing and left with a '
              'specific interest in business development and business analysis '
              'in a technology environment. Having done the work in the field '
              'rather than in a case study, I know both that I can do it and '
              'that I want to, which is a more useful conclusion than a general '
              'affirmation of interest.'),

        ('p', 'Taken together, these outcomes describe a shift from studying a '
              'commercial function to having practised one, which is the '
              'difference an internship is meant to make.'),
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
        ('p_indent', 'The Summer Internship Programme was carried out at '
                     'Ecosoft Zolutions Pvt Ltd, SP75, Sidco Industrial Estate, '
                     'Ambattur, Chennai, from 20 May 2026 to 31 July 2026, a '
                     'period of three months, in the Sales Department with the '
                     'designation of Business Development Executive. The '
                     'internship certificate, issued on 6 August 2026 under the '
                     'authorised signature of **Mr. Santharaj Periyasamy**, '
                     'Director, records my assignments as relating to Pune '
                     'Market Expansion.'),
        ('p', 'The programme ran in four phases. The first fortnight at Chennai '
              'was given to training and orientation under **Mr. Vester '
              'Anandaraj**. Two students from ISSM were then selected for a '
              'field assignment of about a week in the Pune and Chakan '
              'industrial belt, where I identified prospects, generated leads '
              'from three companies and gained my first independent exposure to '
              'requirement discussion. Between two and three weeks at Chennai '
              'followed, given to follow-up, company visits, requirement '
              'understanding, Software Requirements Specification documentation '
              'and roadmap preparation. A second Pune assignment of about two '
              'weeks then followed, weighted towards existing client '
              'relationship management and including client interaction at '
              'Hyundai in the Chakan belt.'),
        ('h2', '5.2  KEY TAKEAWAYS'),
        ('h3', '5.2.1  Business Development in Practice'),
        ('p', 'Learned that the business development sequence runs from '
              'identifying a plausible need through earning a hearing to '
              'understanding the requirement, and that the early stages consume '
              'most of the effort. Understood that a lead is a conversation in '
              'which an organisation has expressed genuine interest rather than '
              'a contact detail. Learned that several approaches fail for each '
              'one that progresses, and that this is the ordinary condition of '
              'the work rather than a sign of doing it badly.'),
        ('h3', '5.2.2  Market Expansion and Fieldwork'),
        ('p', 'Experienced what entering an unfamiliar market actually '
              'requires: no local reputation, no reference client, different '
              'business convention and a lengthened decision cycle. Learned '
              'that a dense industrial cluster rewards physical presence, '
              'because manufacturing clients treat a supplier who travels '
              'differently from one who telephones. Understood that the purpose '
              'of an exploratory assignment is to discover which of the '
              'textbook entry factors actually operate in a particular market.'),
        ('h3', '5.2.3  Professional Communication'),
        ('p', 'Improved my telephone and face-to-face communication with '
              'corporate representatives, learning to open with a reason, to '
              'listen more than I spoke and to close by confirming what each '
              'side would do next. Learned that the difference between diligent '
              'follow-up and nuisance is judged by the recipient and turns on '
              'interval and relevance. Understood that register has to be '
              'adjusted to the organisation rather than applied uniformly.'),
        ('h3', '5.2.4  Requirement Understanding and Documentation'),
        ('p', 'Learned to distinguish a business requirement from a technical '
              'requirement, and that a client cannot be expected to state the '
              'second. Understood why requirements are written and confirmed: a '
              'need remembered differently by two parties is a dispute waiting '
              'to happen. Gained introductory practice in Software Requirements '
              'Specification documentation and in roadmap preparation, and '
              'learned to write for a reader who was not present at the '
              'conversation.'),
        ('h3', '5.2.5  Client Relationship Management'),
        ('p', 'Saw, during the second Pune assignment, that an existing '
              'relationship is the most accessible source of further work, and '
              'that maintaining it is cheaper than winning a new client. '
              'Learned that identifying an additional requirement within a '
              'relationship depends on understanding the client’s current '
              'position rather than on presenting anything. Understood that '
              'relationship management is mostly continuity: remembering, '
              'returning and following through.'),
        ('h3', '5.2.6  Reporting and Self-Management'),
        ('p', 'Acquired working competence in PowerPoint, Figma and Power BI '
              'and learned to structure review material around the decision it '
              'supports rather than the work behind it. Learned to distinguish '
              'activity from outcome, which is why this report attaches no '
              'unverified figures to my own work. Developed the self-direction '
              'to organise productive days away from base and to account for '
              'them afterwards.'),

        ('h2', '5.3  CONCLUSION'),
        ('p', 'Beyond the technical content, three things changed. First, my '
              'understanding of selling: in an intangible business the seller is '
              'the evidence, so relevance and reliability matter more than '
              'persuasion. Second, my understanding of requirements: the '
              'distance between what a client says and what a system must do is '
              'where business analysis lives, and closing that distance in '
              'writing is real work with real consequences. Third, my '
              'understanding of myself. I learned that I am willing to walk '
              'into an unfamiliar organisation and begin a conversation, that I '
              'write more carefully under a professional standard than an '
              'academic one, and that I would rather record an uncertainty than '
              'resolve it with a guess.'),
        ('p', 'In conclusion, the internship achieved what a Summer Internship '
              'Programme is intended to achieve. It connected my MBA study of '
              'sales management, business communication, customer relationship '
              'management and business analysis to live commercial work, it '
              'gave me practical experience of opening a new regional market, '
              'and it settled my career direction towards business development '
              'and business analysis in a technology environment. I am grateful '
              'to the management of Ecosoft Zolutions Pvt Ltd for the '
              'opportunity and for entrusting an intern with field assignments '
              'in another state, to **Mr. Santharaj Periyasamy** for the '
              'internship, and to **Mr. Vester Anandaraj** for the training and '
              'guidance with which the internship began. I leave the '
              'organisation with an accurate sense of what I can currently do, '
              'a specific agenda for what I need to learn next, and the '
              'confidence to contribute to a professional business development '
              'team.'),

        ('p', 'I am grateful to have been trusted with field assignments in '
              'another state as a student, because the independence they '
              'required taught me more than any supervised task could have.'),
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
        ('p', 'The sources below provide the industry, market and standards '
              'context used in this report. The account of the internship '
              'itself is based on the internship certificate and on the work '
              'actually assigned to the author; no source is cited in support '
              'of a claim about the author’s own activity.'),
        ('bullets', [
            'CB Insights. (n.d.). EcoSoft Zolutions: company profile. '
            'Retrieved September 2026, from '
            'https://www.cbinsights.com/company/ecosoft-zolutions',

            'CNBC TV18. (2026, February). India tech to reach USD 315 billion '
            'in FY26 and add 135,000 jobs as artificial intelligence emerges '
            'as a revenue driver: NASSCOM. Retrieved September 2026, from '
            'https://www.cnbctv18.com/technology/',

            'Economic Times. (2026, February). Information technology sector '
            'FY26 revenues set to grow 6.1 per cent to USD 315 billion. ETCIO. '
            'Retrieved September 2026, from '
            'https://cio.economictimes.indiatimes.com/',

            'Ecosoft Zolutions Pvt Ltd. (2026, August 6). Internship '
            'completion certificate issued to the author, recording the '
            'internship period, department, designation and the Pune Market '
            'Expansion assignments.',

            'IEEE. (n.d.-a). IEEE 830-1998: recommended practice for software '
            'requirements specifications, superseded by ISO/IEC/IEEE '
            '29148:2011. Retrieved September 2026, from '
            'https://standards.ieee.org/ieee/830/1222/',

            'IEEE. (n.d.-b). IEEE/ISO/IEC 29148-2018: systems and software '
            'engineering, life cycle processes, requirements engineering. '
            'Retrieved September 2026, from '
            'https://standards.ieee.org/ieee/29148/6937/',

            'Indian Express. (2026a). Chakan industrial area: infrastructure '
            'concerns and the manufacturers based in the belt. Retrieved '
            'September 2026, from https://indianexpress.com/section/cities/pune/',

            'Indian Express. (2026b). The Talegaon and Chakan belt as an '
            'automobile and auto-component hub between Pune and Mumbai. '
            'Retrieved September 2026, from '
            'https://indianexpress.com/section/cities/pune/',

            'International Organization for Standardization. (n.d.). ISO/IEC/'
            'IEEE 29148: systems and software engineering, life cycle '
            'processes, requirements engineering. Retrieved September 2026, '
            'from https://www.iso.org/standard/72089.html',

            'Mahindra and Mahindra Ltd. (2026, July 16). Mahindra’s Chakan '
            'manufacturing facility rolls out its three-millionth vehicle. '
            'Retrieved September 2026, from '
            'https://www.mahindra.com/news-room/press-release/',

            'Microsoft. (n.d.). Power BI documentation: reports, visualisations '
            'and data presentation. Retrieved September 2026, from '
            'https://learn.microsoft.com/power-bi/',

            'TechTarget. (n.d.). Software requirements specification and the '
            'IEEE standard. Retrieved September 2026, from '
            'https://www.techtarget.com/searchsoftwarequality/',

            'The Print. (2026). Automotive companies in Chakan seek a dedicated '
            'cell from the Maharashtra government to address infrastructure '
            'issues. Retrieved September 2026, from https://theprint.in/economy/',

            'Times of India. (2026, March). Auto hub Chakan and Talegaon drives '
            '80 per cent of Pune’s warehousing demand, citing Knight Frank '
            'India. Retrieved September 2026, from '
            'https://timesofindia.indiatimes.com/city/pune/',

            'Times of India. (2026, February). Information technology business '
            'to grow 6.1 per cent in FY26: revenue mix by segment. Retrieved '
            'September 2026, from '
            'https://timesofindia.indiatimes.com/business/india-business/',
        ]),

        ('bullets', [
            'International Institute of Business Analysis. (n.d.). A guide to '
            'the business analysis body of knowledge: requirements elicitation '
            'and collaboration. Retrieved September 2026, from '
            'https://www.iiba.org/',

            'Figma. (n.d.). Design and prototyping documentation. Retrieved '
            'September 2026, from https://help.figma.com/',
        ]),
    ],
}

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]
