# -*- coding: utf-8 -*-
"""
Content of the Summer Internship Project report of Lingesh K (OSI2509030),
MBA (Finance), ISSM Business School, Chennai.

Internship: M/s S. Ravi & Associates, Chartered Accountants, Mylapore, Chennai
Domain: Accounting and Finance | Period: 12.05.2026 to 17.07.2026

Block vocabulary consumed by build_report.py:
    ('big', text)        centred, large, bold
    ('center', text)     centred normal text
    ('cbold', text)      centred bold text
    ('h1', text)         chapter title inside the chapter body
    ('h2', text)         numbered section heading
    ('h3', text)         numbered sub-section heading
    ('p', text)          justified body paragraph  (**bold** supported)
    ('bullets', [..])    bulleted list
    ('table', {rows, widths})
    ('gap', n)           n blank lines
    ('pagebreak',)
    ('box', text)        bordered placeholder box
    ('sign', (l, r))     two items on one line, left and right aligned
"""

STUDENT = 'LINGESH K'
REG_NO = 'OSI2509030'
FIRM = 'M/s S. Ravi & Associates, Chartered Accountants'
FIRM_SHORT = 'S. Ravi & Associates'
MENTOR = 'Ms. A. Lakshmi'
MENTOR_ROLE = 'Manager'
PERIOD = '12th May 2026 to 17th July 2026'

# The INTERNSHIP CERTIFICATE page carries the heading only, matching both
# sample reports. Set this to True to print the scanned certificate on it.
EMBED_CERTIFICATE = False

