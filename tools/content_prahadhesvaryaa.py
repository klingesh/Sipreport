# -*- coding: utf-8 -*-
"""
Content of the Summer Internship Project report of Prahadhesvaryaa K. S.
(OSI2509093), MBA (Finance), ISSM Business School, Chennai.

Internship: Neuberg Diagnostics Private Limited, Chennai
Department: Internal Audit | Period: 11.05.2026 to 30.07.2026

Block vocabulary is documented in report_content.py.
"""

STUDENT = 'PRAHADHESVARYAA K. S.'
REG_NO = 'OSI2509093'
FIRM = 'Neuberg Diagnostics Private Limited'
FIRM_SHORT = 'Neuberg Diagnostics'
MENTOR = 'Ms. S. Saradha'
MENTOR_ROLE = 'Chartered Accountant'
PERIOD = '11th May 2026 to 30th July 2026'

# The INTERNSHIP CERTIFICATE page carries the heading only, matching the
# sample reports; the certificate is attached as a separate sheet.
EMBED_CERTIFICATE = False

# The sample reports list chapters only in the contents table, so the page
# is filled by giving those rows generous, evenly spaced heights rather
# than by inventing extra entries.
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
          'authentic record of **Ms. Prahadhesvaryaa K. S.** (OSI2509093) carried '
          'out at Neuberg Diagnostics Private Limited, Chennai, in partial '
          'fulfilment of the requirements for the award of the MBA degree.'),
    ('gap', 1),
    ('p', 'The project was completed under the guidance of **Ms. S. Saradha**, '
          'Chartered Accountant, Internal Audit, Neuberg Diagnostics Private '
          'Limited, during the period from May 11th to July 30th, 2026.'),
    ('gap', 4),
    ('p', '**Ms.Kavitha Manikandan**', 14),
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
    ('p', 'I, **Ms. Prahadhesvaryaa K. S.**, hereby declare that this SIP Project '
          'Report is based on my internship of approximately two and a half '
          'months done at '
          'Neuberg Diagnostics Private Limited, Chennai, as an Intern in the '
          'Internal Audit department, during the period from May 11th to July '
          '30th, 2026, under the guidance of **Ms. S. Saradha**, Chartered '
          'Accountant, Neuberg Diagnostics Private Limited and Indian School of '
          'Science and Management, Chennai.'),
    ('gap', 1),
    ('p', 'I further declare that the work presented in this report is my own, '
          'that it has been prepared from the assignments actually handled by me '
          'during the internship, and that it has not been submitted earlier for '
          'the award of any other degree or diploma.'),
    ('gap', 6),
    ('sign', ('Place: Chennai', 'Signature')),
    ('sign', ('Date:', '')),
    ('pagebreak',),

    # ---- acknowledgement ----
    ('gap', 4),
    ('big', 'ACKNOWLEDGEMENT'),
    ('gap', 1),
    ('p', 'I have undergone extensive training to complete this internship. '
          'However, it would not have been possible without the kind support and '
          'help of many individuals. I am using this opportunity to express my '
          'gratitude to everyone who supported me throughout this internship '
          'period.'),
    ('p', 'I would like to express my sincere gratitude to our respected '
          'Chairman, **Mr. KATHIRVEL GANAPATHIAPPAN**, for providing us with '
          'the '
          'valuable opportunity to carry out and complete this project.'),
    ('p', 'I express my heartfelt thanks to our visionary, dedicated and '
          'empowering Founder and Managing Director, **Dr. PARKAVI MAHALINGAM**, '
          'for her continuous support and meaningful guidance, which played a '
          'key role in our progress.'),
    ('p', 'I am highly indebted to our Academic Head, **Ms. KAVITHA '
          'MANIKANDAN**, '
          'for her guidance and constant supervision, for providing the '
          'necessary information regarding the project and for her support in '
          'completing it.'),
    ('p', 'I would also like to thank all the faculty members and staff of ISSM '
          'Business School who provided me with the facilities and the conducive '
          'conditions that were required for this project.'),
    ('p', 'My sincere gratitude to **MS. S. SARADHA**, CHARTERED ACCOUNTANT, '
          'INTERNAL AUDIT, NEUBERG DIAGNOSTICS PRIVATE LIMITED, for mentoring '
          'me, reviewing my work and offering immense support and knowledge '
          'throughout the internship, and to the management of Neuberg '
          'Diagnostics Private Limited for permitting me to undergo my Summer '
          'Internship Programme with the organisation.'),
    ('p', 'I am also thankful to the members of the internal audit team and to '
          'the branch and billing staff who responded to my queries, explained '
          'their processes and made it possible for me to work on live audit '
          'assignments.'),
    ('pagebreak',),

    # ---- executive summary ----
    ('gap', 1),
    ('big', 'The Executive Summary', 12),
    ('gap', 1),
    ('p', 'This report presents the work carried out during my Summer '
          'Internship Programme at Neuberg Diagnostics Private Limited, a '
          'Chennai headquartered diagnostics and pathology organisation. '
          'The internship was undertaken on-site in the Internal Audit '
          'department from 11 May 2026 to 30 July 2026, a period of '
          'twelve working weeks, under the guidance of **Ms. S. '
          'Saradha**, Chartered Accountant.'),
    ('p', 'The internship was located in a part of the business that '
          'students rarely see from the inside. A diagnostics chain earns '
          'its revenue through a very large number of small transactions '
          'across branches, collection centres, walk-in patients and '
          'corporate clients, each of which can be discounted, cancelled, '
          'amended or billed on credit. Internal audit exists to test '
          'whether those events happened within the organisation’s own '
          'rules, and that testing is what I was given to do.'),
    ('p', 'The work covered seven connected areas. I verified '
          'business-to-business KYC documents so that only eligible '
          'corporate customers received corporate benefits, and checked '
          'Test Requisition Forms for the laboratory seal. Two areas '
          'concerned pricing: deep discount verification, identifying '
          'walk-in customers discounted above thirty per cent, and free '
          'of cost verification, tracing cases billed at a full discount.'),
    ('p', 'The remaining areas were cash due monitoring, where I '
          'calculated the ageing of outstanding payments; service '
          'deletion verification, where I examined tests booked and later '
          'removed from the system and established who had deleted each '
          'one and why; and follow-up of Action Taken Reports, where I '
          'contacted branch staff for the evidence needed to close '
          'observations raised during branch audits. The tools were '
          'Suflam LIMS, Microsoft Excel and Microsoft Word.'),
    ('p', 'Professionally, the internship gave me three things a '
          'classroom cannot. First, an understanding of internal control '
          'as something tested rather than described, since a discount '
          'policy means little until somebody verifies transactions '
          'against it. Second, an appreciation of documentation as '
          'evidence. Third, the professional skill of following up with '
          'people busy with their own work, which is what closing an '
          'audit observation actually requires.'),
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

        ('h2', '1.1  GLOBAL DIAGNOSTICS LANDSCAPE'),
        ('p_indent', 'Diagnostics occupies an unusual position in healthcare. It '
                     'accounts for a modest share of total healthcare spending '
                     'but influences the majority of clinical decisions, because '
                     'treatment ordinarily begins with a test result. Over the '
                     'past two decades the sector has moved from hospital '
                     'laboratories serving their own patients towards large '
                     'independent chains that operate networks of laboratories '
                     'and collection centres, process samples at scale and '
                     'deliver reports digitally.'),
        ('p', 'Three developments have shaped the industry globally. The first is '
              'consolidation. Laboratory testing rewards scale, because a '
              'high-throughput analyser is expensive to buy and cheap to run per '
              'sample, so larger networks can offer wider test menus at lower '
              'cost per test. The second is automation and digitisation: barcoded '
              'samples, analyser interfacing, laboratory information management '
              'systems and electronic report delivery have reduced manual '
              'handling and shortened turnaround times. The third is the rise of '
              'preventive and wellness testing, which has changed the customer '
              'from a patient sent by a physician into a consumer who purchases '
              'a health package directly.'),
        ('p', 'These developments have consequences for control as much as for '
              'operations. A network that books tests at hundreds of points, '
              'prices them differently for corporate and retail customers, and '
              'allows amendments and cancellations at branch level, generates '
              'thousands of small decisions every day. In such an environment, '
              'financial control cannot rest on a monthly review of accounts '
              'alone; it depends on continuous testing of transactions against '
              'policy. This is why internal audit has become a standing function '
              'in the larger diagnostic organisations rather than an annual '
              'exercise.'),

        ('h2', '1.2  THE INDIAN DIAGNOSTICS CONTEXT'),
        ('p', 'India is one of the fastest growing diagnostics markets in the '
              'world. The Indian pathology laboratory services market grew from '
              'about USD 19.5 billion in 2025 to an estimated USD 22.2 billion '
              'in 2026 and is projected to reach USD 45.4 billion by 2034, a '
              'compound annual growth rate of roughly 9.4 per cent (IMARC Group, '
              'n.d.-a). The diagnostic laboratories segment is expected to grow '
              'at a similar pace, supported by rising health awareness, wider '
              'insurance coverage, the growing burden of lifestyle-related '
              'illness and increasing demand for preventive testing (IMARC '
              'Group, n.d.-b).'),
        ('p', 'The structure of the market is as significant as its size. '
              'Organised diagnostic chains account for only about twenty to '
              'twenty-five per cent of the Indian market, with the remainder '
              'served by standalone laboratories and hospital-based laboratories '
              '(CareEdge Ratings, n.d.). The sector is therefore highly '
              'fragmented, and the organised chains compete not only with each '
              'other but with a very large number of small local laboratories '
              'whose costs are lower and whose quality standards vary.'),
        ('p', 'Competition in this setting is conducted substantially through '
              'price. Chains offer discounted health packages, corporate rate '
              'cards, seasonal offers and business-to-business arrangements with '
              'hospitals, clinics, collection centres and companies. That is '
              'commercially necessary, but it creates a control problem: the '
              'difference between an authorised corporate rate and an '
              'unauthorised discount to a walk-in customer is a matter of '
              'documentation, and documentation is precisely what tends to be '
              'incomplete at a busy branch. Revenue leakage in a laboratory '
              'business rarely takes the form of one large loss; it accumulates '
              'through many small unverified concessions, cancelled or deleted '
              'bookings and receivables that are never collected.'),
        ('p', 'Regulation and accreditation also shape the Indian market. '
              'Accreditation by the National Accreditation Board for Testing and '
              'Calibration Laboratories is a mark of technical quality that '
              'corporate and institutional customers increasingly require, and '
              'accreditation itself depends on documented procedures and '
              'traceable records (NABL, n.d.). The discipline that quality '
              'accreditation imposes on laboratory processes closely resembles '
              'the discipline internal audit imposes on commercial processes, and '
              'during the internship I could see both operating in the same '
              'organisation.'),
        ('p', 'Technology adoption has been rapid. Laboratory information '
              'management systems now record the entire life of a sample, from '
              'booking and barcoding through testing, validation, billing and '
              'report delivery. For an auditor this is an advantage, because the '
              'system holds a record of who booked a test, who amended it, who '
              'deleted it and what discount was applied. Much of my work during '
              'the internship consisted of reading exactly those records.'),

        ('h2', '1.3  COMPANY OVERVIEW: NEUBERG DIAGNOSTICS PRIVATE LIMITED'),
        ('h3', '1.3.1  BACKGROUND AND OPERATIONS'),
        ('p', 'Neuberg Diagnostics Private Limited is a Chennai headquartered '
              'diagnostics organisation formed as an international consortium of '
              'established laboratories. It was founded by the healthcare '
              'entrepreneur **Dr. G. S. K. Velu**, and the consortium was announced '
              'in October 2017 as an alliance of leading laboratories across '
              'several countries (ETHealthworld, 2017). Its founding members are '
              'Anand Diagnostic Laboratory of Bengaluru, Supratech Micropath of '
              'Ahmedabad, Ehrlich Laboratory of Chennai, Global Labs of South '
              'Africa and Minerva Diagnostics of Dubai, which between them bring '
              'a combined heritage of more than two hundred years and process in '
              'excess of twenty million samples a year (Neuberg Diagnostics, '
              'n.d.-a).'),
        ('p', 'The organisation therefore differs from a chain built outwards '
              'from a single laboratory. It was assembled from laboratories that '
              'already had reputations in their own regions, and its growth has '
              'come from integrating them into a common network while retaining '
              'their local standing. The group operates across India, the United '
              'Arab Emirates, South Africa and the United States, and in India it '
              'runs reference laboratories, regional laboratories, diagnostic '
              'centres and collection points (Neuberg Diagnostics, n.d.-b).'),
        ('p', 'Operationally, the business serves two broad customer types, and '
              'the distinction between them was central to my internship. '
              'Walk-in or retail customers come to a branch or collection centre '
              'and are billed at retail rates, subject to authorised discounts '
              'and packages. Business-to-business customers, which include '
              'hospitals, clinics, nursing homes, corporate clients and '
              'collection partners, are billed at negotiated rates under '
              'documented arrangements, frequently on credit. Both streams pass '
              'through the same laboratory and the same information system, but '
              'they carry different pricing, different documentation requirements '
              'and different credit consequences.'),
        ('p', 'The internal audit function sits across this activity. It examines '
              'whether B2B relationships are supported by KYC documents and '
              'signed agreements, whether discounts granted fall within policy, '
              'whether free of cost services are authorised, whether deletions '
              'and amendments in the system are explained, whether receivables '
              'are being collected within agreed periods and whether observations '
              'raised in branch audits are closed with evidence. Those are the '
              'areas in which I worked.'),
        ('h3', '1.3.2  SERVICE LINES'),
        ('p', 'The organisation’s work can be grouped into the broad service '
              'lines set out below. The grouping reflects what was visible from '
              'the internal audit function during the internship.'),
        ('table', {'rows': [
            ['Service Line', 'Nature of Work', 'Customer'],
            ['Routine Pathology',
             'Biochemistry, haematology, clinical pathology and serology '
             'performed at regional laboratories',
             'Walk-in patients, clinics and hospitals'],
            ['Specialised and Reference Testing',
             'Molecular diagnostics, histopathology, cytogenetics and other '
             'advanced testing carried out at reference laboratories',
             'Referring laboratories, hospitals and specialists'],
            ['Preventive Health Packages',
             'Bundled wellness and health check profiles sold at package prices',
             'Retail and corporate customers'],
            ['Business-to-Business Arrangements',
             'Negotiated rate cards and credit arrangements with hospitals, '
             'clinics, collection centres and corporates',
             'Institutional and corporate clients'],
            ['Home Collection and Digital Reporting',
             'Sample collection at the customer’s premises and electronic '
             'delivery of reports',
             'Retail customers'],
        ], 'widths': [3, 5, 3]}),

        ('h2', '1.4  STRATEGIC FOCUS AND CULTURE'),
        ('p', 'The strategic position of a diagnostics organisation rests on two '
              'things that are difficult to build and easy to lose: clinical '
              'credibility and operational reliability. A laboratory report is '
              'relied upon by a physician who cannot independently verify it, so '
              'the value of the brand is essentially the trust placed in its '
              'accuracy. Reliability follows from turnaround time, network reach '
              'and consistency between locations.'),
        ('p', 'Because the organisation was formed from laboratories with '
              'established reputations, its strategy has emphasised quality '
              'credentials, breadth of test menu and geographic reach rather '
              'than price leadership. That in turn requires disciplined internal '
              'processes, since a network assembled from several member '
              'laboratories must present a single standard of service and a '
              'single standard of commercial conduct.'),
        ('h3', '1.4.1  VALUES IN PRACTICE'),
        ('bullets', [
            '**Accuracy of the report:** technical quality is the product, and '
            'accreditation, internal quality control and documented procedures '
            'exist to protect it.',
            '**Traceability:** every booking, amendment, deletion and discount '
            'is recorded in the laboratory information system against a user and '
            'a laboratory identification number, which makes later verification '
            'possible.',
            '**Policy before concession:** pricing, discounts and free of cost '
            'services are governed by policy rather than by individual '
            'discretion, and departures are treated as exceptions to be '
            'explained.',
            '**Confidentiality:** patient information and client commercial '
            'terms are both treated as confidential, and access is restricted to '
            'those handling the work.',
            '**Evidence-based closure:** an audit observation is closed on the '
            'strength of documentary evidence rather than on an assurance that '
            'the matter has been attended to.',
        ]),
        ('h3', '1.4.2  WORKPLACE CULTURE'),
        ('p', 'The internal audit department works in a manner that is '
              'necessarily independent of the branches and departments it '
              'reviews, and that independence sets the tone of the work. '
              'Observations are recorded factually, supported by extracts from '
              'the system, and pursued until evidence of correction is received. '
              'At the same time the relationship with branch staff has to remain '
              'workable, because the same branches must cooperate with the next '
              'review.'),
        ('p', 'Within the department the culture is instructive and review-based. '
              'I was shown a verification once, allowed to attempt it under '
              'supervision and then expected to carry it out independently, with '
              'my working sheets checked before any exception was reported. '
              'Guidance came from **Ms. S. Saradha**, Chartered Accountant, who '
              'allocated the work and reviewed the output, and from the other '
              'members of the audit team who explained the systems and the '
              'reasoning behind each check.'),
        ('h3', '1.4.3  STRATEGIC POSITIONING'),
        ('p', 'In a market where most laboratories are small and competition is '
              'substantially on price, the organisation positions itself on '
              'quality, test breadth and network reach. Sustaining that position '
              'requires margins to be protected on a very large number of small '
              'transactions, which is where commercial discipline becomes a '
              'strategic matter rather than an administrative one. Discounts '
              'granted outside policy, services provided free without '
              'authorisation, bookings deleted without explanation and '
              'receivables allowed to age all reduce the revenue that funds the '
              'technology and accreditation on which the positioning depends. '
              'Internal audit, seen in that light, is not a compliance overhead '
              'but a direct contributor to the strategy.'),

        ('h2', '1.5  SWOT ANALYSIS'),
        ('p', 'The following analysis is my own assessment, based on what I '
              'observed of the organisation’s working during the internship, and '
              'is presented from the perspective of a diagnostics network '
              'operating in a fragmented and price-competitive market.'),
        ('h3', '1.5.1  STRENGTHS'),
        ('bullets', [
            '**Heritage of the member laboratories:** the consortium brings '
            'together laboratories with long-established reputations in their '
            'own regions, giving the network credibility from the outset.',
            '**Scale of testing:** processing of more than twenty million '
            'samples a year supports a wide test menu and efficient use of '
            'high-throughput equipment.',
            '**Breadth of test offering:** routine pathology alongside '
            'specialised and reference testing allows the network to serve both '
            'retail customers and referring laboratories.',
            '**International footprint:** operations across India, the United '
            'Arab Emirates, South Africa and the United States reduce dependence '
            'on any single market.',
            '**Systems and traceability:** a laboratory information management '
            'system that records bookings, amendments, deletions and discounts '
            'makes disciplined internal audit possible.',
        ]),
        ('h3', '1.5.2  WEAKNESSES'),
        ('bullets', [
            '**Complexity of an assembled network:** integrating laboratories '
            'with different histories, systems and local practices into one '
            'standard of service is a continuing effort.',
            '**Dependence on branch-level discipline:** documentation for KYC, '
            'discounts and deletions is created at branches, so control quality '
            'varies with the staff and workload at each location.',
            '**Exposure to receivables:** business-to-business testing is '
            'largely on credit, which ties up working capital and requires '
            'continuous monitoring of ageing.',
            '**Price pressure on retail testing:** competition from local '
            'laboratories and aggregator platforms constrains retail pricing and '
            'encourages discounting.',
            '**Manual dependencies in verification:** although transactions are '
            'recorded in the system, much of the verification of supporting '
            'documents is still performed manually.',
        ]),
        ('h3', '1.5.3  OPPORTUNITIES'),
        ('bullets', [
            '**Growth of preventive testing:** rising health awareness and '
            'wider insurance coverage continue to expand demand for wellness '
            'packages and routine screening.',
            '**Shift from unorganised to organised testing:** with organised '
            'chains holding only about a fifth to a quarter of the market, there '
            'is considerable room for accredited networks to gain share.',
            '**Corporate and institutional tie-ups:** structured B2B '
            'arrangements with hospitals, clinics and employers offer volume, '
            'provided documentation and credit control are sound.',
            '**Analytics on system data:** the transaction data already held in '
            'the laboratory information system can be used to monitor '
            'discounting, deletions and collection patterns continuously rather '
            'than periodically.',
            '**Home collection and digital delivery:** convenience-led services '
            'extend the reach of the network without a proportionate increase in '
            'physical infrastructure.',
        ]),
        ('h3', '1.5.4  THREATS'),
        ('bullets', [
            '**Intense price competition:** discount-led competition from local '
            'laboratories and online aggregators compresses realisation per '
            'test.',
            '**Revenue leakage:** unauthorised discounts, unapproved free of '
            'cost services, unexplained deletions and uncollected receivables '
            'erode margins quietly and continuously.',
            '**Regulatory and accreditation requirements:** quality, safety and '
            'record-keeping obligations are demanding, and lapses carry both '
            'regulatory and reputational cost.',
            '**Reputational risk from error:** because the product is a clinical '
            'report, a single significant error can affect confidence out of all '
            'proportion to its financial value.',
            '**Attrition of trained staff:** technical and commercial staff are '
            'mobile in a growing sector, and turnover at branches weakens '
            'process discipline.',
        ]),

        ('h2', '1.6  KEY COMPETITORS'),
        ('p', 'The organisation competes with three different groups, each at a '
              'different point in the market. The tables below set out the '
              'principal categories with representative names.'),
        ('h3', '1.6.1  NATIONAL DIAGNOSTIC CHAINS'),
        ('table', {'rows': [
            ['Organisation', 'Principal Offering', 'Key Focus Area'],
            ['Dr. Lal PathLabs',
             'Routine and specialised pathology through a national network',
             'Retail testing with a wide collection-centre footprint'],
            ['Metropolis Healthcare',
             'Clinical laboratory testing and wellness packages',
             'Retail and institutional testing across multiple states'],
            ['Agilus Diagnostics (formerly SRL)',
             'Reference and routine laboratory services',
             'Hospital-linked and reference testing'],
            ['Thyrocare Technologies',
             'High-volume preventive test panels at low price points',
             'Wholesale and aggregator-led preventive testing'],
        ], 'widths': [3, 4, 4]}),
        ('h3', '1.6.2  REGIONAL AND HOSPITAL-BASED LABORATORIES'),
        ('table', {'rows': [
            ['Organisation', 'Principal Offering', 'Key Focus Area'],
            ['Vijaya Diagnostic Centre',
             'Integrated pathology and radiology services',
             'Strong regional presence in southern India'],
            ['Apollo Diagnostics',
             'Laboratory services supported by a hospital network',
             'Hospital-linked retail and corporate testing'],
            ['Hospital-attached laboratories',
             'Testing for the hospital’s own inpatients and outpatients',
             'Captive demand within the hospital'],
        ], 'widths': [3, 4, 4]}),
        ('h3', '1.6.3  STANDALONE LABORATORIES AND AGGREGATOR PLATFORMS'),
        ('table', {'rows': [
            ['Category', 'Offering', 'Competitive Effect'],
            ['Local standalone laboratories',
             'Routine tests at low prices with local convenience',
             'Hold the majority of the fragmented market and set local price '
             'expectations'],
            ['Online diagnostic aggregators',
             'Discounted packages booked through applications and websites',
             'Shift retail demand towards price comparison and deep discounting'],
            ['Collection-centre franchisees',
             'Sample collection under a brand, with testing outsourced',
             'Extend reach but require documented commercial arrangements'],
        ], 'widths': [3, 4, 4]}),

        ('h2', '1.7  COMPETITIVE POSITIONING'),
        ('p', 'The competitive logic of Indian diagnostics is that routine tests '
              'are becoming commoditised while specialised testing, accredited '
              'quality and reliable turnaround remain differentiated. '
              'Price-led players compete for volume on common tests; '
              'hospital-attached laboratories hold captive demand; the durable '
              'space for a large independent network lies in combining a wide '
              'test menu with credible quality and dependable service across '
              'many locations.'),
        ('p', 'Neuberg Diagnostics occupies that space. Its advantage is the '
              'reputation and technical depth of its member laboratories '
              'together with the scale of the combined network, and its challenge '
              'is to hold realisation per test while competing against '
              'lower-priced local alternatives. From the internal audit '
              'perspective in which I worked, this positioning translates into '
              'something very concrete: the organisation can afford negotiated '
              'corporate rates and authorised packages, but it cannot afford '
              'undocumented concessions. Verifying that discounts, free '
              'services, deletions and credit terms stay within policy is '
              'therefore part of defending the competitive position, not merely '
              'an accounting formality.'),

        ('h2', '1.8  KEY MILESTONES'),
        ('p', 'The development of the organisation can be traced through a few '
              'clear stages, using publicly reported information.'),
        ('p', 'The first was formation. In October 2017 the consortium was '
              'announced, bringing together laboratories from India, South '
              'Africa, the United Arab Emirates and the wider region under a '
              'single banner, and it was described at the time as one of the '
              'larger laboratory chains in the country from its inception in '
              'both footprint and revenue (ETHealthworld, 2017). Founding '
              'members were Anand Diagnostic Laboratory, Supratech Micropath, '
              'Ehrlich Laboratory, Global Labs and Minerva Diagnostics.'),
        ('p', 'The second stage was investment and expansion. In 2018 the group '
              'announced plans to invest about ₹200 crore over the following '
              'twelve to eighteen months to expand the business, including '
              'laboratory capacity and network reach (Times of India, 2018). '
              'Expansion of this kind is what allows a diagnostics network to '
              'widen its test menu and shorten turnaround times.'),
        ('p', 'The third stage was consolidation of the network into a common '
              'operating standard, supported by laboratory information systems '
              'that record the full life of a sample and by accreditation of '
              'laboratories. This is the stage whose effects I saw most directly, '
              'because the audit work I performed depended on system records of '
              'bookings, discounts, deletions and receipts being available and '
              'attributable.'),
        ('p', 'For a student of finance, the useful lesson in this history is '
              'that growth by consolidation creates a control agenda of its own. '
              'Each laboratory that joins a network brings its own practices, '
              'and the work of turning several good laboratories into one '
              'dependable organisation is largely the work of standardising '
              'processes, systems and documentation.'),

        ('h2', '1.9  REGULATORY AND ACCREDITATION ENVIRONMENT'),
        ('p', 'One feature of this industry deserves separate treatment, '
              'because it explains why the controls I tested exist in the form '
              'they do. A diagnostics organisation operates under a '
              'considerably denser regulatory and accreditation framework than '
              'most service businesses, and that framework reaches directly '
              'into the records an internal auditor examines.'),
        ('p', 'The principal quality framework is accreditation of medical '
              'laboratories against the international standard for quality and '
              'competence, administered in India by the national accreditation '
              'board (National Accreditation Board for Testing and Calibration '
              'Laboratories, n.d.). Accreditation of this kind is not a badge '
              'awarded once; it imposes continuing obligations on process '
              'documentation, traceability of a sample from collection to '
              'report, calibration records, competence of personnel and '
              'handling of non-conformities. Each of those obligations '
              'generates records, and records that are required to exist are '
              'records an internal audit function can test.'),
        ('p', 'Alongside accreditation sits the statutory requirement for '
              'registration of clinical establishments and adherence to '
              'prescribed minimum standards (Ministry of Health and Family '
              'Welfare, n.d.). For an organisation operating a network of '
              'laboratories and collection centres, compliance has to be '
              'demonstrated location by location, which is one reason the '
              'branch audit and action taken report cycle I worked on matters '
              'as much as the corporate controls do.'),
        ('p', 'The third element is data protection. A diagnostics business '
              'holds health information, which is among the most sensitive '
              'categories of personal data, and India’s data protection '
              'legislation imposes obligations on how such data is collected, '
              'used, retained and secured (Government of India, 2023). The '
              'practical effect on my own work was direct: extracts were '
              'limited to the fields a test required, certain identifiers were '
              'masked, and I worked with billing and service records rather '
              'than clinical results.'),
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
        ('p_indent', 'The purpose of the internship was to convert the auditing '
                     'and internal control concepts studied in the MBA programme '
                     'into supervised practical work inside a functioning '
                     'internal audit department. The internship was carried out '
                     'at Neuberg Diagnostics Private Limited, Chennai, from 15 '
                     'May 2026 to 30 July 2026, in the Internal Audit '
                     'department, under the guidance of **Ms. S. Saradha**, '
                     'Chartered Accountant.'),
        ('p', 'The specific objectives agreed at the start of the internship were '
              'as follows:'),
        ('bullets', [
            'To understand how an internal audit department plans, performs and '
            'reports verification work in a multi-branch service organisation.',
            'To learn the difference between a control that exists on paper and '
            'a control that can be demonstrated through records.',
            'To gain practical exposure to revenue-side controls in a '
            'diagnostics business, covering pricing, discounts, free services, '
            'billing amendments and receivables.',
            'To understand the documentation required to support a '
            'business-to-business relationship, including KYC records and signed '
            'agreements.',
            'To acquire working familiarity with the laboratory information '
            'management system in which bookings, laboratory identification '
            'numbers, billing entries and deletions are recorded.',
            'To learn how audit observations are raised, followed up and closed '
            'through an Action Taken Report.',
            'To develop the professional habits of accuracy, confidentiality, '
            'documentation and persistent follow-up.',
        ]),
        ('h3', '2.1.1  METHODOLOGY AND APPROACH'),
        ('p', 'The internship followed a task-based approach rather than a '
              'lecture-based one, and each area of work progressed through the '
              'same three stages. First, the purpose of the check was explained: '
              'what could go wrong in the process and what the organisation’s '
              'policy required. Second, the verification was demonstrated on '
              'live records and I performed it under supervision. Third, I '
              'carried it out independently and submitted the working sheet, with '
              'any exception listed for review before it was reported.'),
        ('p', 'Work was allocated and reviewed by **Ms. S. Saradha**, Chartered '
              'Accountant, and day-to-day guidance on systems and processes came '
              'from the other members of the internal audit team. Because the '
              'records examined were live and the observations raised affected '
              'real branches, every sheet I prepared was checked before it left '
              'the department.'),

        ('h2', '2.2  INITIAL ONBOARDING AND TRAINING'),
        ('p', 'The first days were used to build context before any verification '
              'began. The onboarding covered:'),
        ('bullets', [
            'An introduction to the organisation, the structure of the internal '
            'audit department and the reporting line for the work assigned to me.',
            'An explanation of the two customer streams, walk-in or retail and '
            'business-to-business, and of the different pricing and '
            'documentation each requires.',
            'An overview of the revenue cycle of a diagnostics branch, from '
            'registration and booking of a test to sample collection, testing, '
            'reporting, billing and collection.',
            'Familiarisation with Suflam LIMS, including where bookings, '
            'laboratory identification numbers, discounts, deletions and payment '
            'records are held and how they can be extracted for verification.',
            'An introduction to the company’s discount policy and to the '
            'authorisation levels that apply to concessions and free of cost '
            'services.',
            'An explanation of the internal audit documentation convention, '
            'including how a verification sheet is prepared, how an exception is '
            'described and what evidence must accompany it.',
            'The confidentiality expected while handling patient information, '
            'client rate cards and branch-level records.',
        ]),
        ('p', 'This grounding proved important. Once I understood why a '
              'particular check existed, the verification stopped being a '
              'clerical comparison and became a search for cases that did not '
              'fit the rule.'),

        ('h2', '2.3  WORK PLAN AND SCOPE'),
        ('p', 'The internship covered seven areas of verification within the '
              'internal audit function. The areas are described below in the '
              'order in which they were taken up, although in practice most of '
              'them continued in parallel throughout the internship as records '
              'became available.'),
        ('h3', '2.3.1  B2B KYC Verification and Documentation'),
        ('p', 'Collected KYC documents and signed memoranda of '
              'understanding from the sales personnel responsible for the '
              'business-to-business clients assigned to them. Checked '
              'whether the documentation on record was complete for each '
              'client and followed up with the sales personnel where '
              'documents were missing. Maintained the records properly so '
              'that only eligible B2B customers received the benefits '
              'attaching to a corporate arrangement. Learned how '
              'verification of business credentials distinguishes a genuine '
              'B2B client from a B2C customer, and how that distinction '
              'prevents misuse of corporate discounts. Improved my '
              'communication and follow-up skills, since obtaining '
              'documents from field personnel required repeated and '
              'courteous reminders.'),
        ('h3', '2.3.2  Test Requisition Form (TRF) Verification'),
        ('p', 'Checked Test Requisition Forms received from different '
              'branches against the corresponding billing records. Verified '
              'whether the B2B bills were sealed with the name of the '
              'respective laboratory, which is the evidence that the '
              'requisition was routed through an authorised laboratory. '
              'Noted the details of every form on which the seal was '
              'missing, so that the branch concerned could be asked to '
              'regularise it. Learned the importance of maintaining '
              'accurate records, and found that this work sharpened my '
              'observation, because the difference between an acceptable '
              'and an unacceptable form is often a single missing detail.'),
        ('h3', '2.3.3  Deep Discount Verification'),
        ('p', 'Identified walk-in customers who had received discounts of '
              'more than thirty per cent on their billing. Cross-checked '
              'each of those cases against the company’s discount policy to '
              'establish whether the concession was authorised and properly '
              'approved. Recorded the exceptions, that is the cases which '
              'did not fit the policy, for further verification by the '
              'audit team. Understood through this work the importance of '
              'following company policy while offering discounts, and the '
              'effect that unauthorised concessions have on realisation per '
              'test.'),
        ('h3', '2.3.4  Free of Cost (FOC) Verification'),
        ('p', 'Checked records to identify walk-in and business-to-business '
              'customers who had been given a hundred per cent discount, '
              'that is services provided free of cost. Verified the basis '
              'on which each free service had been granted and whether it '
              'carried the required authorisation. Recorded those cases for '
              'further review by the team so that the pattern of free '
              'services could be examined. Understood the importance of '
              'monitoring free services and of maintaining proper control '
              'over revenue-related transactions, since a free service is a '
              'complete waiver of revenue.'),
        ('h3', '2.3.5  Cash Due Monitoring'),
        ('p', 'Reviewed payment records to establish which billed amounts '
              'remained unpaid. Calculated the number of days between the '
              'payment date and the current date in order to identify the '
              'cash due status of each case. Prepared the resulting '
              'position so that the ageing of dues was visible and the '
              'older items could be pursued first. Gained an understanding '
              'of how pending payments are monitored and learned the '
              'importance of maintaining accurate financial records, since '
              'ageing can only be calculated correctly if the underlying '
              'dates are correct.'),
        ('h3', '2.3.6  Service Deletion Verification'),
        ('p', 'Reviewed deleted service records to identify cases where '
              'tests booked by customers were later removed from the '
              'system. Traced the respective laboratory identification '
              'numbers for the deleted services. Checked the details of who '
              'had made each deletion and the reason recorded for removing '
              'the laboratory identification number. Understood the '
              'importance of monitoring changes made in billing and '
              'recording, since a deletion removes a booking and therefore '
              'the revenue attached to it, and control over the process '
              'depends on every deletion being attributable and explained.'),
        ('h3', '2.3.7  Action Taken Report (ATR) Follow-Up for Branch Audits'),
        ('p', 'Followed up with branch staff through telephone calls to '
              'collect the evidence required to close audit observations '
              'raised during internal audits. Updated the status of pending '
              'and completed remarks regularly so that the position of each '
              'observation was current. Coordinated between the branches '
              'and the audit team where an observation needed clarification '
              'before it could be closed. Improved my communication and '
              'follow-up skills through this work, and learned how timely '
              'responses from the branches help complete the audit process '
              'effectively.'),

        ('h2', '2.4  TIMELINE OF ACTIVITIES'),
        ('p', 'The internship ran from 11 May 2026 to 30 July 2026, twelve '
              'working weeks in all. The daily '
              'internship diary records the areas of verification as continuing '
              'through the whole period, because records for each area became '
              'available at different times; the week-by-week account below '
              'therefore groups the work by the phase in which each area was '
              'principally taken up.'),
        ('h3', 'Week 1 (11 May – 16 May 2026): Orientation and Internal Audit '
               'Induction'),
        ('bullets', [
            'Completed joining formalities and was introduced to the internal '
            'audit team and to the scope of its work.',
            'Learned the revenue cycle of a diagnostics branch and the '
            'distinction between walk-in and business-to-business customers.',
            'Was familiarised with Suflam LIMS and shown where bookings, '
            'laboratory identification numbers, discounts, deletions and payment '
            'records are held.',
            'Studied the company’s discount policy and the authorisation levels '
            'applicable to concessions and free of cost services.',
        ]),
        ('h3', 'Week 2 (18 May – 23 May 2026): B2B KYC Verification'),
        ('bullets', [
            'Began collecting KYC documents and signed memoranda of '
            'understanding from the sales personnel for the B2B clients assigned '
            'to them.',
            'Checked the completeness of documentation for each client and listed '
            'the files in which documents were missing.',
            'Started maintaining the KYC records in the format used by the '
            'department.',
        ]),
        ('h3', 'Week 3 (25 May – 30 May 2026): B2B Documentation and Eligibility'),
        ('bullets', [
            'Continued the follow-up for pending KYC documents and updated the '
            'records as they were received.',
            'Verified that the clients on record were eligible for the '
            'business-to-business benefits being extended to them.',
            'Learned how verification of business credentials distinguishes a '
            'genuine B2B client from a B2C customer.',
        ]),
        ('h3', 'Week 4 (1 June – 6 June 2026): Test Requisition Form '
               'Verification'),
        ('bullets', [
            'Took up verification of Test Requisition Forms received from '
            'different branches.',
            'Verified whether the B2B bills were sealed with the respective '
            'laboratory name and noted the cases in which the seal was missing.',
            'Passed the details of the incomplete forms to the audit team so that '
            'the branches concerned could be asked to regularise them.',
        ]),
        ('h3', 'Week 5 (8 June – 13 June 2026): Deep Discount Verification'),
        ('bullets', [
            'Identified walk-in customers who had received discounts of more '
            'than thirty per cent.',
            'Cross-checked those cases against the company’s discount policy to '
            'establish whether the concession was authorised.',
            'Recorded the exceptions for further verification by the team and '
            'continued TRF verification alongside.',
        ]),
        ('h3', 'Week 6 (15 June – 20 June 2026): Free of Cost Verification'),
        ('bullets', [
            'Checked records to identify walk-in and B2B customers who had been '
            'given a hundred per cent discount.',
            'Verified the basis and authorisation for each free of cost case and '
            'recorded them for review.',
            'Observed how free services and deep discounts together indicate the '
            'extent of concessions being granted at branch level.',
        ]),
        ('h3', 'Week 7 (22 June – 27 June 2026): Cash Due Monitoring'),
        ('bullets', [
            'Reviewed payment records to establish outstanding amounts.',
            'Calculated the number of days between the payment date and the '
            'current date to identify the cash due status.',
            'Presented the ageing position so that older dues could be taken up '
            'first with the branches and clients concerned.',
        ]),
        ('h3', 'Week 8 (29 June – 4 July 2026): Service Deletion Verification'),
        ('bullets', [
            'Reviewed deleted service records to identify tests booked by '
            'customers and later removed from the system.',
            'Traced the respective laboratory identification numbers and '
            'examined who had deleted each service.',
            'Checked the reason recorded for each deletion and listed the cases '
            'in which no adequate reason was available.',
        ]),
        ('h3', 'Week 9 (6 July – 11 July 2026): Action Taken Report Follow-Up'),
        ('bullets', [
            'Began follow-up of Action Taken Reports for branch audits, '
            'contacting branch staff by telephone to collect the evidence needed '
            'to close observations.',
            'Recorded the responses received and updated the pending and '
            'completed status of each observation.',
            'Learned how an observation moves from being raised to being closed, '
            'and why closure requires evidence rather than assurance.',
        ]),
        ('h3', 'Week 10 (13 July – 18 July 2026): Continued Follow-Up and '
               'Recurring Verifications'),
        ('bullets', [
            'Continued the ATR follow-up and escalated observations on which no '
            'response had been received.',
            'Carried out the recurring verifications for the period, covering '
            'deep discounts, free of cost cases and deletions.',
            'Updated the KYC and TRF records with the documents received during '
            'the week.',
        ]),
        ('h3', 'Week 11 (20 July – 25 July 2026): Consolidation of Exception '
               'Records'),
        ('bullets', [
            'Consolidated the exceptions identified across discounts, free of '
            'cost cases, deletions and TRF seals into the formats used by the '
            'department.',
            'Reconciled the cash due position with the latest payment records.',
            'Submitted the consolidated working sheets for review and made the '
            'corrections indicated.',
        ]),
        ('h3', 'Week 12 (27 July – 30 July 2026): Closure and Handover'),
        ('bullets', [
            'Completed the pending updates to the ATR status and to the KYC '
            'records.',
            'Handed over the working sheets, exception listings and pending '
            'items to the audit team in a form in which they could be continued.',
            'Discussed the overall learning from the internship with my guide '
            'and completed the internship formalities.',
        ]),

        ('h2', '2.5  TOOLS AND SYSTEMS USED'),
        ('h3', '2.5.1  Suflam LIMS'),
        ('p', 'Suflam LIMS is the laboratory information management system used '
              'by the organisation, and it was the primary source of the records '
              'I verified. A laboratory information management system records the '
              'whole life of a booking: registration of the customer, allotment '
              'of a laboratory identification number, the tests booked, the '
              'discount applied, the amount billed, any amendment or deletion, '
              'the user who performed it and the payment received.'),
        ('p', 'For an auditor this makes the system an evidence base rather than '
              'merely an operational tool. Working in it taught me how to extract '
              'the records for a period, filter them for the condition being '
              'tested, such as a discount above a threshold or a deleted service, '
              'and then trace individual cases back to the laboratory '
              'identification number and the user concerned. It also taught me '
              'that the quality of any such review depends on the completeness '
              'of what is entered at the branch, since a reason field left blank '
              'cannot be audited.'),
        ('h3', '2.5.2  Microsoft Excel'),
        ('p', 'Excel was the working surface for every verification. I used it to '
              'lay out the records extracted from the system, to sort and filter '
              'them for the cases that met the test condition, to calculate the '
              'number of days between a payment date and the current date for '
              'cash due monitoring, and to prepare exception listings in a form '
              'that a reviewer could follow.'),
        ('p', 'Sorting, filtering, lookup functions, date calculations and '
              'conditional formatting turned long extracts into structured '
              'working papers. I also learned to lay a sheet out so that the '
              'basis of each conclusion is visible: the original record on the '
              'left, the policy requirement against it and the exception '
              'clearly marked, rather than a summary that has to be explained '
              'verbally.'),
        ('h3', '2.5.3  Microsoft Word'),
        ('p', 'Word was used for the written output of the department: audit '
              'notes, descriptions of observations, follow-up communications and '
              'the reports submitted for review. Writing an observation taught me '
              'a discipline that is quite specific to audit work. The statement '
              'has to be factual, has to identify the case precisely, has to '
              'state the policy or control that was not followed and has to avoid '
              'any language that reads as an accusation, because the purpose is '
              'correction of a process rather than blame.'),
        ('h3', '2.5.4  Audit Working Formats and Records'),
        ('p', 'Alongside the software, a set of departmental formats governed the '
              'work: KYC checklists for B2B clients, verification sheets for '
              'discounts and free of cost cases, the cash due statement and the '
              'Action Taken Report through which observations are tracked to '
              'closure. Working with these formats showed me why standardised '
              'documentation matters in audit: it makes the work of different '
              'people comparable, it preserves the evidence for later reference '
              'and it allows an incomplete item to be picked up by somebody '
              'else.'),

        ('h2', '2.6  APPLICATION OF ACADEMIC KNOWLEDGE'),
        ('p', 'One of the most satisfying aspects of the internship was '
              'recognising, in live records, a concept that had been taught in a '
              'classroom. The main areas of application were as follows.'),
        ('h3', '2.6.1  Auditing and Assurance'),
        ('p', 'Applied the basic audit approach of understanding a process, '
              'identifying what can go wrong in it and designing a check '
              'that would detect it. Used sampling and threshold-based '
              'selection in practice, for instance by examining discounts '
              'above thirty per cent and services billed at a hundred per '
              'cent discount. Applied the principle that an audit '
              'conclusion must rest on evidence, which is why every '
              'exception I reported carried the underlying record with it.'),
        ('h3', '2.6.2  Internal Control and Risk'),
        ('p', 'Applied the distinction between preventive and detective '
              'controls: an approval limit on discounts is preventive, '
              'while the verification I performed is detective. Saw how '
              'authorisation, documentation and segregation of duties work '
              'together, and what happens when a booking can be deleted '
              'without a recorded reason. Understood revenue leakage as a '
              'control risk rather than an accounting error, arising from '
              'many small unverified concessions rather than from one large '
              'mistake.'),
        ('h3', '2.6.3  Financial Accounting and Receivables Management'),
        ('p', 'Applied receivables and working capital concepts while '
              'calculating the ageing of dues in cash due monitoring. '
              'Understood how credit extended to business-to-business '
              'clients converts recognised revenue into a collection '
              'problem if it is not monitored. Learned how discounts and '
              'free services affect net realisation and therefore the '
              'revenue actually recorded.'),
        ('h3', '2.6.4  Business Communication'),
        ('p', 'Applied professional communication while collecting KYC '
              'documents from sales personnel and pursuing evidence from '
              'branch staff by telephone. Learned to write an audit '
              'observation factually and without accusation, and to record '
              'the status of a follow-up so that anyone reading it knows '
              'what is outstanding. Practised the skill of persistent but '
              'courteous follow-up, which is what actually closes an '
              'observation.'),
        ('h3', '2.6.5  Service Operations and Healthcare Administration'),
        ('p', 'Applied service operations concepts to a business where the '
              'product is a test report and the process runs from '
              'registration through collection, testing and reporting. '
              'Understood how a multi-branch network creates variation in '
              'process discipline and why standardisation matters for both '
              'quality and commercial control. Observed how documentation '
              'requirements in a regulated, accredited environment support '
              'both clinical quality and financial control.'),

        ('h2', '2.7  SKILLS DEVELOPED DURING THE INTERNSHIP'),
        ('p', 'The internship developed both technical and behavioural skills, '
              'and in this kind of work the two are closely connected, because a '
              'verification is only as good as the persistence behind it.'),
        ('h3', '2.7.1  Verification and Documentation Skills'),
        ('p', 'I became able to take a set of records, test them against a stated '
              'policy and produce a working sheet in which each exception is '
              'identified, supported and capable of being reviewed by somebody '
              'else.'),
        ('h3', '2.7.2  Observation and Attention to Detail'),
        ('p', 'Checking Test Requisition Forms for missing laboratory seals and '
              'deleted services for missing reasons trained me to notice the '
              'single absent detail in an otherwise complete record, which was '
              'the specific skill this work demanded.'),
        ('h3', '2.7.3  System Proficiency'),
        ('p', 'I gained working familiarity with Suflam LIMS, particularly with '
              'extracting booking, discount, deletion and payment records and '
              'tracing individual cases back to their laboratory identification '
              'numbers and users.'),
        ('h3', '2.7.4  Spreadsheet and Analytical Skills'),
        ('p', 'Sorting and filtering large extracts, applying lookups, '
              'calculating date differences for ageing and presenting exceptions '
              'clearly improved both my Excel technique and my ability to reason '
              'from data to a conclusion.'),
        ('h3', '2.7.5  Communication and Follow-Up'),
        ('p', 'Collecting documents from sales personnel and evidence from branch '
              'staff by telephone taught me how to ask precisely, how to keep a '
              'request alive without giving offence and how to record what was '
              'promised and by when.'),
        ('h3', '2.7.6  Professional Judgement'),
        ('p', 'I learned to distinguish an exception that reflects a genuine '
              'control failure from one that has a legitimate explanation, and to '
              'refer the doubtful cases upward instead of deciding them myself.'),
        ('h3', '2.7.7  Confidentiality'),
        ('p', 'Working with patient billing records, client rate cards and '
              'branch-level findings taught me that discretion is part of the '
              'auditor’s obligation and that findings are discussed only within '
              'the department until they are formally reported.'),
        ('h3', '2.7.8  Adaptability'),
        ('p', 'Seven areas of verification, each with its own logic and format, '
              'had to be learned within twelve weeks, and I developed '
              'the habit of noting the steps of a process immediately after it '
              'was demonstrated so that I could repeat it unaided.'),

        ('h2', '2.8  KEY OBSERVATIONS FROM THE JOB'),
        ('p', 'The clearest observation from the internship is that controls in a '
              'service network live or die at the point of entry. Policies on '
              'discounts, free services and B2B eligibility are written centrally '
              'but applied at a counter by a person under time pressure, and the '
              'gap between the two is exactly what internal audit measures.'),
        ('p', 'A second observation is that documentation is what converts a '
              'transaction into something reviewable. A discount with an '
              'approval attached to it is a commercial decision; the same '
              'discount without an approval is an exception, even if the '
              'commercial reasoning behind it was sound. The same is true of a '
              'deleted booking with a recorded reason as against one without.'),
        ('p', 'A third observation concerns the structure of revenue risk in a '
              'diagnostics business. Because each transaction is small, no single '
              'concession appears material, and that is precisely why the '
              'aggregate matters. Deep discounts, free of cost services, deleted '
              'services and ageing receivables are four different routes to the '
              'same outcome, which is revenue earned but not realised.'),
        ('p', 'Finally, I observed that audit depends on cooperation it cannot '
              'compel. Observations are closed by evidence held at branches, and '
              'obtaining that evidence is a matter of relationships and '
              'persistence as much as of authority.'),

        ('h2', '2.9  CHALLENGES ENCOUNTERED DURING THE INTERNSHIP'),
        ('p', 'The internship also presented practical difficulties, each of '
              'which contributed something to the learning.'),
        ('h3', '2.9.1  Obtaining Evidence from Branches'),
        ('p', 'Closing an audit observation required evidence from branch staff '
              'who were occupied with their own work, and responses were often '
              'delayed. Repeated telephone follow-up, a written record of what '
              'had been promised and escalation where nothing was received were '
              'what eventually moved the pending items.'),
        ('h3', '2.9.2  Incomplete Documentation'),
        ('p', 'KYC files were sometimes short of documents, Test Requisition '
              'Forms arrived without the laboratory seal and deletions were '
              'recorded without an adequate reason. I learned to list such cases '
              'precisely rather than attempt to interpret them, since an '
              'incomplete record is itself the finding.'),
        ('h3', '2.9.3  Volume of Records'),
        ('p', 'The number of transactions to be examined was large, and '
              'maintaining the same level of care through a long extract was '
              'demanding. Working in defined blocks, using filters to narrow the '
              'population before reading individual cases, and taking the most '
              'detailed checks early in the day were what kept the accuracy '
              'steady.'),
        ('h3', '2.9.4  Unfamiliar Systems and Terminology'),
        ('p', 'Laboratory identification numbers, Test Requisition Forms, service '
              'deletion entries and the structure of the laboratory information '
              'system were all new to me and are not covered in coursework. '
              'Repetition under supervision, and notes taken immediately after '
              'each demonstration, were what made them routine.'),
        ('h3', '2.9.5  Reporting Findings with Care'),
        ('p', 'An exception identified in audit concerns the work of a colleague '
              'in another part of the organisation, and learning to describe it '
              'factually, with the record attached and without implying intent, '
              'was one of the more subtle skills the internship required.'),

        ('h2', '2.10  OVERALL JOB EXPERIENCE'),
        ('p', 'Taken as a whole, the internship gave me a complete view of the '
              'revenue-side control environment of a diagnostics network rather '
              'than depth in a single task. Working across KYC documentation, '
              'requisition forms, discounts, free services, receivables ageing, '
              'service deletions and audit follow-up allowed me to see how the '
              'same commercial risk appears in different forms at different '
              'points of the process.'),
        ('p', 'The experience also changed how I understand audit as a career. '
              'Before the internship I thought of auditing largely as the '
              'verification of financial statements after the year had closed. '
              'The work showed me that internal audit operates continuously and '
              'much closer to the business, testing live transactions against the '
              'organisation’s own rules and reporting in time for something to be '
              'done about it.'),
        ('p', 'The progression over the period was from being shown each check to '
              'performing the recurring verifications independently and '
              'consolidating the exception records for review. By the closing '
              'weeks I was handling the follow-up of audit observations directly '
              'with branches, which gave me a realistic sense of what an '
              'entry-level role in an internal audit department involves.'),

        ('h2', '2.11  SUMMARY OF RESPONSIBILITIES'),
        ('p', 'The responsibilities handled during the internship are summarised '
              'below.'),
        ('table', {'rows': [
            ['S. No.', 'Area of Work', 'Major Responsibility'],
            ['1', 'B2B KYC Verification',
             'Collection of KYC documents and signed memoranda of understanding '
             'from sales personnel and maintenance of client records'],
            ['2', 'B2B Eligibility',
             'Verification that only eligible B2B customers received corporate '
             'benefits'],
            ['3', 'Test Requisition Forms',
             'Verification of TRFs from branches and of the laboratory seal on '
             'B2B bills, with missing seals recorded'],
            ['4', 'Deep Discounts',
             'Identification of walk-in discounts above thirty per cent and '
             'comparison against the discount policy'],
            ['5', 'Free of Cost Cases',
             'Identification of walk-in and B2B services billed at a hundred per '
             'cent discount and recording for review'],
            ['6', 'Cash Due Monitoring',
             'Review of payment records and calculation of days outstanding to '
             'establish the cash due position'],
            ['7', 'Service Deletions',
             'Examination of deleted services, the laboratory identification '
             'numbers involved, the user responsible and the reason recorded'],
            ['8', 'Branch Audit Follow-Up',
             'Telephone follow-up with branch staff to collect evidence and '
             'update Action Taken Report status'],
            ['9', 'Exception Reporting',
             'Preparation of exception listings and verification sheets for '
             'review by the audit team'],
            ['10', 'Documentation',
             'Maintenance of audit working papers, checklists and records in the '
             'departmental formats'],
        ], 'widths': [1, 3, 6], 'col_bold': [True, True, False],
            'col_align': ['center', 'left', 'left']}),
        ('p', 'These responsibilities provided exposure to several connected '
              'control processes and made the relationship between them visible.'),


        ('h2', '2.12  WORKING PAPERS AND AUDIT EVIDENCE'),
        ('p', 'A theme that ran through every assignment, and one I had not '
              'anticipated, was the standard of documentation expected behind '
              'each finding. An exception is not established when it is '
              'noticed; it is established when the record supporting it is '
              'attached and a reader can reach the same conclusion without '
              'being told. That principle governed how I was asked to work.'),
        ('p', 'In practice it produced several specific habits. Every '
              'exception listing recorded the identifier of the transaction, '
              'the branch, the date, the value, the rule it departed from and '
              'the source from which the data had been extracted. A discount '
              'above the permitted threshold was not reported as an excessive '
              'discount but as a specific bill, at a specific percentage, '
              'against a specific policy limit. That precision is what allows '
              'a branch to respond with evidence rather than with an opinion.'),
        ('p', 'The same discipline applied to the distinction between a '
              'finding and an inference. Where a deletion had been made '
              'without a recorded reason, the observation stated that the '
              'reason field was blank, not that the deletion was improper. '
              'Where a requisition form lacked a laboratory seal, the '
              'observation recorded the missing seal rather than concluding '
              'that the test had not been authorised. Learning to stop at what '
              'the evidence supported, and to leave the conclusion to the '
              'person with the authority to draw it, was among the more '
              'valuable things the twelve weeks taught me.'),
        ('h2', '2.13  CONFIDENTIALITY AND DATA HANDLING'),
        ('p', 'Working with live records in a healthcare organisation brought '
              'obligations no academic exercise had imposed on me. The data I '
              'handled identified patients and corporate clients, and in a '
              'diagnostics business even a test name attached to a name is '
              'sensitive information. The organisation’s expectations were '
              'stated at the outset and were not treated as a formality.'),
        ('h2', '2.14  CONCLUSION OF JOB / TASK DESCRIPTION'),
        ('p', 'The work described in this chapter covered the revenue-side '
              'control cycle of a diagnostics network: establishing that a client '
              'is entitled to the terms being given, that the paperwork supporting '
              'a test is complete, that concessions and free services fall within '
              'policy, that amendments to bookings are explained, that money '
              'billed is collected and that observations raised in audit are '
              'closed with evidence.'),
        ('p', 'It also allowed me to apply concepts from auditing, internal '
              'control, financial accounting and business communication to live '
              'records, and to learn the systems on which the verification '
              'depends. The tasks were routine in form but consequential in '
              'effect, since each exception identified represented either revenue '
              'that had been given away without authority or a control that was '
              'not being operated as intended.'),
        ('p', 'Most importantly, the chapter reflects a progression. The work I '
              'was given in the first week required supervision at every step; by '
              'the closing weeks I was performing the recurring verifications '
              'independently, consolidating exception records and following up '
              'audit observations with branches directly. That progression is the '
              'clearest measure of what the internship achieved.'),

        ('p', 'One further observation belongs here, because it shaped how I '
              'understood the whole assignment. Every test I performed had the '
              'same underlying structure: a rule, a population of transactions, '
              'and a comparison between the two. The rule might be a discount '
              'threshold, an eligibility condition, a credit period or an '
              'authorisation requirement, and the population might be bills, '
              'requisition forms, payment records or deletion logs, but the '
              'method did not change. Recognising that pattern was what turned '
              'seven apparently separate assignments into a single skill, and '
              'it is the reason I would now approach an unfamiliar control with '
              'a clear idea of how to begin testing it.'),
        ('p', 'Taken together, the twelve weeks moved from checking whether a '
              'document carried a seal to understanding why the seal is '
              'required at all, and that shift from procedure to purpose is '
              'the difference between performing an audit step and '
              'understanding one.'),

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
        ('p', 'This chapter is an assessment of how I performed during the '
              'internship. It is based on the work actually allotted to me, the '
              'corrections received from my guide and the audit team, and my own '
              'record of what I found straightforward and what I found difficult.'),

        ('h2', '3.1  QUALITY OF WORK'),
        ('p_indent', 'In an internal audit department the quality of an intern’s '
                     'work is measured in a direct way: whether the exceptions '
                     'reported survive review, and whether the working sheet '
                     'behind them can be understood without explanation. By that '
                     'measure my output improved substantially over the period of '
                     'the internship.'),
        ('bullets', [
            'KYC documents and memoranda of understanding for B2B clients were '
            'collected and the records maintained so that eligibility for '
            'corporate benefits could be demonstrated.',
            'Test Requisition Forms were checked against billing records and '
            'every missing laboratory seal was recorded with the details needed '
            'to take it up with the branch.',
            'Deep discount and free of cost cases were identified against defined '
            'thresholds and compared with the company’s discount policy before '
            'being reported as exceptions.',
            'Cash due positions were calculated from payment records with the '
            'days outstanding worked out case by case.',
            'Deleted services were traced to the laboratory identification '
            'number, the user responsible and the reason recorded, and cases '
            'without an adequate reason were listed.',
        ]),
        ('p', 'In the early weeks my working sheets required correction, mostly '
              'because I presented conclusions without laying out the underlying '
              'record beside them, which left the reviewer unable to check my '
              'reasoning. Once I learned to show the original entry, the policy '
              'requirement and the exception together, the number of corrections '
              'fell sharply. The internship taught me that quality in audit work '
              'is not only a matter of arriving at the right answer but of '
              'presenting it in a form that can be verified and relied upon.'),

        ('h2', '3.2  TIMELINESS AND TASK OWNERSHIP'),
        ('p', 'Audit work carries internal deadlines: verifications belong to a '
              'review period, and Action Taken Reports have to be current when '
              'they are presented. I completed the verifications allotted to me '
              'within the time given and reported the status of pending items '
              'before leaving, so that my guide was never left uncertain about '
              'what had and had not been finished.'),
        ('bullets', [
            'Followed up repeatedly with sales personnel for pending KYC '
            'documents instead of allowing the files to remain incomplete.',
            'Kept the Action Taken Report status updated as responses were '
            'received from branches, rather than updating it in a single batch at '
            'the end.',
            'Completed the recurring monthly verifications of discounts, free of '
            'cost cases and deletions within the review period.',
            'Recorded pending clarifications in writing rather than relying on '
            'memory.',
            'Referred doubtful cases to my guide instead of deciding them myself, '
            'which I came to see as part of ownership rather than a failure of it.',
        ]),
        ('p', 'Task ownership developed gradually. Early in the internship I '
              'treated an assignment as finished when the checking was done; by '
              'the end I treated it as finished only when the exceptions were '
              'listed, the evidence was attached and the file was in a state that '
              'somebody else could continue.'),

        ('h2', '3.3  ADAPTABILITY AND LEARNING CURVE'),
        ('p', 'The internship required adaptation on three fronts at once: an '
              'unfamiliar industry, an unfamiliar system and a form of work that '
              'coursework describes but does not rehearse. The steepest part of '
              'the curve was the first fortnight, in which I had to learn the '
              'revenue cycle of a diagnostics branch, the difference in treatment '
              'between walk-in and business-to-business customers, and the '
              'structure of the records held in Suflam LIMS.'),
        ('bullets', [
            'Learned the diagnostics revenue cycle from registration and booking '
            'through collection, testing, reporting, billing and collection of '
            'dues.',
            'Became able to extract and filter booking, discount, deletion and '
            'payment records from the laboratory information system.',
            'Picked up the company’s discount policy and the authorisation levels '
            'that determine whether a concession is an exception.',
            'Moved from being shown each verification to performing the recurring '
            'checks independently.',
            'Accepted review comments as instruction and tracked my own recurring '
            'mistakes so that they were not repeated.',
        ]),
        ('p', 'What made the adaptation possible was the department’s method of '
              'teaching by demonstration and correction, together with the habit '
              'I formed of writing down the steps of a process immediately after '
              'seeing it performed. Those notes were what I relied on when the '
              'same verification came around in the following month.'),

        ('h2', '3.4  COMMUNICATION AND COLLABORATION'),
        ('p', 'This internship involved more external communication than most '
              'finance internships, because a large part of the work depended on '
              'obtaining documents and evidence from people in other parts of the '
              'organisation.'),
        ('bullets', [
            '**Coordination with sales personnel:** collected KYC documents and '
            'signed memoranda of understanding for the B2B clients assigned to '
            'them, which required courteous and repeated reminders.',
            '**Follow-up with branch staff:** contacted branches by telephone to '
            'collect the evidence needed to close audit observations, and kept a '
            'record of what each branch had undertaken to provide.',
            '**Work within the audit team:** raised queries with my guide and '
            'the team when a case did not fit the policy clearly, and submitted '
            'working sheets for review before any exception was reported.',
            '**Written communication:** described observations factually and '
            'recorded the pending and completed status of each item so that '
            'anybody reading the report knew exactly what was outstanding.',
            '**Response to feedback:** corrections from my guide on the '
            'presentation of working papers improved both the accuracy and the '
            'usefulness of what I produced.',
        ]),
        ('p', 'The specific lesson I take from this is that an audit observation '
              'is closed by cooperation rather than by authority. Asking '
              'precisely, explaining why the evidence is needed and following up '
              'without causing offence were what actually produced results, and '
              'that is a skill I did not expect to develop in a finance '
              'internship.'),

        ('h2', '3.5  STRENGTHS DEMONSTRATED'),
        ('bullets', [
            '**Attention to detail in volume work:** worked through long extracts '
            'of billing, discount and deletion records without losing accuracy, '
            'which is the fundamental requirement of verification.',
            '**Observation:** identified missing laboratory seals on requisition '
            'forms and deletions lacking a recorded reason, where the finding is '
            'the absence of a single detail.',
            '**Persistence in follow-up:** pursued pending KYC documents and '
            'audit evidence until they were received or formally escalated.',
            '**Willingness to learn new systems:** became independent in Suflam '
            'LIMS and improved considerably in Excel within the internship '
            'period.',
            '**Receptiveness to correction:** treated review comments as training, '
            'which is why the error rate in my working papers fell steadily.',
            '**Discretion:** handled billing records, client rate cards and '
            'branch-level findings with the confidentiality the work required.',
        ]),

        ('h2', '3.6  AREAS FOR IMPROVEMENT'),
        ('bullets', [
            '**Speed alongside accuracy:** my accuracy became reliable, but an '
            'experienced team member completed the same verification faster. '
            'Speed here comes from familiarity with recurring patterns, and I '
            'need more volume of practice.',
            '**Advanced Excel:** I used sorting, filters, lookups and date '
            'calculations competently, but pivot tables and more advanced '
            'functions would have reduced my manual effort considerably.',
            '**Depth of audit standards:** I could apply the checks I was shown, '
            'but I want a firmer grounding in the standards on internal audit and '
            'in formal risk assessment so that I can help design checks rather '
            'than only perform them.',
            '**Sampling and analytics:** I would like to learn how to select a '
            'sample statistically and how to use data analytics on full '
            'populations instead of threshold-based extracts.',
            '**Confidence in escalation:** I improved at raising pending matters, '
            'but dealing firmly with a branch that does not respond is something '
            'I am still developing.',
            '**Understanding of the industry:** a deeper knowledge of laboratory '
            'operations, accreditation requirements and test costing would let me '
            'interpret the commercial significance of an exception more fully.',
        ]),

        ('h2', '3.7  OVERALL PERFORMANCE'),
        ('p', 'Overall, I consider the internship to have been performed to the '
              'standard the department expected of an intern, and in the closing '
              'weeks somewhat beyond it. Work on B2B KYC documentation, '
              'requisition form verification, deep discount and free of cost '
              'verification, cash due monitoring, service deletion verification '
              'and Action Taken Report follow-up was completed, reviewed and '
              'accepted, and by the end I was performing the recurring '
              'verifications independently and dealing with branches directly.'),
        ('p', 'The clearest evidence of progress is the change in the review '
              'comments I received. In the early weeks the comments concerned the '
              'basics of presentation and the completeness of evidence; in the '
              'later weeks they concerned interpretation, which is a more '
              'advanced conversation to be having. I also maintained full '
              'attendance through the period and met the timelines given to me.'),
        ('p', 'Where I fell short was in speed, in the use of advanced analytical '
              'tools and in formal knowledge of audit standards, and each of '
              'those is addressed in the previous section. Taken together, the '
              'performance gave me a realistic picture of what an internal audit '
              'department expects: consistent accuracy, evidence for every '
              'statement, honest reporting of what is pending and the persistence '
              'to see an observation through to closure.'),

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
        ('p', 'This chapter sets out what I took away from the internship, '
              'separating the technical knowledge acquired from the professional '
              'habits developed, and connecting both back to my MBA coursework.'),

        ('h2', '4.1  TECHNICAL KNOWLEDGE ACQUIRED'),
        ('bullets', [
            '**Internal audit verification:** the ability to take a process, '
            'identify what can go wrong in it, test transactions against the '
            'governing policy and report the exceptions with evidence.',
            '**B2B documentation and KYC:** an understanding of the documents and '
            'signed agreements that support a business-to-business relationship, '
            'and of why eligibility must be established before corporate benefits '
            'are given.',
            '**Billing and requisition controls:** familiarity with Test '
            'Requisition Forms, the significance of the laboratory seal on a B2B '
            'bill and the consequences of incomplete requisition records.',
            '**Discount and concession control:** practical knowledge of '
            'threshold-based testing of discounts, of comparison against a '
            'discount policy and of the treatment of free of cost services.',
            '**Receivables monitoring:** the ability to calculate days '
            'outstanding from payment records and to present an ageing position '
            'that supports collection follow-up.',
            '**System and amendment controls:** an understanding of how bookings, '
            'laboratory identification numbers, amendments and deletions are '
            'recorded in a laboratory information system and how they can be '
            'traced to a user and a reason.',
            '**Audit follow-up:** knowledge of how observations are raised, '
            'tracked through an Action Taken Report and closed on the strength of '
            'evidence.',
        ]),

        ('h2', '4.2  PRACTICAL EXPOSURE TO BUSINESS PROCESSES'),
        ('p', 'The internship gave me a working map of the revenue cycle of a '
              'diagnostics network that I did not have before. I now understand, '
              'from having verified it, how a test moves from registration and '
              'booking through sample collection, laboratory processing, '
              'reporting, billing and collection, and where in that sequence '
              'revenue can be lost.'),
        ('p', 'More importantly, I understood the architecture of control around '
              'that cycle. Eligibility is controlled at the point of onboarding a '
              'client, through KYC documents and a signed agreement. Pricing is '
              'controlled through a discount policy and authorisation limits. '
              'Billing integrity is controlled through requisition forms and '
              'through the traceability of amendments and deletions in the '
              'system. Collection is controlled through ageing of dues. Internal '
              'audit tests each of these and reports where the control was not '
              'operated. Once I saw the cycle as a chain of controls rather than '
              'a set of separate tasks, the purpose of each verification became '
              'obvious.'),

        ('h2', '4.3  IMPROVEMENT IN ANALYTICAL AND SYSTEM THINKING'),
        ('p', 'Analytically, the biggest change was learning to begin from the '
              'question rather than from the data. Instead of reading a list of '
              'transactions and hoping something would stand out, I learned to '
              'define the condition that would indicate a problem, such as a '
              'discount above a threshold, a service billed free, a deletion '
              'without a reason or a due older than an agreed period, and then to '
              'extract exactly those cases.'),
        ('p', 'In terms of systems thinking, the internship showed me how one '
              'weak link travels. A B2B client onboarded without complete KYC '
              'becomes a client billed at corporate rates without a demonstrable '
              'entitlement; a booking deleted without a reason becomes revenue '
              'that cannot be reconciled; a due not aged becomes a receivable '
              'nobody pursues. Seeing those chains changed how carefully I '
              'treated work that appeared clerical in isolation, because the '
              'clerical step was usually where the control actually sat.'),

        ('h2', '4.4  SOFT SKILLS AND PROFESSIONAL TRAITS STRENGTHENED'),
        ('bullets', [
            '**Communication with unfamiliar colleagues:** requesting documents '
            'and evidence from sales personnel and branch staff over the '
            'telephone, clearly and courteously.',
            '**Persistence:** keeping a request alive until it was answered, '
            'which is what closing an audit observation requires.',
            '**Accuracy as a professional value:** verifying rather than assuming, '
            'because in audit an unverified statement is worse than no statement.',
            '**Objectivity:** describing what the record showed without implying '
            'motive, and referring doubtful cases upward.',
            '**Confidentiality:** handling patient billing data, client rate '
            'cards and audit findings with discretion.',
            '**Learning from correction:** treating review comments as training '
            'and tracking my own recurring errors.',
            '**Discipline in documentation:** producing working papers that a '
            'reviewer or a successor could pick up and use.',
        ]),

        ('h2', '4.5  ALIGNMENT WITH ACADEMIC LEARNING'),
        ('p', 'The internship served as a practical extension of the subjects '
              'studied in the MBA programme. The table below maps each subject to '
              'the work in which it was applied.'),
        ('table', {'rows': [
            ['Academic Subject', 'Internship Application'],
            ['Auditing and Assurance',
             'Verification of discounts, free of cost services, deletions and '
             'requisition forms, and reporting of exceptions with evidence'],
            ['Internal Control and Risk Management',
             'Testing of authorisation, documentation and traceability controls '
             'across the revenue cycle'],
            ['Financial Accounting',
             'Understanding of how discounts, free services and deletions affect '
             'recorded revenue'],
            ['Working Capital and Receivables Management',
             'Cash due monitoring and calculation of days outstanding on billed '
             'amounts'],
            ['Business Communication',
             'Collection of KYC documents from sales personnel and telephone '
             'follow-up with branches for audit evidence'],
            ['Management Information Systems',
             'Use of Suflam LIMS records as audit evidence, including user and '
             'reason trails for amendments'],
            ['Service Operations Management',
             'Understanding of the branch-level processes through which a test is '
             'booked, collected, reported and billed'],
        ], 'widths': [3, 6], 'col_bold': [True, False],
            'col_align': ['center', 'left']}),
        ('p', 'The internship also exposed the limits of purely academic '
              'preparation. Coursework describes internal control in general '
              'terms; practice required me to know which field in a system '
              'record carries the evidence, and what to do when that field is '
              'blank. That gap between a described control and a tested control '
              'is, in my view, the real content of an internship.'),

        ('h2', '4.6  OVERALL REALISATIONS'),
        ('p', 'A control that cannot be evidenced does not exist for audit '
              'purposes, however well it may be operating in practice. '
              'Revenue leakage in a high-volume service business is '
              'cumulative rather than dramatic, which is precisely why '
              'continuous verification is needed. Documentation is not '
              'administrative overhead; it is the only thing that allows a '
              'transaction to be reviewed months later. Internal audit adds '
              'value by being timely, since an observation reported while '
              'the period is still open can actually be corrected. '
              'Objectivity is a discipline rather than an attitude: it '
              'means reporting what the record shows, no more and no less. '
              'Repetitive verification is where competence is built, '
              'because the exceptions only become visible once the normal '
              'pattern is familiar. An audit department depends on the '
              'cooperation of people it has no authority over, which makes '
              'communication a core professional skill.'),

        ('h2', '4.7  PROFESSIONAL INSIGHTS AND LEARNINGS'),
        ('p', 'Three insights from the internship will stay with me beyond the '
              'technical content.'),
        ('p', 'The first concerns the position of internal audit within a '
              'business. It is not a policing function and it is not an '
              'accounting function; it is an assurance function that exists to '
              'tell management whether its own rules are being followed. That '
              'position requires independence from the branches being reviewed '
              'and, at the same time, a working relationship with them, and '
              'holding both together is the professional skill the department '
              'demonstrated every day.'),
        ('p', 'The second concerns learning inside an organisation. I learned '
              'most of what I know now not from being taught formally but from '
              'watching a verification performed, attempting it and having my '
              'working papers corrected. My guide’s review comments told me '
              'precisely where my understanding was thin, and being willing to be '
              'corrected turned out to be the most efficient learning strategy '
              'available.'),
        ('p', 'The third concerns my own career direction. Before the internship '
              'my interest in finance was general. Having worked through '
              'documentation, verification, exception reporting and follow-up on '
              'live records, I now know that I am drawn to audit and assurance, '
              'where the work is precise, the standards are external and the '
              'output is verifiable. I also know the gaps I need to close, namely '
              'speed, advanced analytical tools and formal knowledge of audit '
              'standards, and I have a clear idea of how to work on them.'),

        ('h2', '4.8  RELEVANCE TO FUTURE CAREER AND QUALIFICATION'),
        ('p', 'The internship has a direct bearing on the path I intend to '
              'follow. The work I performed is the work of the early years of a '
              'career in audit and assurance, and having done it under review I '
              'now know both that I can perform it and that I want to. That is '
              'a more useful outcome than the general interest in finance I had '
              'before.'),
        ('h2', '4.9  UNDERSTANDING OF THE DIAGNOSTICS BUSINESS'),
        ('p', 'A less obvious outcome was a working understanding of how a '
              'diagnostics business actually earns and loses money, which I did '
              'not have before. Revenue arrives in very large numbers of small '
              'transactions, each capable of being discounted, cancelled, '
              'amended or billed on credit, and the margin on any one of them '
              'is thin enough that a systematic leakage matters more than an '
              'occasional large error.'),
        ('p', 'That structure explains why the controls I tested exist in the '
              'form they do. Eligibility verification protects corporate '
              'pricing from being extended to walk-in patients; discount '
              'authorisation limits keep pricing discretion at the level that '
              'can be held accountable for it; deletion logging makes a removed '
              'test traceable to a person and a reason; and ageing analysis '
              'keeps credit from quietly becoming a bad debt. Each control '
              'answers a specific way in which revenue can be lost without '
              'anybody intending it.'),
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
        ('p_indent', 'The Summer Internship Programme was carried out at Neuberg '
                     'Diagnostics Private Limited, Chennai, on-site in the '
                     'Internal Audit department, from 11 May 2026 to 30 July '
                     '2026, under the guidance of **Ms. S. Saradha**, Chartered '
                     'Accountant. The work concerned the verification of '
                     'revenue-side controls in a multi-branch diagnostics '
                     'network.'),
        ('p', 'The internship covered seven areas. In business-to-business KYC '
              'verification I collected KYC documents and signed memoranda of '
              'understanding from the sales personnel responsible for their '
              'assigned clients and maintained the records so that only eligible '
              'B2B customers received corporate benefits. In requisition form '
              'verification I checked Test Requisition Forms received from '
              'branches and confirmed whether B2B bills carried the seal of the '
              'respective laboratory, noting every case in which it was missing.'),
        ('p', 'On the pricing side, deep discount verification required me to '
              'identify walk-in customers who had received discounts of more than '
              'thirty per cent, compare them with the company’s discount policy '
              'and record the exceptions for the team’s further verification, '
              'while free of cost verification involved identifying walk-in and '
              'B2B customers billed at a hundred per cent discount and listing '
              'those cases for review. In cash due monitoring I reviewed payment '
              'records and calculated the number of days between the payment date '
              'and the current date to establish the cash due position.'),
        ('p', 'In service deletion verification I examined deleted service '
              'records to identify tests that had been booked and later removed '
              'from the system, traced the laboratory identification numbers '
              'concerned and checked who had made each deletion and the reason '
              'recorded for it. Finally, in Action Taken Report follow-up for '
              'branch audits, I contacted branch staff by telephone to collect '
              'the evidence needed to close audit observations and kept the '
              'pending and completed status updated.'),
        ('p', 'The work was carried out using Suflam LIMS as the source of '
              'records, Microsoft Excel for verification sheets, ageing '
              'calculations and exception listings, and Microsoft Word for audit '
              'notes and reports. Every working sheet was reviewed by my guide '
              'before an exception was reported.'),

        ('h2', '5.2  KEY TAKEAWAYS'),
        ('h3', '5.2.1  Understanding of Internal Audit'),
        ('p', 'Learned how an internal audit department plans a '
              'verification, performs it on live records and reports '
              'exceptions with supporting evidence. Understood the '
              'difference between a control described in a policy and a '
              'control that can be demonstrated from records. Saw why '
              'independence from the process being reviewed is essential to '
              'the value of the function.'),
        ('h3', '5.2.2  Revenue Controls in a Service Business'),
        ('p', 'Learned how discounts, free of cost services, deletions and '
              'ageing receivables each represent a route to revenue '
              'leakage. Understood the role of eligibility documentation in '
              'preventing corporate terms from being extended to retail '
              'customers. Realised that in a high-volume business the '
              'aggregate of small concessions matters more than any single '
              'case.'),
        ('h3', '5.2.3  Documentation and Evidence'),
        ('p', 'Learned that an observation is only as strong as the record '
              'attached to it. Developed the discipline of preparing '
              'working papers in which the original entry, the policy '
              'requirement and the exception are shown together. Understood '
              'why audit closure requires evidence rather than an assurance '
              'that a matter has been attended to.'),
        ('h3', '5.2.4  Systems and Data'),
        ('p', 'Gained working familiarity with Suflam LIMS and with the '
              'extraction of booking, discount, deletion and payment '
              'records. Learned to use spreadsheet techniques for '
              'filtering, lookups and ageing calculations on those '
              'extracts. Understood that a system record is only as useful '
              'as the completeness of what branch staff enter into it.'),
        ('h3', '5.2.5  Communication and Persistence'),
        ('p', 'Improved professional communication with sales personnel and '
              'branch staff, including telephone follow-up with people '
              'under their own work pressure. Learned to keep a request '
              'alive courteously and to record what had been promised and '
              'by when. Understood that cooperation, not authority, is what '
              'closes an audit observation.'),
        ('h3', '5.2.6  Professional Discipline'),
        ('p', 'Developed the habit of verifying before concluding and of '
              'referring doubtful cases upward. Learned to maintain '
              'accuracy through long extracts and repetitive verification. '
              'Strengthened confidentiality and objectivity as working '
              'habits rather than as abstract principles.'),



        ('h3', '5.2.7  Exception Reporting as a Skill'),
        ('p', 'Learned that identifying an exception is only half the task and '
              'that reporting it well is the other half. Understood that an '
              'observation has to state the transaction, the rule it departs '
              'from and the evidence for both, because a finding expressed as '
              'an impression invites argument rather than correction. Learned '
              'to separate a control failure from a documentation gap, since '
              'the two call for different responses from the branch '
              'concerned.'),
        ('h3', '5.2.8  Working Across Branches'),
        ('p', 'Understood that a control tested at the corporate office is '
              'operated by people in branches who have their own priorities and '
              'their own local practices. Learned that consistency across '
              'locations is what makes a policy meaningful, and that variation '
              'is usually a sign of unclear guidance rather than of '
              'indiscipline. Developed the courtesy and persistence needed to '
              'obtain evidence from colleagues for whom an audit query is an '
              'interruption.'),

        ('h3', '5.2.9  Objectivity and Professional Conduct'),
        ('p', 'Learned that internal audit occupies an awkward position by '
              'design, and that the manner in which an observation is raised '
              'determines whether it is answered or resisted. Understood that '
              'neutral language and precise evidence are method rather than '
              'politeness. Learned that a half-verified finding must never '
              'circulate before review, because the damage it does cannot be '
              'undone by a corrected version issued afterwards.'),
        ('h2', '5.3  LIMITATIONS OF THE INTERNSHIP EXPERIENCE'),
        ('p', 'An honest summary has to record the boundaries of what I saw. '
              'Twelve weeks in one internal audit department gives a detailed '
              'view of a particular set of revenue controls rather than a '
              'complete picture of the audit function, and several parts of '
              'that function lay outside my work.'),
        ('p', 'My assignments were concentrated on revenue-side testing: '
              'client eligibility, requisition documentation, discounting, '
              'credit and deletions. I did not work on the expenditure side, '
              'on procurement or inventory of reagents and consumables, on '
              'payroll, or on the fixed asset verification that an internal '
              'audit plan would ordinarily also cover. Nor did I see a full '
              'audit cycle from risk assessment and planning through to the '
              'audit committee presentation; my involvement began with tests '
              'that had already been designed.'),
        ('p', 'I was also working with a defined data window rather than a '
              'full historical trend. Extracts were provided for the periods '
              'under review, which is appropriate for an intern and for data '
              'protection, but it means my exception listings describe the '
              'months I examined and should not be read as statements about '
              'the organisation’s position over time. System access was '
              'read-only and limited to the modules my tests required.'),
        ('p', 'Finally, the patient data that a diagnostics business handles '
              'is sensitive, and access to it was properly restricted. I '
              'worked with billing and service records rather than clinical '
              'results, certain fields were masked, and I did not attend the '
              'discussions at which findings were put to senior management. '
              'These limits are correct, and noting them is part of reporting '
              'the work accurately rather than a complaint about it.'),

        ('h2', '5.4  RECOMMENDATIONS'),
        ('h3', '5.4.1  Suggestions to the Organisation'),
        ('p', 'The following are offered respectfully, from the position of a '
              'trainee who saw one part of a large control environment. They '
              'are not assertions that the organisation lacks these practices, '
              'and each would need to fit the department’s existing methods.'),
        ('bullets', [
            'A short written definition of each exception category, stating '
            'what qualifies and what evidence closes it, would make a new '
            'assistant’s listings consistent with the team’s from the first '
            'week rather than after several rounds of correction.',
            'Recording the authorisation reference against a discount or a '
            'free of cost case at the point of billing would remove much of '
            'the later work of tracing who approved a concession and on what '
            'basis.',
            'A standing template for Action Taken Report follow-up, with the '
            'evidence required for each common observation set out in advance, '
            'would shorten the telephone follow-up that closing observations '
            'currently requires.',
            'Periodic extraction of deletion reports by user and reason, '
            'rather than on request, would let recurring patterns be seen '
            'earlier than a review cycle allows.',
        ]),
        ('h3', '5.4.2  Suggestions for Future Interns'),
        ('p', 'For a student about to join a similar department, four things '
              'would have helped me had I known them at the outset.'),
        ('bullets', [
            'Read the relevant policy before opening the data. A discount '
            'listing is meaningless until you know what the policy permits, '
            'and reading the two in the wrong order wastes a day.',
            'Learn the spreadsheet functions for matching and ageing early. '
            'Most of the testing is comparison work, and fluency there buys '
            'time for the judgement the work actually needs.',
            'Write the observation as you go, not at the end. The reason a '
            'transaction looked exceptional is vivid when you find it and '
            'vague a week later.',
            'Expect follow-up to be the hardest part. Branch colleagues are '
            'busy with their own work, and closing an observation is a matter '
            'of courteous persistence rather than of a single request.',
        ]),

        ('h2', '5.5  PERSONAL REFLECTION'),
        ('p', 'On a personal level the internship changed how I read a set of '
              'records. I arrived expecting internal audit to be a matter of '
              'checking arithmetic and found it to be a matter of asking '
              'whether a transaction should have happened at all. The '
              'difference sounds small and is not: the first question can be '
              'answered by a formula, while the second requires knowing the '
              'policy, the business reason and the person who authorised it.'),
        ('h2', '5.6  CONCLUSION'),
        ('p', 'The internship at Neuberg Diagnostics Private Limited was the '
              'point at which my study of finance became practical. Over twelve '
              'weeks I moved from being shown how a verification is '
              'performed to carrying out the recurring checks independently, '
              'consolidating exception records and following up audit '
              'observations with branches directly. In doing so I acquired a set '
              'of skills that are directly employable: verification against '
              'policy, KYC and documentation review, discount and free of cost '
              'testing, receivables ageing, examination of system amendments and '
              'deletions, exception reporting and audit follow-up.'),
        ('p', 'Beyond the technical content, three things changed. First, my '
              'understanding of control: a rule is only as good as the evidence '
              'that it was followed, and testing that evidence is a distinct '
              'professional activity. Second, my understanding of revenue: in a '
              'business made up of many small transactions, margins are protected '
              'or lost in the detail of discounts, concessions, amendments and '
              'collections. Third, my understanding of myself. I learned that '
              'detailed, verifiable work suits me, that I can follow up '
              'persistently without causing friction, and that I can absorb '
              'correction without losing confidence.'),
        ('p', 'I am also clear about what remains to be developed: greater speed, '
              'stronger analytical tools including pivot tables and data '
              'analytics, a firmer grounding in the standards on internal audit, '
              'and more confidence in escalation. Knowing these gaps precisely, '
              'rather than in general terms, is itself an outcome of the '
              'internship.'),
        ('p', 'In conclusion, the internship achieved what a Summer Internship '
              'Programme is intended to achieve. It connected the MBA (Finance) '
              'curriculum to live professional work, it gave me the habits and '
              'tools used in an internal audit department, and it settled my '
              'career direction towards audit and assurance. I am grateful to the '
              'management of Neuberg Diagnostics Private Limited for the '
              'opportunity, to **Ms. S. Saradha** for her supervision and review, and '
              'to the internal audit team and branch staff for their support, and '
              'I leave the organisation with both the competence and the '
              'confidence to contribute to a professional finance or audit team.'),

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
            'CareEdge Ratings. (n.d.). Indian diagnostics industry: Opinion '
            'piece. Retrieved September 2026, from '
            'https://www.careratings.com/',

            'Economic Times. (2022, May 7). Neuberg may file IPO papers in H2 of '
            'FY23. Retrieved September 2026, from '
            'https://economictimes.com/markets/ipos/fpos/'
            'neuberg-may-file-ipo-papers-in-h2-of-fy23/articleshow/91389468.cms',

            'ETHealthworld. (2017, October 7). India’s first global consortium to '
            'unveil collective diagnostic strength of four countries. The '
            'Economic Times. Retrieved September 2026, from '
            'https://health.economictimes.indiatimes.com/news/diagnostics/'
            'indias-first-global-consortium-to-unveil-collective-diagnostic-'
            'strength-of-four-countries/60984204',

            'IMARC Group. (n.d.-a). India pathology lab services market size and '
            'report, 2034. Retrieved September 2026, from '
            'https://www.imarcgroup.com/india-pathology-lab-services-market',

            'IMARC Group. (n.d.-b). India diagnostic labs market size, share and '
            'forecast, 2026-34. Retrieved September 2026, from '
            'https://www.imarcgroup.com/india-diagnostic-labs-market',

            'Institute of Chartered Accountants of India. (n.d.). Standards on '
            'internal audit. Retrieved September 2026, from '
            'https://www.icai.org/',

            'Institute of Internal Auditors. (n.d.). International Professional '
            'Practices Framework. Retrieved September 2026, from '
            'https://www.theiia.org/',

            'Mordor Intelligence. (n.d.). India in vitro diagnostics market size '
            'and share analysis. Retrieved September 2026, from '
            'https://www.mordorintelligence.com/industry-reports/'
            'india-in-vitro-diagnostics-market',

            'National Accreditation Board for Testing and Calibration '
            'Laboratories. (n.d.). Accreditation of medical laboratories. '
            'Retrieved September 2026, from https://nabl-india.org/',

            'Neuberg Diagnostics. (n.d.-a). About us. Retrieved September 2026, '
            'from https://www.neubergdiagnostics.com/about-us',

            'Neuberg Diagnostics. (n.d.-b). Diagnostic centres and pathology '
            'labs in Chennai. Retrieved September 2026, from '
            'https://www.neubergdiagnostics.com/find-lab/chennai',

            'Neuberg Diagnostics. (n.d.-c). Leadership team. Retrieved September '
            '2026, from https://www.neubergdiagnostics.com/team',

            'Times of India. (2018, August 29). Neuberg Diagnostics to invest Rs '
            '200 cr in 12-18 months. Retrieved September 2026, from '
            'https://timesofindia.indiatimes.com/business/india-business/'
            'neuberg-diagnostics-to-invest-rs-200-cr-in-12-18-months/'
            'articleshow/65599461.cms',
        ]),

        ('bullets', [
            'Institute of Internal Auditors. (n.d.). International Standards '
            'for the Professional Practice of Internal Auditing. Retrieved '
            'September 2026, from https://www.theiia.org/',

            'Institute of Chartered Accountants of India. (n.d.-b). Standards '
            'on Internal Audit and guidance notes. Retrieved September 2026, '
            'from https://www.icai.org/',

            'National Accreditation Board for Testing and Calibration '
            'Laboratories. (n.d.). ISO 15189 accreditation requirements for '
            'medical laboratories. Retrieved September 2026, from '
            'https://nabl-india.org/',

            'Ministry of Health and Family Welfare, Government of India. '
            '(n.d.). Clinical Establishments (Registration and Regulation) '
            'Act: standards for diagnostic laboratories. Retrieved September '
            '2026, from https://clinicalestablishments.gov.in/',

            'Government of India. (2023). Digital Personal Data Protection '
            'Act, 2023. Ministry of Electronics and Information Technology. '
            'Retrieved September 2026, from https://www.meity.gov.in/',

            'Neuberg Diagnostics Private Limited. (n.d.-b). Corporate and '
            'business-to-business services. Retrieved September 2026, from '
            'https://neubergdiagnostics.com/',

            'Neuberg Diagnostics Private Limited. (2026, July 30). Internship '
            'completion certificate issued to the author.',
        ]),

        ('bullets', [
        ]),
    ],
}

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]