# ---------------------------------------------------------------------------
# FRONT MATTER
# ---------------------------------------------------------------------------
FRONT = [
    # ---- title page ----
    ('gap', 4),
    ('big', 'SUMMER INTERNSHIP PROJECT (SIP) – 2026'),
    ('gap', 2),
    ('cbi', 'Summer Internship Project Report submitted to the Malaysia '
            'University of Science and Technology, in partial fulfilment of '
            'the requirements to award the degree of'),
    ('gap', 2),
    ('cbold', 'MASTER OF BUSINESS ADMINISTRATION'),
    ('gap', 3),
    ('center', 'SUBMITTED BY'),
    ('gap', 1),
    ('cbold', STUDENT),
    ('center', REG_NO),
    ('gap', 3),
    ('logo',),                      # MUST + ISSM Business School banner
    ('gap', 2),
    ('cbold', 'Indian School of Science and Management'),
    ('cbold', 'Chennai'),
    ('pagebreak',),

    # ---- certificate ----
    ('gap', 1),
    ('big', 'CERTIFICATE'),
    ('gap', 2),
    ('p', 'This is to certify that the Summer Internship Project Report is an '
          'authentic record of Mr. Lingesh K (OSI2509030) carried out at '
          'M/s S. Ravi & Associates, Chartered Accountants, Chennai, in partial '
          'fulfilment of the requirements for the award of the MBA degree.'),
    ('gap', 1),
    ('p', 'The project was completed under the guidance of Ms. A. Lakshmi, '
          'Manager, S. Ravi & Associates, Chartered Accountants, during the '
          'period from May 12th to July 17th, 2026.'),
    ('gap', 4),
    ('p', 'Dr. Kavitha Manikandan'),
    ('p', 'Academic Head'),
    ('p', 'ISSM Business School'),
    ('gap', 2),
    ('p', 'Viva Voce Examination Conducted on:'),
    ('gap', 4),
    ('sign', ('Internal Examiner', 'External Examiner')),
    ('pagebreak',),

    # ---- internship certificate ----
    # Heading only, as in both sample reports: the certificate is attached as a
    # separate sheet rather than printed into the document. Flip
    # EMBED_CERTIFICATE to True to have the scan placed on this page instead.
    ('gap', 12),
    ('big', 'INTERNSHIP CERTIFICATE'),
    *([('gap', 1), ('certificate_image',)] if EMBED_CERTIFICATE else []),
    ('pagebreak',),

    # ---- declaration ----
    ('gap', 6),
    ('big', 'DECLARATION'),
    ('gap', 2),
    ('p', 'I, Mr. Lingesh K, hereby declare that this SIP Project Report is '
          'based on my internship of a little over two months done at '
          'M/s S. Ravi & Associates, Chartered Accountants, Mylapore, Chennai, '
          'as an Accounting and Finance Intern, during the period from May 12th '
          'to July 17th, 2026, under the guidance of Ms. A. Lakshmi, Manager, '
          'S. Ravi & Associates, Chartered Accountants and Indian School of '
          'Science and Management, Chennai.'),
    ('gap', 1),
    ('p', 'I further declare that the work presented in this report is my own, '
          'that it has been prepared from the assignments actually handled by '
          'me during the internship, and that it has not been submitted earlier '
          'for the award of any other degree or diploma.'),
    ('gap', 6),
    ('sign', ('Place: Chennai', 'Signature')),
    ('sign', ('Date:', '')),
    ('pagebreak',),

    # ---- acknowledgement ----
    ('gap', 4),
    ('big', 'ACKNOWLEDGEMENT'),
    ('gap', 1),
    ('p', 'The completion of this internship has been possible only because of '
          'the guidance, patience and encouragement extended to me by a number '
          'of people, and I would like to place on record my sincere gratitude '
          'to each of them.'),
    ('p', 'I would like to express my sincere gratitude to our respected '
          'Chairman, Mr. KATHIRVEL GANAPATHIAPPAN, for providing us with the '
          'valuable opportunity to carry out and complete this project.'),
    ('p', 'I express my heartfelt thanks to our visionary, dedicated and '
          'empowering Founder and Managing Director, Dr. PARKAVI MAHALINGAM, '
          'for her continuous support and meaningful guidance, which played a '
          'key role in our progress.'),
    ('p', 'I am highly indebted to our Academic Head, Dr. KAVITHA MANIKANDAN, '
          'for her guidance and constant supervision, for providing the '
          'necessary information regarding the project and for her support in '
          'completing it.'),
    ('p', 'I would also like to thank all the faculty members and staff of ISSM '
          'Business School who provided me with the facilities and the conducive '
          'conditions that were required for this project.'),
    ('p', 'My sincere gratitude to MS. A. LAKSHMI, MANAGER, M/s S. RAVI & '
          'ASSOCIATES, CHARTERED ACCOUNTANTS, for mentoring me, reviewing my '
          'work and offering immense support and knowledge throughout the '
          'internship, and to CA S. RAVI, PROPRIETOR, for permitting me to '
          'undergo my Summer Internship Programme at the firm.'),
    ('p', 'I am also thankful to Ms. ARUNA and the other members of the '
          'accounting and taxation team, who patiently demonstrated each process '
          'to me, corrected my mistakes and made me comfortable enough to work '
          'independently on live client assignments.'),
    ('pagebreak',),

    # ---- executive summary ----
    ('gap', 1),
    ('big', 'The Executive Summary'),
    ('gap', 1),
    ('p', 'This report presents the work carried out during my Summer '
          'Internship Programme at M/s S. Ravi & Associates, Chartered '
          'Accountants, a Chennai based professional services firm engaged in '
          'audit, taxation, litigation support and business advisory work. The '
          'internship was undertaken on-site at the firm’s office in Mylapore, '
          'Chennai, in the domain of Accounting and Finance, from 12 May 2026 to '
          '17 July 2026, a period of a little over two months covering ten '
          'working weeks.'),
    ('p', 'The timing of the internship was significant. It coincided with the '
          'busiest compliance window in an Indian chartered accountancy '
          'practice, the run-up to the income tax return filing season for '
          'Assessment Year 2026-27, along with monthly Goods and Services Tax '
          'returns and quarterly Tax Deducted at Source statements. As a result, '
          'the work I was given was not observational or simulated; it was live '
          'client work with real deadlines, reviewed and signed off by the '
          'firm’s manager before submission.'),
    ('p', 'The internship began with the foundation of all accounting work, the '
          'bank statement. In the first two weeks I analysed the bank statements '
          'of individual clients and then of corporate clients, segregating each '
          'credit and debit into income, expenditure, drawings, transfers, '
          'capital items and non-business receipts, and grouping them into the '
          'ledger heads of the bank account. This exercise taught me that a bank '
          'statement, read carefully, is a complete narrative of how an assessee '
          'earns and spends, and that the quality of every downstream '
          'computation depends on how honestly and precisely that narrative is '
          'classified.'),
    ('p', 'From the third week onwards the work moved into the firm’s '
          'compliance software. I was trained on Winman CA-ERP, through which I '
          'accessed the income tax e-filing portal and downloaded Form 26AS, the '
          'Annual Information Statement (AIS) and the Taxpayer Information '
          'Summary (TIS) for client after client. I then recorded client '
          'transactions in Tally, which gave me a clear view of how a set of '
          'books is actually built and how a company’s operations translate into '
          'ledger entries.'),
    ('p', 'The middle phase of the internship was devoted to statutory '
          'compliance. On the indirect tax side I worked on Goods and Services '
          'Tax filings: downloading and analysing acknowledgement forms from the '
          'GST portal, working with GSTR-1, GSTR-2B and GSTR-3B, requesting and '
          'unlocking files, and observing how returns are authenticated both '
          'online and through a Digital Signature Certificate. On the direct tax '
          'side I moved to Tax Deducted at Source, where I requested and '
          'downloaded consolidated (conso) files from TRACES using Winman TDS, '
          'extracted the data through the TDS Return Preparation Utility and '
          'entered it quarter-wise for filing. Reading conso files and Form 26AS '
          'together taught me how a deduction claimed by a deductor appears as a '
          'credit in the deductee’s account, and why any mismatch between the '
          'two must be resolved before a return is filed.'),
    ('p', 'The final phase brought all of this together into the preparation of '
          'the Statement of Total Income. I worked on Securities Transaction Tax '
          'and the related data entry in Winman, and then, using the bank account '
          'abstract, the Tally data and the reconciled Form 26AS credits, I '
          'computed total income for individual and corporate clients, verified '
          'taxes already paid against taxes payable, assisted in the preparation '
          'of balance sheets, and prepared returns for upload. In the last two '
          'weeks I independently completed the filing of three returns end to '
          'end, from data entry to upload, after review by my manager, and '
          'assisted in documentation for statutory audit assignments and in the '
          'reconciliation of books maintained in Tally with GST return filings.'),
    ('p', 'Professionally, the internship gave me three things that a classroom '
          'cannot. First, a working knowledge of the compliance calendar and of '
          'the software that Indian practitioners actually use. Second, an '
          'appreciation of accuracy as a professional obligation rather than as '
          'a personal preference, because in tax work an error is not merely a '
          'wrong figure but a notice, an interest liability and a loss of client '
          'confidence. Third, the discipline of sustained routine work, including '
          'a daily two-hour commute and long hours at a screen, and the habit of '
          'staying attentive through repetitive tasks. Working under Ms. A. '
          'Lakshmi and alongside Ms. Aruna, I also learned how a professional '
          'firm builds capability by review and correction rather than by '
          'instruction alone. In summary, the internship converted my MBA '
          '(Finance) coursework in financial accounting, direct and indirect '
          'taxation and financial reporting into something I can now perform, '
          'and it clarified my intention to build a career in accounting, '
          'taxation and audit.'),
    ('pagebreak',),

    # ---- table of contents ----
    ('gap', 1),
    ('big', 'TABLE OF CONTENTS'),
    ('gap', 1),
    # page numbers are Word PAGEREF fields, filled in from the bookmarks
    # placed at the start and end of each chapter
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

        ('h2', '1.1  GLOBAL ACCOUNTING AND TAXATION LANDSCAPE'),
        ('p_indent', 'Accountancy is one of the oldest business services in the world '
              'and, at the same time, one of the fastest changing. The global '
              'accounting services market was valued at about USD 688.2 billion '
              'in 2025 and is expected to move from USD 740.1 billion in 2026 to '
              'nearly USD 1,275.8 billion by 2033, a compound annual growth rate '
              'of roughly 8.1 per cent (Grand View Research, n.d.-a). Within '
              'this, the audit and assurance segment alone is estimated at about '
              'USD 179.3 billion in 2026 and is projected to reach USD 228.9 '
              'billion by 2030 (Grand View Research, n.d.-b). Demand is growing '
              'not because businesses have suddenly become fonder of accountants, '
              'but because regulation, cross-border transactions and stakeholder '
              'scrutiny have all increased at the same time.'),
        ('p', 'Three forces are reshaping the profession globally. The first is '
              'digitisation of the record itself. Bank feeds, payment gateways, '
              'e-invoicing and government portals now generate a machine-readable '
              'trail of most transactions, which means that the accountant’s '
              'starting point is increasingly a downloaded data set rather than a '
              'physical voucher file. The second is automation of routine '
              'processing. Rule-based classification, reconciliation, and return '
              'preparation are steadily being handled by software, which shifts '
              'the professional’s value from data entry towards interpretation, '
              'judgement and exception handling. The third is the tightening of '
              'reporting and disclosure standards, which has raised the '
              'documentation burden on every assurance engagement.'),
        ('p', 'The consequence for practice is a clear division of labour. Large '
              'international networks compete on scale, technology investment and '
              'multi-country capability, while small and medium practices compete '
              'on relationship depth, responsiveness, and command of local '
              'statute. Both models are viable, but neither can now function '
              'without technology: the practical difference between a firm that '
              'closes a client’s compliance on time and one that does not is '
              'usually the quality of its software workflow and the discipline of '
              'its documentation.'),

        ('h2', '1.2  THE INDIAN ACCOUNTING AND TAXATION CONTEXT'),
        ('p', 'India is one of the most compliance-intensive accounting markets '
              'in the world, and it is also one of the most digitised. The Indian '
              'accounting professional services market is estimated at about USD '
              '15.97 billion in 2026, up from USD 15.32 billion in 2025, and is '
              'projected to reach USD 19.66 billion by 2031 (Mordor Intelligence, '
              'n.d.). The profession itself is large and highly fragmented: as on '
              '1 October 2025 there were 1,00,138 chartered accountancy firms '
              'registered with the Institute of Chartered Accountants of India '
              '(ICAI), employing 1,83,642 professionals, with mid-sized and large '
              'partnership firms accounting for only about a fifth of that '
              'workforce (ETCFO, 2025). In other words, the overwhelming majority '
              'of Indian accounting work is delivered by proprietary and small '
              'partnership practices of exactly the kind in which this internship '
              'was undertaken.'),
        ('p', 'The volume of statutory work explains this structure. A record 7.8 '
              'crore income tax returns were filed for Assessment Year 2026-27 as '
              'on 31 August 2026, of which more than 5.9 crore had already been '
              'filed by 31 July 2026 (Livemint, 2026). On the indirect tax side, '
              'the number of registered GST taxpayers has grown from about 65 '
              'lakh at the introduction of GST in 2017 to more than 1.51 crore, '
              'and gross GST collections reached a record ₹22.08 lakh crore in '
              'FY 2024-25 (Economic Times, 2025). Every one of those registrations '
              'generates monthly or quarterly returns, annual returns and '
              'reconciliations, and a large share of that work reaches a '
              'chartered accountant’s office.'),
        ('p', 'What has changed most in the Indian context, however, is the '
              'nature of the information the tax administration already holds. '
              'Form 26AS, the Annual Information Statement (AIS) and the Taxpayer '
              'Information Summary (TIS) now give the department a consolidated '
              'view of an assessee’s tax deducted at source, interest, dividends, '
              'securities transactions and high-value payments before the return '
              'is even filed. Filing has therefore become a reconciliation '
              'exercise: the practitioner’s task is to ensure that the books, the '
              'bank statement and the department’s own data tell the same story, '
              'and to explain any difference. This is precisely the skill set the '
              'internship was built around.'),
        ('p', 'Technology adoption has followed. Tally remains the default '
              'accounting platform for Indian small and medium enterprises, while '
              'specialised compliance suites such as Winman CA-ERP handle income '
              'tax computation, return e-filing, audit reports, balance sheet '
              'preparation and TDS statements within a single environment. The '
              'Indian accounting software market, valued at about USD 698.87 '
              'million in 2025, is projected to reach USD 1,496.95 million by '
              '2034 (IMARC Group, n.d.). For a practising firm, these tools are '
              'not a convenience but the production line on which client work '
              'moves.'),

        ('h2', '1.3  COMPANY OVERVIEW: S. RAVI & ASSOCIATES, CHARTERED '
               'ACCOUNTANTS'),
        ('h3', '1.3.1  BACKGROUND AND OPERATIONS'),
        ('p', 'S. Ravi & Associates (referred to within the firm as SRA) is a '
              'Chennai based firm of chartered accountants founded by CA S. Ravi, '
              'B.Com., F.C.A., in 2001 as an audit practice. The firm has since '
              'broadened its work to cover audit and assurance, direct and '
              'indirect taxation, litigation and representation support, and '
              'financial and business advisory services (S. Ravi & Associates, '
              'n.d.). It operates as a proprietary concern led by CA S. Ravi, '
              'with a professional team of managers, qualified assistants, '
              'article assistants and support staff.'),
        ('p', 'The firm’s office is located at Flat No. 2, 2nd Floor, '
              '"Kamalini", New No. 31, Old No. 16, CIT Colony 1st Main Road, '
              'Mylapore, Chennai 600 004. Mylapore is one of the traditional '
              'professional and commercial districts of Chennai, and the '
              'location places the firm within easy reach of its client base of '
              'individuals, professionals, partnership firms, trusts and '
              'closely-held companies.'),
        ('p', 'Operationally, the practice is organised around the statutory '
              'calendar rather than around products. Monthly work is driven by '
              'GST returns and TDS payments; quarterly work by TDS statements and '
              'advance tax; and the May to September window by finalisation of '
              'accounts, tax audit and income tax return filing. Client files '
              'move through a consistent internal sequence: collection of records '
              'and portal data, recording and classification, reconciliation with '
              'departmental data, computation, internal review by the manager, and '
              'finally filing and archiving of working papers. During the '
              'internship I worked at every stage of this sequence except the '
              'final signing authority, which rests with the proprietor.'),
        ('h3', '1.3.2  SERVICE LINES'),
        ('p', 'The firm’s work can be grouped into four broad service lines, '
              'summarised below. The classification is based on the assignments '
              'observed and worked on during the internship period.'),
        ('table', {'rows': [
            ['Service Line', 'Nature of Work', 'Typical Deliverable'],
            ['Audit and Assurance',
             'Statutory audit of companies, tax audit, documentation of audit '
             'evidence and verification of books',
             'Audit working papers, audit report, Form 3CA/3CB-3CD'],
            ['Direct Taxation',
             'Computation of total income, income tax return filing, TDS '
             'statements, corrections and 26AS/AIS reconciliation',
             'Statement of Total Income, ITR acknowledgement, TDS returns'],
            ['Indirect Taxation (GST)',
             'Monthly and annual GST returns, input tax credit reconciliation '
             'with GSTR-2B, reconciliation of books with returns',
             'GSTR-1, GSTR-3B, reconciliation statements'],
            ['Advisory and Litigation Support',
             'Assistance in responding to departmental notices, representation '
             'support and general financial advisory',
             'Replies, submissions and advisory notes'],
        ], 'widths': [2, 4, 3]}),

        ('h2', '1.4  STRATEGIC FOCUS AND CULTURE'),
        ('p', 'The strategic position of a firm such as SRA is built on trust '
              'rather than on scale. Clients of a mid-sized practice do not buy a '
              'brand; they buy the assurance that their compliance will be '
              'completed correctly and on time, that someone in the office knows '
              'their history, and that a query will be answered by a person '
              'rather than by a ticketing system. The firm’s focus therefore '
              'rests on accuracy, continuity of relationship and responsiveness '
              'during statutory deadlines.'),
        ('h3', '1.4.1  VALUES IN PRACTICE'),
        ('bullets', [
            '**Accuracy before speed:** every computation is prepared by one '
            'person and reviewed by another before it leaves the office. Nothing '
            'is filed on the strength of a single pair of eyes.',
            '**Documentation as a habit:** working papers, downloaded portal '
            'statements and reconciliations are filed client-wise so that any '
            'figure can be traced back to its source months later, which is '
            'essential when a notice arrives.',
            '**Confidentiality:** client financial data, login credentials and '
            'digital signature tokens are treated as privileged, and access is '
            'restricted to the person handling the assignment.',
            '**Client education:** clients are told not only what is being filed '
            'but why a particular treatment has been adopted, which reduces '
            'disputes and improves the quality of records the client maintains.',
        ]),
        ('h3', '1.4.2  WORKPLACE CULTURE'),
        ('p', 'The working culture of the firm is disciplined and deadline-led, '
              'but it is also unusually instructive. Because a practice trains '
              'article assistants as a matter of course, teaching is part of the '
              'daily routine: a senior demonstrates a process once, supervises it '
              'the second time, and expects it to be done independently by the '
              'third. Errors are corrected directly and without ceremony, which '
              'is initially uncomfortable and eventually very effective.'),
        ('p', 'Reporting lines are short. During my internship the entire team '
              'reported to Ms. A. Lakshmi, Manager, who allocated work, reviewed '
              'output and escalated matters to the proprietor, CA S. Ravi. This '
              'flat structure meant that an intern’s work reached a reviewer '
              'within hours rather than weeks, and that feedback was immediate '
              'and specific. Peer support was equally important: Ms. Aruna, a '
              'colleague in the team, walked me through most processes for the '
              'first time and remained available whenever I was unsure.'),
        ('h3', '1.4.3  STRATEGIC POSITIONING'),
        ('p', 'SRA does not compete with the large networks on scale, and does '
              'not need to. Its positioning lies in the space between the '
              'unorganised bookkeeping segment, which lacks statutory depth, and '
              'the large firms, whose cost structures do not suit an individual '
              'assessee or a closely-held company. The firm offers the statutory '
              'competence of a qualified practice with the accessibility of a '
              'local adviser, and it defends that position by investing in '
              'compliance software, by retaining trained staff, and by holding '
              'itself to internal review discipline that is stricter than the '
              'statute requires.'),

        ('h2', '1.5  SWOT ANALYSIS'),
        ('p', 'The following analysis is my own assessment, based on what I '
              'observed of the firm’s working during the internship period. It is '
              'presented from the perspective of a mid-sized professional '
              'practice operating in a highly regulated market.'),
        ('h3', '1.5.1  STRENGTHS'),
        ('bullets', [
            '**Established practice with a long record:** a firm founded in 2001 '
            'and still growing has survived two full decades of statutory change, '
            'including the introduction of GST and the digitisation of income tax '
            'administration.',
            '**Breadth across direct and indirect tax:** the same team handles '
            'accounting, GST, TDS, income tax and audit support, which allows the '
            'firm to see a client’s position as a whole rather than in fragments.',
            '**Strong review culture:** independent internal review before filing '
            'materially reduces the risk of notices and rectifications.',
            '**Software-enabled workflow:** the use of Tally for books, Winman '
            'CA-ERP for computation and e-filing, and the TDS Return Preparation '
            'Utility for statements gives the office a repeatable production '
            'process rather than an ad hoc one.',
            '**Capability building through training:** the practice of training '
            'article assistants and interns creates a steady internal pipeline of '
            'staff who already know the firm’s methods.',
        ]),
        ('h3', '1.5.2  WEAKNESSES'),
        ('bullets', [
            '**Dependence on key individuals:** in a proprietary practice, '
            'technical judgement and client relationships are concentrated in the '
            'proprietor and a small number of senior staff.',
            '**Seasonal workload peaks:** capacity is stretched between May and '
            'September, when return filing, tax audit and monthly compliance '
            'coincide, while other months are comparatively lighter.',
            '**Limited scope for specialisation:** in a general practice, staff '
            'must cover many areas competently rather than develop deep expertise '
            'in one, which can be a disadvantage in complex assignments.',
            '**Manual dependencies at the input stage:** where clients maintain '
            'incomplete records, a significant part of the work still begins with '
            'manual classification of bank statements and vouchers.',
        ]),
        ('h3', '1.5.3  OPPORTUNITIES'),
        ('bullets', [
            '**Widening compliance base:** growth in registered GST taxpayers and '
            'in the number of returns filed each year expands the addressable '
            'market for professional compliance services.',
            '**Increased reliance on reconciliation:** as the department '
            'pre-populates more data through AIS, TIS and GSTR-2B, clients need '
            'professionals who can reconcile and explain differences.',
            '**Advisory and litigation support:** faceless assessment and '
            'automated notices have increased demand for representation and '
            'response drafting, which carries higher value than routine filing.',
            '**Further automation of routine work:** deeper use of software '
            'imports, bank statement templates and reconciliation utilities can '
            'release senior time for review and advisory work.',
            '**Growth of the Indian small business sector:** new incorporations, '
            'professionals and start-ups continue to add first-time assessees who '
            'need a full-service local adviser.',
        ]),
        ('h3', '1.5.4  THREATS'),
        ('bullets', [
            '**Frequent statutory change:** amendments to the income tax and GST '
            'framework require continuous re-learning and software updates, and '
            'the cost of falling behind is borne by the firm.',
            '**Fee pressure and price competition:** the fragmented nature of the '
            'profession, with over a lakh registered firms, keeps compliance fees '
            'under pressure.',
            '**Technology platforms serving clients directly:** online filing '
            'portals and do-it-yourself tax platforms can absorb the simplest '
            'assignments at the lower end of the market.',
            '**Talent retention:** trained assistants are attractive to industry '
            'and to larger firms, and a small practice cannot always match the '
            'compensation offered.',
            '**Data security and confidentiality risk:** the office handles '
            'portal credentials, digital signature tokens and complete financial '
            'histories, and any lapse would be serious for both client and firm.',
        ]),

        ('h2', '1.6  KEY COMPETITORS'),
        ('p', 'A practice such as SRA competes with three different groups of '
              'service providers, each at a different point in the market. The '
              'tables below set out the principal categories with representative '
              'names.'),
        ('h3', '1.6.1  GLOBAL NETWORKS AND THEIR INDIAN MEMBER FIRMS'),
        ('table', {'rows': [
            ['Firm / Network', 'Principal Services', 'Key Focus Area'],
            ['Deloitte, PwC, EY and KPMG affiliates',
             'Statutory audit, assurance, tax and consulting',
             'Large corporates, listed entities and multinationals'],
            ['BDO India, Grant Thornton Bharat',
             'Audit, tax, risk advisory and transaction services',
             'Mid-market and growth-stage corporate clients'],
        ], 'widths': [3, 4, 4]}),
        ('h3', '1.6.2  ESTABLISHED INDIAN AND CHENNAI-BASED PRACTICES'),
        ('table', {'rows': [
            ['Firm', 'Principal Services', 'Key Focus Area'],
            ['Brahmayya & Co.',
             'Audit, taxation and management consultancy',
             'Long-established multi-city practice with a wide corporate base'],
            ['PKF Sridhar & Santhanam LLP',
             'Audit and assurance, tax and advisory',
             'Chennai-founded firm with national reach and network affiliation'],
            ['Suri & Co., R. Subramanian & Co. and similar practices',
             'Statutory and tax audit, direct and indirect taxation',
             'Regional corporate and mid-market clients'],
            ['Local proprietary and small partnership firms',
             'Accounting, GST, TDS and income tax compliance',
             'Individuals, professionals and closely-held businesses'],
        ], 'widths': [3, 4, 4]}),
        ('h3', '1.6.3  TECHNOLOGY PLATFORMS AND COMPLIANCE SERVICE PROVIDERS'),
        ('table', {'rows': [
            ['Platform', 'Offering', 'Competitive Effect'],
            ['Online tax filing portals',
             'Assisted and self-service income tax return filing',
             'Absorbs simple salaried filings at low fee points'],
            ['Cloud accounting and compliance suites',
             'Bookkeeping, GST return preparation and reconciliation tools',
             'Reduces the routine processing component of professional work'],
            ['Accounting outsourcing providers',
             'Volume bookkeeping and back-office accounting',
             'Competes on cost for high-volume, low-judgement work'],
        ], 'widths': [3, 4, 4]}),

        ('h2', '1.7  COMPETITIVE POSITIONING'),
        ('p', 'The competitive logic of the Indian accounting market is '
              'straightforward: routine processing is becoming cheaper, while '
              'judgement, reconciliation and representation are becoming more '
              'valuable. Large networks hold the top of the market because they '
              'can absorb the cost of technology and specialisation. Technology '
              'platforms are taking the bottom of the market because a simple '
              'salaried return does not need a professional. The durable space in '
              'between belongs to firms that can do three things at once: '
              'maintain books accurately, reconcile them against the '
              'department’s own data, and defend the resulting position if it is '
              'questioned.'),
        ('p', 'S. Ravi & Associates occupies that middle position. Its advantage '
              'is not cost and not scale, but the combination of statutory '
              'competence, continuity of relationship and internal review '
              'discipline. During my internship I saw this positioning in '
              'practice: clients approached the firm not merely to have a return '
              'filed, but to have their records put in order, their TDS credits '
              'verified against Form 26AS and AIS, their GST returns reconciled '
              'with their books, and their filings supported by documentation '
              'strong enough to answer a future query. That combination is '
              'difficult for a software platform to replicate and uneconomical '
              'for a large firm to offer at the same fee level.'),

        ('h2', '1.8  KEY MILESTONES'),
        ('p', 'The development of the firm reflects the development of the '
              'profession in India over the same period. SRA was established in '
              '2001 as an audit practice at a time when Indian accounting was '
              'still largely paper-based: books were written up manually or in '
              'early accounting software, returns were filed physically, and '
              'verification depended on documents produced by the client.'),
        ('p', 'The first major shift came with the computerisation of accounting '
              'and the spread of Tally across Indian small and medium '
              'enterprises, which changed the firm’s work from writing books to '
              'reviewing and correcting client-maintained books. The second shift '
              'came with the electronic administration of income tax, including '
              'e-filing, Form 26AS and later the Annual Information Statement, '
              'which introduced reconciliation against departmental data as a '
              'standard step in every assignment. The third and most demanding '
              'shift was the introduction of GST in 2017, which replaced a set of '
              'indirect taxes with a single return-driven system and added a '
              'recurring monthly compliance cycle to almost every business '
              'client’s file.'),
        ('p', 'Alongside these statutory changes, the firm expanded from its '
              'original audit base into taxation, litigation support and business '
              'advisory work, as recorded on its own website (S. Ravi & '
              'Associates, n.d.). Each expansion followed the same pattern: a '
              'statutory change created a new client need, the firm built the '
              'capability to meet it, and the new service became part of the '
              'regular practice. The current phase of that journey is the one I '
              'observed at first hand, in which almost every assignment begins '
              'with data downloaded from a government portal and ends with a '
              'reconciliation that must be explainable to a reviewer.'),
        ('p', 'For a student of finance, this history carries a useful lesson. A '
              'professional practice does not grow by acquiring more clients '
              'alone; it grows by absorbing each regulatory change faster than '
              'its clients can, and by converting that capability into a service. '
              'The firms that treated GST, e-filing and AIS as opportunities '
              'rather than as burdens are the ones that expanded through them.'),
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
        ('p_indent', 'The purpose of the internship was to convert the accounting and '
              'taxation concepts studied in the first year of the MBA programme '
              'into practical, supervised work inside a functioning chartered '
              'accountancy practice. The internship was carried out at '
              'M/s S. Ravi & Associates, Chartered Accountants, Mylapore, '
              'Chennai, from 12 May 2026 to 17 July 2026, in the domain of '
              'Accounting and Finance.'),
        ('p', 'The specific objectives agreed at the start of the internship were '
              'as follows:'),
        ('bullets', [
            'To understand how a professional firm records, classifies and '
            'verifies the financial transactions of individual and corporate '
            'clients.',
            'To gain working proficiency in the software used in Indian practice, '
            'principally Tally for books of account and Winman CA-ERP for '
            'computation and e-filing.',
            'To learn the statutory compliance cycle in practice, covering income '
            'tax, Tax Deducted at Source and Goods and Services Tax.',
            'To acquire the reconciliation discipline required to match books of '
            'account with departmental records such as Form 26AS, the Annual '
            'Information Statement and GSTR-2B.',
            'To assist in documentation relating to statutory audit assignments '
            'and to understand the evidence an auditor relies upon.',
            'To develop the professional habits of accuracy, confidentiality, '
            'documentation and working to deadlines.',
        ]),
        ('h3', '2.1.1  Methodology and Approach'),
        ('p', 'The internship followed a graduated, task-based approach rather '
              'than a lecture-based one. Each new area began with a demonstration '
              'by a senior colleague on a live client file, followed by '
              'supervised execution on a similar file, and finally independent '
              'execution with review before filing. Work was allocated and '
              'reviewed by Ms. A. Lakshmi, Manager, and day-to-day process '
              'guidance was provided by Ms. Aruna and other members of the team. '
              'Because the internship fell inside the filing season for '
              'Assessment Year 2026-27, every assignment I handled was a real '
              'client assignment with a statutory due date attached to it.'),

        ('h2', '2.2  INITIAL ONBOARDING AND TRAINING'),
        ('p', 'The first days were used to establish context before any '
              'processing began. The onboarding covered:'),
        ('bullets', [
            'An introduction to the structure of the firm, the reporting line to '
            'the Manager and the role of the proprietor as the signing authority.',
            'An explanation of the firm’s client categories, individuals, '
            'professionals, firms and companies, and of the different compliance '
            'obligations attaching to each.',
            'The compliance calendar: monthly GST returns and TDS payments, '
            'quarterly TDS statements, and the income tax return filing season '
            'that the internship period fell within.',
            'The confidentiality expected while handling client bank statements, '
            'portal credentials and digital signature tokens.',
            'The firm’s documentation convention: client-wise folders, naming of '
            'downloaded portal statements, and the requirement that every figure '
            'in a computation be traceable to a source document.',
            'Hands-on familiarisation with Tally and Winman CA-ERP, including how '
            'client companies are set up, how ledgers are grouped and how data '
            'moves from the books into a computation.',
        ]),
        ('p', 'This grounding proved important. Because I understood the '
              'compliance calendar before I began processing, I could see why a '
              'particular file was urgent and what the consequence of a delay '
              'would be, which made routine work much easier to take seriously.'),

        ('h2', '2.3  WORK PLAN AND SCOPE'),
        ('p', 'The internship ran for ten working weeks and was structured so '
              'that each phase built on the previous one, beginning with raw '
              'financial data and ending with filed returns. The areas of work '
              'set out below correspond to the training areas certified by the '
              'firm in the internship completion certificate.'),
        ('h3', '2.3.1  Analysis of Individual Bank Statements'),
        ('bullets', [
            'Analysed the bank statements of individual clients line by line and '
            'split every entry into income, expenditure, drawings, transfers and '
            'non-taxable receipts within the bank ledger account.',
            'Identified the sources of income of the assessee, distinguishing '
            'business receipts from interest, dividends and reimbursements, and '
            'separated personal drawings from business expenditure.',
            'Sorted a large volume of miscellaneous entries that carried no clear '
            'narration, listing them for clarification rather than assuming a '
            'treatment.',
            'Learned that classification, not entry, is the real work: the same '
            'credit can be income, a loan or a transfer, and only the '
            'client’s explanation and supporting documents settle the question.',
        ]),
        ('h3', '2.3.2  Analysis of Corporate Bank Statements and Ledger '
               'Segregation'),
        ('bullets', [
            'Extended the same analysis to corporate clients, segregating income '
            'and expenses in the bank ledger account of the company.',
            'Grouped recurring payments such as salaries, statutory dues, rent, '
            'utilities and vendor settlements, and traced receipts against '
            'customer collections.',
            'Observed how a company’s cost structure and cash discipline can be '
            'read from its bank account, including how and where it controls '
            'expenditure.',
            'Gained a clearer understanding of the difference between the '
            'accounting treatment of an item and its tax treatment, which becomes '
            'important later in the computation stage.',
        ]),
        ('h3', '2.3.3  Winman CA-ERP and Retrieval of Form 26AS, AIS and TIS'),
        ('bullets', [
            'Was trained on Winman CA-ERP, the firm’s income tax and compliance '
            'software, and learned how client masters, computations and returns '
            'are organised within it.',
            'Used the software to access the income tax e-filing portal and '
            'download the forms required for return preparation, principally '
            'Form 26AS, the Annual Information Statement (AIS) and the Taxpayer '
            'Information Summary (TIS).',
            'Learned what each statement contains: Form 26AS for tax deducted '
            'and collected at source and taxes paid, AIS for reported financial '
            'transactions such as interest, dividends and securities '
            'transactions, and TIS for the summarised position derived from AIS.',
            'Understood why these downloads are the starting point of every '
            'income tax assignment: they show what the department already knows '
            'before the return is filed.',
        ]),
        ('h3', '2.3.4  Real-Time Accounting in Tally'),
        ('bullets', [
            'Recorded the transactions of client companies in the respective '
            'Tally company files maintained by the firm, covering receipts, '
            'payments, purchases, sales and journal entries.',
            'Selected the appropriate ledger and voucher type for each entry and '
            'wrote narrations clear enough for a reviewer or auditor to follow '
            'without asking questions.',
            'Observed how ledger grouping determines the final presentation in '
            'the profit and loss account and balance sheet, and how a single '
            'misclassification distorts both.',
            'Built up a much better sense of how the client’s business actually '
            'operates, because the ledger reveals the pattern of its dealings far '
            'more honestly than any summary.',
        ]),
        ('h3', '2.3.5  Goods and Services Tax Filing Support'),
        ('bullets', [
            'Downloaded and analysed acknowledgement forms and filed returns from '
            'the GST portal for client-wise records, including GSTR-1 for '
            'outward supplies, GSTR-2B for available input tax credit and GSTR-3B '
            'as the summary return.',
            'Assisted in requesting and unlocking files on the portal and '
            'observed both modes of authentication used in practice, online '
            'verification and signing through a Digital Signature Certificate.',
            'Assisted in the reconciliation of the books of account maintained in '
            'Tally with the GST returns filed, so that turnover and input tax '
            'credit as per the books agreed with the returns.',
            'Read the relevant provisions of the GST law while doing the work, '
            'which made the sections and their practical effect much easier to '
            'connect than reading them in isolation.',
        ]),
        ('h3', '2.3.6  TDS Compliance: Conso Files and the Return Preparation '
               'Utility'),
        ('bullets', [
            'Requested and downloaded consolidated (conso) files for client '
            'deductors through Winman TDS from the TRACES portal, following the '
            'request-and-download sequence required by the system.',
            'Extracted the data from the conso file using the TDS Return '
            'Preparation Utility (RPU version 4.6) and entered the details '
            'quarter-wise in the format required for filing.',
            'Analysed and interpreted the transactions and deductions contained '
            'in the conso files, identifying which payments attracted deduction, '
            'at what rate, and which were not chargeable.',
            'Read the conso file against Form 26AS to see how a deduction '
            'reported by the deductor appears as a credit in the deductee’s '
            'account, and why an error in a TDS statement becomes the '
            'deductee’s problem at the time of filing.',
        ]),
        ('h3', '2.3.7  Securities Transaction Tax, Bank Account Abstract and '
               'Statement of Total Income'),
        ('bullets', [
            'Worked on Securities Transaction Tax (STT): identified securities '
            'transactions from the Annual Information Statement and the '
            'broker-wise statements, verified the STT reflected against them and '
            'entered the details in Winman for the computation.',
            'Prepared bank account abstracts summarising the classified bank data '
            'into a working paper that could be used directly for computation.',
            'Entered the data in Winman and prepared the Statement of Total '
            'Income for individual and corporate clients, head of income by head '
            'of income.',
            'Reconciled tax credits appearing in Form 26AS with the taxes '
            'recorded in the books and the bank statement, so that advance tax, '
            'self-assessment tax and TDS were all correctly claimed.',
            'Assisted in the preparation of balance sheets and in computing the '
            'balance of tax payable or refundable after giving credit for taxes '
            'already paid.',
        ]),
        ('h3', '2.3.8  Return Filing and Statutory Audit Documentation'),
        ('bullets', [
            'Prepared income tax returns for upload once the Statement of Total '
            'Income was approved, allowing Winman to process the classified '
            'income and expenditure and generate the computation and the return.',
            'Independently completed the filing of three returns end to end '
            'during the closing weeks, from data entry to upload, after review '
            'by the Manager.',
            'Assisted in documentation work relating to statutory audit '
            'assignments of companies, including assembling ledgers, '
            'reconciliations and portal statements into audit working papers.',
            'Reconciled Form 26AS, AIS and TIS with the books of account as part '
            'of statutory audit and income tax verification procedures, and '
            'listed the differences requiring the client’s confirmation.',
        ]),

        ('h2', '2.4  TIMELINE OF ACTIVITIES'),
        ('p', 'The week-by-week record below is taken from the daily internship '
              'diary maintained during the programme and countersigned by the '
              'firm.'),
        ('h3', 'Week 1 (12 May – 15 May 2026): Individual Bank Statement '
               'Analysis'),
        ('bullets', [
            'Completed joining formalities, was introduced to the team and to the '
            'firm’s working conventions, and was allotted my first assignment.',
            'Analysed an individual client’s bank statement and split the income '
            'and expenses into the appropriate heads in the bank ledger account.',
            'Learned to distinguish income sources from drawings, and sorted a '
            'large number of miscellaneous receipts and payments by examining '
            'each transaction individually to determine whether it was income or '
            'expenditure.',
        ]),
        ('h3', 'Week 2 (18 May – 22 May 2026): Company Bank Statement Analysis'),
        ('bullets', [
            'Analysed the bank statements of corporate clients and segregated '
            'income and expenses in the bank ledger account of each company.',
            'Grouped recurring outflows such as salaries, statutory payments and '
            'vendor settlements, and matched inflows against customer receipts.',
            'Gained substantial exposure to how a company operates and controls '
            'its costs, simply by reading its bank account in detail.',
        ]),
        ('h3', 'Week 3 (25 May – 29 May 2026): Winman Software and Portal Forms'),
        ('bullets', [
            'Was trained on Winman, the software used by the firm to prepare '
            'computations and file returns, and learned its module structure.',
            'Used Winman to access the income tax portal and download the forms '
            'relating to return filing, including Form 26AS, AIS and TIS, for '
            'multiple clients.',
            'Learned how the information in these statements is used later in the '
            'computation, and organised the downloads client-wise in the firm’s '
            'documentation format.',
        ]),
        ('h3', 'Week 4 (1 June – 5 June 2026): Real-Time Accounting in Tally'),
        ('bullets', [
            'Entered client company transactions in the respective Tally version '
            'maintained for that company.',
            'Selected ledgers and voucher types appropriately and wrote clear '
            'narrations for each entry.',
            'Gained deeper insight into the client’s transactions and into how '
            'the company is being operated, and saw how ledger grouping affects '
            'the final financial statements.',
        ]),
        ('h3', 'Week 5 (8 June – 12 June 2026): Goods and Services Tax Filing'),
        ('bullets', [
            'Downloaded and analysed acknowledgement forms from the GST portal '
            'and worked with GSTR-1, GSTR-2B and GSTR-3B for client filings.',
            'Assisted in requesting and unlocking files on the portal, and '
            'observed authentication both online and through the Digital '
            'Signature Certificate method.',
            'Studied the relevant provisions of the GST Act while the work was in '
            'progress, which made the sections concerned much clearer.',
        ]),
        ('h3', 'Week 6 (15 June – 19 June 2026): TDS Conso Files and RPU'),
        ('bullets', [
            'Requested and downloaded consolidated (conso) files for client '
            'deductors using Winman TDS from the TRACES portal.',
            'Used the TDS Return Preparation Utility (RPU 4.6) to extract the '
            'data from the conso files and entered the details quarter-wise for '
            'filing.',
            'Learned to analyse and interpret the transactions and deductions '
            'recorded in the conso files, and understood the quarterly structure '
            'of TDS compliance.',
        ]),
        ('h3', 'Week 7 (22 June – 26 June 2026): TDS Analysis and 26AS Reading'),
        ('bullets', [
            'Continued working on TDS: downloaded further statements including '
            'Form 26AS for the clients concerned, and read them together with the '
            'conso files.',
            'Gained practical knowledge of TDS provisions and was able to '
            'identify which payments were chargeable to deduction and which '
            'deductions were correctly claimed.',
            'Understood how a mismatch between a deductor’s statement and a '
            'deductee’s Form 26AS arises, and why it must be corrected before the '
            'return is filed.',
        ]),
        ('h3', 'Week 8 (29 June – 3 July 2026): Securities Transaction Tax, '
               'Bank Abstract and Computation'),
        ('bullets', [
            'Worked on Securities Transaction Tax and the related data entry in '
            'Winman, tracing securities transactions and the STT against them '
            'from the Annual Information Statement and broker statements.',
            'Used the bank account abstract to prepare the working papers for '
            'computation, and carried out reconciliation of Form 26AS with the '
            'books.',
            'Assisted in the preparation of the balance sheet from the classified '
            'data.',
            'Entered the data in Winman and computed the Statement of Total '
            'Income, comparing tax already paid as per the bank statement and '
            'Tally with the tax still payable, for both individual and corporate '
            'clients.',
        ]),
        ('h3', 'Week 9 (6 July – 10 July 2026): Computation and Return '
               'Preparation'),
        ('bullets', [
            'Completed the computation of the Statement of Total Income for '
            'assigned clients and prepared the corresponding income tax returns '
            'for upload.',
            'Learned how the return is generated once the income and expenditure '
            'are entered in Winman, and how the software processes the data '
            'through to the final tax output.',
            'Cross-checked the computation manually against the working papers '
            'before submitting it for review, rather than relying on the software '
            'output alone.',
        ]),
        ('h3', 'Week 10 (13 July – 17 July 2026): Compliance Closure and '
               'Independent Filing'),
        ('bullets', [
            'Worked on the compliances of both individual and corporate clients '
            'and assisted in closing the files that had been compiled during the '
            'internship.',
            'Independently completed three filings end to end and closed them '
            'after review, which confirmed that I could carry out the full '
            'sequence from data entry to return filing.',
            'Assembled the final documentation, handed over the pending items to '
            'the team and completed the internship formalities.',
        ]),

        ('h2', '2.5  TOOLS AND SOFTWARE USED'),
        ('h3', '2.5.1  Tally'),
        ('p', 'Tally was the firm’s accounting platform and the tool in which I '
              'recorded client transactions. Working in it taught me the '
              'practical side of book-keeping that a textbook cannot convey: how '
              'ledgers are created and grouped, how voucher types determine the '
              'effect of an entry, how narrations serve as evidence for a later '
              'reviewer, and how the trial balance, profit and loss account and '
              'balance sheet are produced from the same underlying data. It also '
              'showed me how quickly a single wrong ledger selection propagates '
              'into the financial statements.'),
        ('h3', '2.5.2  Winman CA-ERP'),
        ('p', 'Winman CA-ERP was the firm’s income tax and compliance software '
              'and the tool I used most. It integrates income tax computation, '
              'return e-filing, balance sheet preparation, audit report utilities '
              'and TDS modules in a single environment (Winman Software, n.d.). I '
              'used it to access the income tax portal, download Form 26AS, AIS '
              'and TIS, enter income and expenditure data, prepare the Statement '
              'of Total Income and generate returns for upload. The software also '
              'runs validation checks, and learning to read those warnings '
              'carefully rather than clicking past them was itself a useful '
              'lesson.'),
        ('h3', '2.5.3  Winman TDS, TRACES and the Return Preparation Utility'),
        ('p', 'For TDS work I used Winman TDS to request and download conso '
              'files from TRACES, and the TDS Return Preparation Utility (RPU '
              '4.6) to extract and enter the quarterly data required for filing. '
              'This part of the internship gave me an understanding of the '
              'deductor’s side of the tax system, which is often invisible to a '
              'student: the quarterly statement, the challan, the deductee '
              'details and the resulting credit in the deductee’s Form 26AS are '
              'all links in one chain, and a break anywhere in that chain '
              'surfaces later as a mismatch.'),
        ('h3', '2.5.4  Income Tax e-Filing Portal'),
        ('p', 'The income tax e-filing portal was the source of the '
              'department’s own data on each assessee. I worked with Form 26AS, '
              'the Annual Information Statement and the Taxpayer Information '
              'Summary, and used them as the reference against which the books '
              'and bank data were verified. Understanding these statements '
              'changed the way I think about a tax return: filing is not a '
              'declaration made in isolation, it is a statement that must agree '
              'with information the department already holds.'),
        ('h3', '2.5.5  GST Portal'),
        ('p', 'On the indirect tax side I worked on the GST portal with GSTR-1, '
              'GSTR-2B and GSTR-3B, downloaded acknowledgements of filed returns, '
              'and assisted in requesting and unlocking files and in '
              'authenticating submissions online and through a Digital Signature '
              'Certificate. The portal made the mechanics of input tax credit '
              'concrete: credit available in GSTR-2B is credit reported by a '
              'supplier, so a client’s eligibility depends on someone else’s '
              'compliance.'),
        ('h3', '2.5.6  Microsoft Excel'),
        ('p', 'Excel was the working surface for everything that had to be '
              'sorted, classified or reconciled before it entered the accounting '
              'or tax software. I used it to classify bank statement entries, '
              'prepare bank account abstracts, build reconciliation statements '
              'between books and portal data, and summarise client positions for '
              'review. Sorting, filtering, lookup functions and pivot tables '
              'turned long statements into structured working papers, and I '
              'learned to lay a sheet out so that a reviewer can follow it '
              'without an explanation.'),
        ('h3', '2.5.7  Microsoft Word'),
        ('p', 'Word was used for the written output of the office: covering '
              'notes, client communications, documentation memos for audit files '
              'and the reports I submitted to my Manager for verification and '
              'approval. Preparing documents that would be read by a senior '
              'professional taught me to write briefly, in a fixed format, and '
              'without leaving loose ends for the reader to resolve.'),

        ('h2', '2.6  APPLICATION OF ACADEMIC KNOWLEDGE'),
        ('p', 'One of the most satisfying aspects of the internship was '
              'recognising, in a live file, a concept that had been taught in a '
              'classroom. The main areas of application were as follows.'),
        ('h3', '2.6.1  Financial Accounting and Bank Reconciliation'),
        ('bullets', [
            'Applied the fundamentals of double entry, ledger classification and '
            'grouping while recording transactions in Tally.',
            'Used the accounting equation and the distinction between capital and '
            'revenue items to decide the treatment of entries appearing in bank '
            'statements.',
            'Applied reconciliation technique in matching the bank account with '
            'the books, and in matching taxes recorded in the books against '
            'credits appearing in Form 26AS.',
        ]),
        ('h3', '2.6.2  Direct Taxation'),
        ('bullets', [
            'Applied the five heads of income and the structure of the Statement '
            'of Total Income while computing income for individuals and '
            'companies.',
            'Used the provisions relating to Tax Deducted at Source in practice, '
            'including deduction rates, chargeability and the quarterly statement '
            'cycle.',
            'Applied the concepts of advance tax, self-assessment tax and credit '
            'for taxes paid while arriving at the net tax payable or refundable.',
            'Applied the taxation of securities transactions, including '
            'Securities Transaction Tax, while working on client data drawn from '
            'the Annual Information Statement and broker statements.',
        ]),
        ('h3', '2.6.3  Indirect Taxation and GST'),
        ('bullets', [
            'Applied the return structure of GST, with outward supplies in '
            'GSTR-1, credit availability in GSTR-2B and the summary in GSTR-3B.',
            'Used the concept of input tax credit and its matching requirement '
            'while reconciling the books maintained in Tally with the returns '
            'filed.',
            'Read the relevant sections of the GST Act alongside the filings, '
            'which gave the statutory language a practical meaning.',
        ]),
        ('h3', '2.6.4  Accounting Systems and ERP Usage'),
        ('bullets', [
            'Extended classroom exposure to accounting systems by working in '
            'Tally and Winman on live client data.',
            'Understood how integrated software links books, computation, '
            'statutory forms and filing, and where human judgement still has to '
            'intervene.',
            'Learned the importance of master data, ledger structure and correct '
            'client set-up, since every downstream report depends on them.',
        ]),
        ('h3', '2.6.5  Financial Reporting and Analysis'),
        ('bullets', [
            'Applied financial statement knowledge while assisting in the '
            'preparation of balance sheets and while reviewing profit and loss '
            'presentation in Tally.',
            'Used analytical techniques from financial reporting coursework to '
            'interpret a client’s income and expenditure pattern from its bank '
            'account.',
            'Applied reporting discipline in preparing working papers and '
            'client reports for my Manager’s verification and approval.',
        ]),

        ('h2', '2.7  SKILLS DEVELOPED DURING THE INTERNSHIP'),
        ('p', 'The internship developed both technical and behavioural skills, '
              'and in most cases the two grew together, because accuracy in this '
              'work is as much a habit as it is a technique.'),
        ('h3', '2.7.1  Classification and Documentation Skills'),
        ('p', 'I became confident in reading a bank statement or a ledger and '
              'deciding how each entry should be treated, and in assembling the '
              'supporting downloads and working papers into a file that a '
              'reviewer could follow without explanation.'),
        ('h3', '2.7.2  Attention to Detail'),
        ('p', 'Tax work punishes carelessness. Checking a figure against its '
              'source before accepting it, and flagging what could not be '
              'verified, became automatic by the later weeks of the internship.'),
        ('h3', '2.7.3  Software Proficiency'),
        ('p', 'I moved from being a beginner to working independently in Tally '
              'and Winman CA-ERP, and gained working familiarity with Winman TDS, '
              'the TDS Return Preparation Utility, the income tax e-filing portal '
              'and the GST portal.'),
        ('h3', '2.7.4  Time Management'),
        ('p', 'With several client files open at once during filing season, I '
              'learned to sequence work by due date rather than by convenience, '
              'and to finish one file completely before starting the next.'),
        ('h3', '2.7.5  Organizational Skills'),
        ('p', 'Maintaining client-wise folders, naming downloaded statements '
              'consistently and keeping a written list of pending clarifications '
              'improved the way I organise my own work.'),
        ('h3', '2.7.6  Teamwork'),
        ('p', 'Working under Ms. A. Lakshmi and alongside Ms. Aruna taught me how '
              'a small professional team divides work, reviews it and covers for '
              'each other during deadline periods.'),
        ('h3', '2.7.7  Confidentiality'),
        ('p', 'Handling client bank statements, portal credentials and digital '
              'signature tokens taught me that discretion is part of the job and '
              'not an optional courtesy.'),
        ('h3', '2.7.8  Adaptability'),
        ('p', 'I learned to pick up an unfamiliar process by watching it once, '
              'noting the steps, attempting it under supervision and then '
              'performing it independently.'),

        ('h2', '2.8  KEY OBSERVATIONS FROM THE JOB'),
        ('p', 'The clearest observation from the internship is that compliance '
              'work rests on the quality of the underlying records. Where a '
              'client maintained proper books and gave prompt clarifications, a '
              'return could be prepared and filed quickly; where records were '
              'incomplete, most of the effort went into establishing what had '
              'actually happened before any computation could begin.'),
        ('p', 'A second observation is that the tax administration now holds a '
              'great deal of information independently of the assessee. Form '
              '26AS, the Annual Information Statement, the Taxpayer Information '
              'Summary and GSTR-2B all arrive before the return is filed, which '
              'means the professional’s task is to reconcile and explain rather '
              'than merely to report.'),
        ('p', 'A third observation concerns interdependence. A deduction reported '
              'incorrectly by a deductor becomes a missing credit for a client of '
              'the firm; an input tax credit depends on a supplier’s own filing. '
              'Much of the work therefore involves chasing information that sits '
              'outside the firm’s control.'),
        ('p', 'Finally, I observed that a professional office runs on review. No '
              'figure leaves the firm on the strength of one person’s work, and '
              'that discipline, rather than individual brilliance, is what keeps '
              'the error rate low.'),

        ('h2', '2.9  CHALLENGES ENCOUNTERED DURING THE INTERNSHIP'),
        ('p', 'The internship was demanding in ways that had little to do with '
              'accounting, and it would be dishonest to present it otherwise. '
              'Each of the following difficulties contributed something to the '
              'experience.'),
        ('h3', '2.9.1  Daily Travel'),
        ('p', 'The internship was on-site at the firm’s Mylapore office and I '
              'commuted by bus for about an hour each way, in crowded conditions, '
              'every working day for a little over two months. The first '
              'fortnight was genuinely tiring. I managed it by leaving early '
              'enough to avoid the worst of the rush and by treating the journey '
              'as fixed personal time rather than lost time. By the second month '
              'the routine had become normal, and punctuality became a matter of '
              'professional commitment rather than effort.'),
        ('h3', '2.9.2  Screen Fatigue'),
        ('p', 'The work is almost entirely computer-based, and after long '
              'stretches of classifying entries and reading statements my eyes '
              'would burn by the end of the day. I learned to alternate between '
              'on-screen data entry and paper-based verification, to look away '
              'periodically, and to schedule the most detailed reconciliation '
              'work for the earlier part of the day when concentration was '
              'highest.'),
        ('h3', '2.9.3  Repetitive Work and Monotony'),
        ('p', 'A compliance practice involves performing the same process across '
              'many client files, and there were days when the repetition became '
              'tiring and my interest dipped. What helped was changing my frame '
              'of reference: instead of counting files, I treated each client as '
              'a different set of facts, looked for what was unusual in that '
              'particular statement and tried to reduce the time I took per file. '
              'Setting small internal targets made the routine much easier to '
              'sustain, and I came to see that accuracy maintained through '
              'monotony is itself a professional skill.'),
        ('h3', '2.9.4  Unfamiliar Statutory Processes'),
        ('p', 'Conso files, the Return Preparation Utility, quarterly TDS '
              'statements and the mechanics of GST authentication were entirely '
              'new to me and are not covered in detail in coursework. Repetition '
              'under supervision, and written notes taken immediately after each '
              'demonstration, were what eventually made them routine.'),
        ('h3', '2.9.5  Incomplete Client Information'),
        ('p', 'Bank statements frequently contained entries with no usable '
              'narration, and the correct treatment could not be settled without '
              'the client’s explanation. I learned to list such items for '
              'clarification instead of deciding them myself, which was the single '
              'most useful correction I received during the internship.'),

        ('h2', '2.10  OVERALL JOB EXPERIENCE'),
        ('p', 'Taken as a whole, the internship gave me exposure across the full '
              'width of a compliance practice rather than depth in a single task. '
              'I worked on bank statement analysis, accounting in Tally, GST '
              'returns, TDS statements, Securities Transaction Tax data, the '
              'Statement of Total Income, return filing and audit documentation, '
              'and I could see how each of these fed into the others.'),
        ('p', 'The experience also changed how I understand finance as a career. '
              'Before the internship I thought of accounting largely as '
              'record-keeping and of taxation as a set of rules to be learned. '
              'The work showed me that both are exercises in evidence: the figure '
              'matters less than the ability to demonstrate where it came from. '
              'That shift in perspective is probably the most durable thing I '
              'take away from the two months.'),
        ('p', 'The progression from observation to independent filing within ten '
              'weeks was possible only because responsibility was handed over '
              'gradually and every piece of work was reviewed. By the final week '
              'I was completing filings end to end, which gave me a realistic '
              'sense of what an entry-level role in a practice actually involves.'),

        ('h2', '2.11  SUMMARY OF RESPONSIBILITIES'),
        ('p', 'The responsibilities handled during the internship are summarised '
              'below.'),
        ('table', {'rows': [
            ['S. No.', 'Area of Work', 'Major Responsibility'],
            ['1', 'Bank Statement Analysis',
             'Classification of individual and corporate bank entries into '
             'income, expenditure, drawings and transfers'],
            ['2', 'Real-Time Accounting',
             'Recording client transactions in Tally with correct ledgers and '
             'narrations'],
            ['3', 'Portal Downloads',
             'Retrieval of Form 26AS, AIS and TIS through Winman CA-ERP'],
            ['4', 'GST Compliance',
             'GSTR-1, GSTR-2B and GSTR-3B support, acknowledgements, file '
             'requests and DSC authentication'],
            ['5', 'GST Reconciliation',
             'Matching books maintained in Tally with the GST returns filed'],
            ['6', 'TDS Compliance',
             'Conso files from TRACES and quarter-wise data entry through the '
             'Return Preparation Utility'],
            ['7', 'Securities Transaction Tax',
             'Tracing securities transactions and STT from AIS and broker '
             'statements into the computation'],
            ['8', 'Bank Account Abstract',
             'Preparation of bank abstracts as working papers for computation'],
            ['9', 'Statement of Total Income',
             'Computation of total income and verification of taxes paid against '
             'taxes payable'],
            ['10', 'Return Filing',
             'Preparation and upload of income tax returns, including three '
             'filings completed independently'],
            ['11', 'Audit Documentation',
             'Assembly of ledgers, reconciliations and portal statements for '
             'statutory audit assignments'],
            ['12', 'Reporting',
             'Client reports prepared for the Manager’s verification and approval'],
        ], 'widths': [1, 3, 6], 'col_bold': [True, True, False],
            'col_align': ['center', 'left', 'left']}),
        ('p', 'These responsibilities provided exposure to several connected '
              'compliance processes and made their interdependence visible.'),

        ('h2', '2.12  CONCLUSION OF JOB / TASK DESCRIPTION'),
        ('p', 'The work described in this chapter covered the entire sequence of '
              'a compliance assignment in a chartered accountancy practice: '
              'collection of records and portal data, classification and '
              'recording, reconciliation against departmental information, '
              'computation, review and filing.'),
        ('p', 'It also allowed me to apply concepts from financial accounting, '
              'direct taxation, indirect taxation, accounting systems and '
              'financial reporting to live client files, and to learn the '
              'software on which Indian practice actually runs. The tasks were '
              'routine in form but consequential in effect, since each one ended '
              'in a filing that carried a statutory deadline and a client’s '
              'liability.'),
        ('p', 'Most importantly, the chapter reflects a progression. The work I '
              'was given in the first week required supervision at every step; '
              'the work I completed in the last week was carried out '
              'independently and was approved with only minor observations. That '
              'progression is the clearest measure of what the internship '
              'achieved.'),
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
        ('p', 'This chapter is an honest assessment of how I performed during the '
              'ten weeks of the internship. It is based on the work actually '
              'allotted to me, the corrections I received from my Manager and '
              'colleagues, and my own record of what I found easy and what I '
              'found difficult.'),

        ('h2', '3.1  QUALITY OF WORK'),
        ('p_indent', 'In a chartered accountancy practice, the quality of an '
              'intern’s work is measured in a very direct way: how much of it '
              'survives review unchanged. By that measure my output improved '
              'substantially over the course of the internship. In the first two '
              'weeks my classification of bank statement entries required '
              'frequent correction, mostly because I treated ambiguous credits as '
              'income instead of listing them for clarification. Once I learned to '
              'flag doubtful items rather than decide them, the number of '
              'corrections fell sharply.'),
        ('p', 'The most demanding work from a quality standpoint was the '
              'reconciliation of Form 26AS, AIS and TIS with the books of '
              'account, because a difference of even a small amount has to be '
              'explained rather than absorbed. I learned to work to the figure '
              'rather than to the appearance of the figure, to tick and trace '
              'each credit to its source, and to record on the working paper '
              'where each number came from. By the final phase, the Statement of '
              'Total Income computations I prepared were being approved with only '
              'minor observations, and in the last two weeks I completed three '
              'filings independently from data entry through to upload after '
              'review. The client reports I prepared for my Manager were verified '
              'and approved, which I regard as the clearest evidence that the '
              'quality of the work met the firm’s standard.'),

        ('h2', '3.2  TIMELINESS AND TASK OWNERSHIP'),
        ('p', 'The internship fell in the filing season, so timeliness was not a '
              'matter of personal efficiency but of statutory consequence. I '
              'reached the office on time each day despite a long commute, and I '
              'made it a rule to report the status of a pending file before '
              'leaving, so that my Manager was never left guessing about what had '
              'and had not been completed.'),
        ('p', 'Task ownership developed gradually. Early in the internship I '
              'treated an assignment as finished when the entries were made; by '
              'the end I treated it as finished only when the working papers were '
              'complete, the reconciliation differences were listed, and the file '
              'was in a state that someone else could pick up. Where I could not '
              'complete something because a client clarification was awaited, I '
              'recorded the pending point in writing instead of leaving it in '
              'memory. Over ten weeks I did not miss a deadline given to me, '
              'although on a few occasions I needed help to meet one.'),

        ('h2', '3.3  ADAPTABILITY AND LEARNING CURVE'),
        ('p', 'The internship demanded adaptation on three fronts at once: new '
              'software, new statutory subject matter and a professional working '
              'environment. The software learning curve was the steepest in the '
              'third week, when I moved from Excel and Tally into Winman and had '
              'to understand not only the tool but the tax logic it encoded. The '
              'TDS work in weeks six and seven was the most conceptually '
              'difficult, because conso files, the Return Preparation Utility and '
              'quarterly statements form a system with its own vocabulary that '
              'nothing in my coursework had prepared me for.'),
        ('p', 'What made adaptation possible was the firm’s method of teaching by '
              'demonstration and correction. I was shown a process once, allowed '
              'to attempt it under supervision, and then expected to repeat it '
              'independently. I found that taking notes immediately after a '
              'demonstration, rather than relying on memory, was the single most '
              'useful habit I formed, and I referred back to those notes '
              'constantly. By the eighth week I was able to move between bank '
              'abstracts, Tally, Winman and the portals without needing '
              'step-by-step guidance.'),

        ('h2', '3.4  COMMUNICATION AND COLLABORATION'),
        ('p', 'Because the reporting line in the firm was short, communication '
              'was frequent and direct. I reported to Ms. A. Lakshmi, Manager, who '
              'reviewed my work and to whom the whole team reported, and I worked '
              'day to day alongside Ms. Aruna, who demonstrated most of the '
              'processes to me for the first time and continued to guide my work '
              'throughout the internship. Her willingness to explain a process '
              'twice, and to check my output before it went for review, was the '
              'main reason I was able to take on independent work by the end of '
              'the programme.'),
        ('p', 'I learned three specific communication lessons. First, that a '
              'question asked early costs far less than an error corrected late, '
              'and that in a professional office asking is not treated as '
              'weakness. Second, that queries should be raised with the '
              'preparatory work already done, so that a senior is asked to decide '
              'rather than to investigate. Third, that written communication '
              'matters: a short, clear note attached to a file saves an entire '
              'conversation. Working in a team of qualified and experienced '
              'colleagues also taught me the professional etiquette of an office '
              'where client confidentiality is absolute and casual discussion of '
              'client affairs is simply not done.'),

        ('h2', '3.5  STRENGTHS DEMONSTRATED'),
        ('bullets', [
            '**Attention to detail in volume work:** I was able to work through '
            'long bank statements and conso files entry by entry without losing '
            'accuracy, which is the fundamental requirement of the work.',
            '**Willingness to learn new systems:** I picked up Tally, Winman, the '
            'Return Preparation Utility and two government portals within the '
            'internship period and was able to use them independently.',
            '**Reliability:** work allotted to me was completed and reported, and '
            'pending items were disclosed rather than concealed.',
            '**Receptiveness to correction:** I treated review comments as '
            'instruction rather than as criticism, which is why the error rate in '
            'my work fell steadily.',
            '**Perseverance:** I sustained a demanding routine, including a '
            'two-hour daily commute, for the full duration of the internship '
            'without absence.',
        ]),

        ('h2', '3.6  AREAS FOR IMPROVEMENT'),
        ('bullets', [
            '**Speed alongside accuracy:** my accuracy became reliable, but I was '
            'slower than an experienced assistant on the same file. Speed in this '
            'work comes from familiarity with recurring patterns, and I need more '
            'volume of practice to build it.',
            '**Depth of statutory knowledge:** I could apply the provisions I was '
            'shown, but I want a firmer grounding in the sections of the Income '
            'Tax Act and the GST Act so that I can reason from the statute rather '
            'than from the process.',
            '**Advanced Excel:** I used sorting, filters, lookups and pivot '
            'tables competently, but more advanced functions and templated '
            'working papers would have reduced my manual effort considerably.',
            '**Client-facing communication:** my interaction was mostly internal. '
            'Handling client queries and collecting information directly from '
            'clients is a skill I still need to develop.',
            '**Managing energy over long periods:** learning to structure the '
            'working day so that concentration is preserved through routine work '
            'is something I improved during the internship but have not yet '
            'mastered.',
        ]),

        ('h2', '3.7  OVERALL PERFORMANCE'),
        ('p', 'Overall, I consider the internship to have been performed to the '
              'standard the firm expected of an intern, and in the closing weeks '
              'slightly beyond it. Work on bank statement analysis, accounting in '
              'Tally, GST returns, TDS statements, Securities Transaction Tax '
              'data, the Statement of Total Income and audit documentation was '
              'completed and accepted, the client reports I prepared were '
              'verified and approved by my Manager, and three returns were filed '
              'independently after review.'),
        ('p', 'The clearest evidence of progress is the fall in corrections. In '
              'the first fortnight my classification of bank entries was '
              'frequently amended; by the final phase computations were approved '
              'with only minor observations. I also maintained full attendance '
              'and met every deadline given to me, which in a filing season '
              'matters as much as technical accuracy.'),
        ('p', 'Where I fell short was speed and statutory depth, and both are '
              'addressed in the previous section. Taken together, the performance '
              'gave me a realistic picture of what a practice expects: consistent '
              'accuracy, honest reporting of what is pending, and the willingness '
              'to be corrected. The internship has provided a solid foundation '
              'for further development in accounting, taxation and audit work.'),
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
        ('p', 'This chapter sets out what I actually took away from the '
              'internship, separating the technical knowledge acquired from the '
              'professional habits developed, and connecting both back to my MBA '
              'coursework.'),

        ('h2', '4.1  TECHNICAL KNOWLEDGE ACQUIRED'),
        ('bullets', [
            '**Real-time accounting:** the ability to record varied accounting '
            'transactions in Tally with correct ledger selection, voucher type '
            'and narration, for both individual and corporate clients.',
            '**Bank statement analysis:** the ability to read a bank statement as '
            'a primary accounting record, splitting entries into income, '
            'expenditure, drawings, transfers and capital items, and to prepare a '
            'bank account abstract from it.',
            '**Statement of Total Income:** the ability to compute total income '
            'head by head for individuals and companies in Winman, give credit '
            'for taxes already paid, and arrive at the net tax payable or '
            'refundable.',
            '**Securities Transaction Tax:** exposure to STT and to the treatment '
            'of securities transactions, including tracing them from the Annual '
            'Information Statement and broker statements into the computation.',
            '**Income tax return filing:** familiarity with the full filing '
            'sequence, from portal downloads and computation through to generation '
            'and upload of the return, including three filings completed '
            'independently.',
            '**TDS compliance:** working knowledge of conso files from TRACES, the '
            'TDS Return Preparation Utility, quarter-wise statement preparation, '
            'and the relationship between a deductor’s statement and the '
            'deductee’s Form 26AS.',
            '**GST compliance:** practical exposure to GSTR-1, GSTR-2B and '
            'GSTR-3B, to acknowledgement and unlocking of files on the portal, to '
            'Digital Signature Certificate authentication, and to reconciliation '
            'of books with returns filed.',
            '**Audit documentation:** an understanding of the working papers a '
            'statutory audit requires, and of how ledgers, reconciliations and '
            'portal statements are assembled into audit evidence.',
        ]),

        ('h2', '4.2  PRACTICAL EXPOSURE TO COMPLIANCE PROCESSES'),
        ('p', 'The internship gave me a working map of the Indian compliance '
              'calendar that I did not have before. I now understand, from having '
              'done the work, that monthly GST returns and TDS payments, '
              'quarterly TDS statements and the annual income tax filing cycle '
              'each impose their own rhythm on a practice, and that these cycles '
              'overlap in the months between May and September.'),
        ('p', 'More importantly, I understood the architecture behind them. The '
              'tax administration now collects information independently of the '
              'assessee, through TDS statements filed by deductors, through '
              'reporting by banks and financial institutions, and through the GST '
              'return chain. Form 26AS, AIS and TIS on the direct tax side, and '
              'GSTR-2B on the indirect tax side, are the visible outputs of that '
              'collection. The professional’s job is to reconcile the '
              'client’s records with that independently gathered data and to '
              'explain the differences. Once I saw this, filing stopped looking '
              'like form-filling and started looking like evidence-based '
              'reporting.'),

        ('h2', '4.3  IMPROVEMENT IN ANALYTICAL AND SYSTEM THINKING'),
        ('p', 'Analytically, the biggest change was learning to ask what a figure '
              'means rather than where it goes. A credit in a bank account is not '
              'self-explanatory: it may be a sale, a loan, a refund, a transfer '
              'between the client’s own accounts or a capital introduction, and '
              'each carries a different accounting and tax consequence. Learning '
              'to interrogate entries in this way, and to withhold judgement '
              'until the supporting fact is available, is the analytical habit I '
              'value most from the internship.'),
        ('p', 'In terms of systems thinking, I learned to see the whole chain '
              'rather than the step in front of me. A single misclassified entry '
              'in Tally travels into the trial balance, the balance sheet, the '
              'computation of total income and finally into a filed return, where '
              'it becomes very expensive to correct. A TDS deduction wrongly '
              'reported by a deductor becomes a missing credit in someone '
              'else’s Form 26AS and a dispute at the time of assessment. '
              'Understanding these dependencies changed how carefully I treated '
              'work that appeared trivial in isolation.'),

        ('h2', '4.4  SOFT SKILLS AND PROFESSIONAL TRAITS STRENGTHENED'),
        ('bullets', [
            '**Discipline and punctuality:** sustaining a fixed office routine '
            'with a long daily commute for the full internship period.',
            '**Accuracy as a professional value:** developing the instinct to '
            'verify rather than assume, because in tax work the cost of an error '
            'is borne by the client.',
            '**Confidentiality:** handling client bank statements, portal '
            'credentials and digital signature tokens with the discretion the '
            'profession requires.',
            '**Learning from correction:** treating review comments as training '
            'rather than as criticism, and tracking my own recurring mistakes.',
            '**Teamwork:** working effectively with colleagues, particularly in '
            'learning processes from Ms. Aruna and in coordinating pending items '
            'with the team.',
            '**Communication:** asking precise questions, reporting status '
            'proactively, and writing notes a reviewer can act upon.',
            '**Resilience:** maintaining output through fatigue, repetition and '
            'deadline pressure.',
        ]),

        ('h2', '4.5  ALIGNMENT WITH ACADEMIC LEARNING'),
        ('p', 'The internship served as a practical extension of the subjects '
              'studied in the MBA programme. The table below maps each subject to '
              'the work in which it was applied.'),
        ('table', {'rows': [
            ['Academic Subject', 'Internship Application'],
            ['Financial Accounting',
             'Ledger classification, voucher entry and recording of client '
             'transactions in Tally'],
            ['Direct Taxation',
             'Heads of income, Statement of Total Income, TDS provisions, '
             'Securities Transaction Tax and return filing'],
            ['Indirect Taxation (GST)',
             'GSTR-1, GSTR-2B and GSTR-3B filings and reconciliation of books '
             'with returns'],
            ['Auditing and Assurance',
             'Documentation for statutory audit assignments and verification of '
             '26AS, AIS and TIS against the books'],
            ['Financial Reporting and Analysis',
             'Assistance in balance sheet preparation and interpretation of '
             'income and expenditure patterns'],
            ['Accounting Systems and ERP',
             'Practical work in Tally and Winman CA-ERP, including master data '
             'and ledger structure'],
            ['Business Communication',
             'Working papers, client reports for the Manager’s approval and '
             'internal queries on pending clarifications'],
        ], 'widths': [3, 6], 'col_bold': [True, False],
            'col_align': ['center', 'left'], 'row_height': 500}),
        ('p', 'The internship aligned closely with the first-year MBA (Finance) '
              'curriculum, and in several places it inverted the order in which I '
              'had learned things, which turned out to be instructive. Financial '
              'accounting concepts of double entry, ledger grouping and '
              'capital-versus-revenue distinction were applied daily in Tally. '
              'Direct taxation concepts, the heads of income, computation of total '
              'income, TDS and advance tax, were applied in every Winman '
              'computation. Indirect taxation was applied in the GST filings and '
              'input tax credit reconciliation. Financial reporting and analysis '
              'were applied while assisting with balance sheets and while reading '
              'a client’s income and expenditure pattern from its bank account.'),
        ('p', 'Equally, the internship exposed the limits of purely academic '
              'preparation. Coursework taught me the treatment of a transaction '
              'once its nature is known; practice taught me that establishing the '
              'nature of the transaction is most of the work. Coursework presented '
              'reconciliation as an exercise with a known answer; practice '
              'presented it as an investigation where the difference may lie in '
              'the client’s records, the bank’s records or the '
              'department’s data. That gap between a clean textbook problem and a '
              'live client file is, in my view, the real content of an '
              'internship.'),

        ('h2', '4.6  OVERALL REALISATIONS'),
        ('bullets', [
            'Compliance work is judgement work. The software performs the '
            'arithmetic; the professional decides the treatment, and that decision '
            'is what the client is paying for.',
            'Documentation is not administrative overhead. A working paper that '
            'shows where each figure came from is the only practical defence when '
            'a filing is questioned months later.',
            'Deadlines in this profession are external and non-negotiable, which '
            'imposes a discipline of planning that is quite different from '
            'academic deadlines.',
            'Accuracy is a form of respect for the client, because the '
            'consequences of an error, a notice, interest, penalty or a lost '
            'refund, fall on them and not on the person who made it.',
            'Repetitive work is where competence is actually built. The tenth '
            'bank statement teaches more than the first, because by then the '
            'exceptions start to become visible.',
            'A small professional firm can be an outstanding place to learn, '
            'because exposure is broad, review is immediate and responsibility '
            'arrives early.',
        ]),

        ('h2', '4.7  PROFESSIONAL INSIGHTS AND LEARNINGS'),
        ('p', 'Three insights from the internship will stay with me beyond the '
              'technical content.'),
        ('p', 'The first concerns the nature of professional trust. Clients '
              'handed the firm their complete financial histories, portal '
              'credentials and signing tokens on the strength of a relationship '
              'built over years. That trust visibly governed the firm’s internal '
              'behaviour, in the review discipline, in the care taken with '
              'documentation and in the refusal to guess at a treatment when a '
              'clarification could be obtained. I now understand that a '
              'professional practice is not selling documents; it is selling '
              'reliability.'),
        ('p', 'The second concerns learning inside an organisation. I learned '
              'most of what I know now not from being taught formally but from '
              'watching a colleague work, attempting it myself and having my '
              'output corrected. Ms. Aruna demonstrated processes to me patiently '
              'and repeatedly, and my Manager’s review comments told me exactly '
              'where my understanding was thin. Being willing to be corrected '
              'turned out to be the most efficient learning strategy available.'),
        ('p', 'The third concerns my own career direction. Before the internship '
              'my interest in finance was general. Having worked through '
              'classification, reconciliation, computation and filing on live '
              'files, I now know that I am drawn to the accounting, taxation and '
              'audit side of finance, where the work is precise, the standards '
              'are external and the output is verifiable. I also know the '
              'weaknesses I need to address, namely speed, statutory depth and '
              'client-facing experience, and I have a clear idea of how to work '
              'on them.'),
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
              'M/s S. Ravi & Associates, Chartered Accountants, Mylapore, '
              'Chennai, from 12 May 2026 to 17 July 2026, on-site, in the domain '
              'of Accounting and Finance, under the guidance of Ms. A. Lakshmi, '
              'Manager. The ten-week programme coincided with the income tax '
              'return filing season for Assessment Year 2026-27, and the work '
              'allotted to me was live client work with statutory deadlines.'),
        ('p', 'The internship progressed in a deliberate sequence. It began with '
              'the analysis of bank statements, first of individual clients and '
              'then of corporate clients, where I classified every entry into '
              'income, expenditure, drawings and transfers within the bank ledger '
              'account. It moved to the firm’s software environment, where I was '
              'trained on Winman CA-ERP, accessed the income tax portal and '
              'downloaded Form 26AS, AIS and TIS, and recorded client '
              'transactions in Tally. The middle weeks were devoted to statutory '
              'compliance: GST filings involving GSTR-1, GSTR-2B and GSTR-3B, '
              'acknowledgement and unlocking of files on the portal and Digital '
              'Signature Certificate authentication, followed by TDS work '
              'involving conso files from TRACES, the Return Preparation Utility '
              'and quarter-wise data entry.'),
        ('p', 'The closing weeks brought the strands together. I worked on '
              'Securities Transaction Tax and the related data entry in Winman, '
              'and then, using bank account abstracts, Tally data and reconciled '
              'Form 26AS credits, computed the Statement of Total Income for '
              'individual and corporate clients in Winman, assisted in the '
              'preparation of balance sheets, verified taxes paid against taxes '
              'payable, and prepared returns for upload. '
              'I independently completed three filings end to end after review, '
              'assisted in documentation for statutory audit assignments, and '
              'reconciled Form 26AS, AIS and TIS with the books of account as '
              'part of audit and income tax verification procedures. The client '
              'reports I prepared were verified and approved by my Manager.'),

        ('h2', '5.2  KEY TAKEAWAYS'),
        ('h3', '5.2.1  Technical Competence in Accounting and Taxation'),
        ('bullets', [
            'Acquired the ability to record accounting transactions in Tally and '
            'to prepare a bank account abstract and Statement of Total Income '
            'from primary records.',
            'Learned to work in Winman CA-ERP across computation, portal '
            'downloads, return preparation and filing.',
            'Gained working knowledge of TDS statement preparation through conso '
            'files and the Return Preparation Utility, and of GST return filing '
            'and reconciliation.',
        ]),
        ('h3', '5.2.2  Reconciliation as a Core Discipline'),
        ('bullets', [
            'Understood that reconciliation, not data entry, is the central skill '
            'in modern compliance work.',
            'Learned to reconcile books maintained in Tally with GST returns '
            'filed, and Form 26AS, AIS and TIS with the books of account.',
            'Learned to treat a difference as a question to be answered rather '
            'than a figure to be adjusted.',
        ]),
        ('h3', '5.2.3  Understanding of Statutory Compliance and Deadlines'),
        ('bullets', [
            'Learned the monthly, quarterly and annual compliance cycles of an '
            'Indian practice and how they overlap during the filing season.',
            'Understood the consequences of delay and error, including notices, '
            'interest and loss of credit, and therefore why verification precedes '
            'submission.',
            'Saw how a professional firm plans its work backwards from an external '
            'due date.',
        ]),
        ('h3', '5.2.4  Adaptability in a Digital Compliance Environment'),
        ('bullets', [
            'Worked across Tally, Winman CA-ERP, Winman TDS, the TDS Return '
            'Preparation Utility, the income tax e-filing portal, the GST portal, '
            'Excel and Word within a single internship.',
            'Learned how far Indian tax administration has moved towards '
            'pre-populated, data-driven assessment, and what that means for the '
            'accountant’s role.',
            'Became comfortable learning a new system quickly by observing, '
            'noting the steps and then executing under review.',
        ]),
        ('h3', '5.2.5  Professional Discipline and Resilience'),
        ('bullets', [
            'Sustained a demanding on-site routine, including a two-hour daily '
            'commute, for the full duration of the internship.',
            'Learned to manage screen fatigue and the monotony of repetitive '
            'processing without allowing accuracy to slip.',
            'Understood that consistency over ten weeks is valued more highly in '
            'a professional office than occasional brilliance.',
        ]),
        ('h3', '5.2.6  Teamwork and Learning from Colleagues'),
        ('bullets', [
            'Learned most processes through demonstration and correction by '
            'colleagues, particularly Ms. Aruna, whose guidance and support made '
            'independent working possible.',
            'Learned to work within a review structure, submitting work for '
            'verification and accepting correction as part of the process.',
            'Developed the confidence to ask questions early, report status '
            'honestly and hand over a file in a state another person can '
            'continue.',
        ]),

        ('h2', '5.3  CONCLUSION'),
        ('p', 'The internship at M/s S. Ravi & Associates, Chartered Accountants, '
              'was the point at which my study of finance became practical. Over '
              'ten weeks I moved from reading a bank statement for the first time '
              'to filing income tax returns independently, and in doing so I '
              'acquired a set of skills that are directly employable: accounting '
              'in Tally, computation and filing in Winman, TDS statement '
              'preparation, GST return work, reconciliation against departmental '
              'data, and documentation for statutory audit.'),
        ('p', 'Beyond the technical content, three things changed. First, my '
              'understanding of accuracy: in a professional practice, accuracy is '
              'not a personal standard but an obligation owed to the client, '
              'enforced by internal review and tested by the tax administration. '
              'Second, my understanding of process: compliance work has a '
              'sequence, and each step exists because someone once suffered the '
              'consequence of skipping it. Third, my understanding of myself. I '
              'learned that I can sustain a demanding routine, that I can absorb '
              'correction without losing confidence, and that detailed, '
              'verifiable work suits me.'),
        ('p', 'I am also clear about what remains to be developed. I need greater '
              'speed, a firmer command of the statutory provisions behind the '
              'processes I performed, stronger Excel technique and direct '
              'experience of dealing with clients. Knowing these gaps precisely, '
              'rather than in general terms, is itself an outcome of the '
              'internship.'),
        ('p', 'In conclusion, the internship achieved what a Summer Internship '
              'Programme is intended to achieve. It connected the MBA (Finance) '
              'curriculum to live professional work, it gave me the tools and '
              'habits used in Indian accounting practice, and it settled my '
              'career direction towards accounting, taxation and audit. I am '
              'grateful to CA S. Ravi for the opportunity, to Ms. A. Lakshmi for '
              'her supervision and review, and to Ms. Aruna and the team for '
              'their patient guidance, and I leave the firm with both the '
              'competence and the confidence to contribute to a professional '
              'finance team.'),
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
        ('bullets', [
            'Economic Times. (2025, June 30). Gross GST collections double in '
            'five years to hit record ₹22.08 lakh crore in FY25. Retrieved '
            'September 2026, from https://economictimes.indiatimes.com/news/'
            'economy/finance/indias-gst-collections-skyrocket-to-2208-lakh-crore-'
            'doubling-in-five-years/articleshow/122158450.cms',

            'ETCFO. (2025, October 16). Growth of India’s domestic Big Four in '
            'the chartered accountancy sector. The Economic Times. Retrieved '
            'September 2026, from https://cfo.economictimes.indiatimes.com/news/'
            'tax-legal-accounting/growth-of-indias-domestic-big-four-in-the-'
            'chartered-accountancy-sector/124596837',

            'Goods and Services Tax Network. (n.d.). Goods and Services Tax '
            'portal. Retrieved September 2026, from https://www.gst.gov.in/',

            'Grand View Research. (n.d.-a). Accounting services market size and '
            'share report, 2026-2033. Retrieved September 2026, from '
            'https://www.grandviewresearch.com/industry-analysis/'
            'accounting-services-market-report',

            'Grand View Research. (n.d.-b). Financial auditing professional '
            'services market report, 2025-2030. Retrieved September 2026, from '
            'https://www.grandviewresearch.com/industry-analysis/'
            'financial-auditing-professional-services-market',

            'IMARC Group. (n.d.). India accounting software market size, share '
            'and analysis, 2034. Retrieved September 2026, from '
            'https://www.imarcgroup.com/india-accounting-software-market',

            'Income Tax Department, Government of India. (n.d.). e-Filing portal: '
            'Form 26AS, Annual Information Statement and Taxpayer Information '
            'Summary. Retrieved September 2026, from '
            'https://www.incometax.gov.in/',

            'Institute of Chartered Accountants of India. (n.d.). About ICAI. '
            'Retrieved September 2026, from https://www.icai.org/',

            'Livemint. (2026, August 31). ITR filings cross 78 million for AY27, '
            'setting a new record. Retrieved September 2026, from '
            'https://www.livemint.com/news/india/'
            'itr-filings-cross-78-million-for-ay27-setting-new-record-'
            '11788271051056.html',

            'Mordor Intelligence. (n.d.). India accounting professional services '
            'market size and report analysis, 2031. Retrieved September 2026, '
            'from https://www.mordorintelligence.com/industry-reports/'
            'india-accounting-professional-services-market',

            'S. Ravi & Associates. (n.d.). About the firm. Retrieved September '
            '2026, from https://sravica.com/',

            'TRACES, Income Tax Department. (n.d.). TDS Reconciliation Analysis '
            'and Correction Enabling System. Retrieved September 2026, from '
            'https://www.tdscpc.gov.in/',

            'Winman Software. (n.d.). Winman CA-ERP: income tax, balance sheet, '
            'audit report and TDS software. Retrieved September 2026, from '
            'https://www.winmansoftware.com/',
        ]),
    ],
}

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]
