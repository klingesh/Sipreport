# -*- coding: utf-8 -*-
"""
Content of the Summer Internship Project report of Ganeshkumar S, MBA,
ISSM Business School, Chennai.

Internship: Doodleblue Innovations Private Limited
Role: Digital Marketing Intern
Duration: 35 days

Sourced from the author's own five-chapter draft ("Ganesh chapther 1.docx"),
restructured into the house format used by the other reports in this
repository.

PLACEHOLDERS STILL TO BE FILLED IN BY THE AUTHOR - all four appear as
[SQUARE-BRACKET CAPITALS] and can be found with a single search:
    [REGISTER NUMBER]        - college register number
    [START DATE], [END DATE] - exact dates printed on the internship
                               certificate
    [NAME OF INDUSTRY MENTOR] - company mentor, with designation if shown
The author's name below is taken from the document properties of his draft
and should be confirmed against college records.

Block vocabulary is documented in report_content.py.
"""

STUDENT = 'GANESHKUMAR S'
REG_NO = '[REGISTER NUMBER]'
FIRM = 'Doodleblue Innovations Private Limited'
FIRM_SHORT = 'Doodleblue'
MENTOR = '[NAME OF INDUSTRY MENTOR]'
MENTOR_ROLE = ''
PERIOD = '[START DATE] to [END DATE], 2026'

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
          'authentic record of Mr. Ganeshkumar S ([REGISTER NUMBER]) carried '
          'out at Doodleblue Innovations Private Limited in partial fulfilment '
          'of the requirements for the award of the MBA degree.'),
    ('gap', 1),
    ('p', 'The project was completed under the guidance of [NAME OF INDUSTRY '
          'MENTOR], Doodleblue Innovations Private Limited, during the '
          '35-day internship period from [START DATE] to [END DATE], 2026.'),
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
    ('p', 'I, Mr. Ganeshkumar S, hereby declare that this SIP Project Report '
          'is based on my 35-day internship done at Doodleblue Innovations '
          'Private Limited, as a Digital Marketing Intern, during the period '
          'from [START DATE] to [END DATE], 2026, under the guidance of [NAME '
          'OF INDUSTRY MENTOR], Doodleblue Innovations Private Limited and '
          'Indian School of Science and Management, Chennai.'),
    ('gap', 1),
    ('p', 'I further declare that the work presented in this report is my own, '
          'that it has been prepared from the work areas actually assigned to '
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
    ('p', 'My sincere gratitude to [NAME OF INDUSTRY MENTOR], DOODLEBLUE '
          'INNOVATIONS PRIVATE LIMITED, for mentoring me, reviewing my work '
          'and offering immense support and knowledge throughout the '
          'internship, and to the management of Doodleblue Innovations Private '
          'Limited for permitting me to undergo my Summer Internship '
          'Programme with the organisation.'),
    ('p', 'I am also thankful to the members of the marketing and business '
          'development teams, who explained their work to me, answered my '
          'questions on account research and outreach, and helped me '
          'understand how digital marketing activity connects to the '
          'organisation’s wider business objectives.'),
    ('pagebreak',),

    # ---- executive summary ----
    ('gap', 1),
    ('big', 'The Executive Summary', 12),
    ('gap', 1),
    ('p', 'This report presents the work carried out during my Summer '
          'Internship Programme at Doodleblue Innovations Private Limited, a '
          'Chennai-based digital product engineering and digital '
          'transformation company. The internship ran for 35 days, from '
          '[START DATE] to [END DATE], 2026, with the designation of Digital '
          'Marketing, under the guidance of [NAME OF INDUSTRY MENTOR].'),
    ('p', 'The internship was located in the part of marketing that a '
          'technology services company depends on for its pipeline: business '
          'to business demand generation. A digital services firm does not '
          'sell to a mass audience. It sells considered, high-value '
          'engagements to a comparatively small number of organisations, each '
          'of which evaluates the provider over weeks or months and through '
          'several stakeholders. Marketing in that setting is less about reach '
          'and more about relevance, credibility and disciplined follow-up.'),
    ('p', 'My work covered four principal areas. The first was account-based '
          'marketing, in which selected organisations are treated as '
          'individual markets and researched before any message is written. '
          'The second was LinkedIn marketing, the professional platform on '
          'which most Indian business to business discovery and outreach now '
          'begins. The third was email marketing, the structured written '
          'channel through which a service is introduced and a conversation is '
          'followed up. The fourth was lead generation, the identification and '
          'organised recording of organisations and professional roles that '
          'may represent a genuine business opportunity.'),
    ('p', 'Alongside these four areas the internship included digital '
          'marketing research and content support, and the coordination, '
          'documentation and reporting that keep such work usable by other '
          'members of a team. The 35 days progressed through five phases: '
          'orientation and industry familiarisation, account-based marketing '
          'research, LinkedIn marketing, email marketing together with lead '
          'generation, and a closing phase of consolidation and review.'),
    ('p', 'An important point should be stated plainly at the outset. This '
          'report describes the work areas assigned to me and the learning '
          'drawn from them. It does not state campaign results, numbers of '
          'accounts researched, message or email volumes, response rates or '
          'lead totals, because verified figures for those items were not '
          'available to me for inclusion. Nor does it claim independent '
          'campaign ownership. Where the report offers recommendations, they '
          'are general process suggestions drawn from the learning themes of '
          'the internship and are not assertions that the organisation lacks '
          'those practices. I have preferred an accurate report to an '
          'impressive one.'),
    ('p', 'Professionally, the internship gave me three things a classroom '
          'cannot. First, an understanding that targeting precedes messaging: '
          'a well-written message sent to an irrelevant audience is still a '
          'failure, and the research that establishes relevance is therefore '
          'the real work. Second, the discipline of accuracy, because in '
          'outreach a wrong company detail or an unsupported assumption is '
          'visible to the recipient and costs credibility immediately. Third, '
          'an honest sense of the difference between activity and outcome, '
          'which changed how I read marketing numbers. The internship '
          'converted my MBA coursework in marketing management, marketing '
          'research, business communication and organisational buying '
          'behaviour into work I can now perform, and it clarified my interest '
          'in business to business digital marketing.'),
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

        ('h2', '1.1  THE DIGITAL MARKETING INDUSTRY'),
        ('p_indent', 'Digital marketing is the use of digital channels, data and '
                     'content to reach a defined audience, communicate the value '
                     'of an offering and support a measurable business '
                     'objective. The industry serves organisations of very '
                     'different sizes and across widely varied sectors. A '
                     'business may use digital channels to introduce a new '
                     'product, strengthen its reputation, educate a defined '
                     'audience, generate qualified leads or maintain '
                     'relationships with existing customers. The objective, not '
                     'the channel, is the starting point.'),
        ('p', 'The choice of channel depends on the nature of the offering, the '
              'buying process, audience behaviour, available resources and the '
              'business objective. A business selling to other businesses '
              'usually requires relationship-led communication and longer '
              'nurturing cycles, because the purchase is considered, involves '
              'several people and is evaluated over time. A consumer brand may '
              'instead prioritise reach, engagement and online conversion. The '
              'same tools serve both, but the way they are used differs '
              'fundamentally.'),
        ('p', 'The industry is not limited to publishing content or running '
              'advertisements. Effective digital marketing requires an '
              'understanding of the market, customer needs, positioning, '
              'messaging, channel selection and performance indicators. '
              'Research and planning establish the direction; execution turns '
              'the plan into communication; measurement provides feedback; and '
              'optimisation improves the relevance of future activity. That '
              'cycle is what distinguishes marketing as a discipline from '
              'marketing as a set of activities. The main channels within it '
              'include search engine optimisation, paid search and social '
              'advertising, content marketing, social media marketing and email '
              'marketing, supported by the automation and customer relationship '
              'systems that hold the records making follow-up possible.'),
        ('h2', '1.2  THE INDIAN MARKET AND SECTOR CONTEXT'),
        ('p', 'India is one of the fastest growing advertising markets in the '
              'world, and digital is the part of it that is growing. WPP '
              'Media’s This Year Next Year forecast projected the total Indian '
              'advertising market to grow by 9.7 per cent in 2026 to about INR '
              '2,01,891 crore, an incremental addition of roughly INR 17,844 '
              'crore over 2025, with digital formats leading that expansion '
              '(WPP Media, 2026). Longer-range estimates place the market at '
              'approximately INR 993.7 billion in 2025, rising to about INR '
              '2,157.7 billion by 2034 at a compound annual growth rate near 9 '
              'per cent (IMARC Group, n.d.).'),
        ('p', 'Measured in dollars, the digital segment alone was estimated at '
              'about USD 11 billion in 2025 and is projected to grow at 10 to '
              '15 per cent a year to between USD 19 billion and USD 22 billion '
              'by 2030 (Redseer Consulting, as reported in Economic Times, '
              '2026a). A separate analysis found that digital already '
              'contributes between 50 and 60 per cent of total Indian '
              'advertising spend, projecting growth of about 15 per cent a year '
              'to USD 17 to 19 billion by 2029. The stated drivers were rising '
              'private consumption and the extension of mobile broadband '
              'coverage to more than ninety per cent of subscriptions (Bain and '
              'Company, as reported in Livemint, 2025). Grand View Research '
              'projects the market at about USD 46.6 billion by 2033 at a '
              'compound annual rate of 14.1 per cent (Grand View Research, '
              'n.d.).'),
        ('p', 'Definitions differ and the estimates differ with them, but the '
              'direction does not. Digital has moved from being one line in a '
              'media plan to being the plan itself. The Pitch Madison '
              'Advertising Report for 2026 placed digital at about 60 per cent '
              'of total advertising expenditure under a definition including '
              'quick-commerce and smaller-business spending (ETBrandEquity, '
              '2026). A separate industry study projected digital advertising '
              'spend growing about 15 per cent to roughly INR 56,400 crore in '
              'the 2026 financial year (Ipsos, 2025).'),
        ('p', 'Two consequences of this shift matter for a company of the kind '
              'I worked in. The first is competition for attention. When every '
              'organisation markets through the same handful of platforms, the '
              'scarce resource stops being media space and becomes the '
              'recipient’s willingness to read, which is the argument for '
              'targeted, research-led approaches over broad outreach. The '
              'second is measurement. As spending concentrates in channels that '
              'report everything, the temptation is to treat whatever is easily '
              'counted as evidence of success, and distinguishing activity from '
              'outcome becomes a genuine professional skill.'),
        ('p', 'Doodleblue Innovations belongs to the Indian technology services '
              'sector, whose health determines the demand its marketing '
              'addresses. According to the annual strategic review of the '
              'National Association of Software and Service Companies, the '
              'sector was expected to record revenues of about USD 315 billion '
              'in the 2026 financial year, a growth of 6.1 per cent from USD '
              '282.6 billion (NASSCOM, as reported in Economic Times, 2026b). '
              'Information technology services accounted for approximately USD '
              '149 billion of that total, engineering research and development '
              'for about USD 63 billion and business process management for '
              'around USD 59 billion (Times of India, 2026). Revenue '
              'attributable to artificial intelligence services was estimated '
              'at USD 10 billion to USD 12 billion, and sector headcount was '
              'expected to reach about 5.95 million people (CNBC TV18, 2026).'),
        ('p', 'For a mid-sized digital product company, a sector of this size '
              'is both an opportunity and a difficulty. The opportunity is that '
              'demand for digital transformation, application development and '
              'user experience work is broad and no longer confined to large '
              'enterprises. The difficulty is that the same sector contains '
              'firms of every scale, from global consultancies to two-person '
              'studios, all addressing overlapping audiences in similar '
              'language. In that environment marketing cannot rely on category '
              'claims. It has to connect a specific capability to a specific '
              'organisation’s situation, which is the reasoning behind the '
              'account-based approach I worked with. The business to business '
              'segment reflects this: industry surveys report that about 81 per '
              'cent of marketers consider account-based marketing to deliver a '
              'higher return than their other approaches (Powered by Search, '
              '2026), and roughly 72 per cent observed improved customer '
              'engagement after adopting it (G2, 2026). These come from '
              'practitioner surveys rather than audited data and are subject to '
              'self-selection, but they indicate why the method has become '
              'standard practice.'),

        ('h2', '1.3  COMPANY OVERVIEW: DOODLEBLUE INNOVATIONS PRIVATE LIMITED'),
        ('h3', '1.3.1  BACKGROUND AND OPERATIONS'),
        ('p', 'Doodleblue Innovations Private Limited is a digital product '
              'engineering and digital transformation company headquartered in '
              'Chennai. The organisation was started in 2011 by Atishe Chordia '
              'and Nishyta Chordia, beginning as a very small Chennai team and '
              'being incorporated as a private limited company shortly '
              'afterwards (Doodleblue Innovations, n.d.). It has since grown '
              'into an established digital services firm with a presence in '
              'India and the United States, and it reports client work spanning '
              'large enterprises, funded start-ups and organisations in the '
              'public and social sectors.'),
        ('p', 'The company describes its work as digital transformation '
              'delivered through design and engineering rather than as staffing '
              'or maintenance support. Its service lines cover user interface '
              'and user experience design, mobile application development, web '
              'and progressive web application development, enterprise '
              'application development and modernisation, cloud and back-end '
              'engineering, data and analytics work, emerging technology '
              'practices, and digital marketing services for its clients '
              '(Doodleblue Innovations, n.d.).'),
        ('p', 'The shape of the business matters to a marketing intern for a '
              'reason worth stating. A company that builds digital products '
              'sells outcomes the buyer cannot inspect in advance. The '
              'prospective client is not comparing a specification on a shelf; '
              'it is forming a judgement about whether this provider '
              'understands its problem and can be trusted to solve it. '
              'Marketing therefore carries an unusually heavy burden in this '
              'sector, because it has to establish comprehension and '
              'credibility before a commercial conversation can begin. '
              'Everything I was asked to do followed from that fact.'),

        ('h3', '1.3.2  BUSINESS ACTIVITIES OBSERVED'),
        ('p', 'The activities visible to me were those of the marketing and '
              'business development function rather than of the delivery teams. '
              'The work was organised around identifying organisations that '
              'might plausibly need digital product work, understanding enough '
              'about each to say why, reaching the professional roles likely to '
              'be involved in such a decision, and keeping an orderly record of '
              'what had been researched, sent and answered.'),
        ('p', 'Three characteristics were apparent. The first was that research '
              'came before communication, consistently and as a matter of '
              'method rather than preference. The second was that the channels '
              'were used in combination: an account identified through research '
              'might be approached on a professional network and followed up by '
              'email, with a single record tying the two together. The third '
              'was caution about claims, since communication was expected to '
              'describe capability accurately and to avoid implying knowledge '
              'of a prospect’s situation that had not been established. I '
              'should add that I saw this function as an intern over 35 days, '
              'without visibility of commercial terms, client contracts, '
              'revenue or pipeline data, and this report accordingly does not '
              'describe them.'),


        ('table', {'rows': [
            ['Activity', 'Nature of Work', 'Purpose'],
            ['Account research',
             'Reviewing public company, industry and professional role '
             'information for selected organisations',
             'Establishing whether and why an account is relevant before any '
             'outreach is prepared'],
            ['Stakeholder identification',
             'Identifying the professional roles likely to influence a digital '
             'product decision',
             'Directing communication to a role that is able to act on it'],
            ['Professional-platform outreach',
             'Preparing relevant, appropriately reasoned messages on a '
             'professional network',
             'Opening a credible business conversation without overstating '
             'knowledge of the prospect'],
            ['Email communication',
             'Drafting introductory and follow-up business correspondence',
             'Explaining capability clearly and proposing a proportionate next '
             'step'],
            ['Lead recording',
             'Maintaining consistent prospect records with an explicit status '
             'and next action',
             'Making follow-up possible and preventing duplicated or '
             'irrelevant outreach'],
            ['Documentation and reporting',
             'Summarising research, progress and open questions for the team',
             'Preserving context and supporting honest reporting of activity'],
        ], 'widths': [3, 5, 4], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),
        ('h2', '1.4  THE B2B MARKETING FUNCTION IN A DIGITAL SERVICES FIRM'),
        ('h3', '1.4.1  ACCOUNT-BASED MARKETING'),
        ('p', 'Account-based marketing is a focused business to business '
              'approach in which selected organisations are treated as '
              'individual markets rather than as members of a broad segment. It '
              'commonly involves account selection, research, stakeholder '
              'mapping, personalisation, coordinated outreach and review. '
              'Account selection may consider industry, organisation size, '
              'business model, geography, likely need and fit with the service '
              'offered. Research builds an understanding of the account’s '
              'business environment and probable priorities, while stakeholder '
              'mapping identifies the roles that may influence a purchase.'),
        ('p', 'The method is not simply a matter of sending individually '
              'addressed messages. Its value depends on the quality of the '
              'account research and the relevance of what is proposed. A '
              'personalised message should rest on credible information, avoid '
              'unsupported assumptions and make it easy for the recipient to '
              'understand why the communication might be useful. The approach '
              'also requires coordination between marketing and sales, so that '
              'account insight, outreach history and agreed next steps are held '
              'consistently rather than in separate heads. The underlying logic '
              'is straightforward: if a company’s realistic market consists of '
              'a few hundred organisations rather than a few million consumers, '
              'an hour spent understanding one of them is a better investment '
              'than a thousand identical messages.'),

        ('h3', '1.4.2  LINKEDIN AND PROFESSIONAL NETWORK MARKETING'),
        ('p', 'LinkedIn is a professional platform used for networking, '
              'industry communication, employer branding and business to '
              'business marketing. Organisations use company pages to share '
              'updates, explain capabilities and maintain a professional '
              'presence, while individual profiles contribute through relevant '
              'posts, considered engagement and professional connections. For '
              'business to business marketing the platform is valuable less as '
              'a publishing surface than as a way to understand professional '
              'roles and build familiarity with an organisation’s expertise '
              '(LinkedIn, n.d.).'),
        ('h3', '1.4.3  EMAIL MARKETING AND LEAD NURTURING'),
        ('p', 'Email marketing is a direct channel used to share relevant '
              'information with an audience. In business to business settings '
              'an email may introduce an organisation, provide a useful '
              'resource, follow up on an earlier interaction or maintain a '
              'relationship over time, and its effectiveness depends on '
              'relevance, clarity, timing and respect for the recipient’s '
              'preferences (Mailchimp, n.d.). A well-structured message '
              'generally has a clear subject line, a relevant opening, a '
              'concise value proposition, supporting context and one '
              'appropriate call to action.'),
        ('h3', '1.4.4  LEAD GENERATION AND THE MARKETING FUNNEL'),
        ('p', 'Lead generation is the process of identifying people or '
              'organisations that may have an interest in a product or service '
              'and creating an appropriate path for them to express it. Leads '
              'may originate from professional networking, website forms, '
              'content responses, events, referrals or email engagement, and '
              'the value of a lead depends on its relevance and readiness '
              'rather than on the mere presence of contact information '
              '(HubSpot, n.d.).'),
        ('h2', '1.5  SWOT ANALYSIS'),
        ('p', 'The following analysis is based on what was observable to me '
              'during a 35-day internship in the marketing function, read '
              'together with publicly available information about the company '
              'and its sector. It is a student’s assessment rather than an '
              'internal strategic review, and it avoids claims about financial '
              'or commercial matters I was not in a position to verify.'),

        ('h3', '1.5.1  STRENGTHS'),
        ('bullets', [
            'An established operating history, having been founded in 2011, '
            'which in a sector with high firm turnover is itself a signal of '
            'delivery capability and client retention.',
            'A combined design and engineering proposition, allowing the company '
            'to address a client problem from user experience through to '
            'deployment rather than at one stage only.',
            'Breadth of service lines across mobile, web, enterprise and cloud '
            'engineering, which widens the range of conversations any outreach '
            'can credibly open.',
            'A base in Chennai, a major Indian technology centre with an '
            'established talent pool and a dense concentration of prospective '
            'clients, together with a presence in overseas markets.',
            'A research-led marketing method, in which account understanding '
            'precedes outreach, which suits the considered nature of the '
            'purchase being marketed.',
        ]),

        ('h3', '1.5.2  WEAKNESSES'),
        ('bullets', [
            'Services of this kind are difficult to differentiate in words, '
            'because most providers in the sector describe their capabilities '
            'using similar vocabulary.',
            'Marketing outcomes depend on long evaluation cycles, which makes it '
            'hard to attribute a result to a particular activity and therefore '
            'hard to justify effort in the short term.',
            'Account-based methods are labour-intensive by design, so the number '
            'of accounts that can be addressed properly is limited by available '
            'research time.',
            'A mid-sized firm competes for attention against consultancies whose '
            'brand recognition alone secures a first meeting.',
            'Dependence on a small number of outreach channels means a change in '
            'a platform’s policies or reach can affect the pipeline '
            'disproportionately.',
        ]),

        ('h3', '1.5.3  OPPORTUNITIES'),
        ('bullets', [
            'Sustained growth in the Indian technology services sector, '
            'projected at about USD 315 billion in the 2026 financial year, '
            'which widens the addressable market (NASSCOM, as reported in '
            'Economic Times, 2026b).',
            'Rapid enterprise adoption of artificial intelligence, with sector '
            'revenue from such services estimated at USD 10 billion to USD 12 '
            'billion, creating demand for new categories of digital product '
            'work.',
            'Digital transformation spending by mid-market organisations that '
            'previously considered custom development beyond their reach.',
            'Continued expansion of Indian digital advertising, which increases '
            'client demand for the digital marketing services the company also '
            'offers.',
            'The scope for genuinely research-led outreach to stand out '
            'precisely because so much business to business communication has '
            'become automated and generic.',
        ]),

        ('h3', '1.5.4  THREATS'),
        ('bullets', [
            'Intense competition across every scale of provider, from global '
            'consultancies to small independent studios addressing the same '
            'audiences.',
            'Downward pressure on custom development work as low-code, no-code '
            'and code-generating tools reduce the effort required for '
            'straightforward applications.',
            'Falling engagement with business to business outreach as the volume '
            'of automated messaging rises and recipients become more selective.',
            'Tightening data protection expectations, including the requirements '
            'of the Digital Personal Data Protection Act, 2023, which constrain '
            'how contact information may be sourced and used (Government of '
            'India, 2023).',
            'Dependence on external platforms for professional outreach, where '
            'changes to policy, algorithms or pricing are outside the company’s '
            'control.',
        ]),

        ('h2', '1.6  KEY COMPETITORS'),
        ('p', 'The competitive environment includes agencies, consulting firms, '
              'technology providers and the in-house teams of prospective '
              'clients, all of which may compete for the attention of similar '
              'business audiences. Competition occurs around expertise, service '
              'relevance, delivery approach, industry understanding, '
              'communication quality and trust, and a potential customer will '
              'often compare several providers before deciding whether to begin '
              'a conversation at all.'),

        ('h3', '1.6.1  DIGITAL PRODUCT AND DESIGN STUDIOS'),
        ('p', 'The closest competitors are other digital product studios '
              'offering design and engineering together. These firms compete on '
              'portfolio, design quality and demonstrated domain experience, '
              'and the decision between them frequently turns on whether the '
              'prospective client believes the provider has solved a comparable '
              'problem before. Marketing for this group tends to emphasise case '
              'evidence rather than capability lists, which raises the standard '
              'any outreach has to meet.'),


        ('table', {'rows': [
            ['Provider Type', 'Typical Proposition', 'Competitive Effect'],
            ['Independent product studios',
             'Design-led development delivered by a small senior team',
             'Compete on portfolio depth, design quality and comparable '
             'problem experience'],
            ['Specialist engineering firms',
             'Platform-specific or domain-specific development capability',
             'Compete wherever a narrow technical requirement dominates the '
             'brief'],
            ['Boutique design consultancies',
             'Research and interface design without build capability',
             'Compete at the front of an engagement and can influence the '
             'choice of build partner'],
        ], 'widths': [3, 4, 4], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),
        ('h3', '1.6.2  DIGITAL MARKETING AND FULL-SERVICE AGENCIES'),
        ('p', 'Agencies compete for the digital marketing portion of the '
              'company’s services and sometimes for adjacent product work. '
              'Their advantage is that marketing services can be bought in '
              'smaller increments than a development engagement, which makes '
              'the first purchase easier. Their disadvantage, from a client’s '
              'point of view, is that an agency may not be able to build what '
              'it recommends. A firm that can do both has a real argument to '
              'make, provided it is made specifically.'),


        ('table', {'rows': [
            ['Provider Type', 'Typical Proposition', 'Competitive Effect'],
            ['Digital marketing agencies',
             'Campaign, content and performance marketing services',
             'Compete for the marketing services line and often hold the '
             'client relationship'],
            ['Full-service agencies',
             'Brand, marketing and light product delivery combined',
             'Compete across both service lines under a single commercial '
             'relationship'],
        ], 'widths': [3, 4, 4], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),
        ('h3', '1.6.3  LARGE FIRMS, OFFSHORE PROVIDERS AND IN-HOUSE TEAMS'),
        ('p', 'Large technology services and consulting organisations compete '
              'chiefly for enterprise budgets. Their advantages are scale, '
              'brand recognition, procurement familiarity and the ability to '
              'absorb risk on large programmes. Their limitations, in the '
              'segment where a mid-sized studio competes, are cost, speed and '
              'the degree of senior attention a smaller engagement receives. '
              'Competing against them is rarely a matter of claiming '
              'equivalence; it is a matter of being clearly better suited to a '
              'particular kind of work.'),
        ('p', 'Two further alternatives belong in this group. Lower-cost '
              'offshore providers compete on price wherever the requirement is '
              'fully specified, and the in-house technology team of a '
              'prospective client represents the option of not outsourcing at '
              'all. The in-house alternative is easy to omit from a competitor '
              'analysis, but in practice any outreach has to answer the '
              'implicit question of why the work should go to an external '
              'partner rather than onto an existing team’s roadmap.'),


        ('table', {'rows': [
            ['Provider Type', 'Typical Proposition', 'Competitive Effect'],
            ['Global consulting firms',
             'Strategy advice combined with large-scale delivery capability',
             'Compete for enterprise budgets on brand recognition and the '
             'ability to absorb programme risk'],
            ['Large IT services companies',
             'Scale delivery, managed services and long-term maintenance',
             'Compete on cost at volume and on procurement familiarity'],
            ['Offshore development providers',
             'Lower-cost delivery of well-specified development work',
             'Compete on price wherever the requirement is fully defined in '
             'advance'],
            ['Client in-house technology teams',
             'Internal delivery without an external partner',
             'Compete as the option of not outsourcing, which any outreach '
             'has to answer implicitly'],
        ], 'widths': [3, 4, 4], 'col_bold': [True, False, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),
        ('h2', '1.7  COMPETITIVE POSITIONING'),
        ('p', 'Differentiation in this sector requires a clear explanation of '
              'the problem addressed, the value offered and the reasons the '
              'organisation may be relevant to a particular customer. Generic '
              'claims such as being innovative or customer-focused are '
              'insufficient on their own, because every competitor makes them '
              'and the prospect discounts them accordingly. Account research '
              'and tailored messaging are the mechanism by which a general '
              'capability is connected to a specific business situation, and '
              'that connection is what positioning actually consists of.'),
        ('h2', '1.8  KEY MILESTONES'),
        ('p', 'On the matter of company milestones I have to be explicit about '
              'the limits of what I can state. The publicly available record '
              'establishes that the organisation was founded in 2011 by Atishe '
              'Chordia and Nishyta Chordia, that it began as a very small '
              'Chennai team and was incorporated as a private limited company '
              'shortly afterwards, and that it has since expanded its service '
              'lines and established a presence in overseas markets (Doodleblue '
              'Innovations, n.d.). Beyond that, the information available to me '
              'during the internship does not provide sufficient verified '
              'detail about funding history, revenue, client counts, employee '
              'numbers at particular dates or specific dated achievements. Such '
              'figures should not be stated in an academic report without '
              'official confirmation from the company, and I have therefore '
              'left them out.'),
        ('p', 'What can be described is the stage of development visible in the '
              'nature of the marketing work being done. The company was '
              'pursuing considered business to business engagements through '
              'researched, targeted outreach rather than through mass '
              'advertising, which is characteristic of an established '
              'professional services firm growing by reputation and '
              'relationship rather than by volume. Within the internship itself '
              'a clear progression can be recorded, from orientation and '
              'industry familiarisation, through account research, to '
              'channel-specific outreach and finally to consolidation and '
              'review. That sequence, from understanding to communication to '
              'reflection, is the shape of the marketing cycle in miniature.'),
        ('p', 'For a student of management, the lesson in a company at this '
              'stage is that growth in professional services is rarely bought. '
              'It is earned through the unglamorous work of understanding a '
              'prospect properly, saying something relevant to them, recording '
              'what happened and following up when it is appropriate to do so.'),
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
        ('p_indent', 'The purpose of the internship was to convert the marketing '
                     'and management concepts studied in the MBA programme into '
                     'practical work inside a functioning digital services '
                     'company. The internship was carried out at Doodleblue '
                     'Innovations Private Limited over 35 days, from [START '
                     'DATE] to [END DATE], 2026, with the designation of Digital '
                     'Marketing, under the guidance of [NAME OF INDUSTRY '
                     'MENTOR]. It provided an opportunity to observe and '
                     'participate in selected digital marketing activities, '
                     'particularly account-based marketing, LinkedIn marketing, '
                     'email marketing and lead generation.'),
        ('p', 'The central objective was to connect academic learning with '
              'practical marketing work. Classroom concepts such as '
              'segmentation, targeting, positioning, customer behaviour, '
              'communication and marketing planning became substantially more '
              'meaningful when considered alongside actual research, outreach '
              'and lead-generation activity. The internship also gave me a '
              'sense of the discipline required to carry out marketing tasks in '
              'a professional setting, which is not something a syllabus can '
              'convey.'),
        ('bullets', [
            'To understand how target accounts are researched, assessed for '
            'relevance and selected for outreach.',
            'To understand how professional audiences are approached on a '
            'business network and what makes contact appropriate.',
            'To learn how a business email is structured, from subject line '
            'through to a proportionate call to action.',
            'To understand how potential leads are identified, qualified and '
            'organised into usable records.',
            'To see how marketing communication supports business development '
            'in a company selling considered services.',
            'To strengthen written communication, attention to detail and the '
            'habit of verifying before recording.',
            'To develop time management, prioritisation and the practice of '
            'raising blockers early.',
            'To learn to coordinate with other people’s work through clear '
            'documentation and progress reporting.',
        ]),
        ('h3', '2.1.1  METHODOLOGY AND APPROACH'),
        ('p', 'The internship followed a practical learning approach based on '
              'understanding the task, reviewing the available information, '
              'carrying out the assigned activity and learning from feedback. '
              'As a trainee I approached unfamiliar work by clarifying the '
              'objective and the expected output before starting. This mattered '
              'particularly for research and communication tasks, where an '
              'assumption made early or a gap in the information can quietly '
              'reduce the quality of everything produced afterwards.'),
        ('p', 'A typical workflow can be described as a sequence: understand the '
              'objective; identify the intended audience or account; collect '
              'relevant information; organise that information; prepare or '
              'support the required marketing communication; review the output '
              'for accuracy and relevance; and record what was completed and '
              'what the next action should be. The exact sequence varied with '
              'the activity, but the first and last steps rarely changed, '
              'because a task without a clear objective cannot be reviewed and '
              'a task without a record cannot be continued by anybody else.'),
        ('h2', '2.2  INITIAL ONBOARDING AND ORIENTATION'),
        ('p', 'The first days of the internship were given to orientation '
              'rather than to output, which in retrospect was the right '
              'allocation. I was introduced to the nature of the company’s '
              'work, the kind of organisations it serves, the services it '
              'offers and the professional standards expected of anybody '
              'communicating on its behalf. Understanding what the company '
              'actually does had to come first, because it is not possible to '
              'explain a capability credibly to a prospect without '
              'understanding it oneself.'),
        ('bullets', [
            'The nature of the company’s work, its service lines and the kinds '
            'of organisation it serves.',
            'The objectives of the internship and the four work areas assigned '
            'to me.',
            'How tasks are assigned and clarified, and what a completed output '
            'is expected to look like.',
            'How research, account and prospect records are kept and to what '
            'standard.',
            'What has to be reviewed before anything reaches an external '
            'recipient, and why that step exists.',
            'The requirement that information be credible, current and '
            'distinguishable from inference.',
            'The principle that recording something as unknown is acceptable '
            'and recording a guess is not.',
        ]),
        ('h2', '2.3  WORK PLAN AND SCOPE'),
        ('p', 'The work fell into eight related areas, described below. The '
              'first six are the substantive marketing areas; the last two are '
              'the research and coordination work that supports them. The '
              'description that follows sets out the nature of my involvement '
              'and the learning focus of each area.'),

        ('h3', '2.3.1  Target-Account Research'),
        ('p', 'Account-based marketing begins with research, and this was the '
              'first substantial area of work. Research involved reviewing '
              'publicly available company information, business activities, '
              'industry context and relevant professional roles, with the '
              'object of building a basic understanding of why a particular '
              'account might be relevant to the services offered. The standard '
              'applied was that information should be current enough for the '
              'intended use and that an uncertain point should never be '
              'presented as a verified fact.'),

        ('bullets', [
            'Reviewing public company information, business activities and '
            'industry context for selected organisations.',
            'Identifying the professional roles relevant to a digital product '
            'decision within each account.',
            'Judging whether information was current enough for the intended '
            'use before relying on it.',
            'Recording research so that a verified point could never be '
            'confused with an inference.',
        ]),
        ('h3', '2.3.2  Account Relevance and Stakeholder Context'),
        ('p', 'The second area concerned relevance and personalisation. A '
              'message becomes meaningful when it refers to a genuine business '
              'context and offers a plausible reason for making contact. '
              'Personalisation that is merely cosmetic, such as inserting a '
              'company name into an otherwise generic message, does not '
              'achieve this and is usually transparent to the recipient. '
              'Meaningful personalisation connects the message to relevant '
              'business information while avoiding any assumption that cannot '
              'be supported.'),

        ('bullets', [
            'Establishing a genuine business reason for contacting a '
            'particular organisation.',
            'Distinguishing meaningful personalisation from the cosmetic '
            'insertion of a company name.',
            'Considering which stakeholder role a message was addressed to and '
            'what that role would care about.',
            'Avoiding any assumption about a prospect’s needs that could not '
            'be supported by evidence.',
        ]),
        ('h3', '2.3.3  LinkedIn Marketing and Professional Outreach'),
        ('p', 'LinkedIn marketing formed a significant part of the work because '
              'of the platform’s relevance to professional communication and '
              'business to business networking. The area covered how the '
              'platform supports visibility, professional engagement and '
              'outreach to relevant business audiences, and how each of those '
              'differs in purpose.'),
        ('bullets', [
            'Researching profiles and organisations to establish professional '
            'relevance before making contact.',
            'Preparing concise messages with a clear reason for contact and a '
            'reasonable next step.',
            'Observing how visibility, engagement and direct outreach serve '
            'different purposes on the platform.',
            'Maintaining professional conduct, since everything said on such a '
            'platform is attributable.',
        ]),
        ('h3', '2.3.4  Email Marketing and Business Correspondence'),
        ('p', 'Email marketing was the second communication channel in scope. '
              'The work covered the role of email as a structured channel for '
              'business communication, used to introduce a service, provide '
              'context, follow up on an earlier interaction or share '
              'information that may be useful to a prospective customer.'),
        ('bullets', [
            'Framing subject lines that reflect the message honestly and avoid '
            'misleading claims.',
            'Opening with relevance and stating a value proposition in plain '
            'language.',
            'Closing with a call to action proportionate to the existing '
            'relationship.',
            'Proofreading for names, company details and links, each of which '
            'is preventable as an error.',
            'Handling contact data according to organisational procedure and '
            'respecting requests not to be contacted.',
        ]),
        ('h3', '2.3.5  Lead Generation and Prospect Research'),
        ('p', 'Lead generation was a core area of practical exposure. The first '
              'thing it taught me is that lead generation involves considerably '
              'more than collecting names and contact details. It begins by '
              'defining the kind of organisation or professional who may '
              'plausibly be relevant, and only then identifies the information '
              'that would support a legitimate business conversation with '
              'them.'),
        ('bullets', [
            'Defining the kind of organisation and professional role that '
            'would make a lead relevant.',
            'Collecting only the information that served the task, and no '
            'unnecessary personal data.',
            'Recording unavailable information as unavailable rather than '
            'inferring it.',
            'Distinguishing a reachable contact from a relevant one, and a '
            'reply from a qualified opportunity.',
        ]),
        ('h3', '2.3.6  Lead Records, Tracking and Follow-Up'),
        ('p', 'Lead organisation matters because follow-up depends entirely on '
              'usable records. A clear tracker distinguishes between records '
              'that are new, reviewed, contacted, responded to and awaiting '
              'follow-up, where such statuses form part of the team’s '
              'workflow. Consistent fields and careful checking reduce '
              'duplication and make the next action legible to whoever picks '
              'the record up.'),

        ('bullets', [
            'Maintaining consistent record fields so that entries could be '
            'compared and checked.',
            'Keeping an explicit status against each record, such as new, '
            'reviewed, contacted or awaiting follow-up.',
            'Recording the next action so that the record could be acted on '
            'without consulting its author.',
            'Checking for duplication before adding a record, and correcting '
            'at source rather than working around an error.',
        ]),
        ('h3', '2.3.7  Digital Marketing Research and Content Support'),
        ('p', 'Research supports nearly every stage of digital marketing, '
              'helping marketers understand industries, organisations, '
              'audiences and communication context. During the internship this '
              'work connected closely with account-based marketing and lead '
              'generation, for the simple reason that the usefulness of any '
              'outreach depends on the quality of the information behind it.'),
        ('bullets', [
            'Asking what decision a piece of information would support before '
            'collecting it.',
            'Judging source credibility and checking details wherever checking '
            'was possible.',
            'Separating verified findings from interpretation within my own '
            'notes.',
            'Reviewing content for clarity, jargon and alignment with the '
            'organisation’s professional identity before use.',
        ]),
        ('h3', '2.3.8  Coordination, Documentation and Reporting'),
        ('p', 'Digital marketing tasks depend on coordination, because '
              'research, messaging, outreach and follow-up are frequently '
              'connected to the work of other team members. Clear '
              'documentation preserves context and reduces the possibility of '
              'duplicated or missed actions. A useful record is concise, '
              'accurate and easy for the intended reader to interpret, which is '
              'a higher standard than being merely complete.'),
        ('bullets', [
            'Clarifying the expected output before starting an unfamiliar '
            'task.',
            'Communicating progress and raising incomplete information as a '
            'question rather than resolving it by assumption.',
            'Documenting work concisely enough that the intended reader could '
            'interpret it without help.',
            'Separating activity measures from outcome measures when reporting '
            'what had been done.',
        ]),
        ('p', 'Reporting should reflect the work actually completed and the '
              'evidence actually available. It is important to distinguish '
              'activity measures, such as research completed or messages '
              'prepared, from outcome measures such as qualified responses or '
              'genuine business opportunities. That distinction supports honest '
              'evaluation and prevents activity volume from being mistaken for '
              'business impact, which is a failure mode that digital marketing '
              'is unusually prone to.'),

        ('h2', '2.4  TIMELINE OF ACTIVITIES'),
        ('p', 'The internship lasted 35 days. The timeline below presents the '
              'learning progression across that period in five phases of seven '
              'days each. It is a structured account of the work areas and '
              'their sequence, not a day-by-day claim about specific meetings, '
              'message volumes or numerical outcomes. The actual assignment of '
              'tasks overlapped across the 35 days, and the phases should be '
              'read as describing where the emphasis lay rather than as '
              'exclusive blocks of work.'),

        ('h3', 'Phase 1 (Days 1–7): Orientation and Familiarisation'),
        ('bullets', [
            'Introduction to the organisation, its services and the kinds of '
            'client it works with.',
            'Understanding the objectives of the internship and the work areas '
            'assigned to me.',
            'Familiarisation with workflow, communication standards and the '
            'review expectations that apply to external-facing material.',
            'Understanding the research requirements that apply to account and '
            'prospect information, including the distinction between verified '
            'information and inference.',
        ]),

        ('h3', 'Phase 2 (Days 8–14): Account-Based Marketing Research'),
        ('bullets', [
            'Learning how target accounts are identified and why account '
            'relevance is assessed before any outreach is prepared.',
            'Reviewing publicly available company and industry information to '
            'build an understanding of an account’s business context.',
            'Developing awareness of stakeholder roles and of which concerns '
            'are likely to matter to which role.',
            'Practising structured note-keeping so that account research '
            'remains usable by somebody other than its author.',
        ]),

        ('h3', 'Phase 3 (Days 15–21): LinkedIn Marketing'),
        ('bullets', [
            'Understanding audience relevance on a professional platform and '
            'how role, organisation and interest determine it.',
            'Learning the conventions of professional tone, message clarity and '
            'an appropriate reason for contact.',
            'Observing how visibility, engagement and direct outreach serve '
            'different purposes and should not be confused.',
            'Understanding relationship-building as a longer-term objective '
            'rather than as a route to immediate conversion.',
        ]),

        ('h3', 'Phase 4 (Days 22–28): Email Marketing and Lead Generation'),
        ('bullets', [
            'Learning the structure of a business email from subject line '
            'through to a proportionate call to action.',
            'Understanding lead relevance and the difference between a '
            'reachable contact and a qualified opportunity.',
            'Practising the organisation of prospect information into '
            'consistent, checkable records.',
            'Understanding follow-up discipline and the role of status and next '
            'action in making follow-up possible.',
            'Developing awareness of consent, data handling and the respect of '
            'recipient preferences in email outreach.',
        ]),

        ('h3', 'Phase 5 (Days 29–35): Review and Consolidation'),
        ('bullets', [
            'Quality checking of research and records, and correction of gaps '
            'and inconsistencies.',
            'Understanding the interdependence of the four work areas and how '
            'each one feeds the next.',
            'Reflecting on the learning from each phase and identifying which '
            'skills needed further development.',
            'Consolidating notes and documentation into a form suitable for '
            'handover and for this report.',
        ]),

        ('h2', '2.5  TOOLS AND SYSTEMS USED'),
        ('h3', '2.5.1  Professional Networking Platform'),
        ('p', 'LinkedIn was the principal platform for professional audience '
              'research and outreach. It was used to understand organisations '
              'and professional roles, to observe how companies present their '
              'capabilities, and to learn the conventions of outreach on a '
              'platform where the recipient’s professional identity is public '
              'and permanent. Working on such a platform teaches restraint, '
              'because everything said there is attributable.'),

        ('h3', '2.5.2  Spreadsheets and Lead Trackers'),
        ('p', 'Spreadsheets were the working tool for organising account and '
              'prospect information. Their value lies less in any advanced '
              'function than in consistency: the same fields in the same order, '
              'with a status and a next action against each record. I learned '
              'that a tracker is a communication document rather than a '
              'personal notebook, and that its quality is judged by whether '
              'another person can act on it without explanation.'),

        ('h3', '2.5.3  Professional Email and Correspondence'),
        ('p', 'Business email was used for outreach drafting and follow-up '
              'correspondence. The learning here was as much about convention '
              'as about tooling: how a subject line is framed, how a first '
              'message to a stranger differs from a follow-up, how to be brief '
              'without being abrupt, and how to close a message with a next '
              'step the recipient can accept or decline easily.'),

        ('h3', '2.5.4  Research Sources and Public Information'),
        ('p', 'Company websites, public professional profiles, industry '
              'publications and general secondary sources provided the raw '
              'material for account research. The skill involved is source '
              'discrimination: judging whether a source is credible, whether '
              'the information is current enough for the purpose, and whether '
              'what has been found actually answers the question that prompted '
              'the search.'),

        ('h3', '2.5.5  Documentation and Reporting Formats'),
        ('p', 'Documents and reporting formats were used to record research, '
              'summarise work and communicate progress. Writing for an internal '
              'reader is a distinct skill from writing for a prospect: the '
              'internal reader needs to know what was done, what was found, '
              'what remains uncertain and what should happen next, and wants '
              'all of it briefly.'),

        ('h2', '2.6  APPLICATION OF ACADEMIC KNOWLEDGE'),
        ('h3', '2.6.1  Marketing Management'),
        ('p', 'Segmentation, targeting and positioning moved from being '
              'examinable concepts to being the actual structure of the work. '
              'Account-based marketing is a direct application of targeting '
              'taken to its logical conclusion, in which the segment is reduced '
              'to a single organisation. The internship reinforced the '
              'sequence the subject teaches but that practice easily forgets: '
              'choose the audience before writing the message.'),


        ('bullets', [
            'Applied segmentation and targeting by treating individual organisations as the unit of marketing attention.',
            'Used positioning to connect a general service capability to a specific business situation.',
            'Reinforced the sequence the subject teaches: choose the audience before writing the message.',
        ]),
        ('h3', '2.6.2  Marketing Research'),
        ('p', 'The research methods studied in the programme applied directly '
              'to account and prospect work: defining the question, selecting '
              'sources, judging credibility, recording findings and '
              'distinguishing data from interpretation. The practical addition '
              'was economy. Academic research rewards thoroughness, while '
              'commercial research rewards sufficiency, and recognising when '
              'enough has been established is a judgement the classroom does '
              'not require.'),


        ('bullets', [
            'Defined the research question before selecting sources, rather than collecting first.',
            'Judged source credibility and recorded findings so that data and interpretation stayed separate.',
            'Learned the commercial discipline of sufficiency, which academic research does not require.',
        ]),
        ('h3', '2.6.3  Organisational Buying Behaviour'),
        ('p', 'The study of business buying behaviour explained what I observed '
              'in outreach. A business decision of this kind involves several '
              'stakeholders, extends over time, and is evaluated against '
              'organisational rather than personal criteria. That is why '
              'stakeholder mapping matters, why a single message rarely '
              'produces a decision, and why patience is a professional '
              'requirement rather than a temperament.'),


        ('bullets', [
            'Recognised that a business purchase involves several stakeholders with differing concerns.',
            'Understood that evaluation extends over time and against organisational rather than personal criteria.',
            'Accepted patience as a professional requirement rather than a matter of temperament.',
        ]),
        ('h3', '2.6.4  Business Communication'),
        ('p', 'Business communication was the subject most continuously in use. '
              'Professional communication requires clarity, appropriate tone, '
              'correct information and an evident purpose, and the internship '
              'showed how directly writing quality and audience awareness '
              'affect whether a message is read, understood and treated as '
              'credible. The subject also supplied the discipline of revision, '
              'which in outreach is not optional.'),


        ('bullets', [
            'Wrote for an unknown professional reader with attention to clarity, tone and evident purpose.',
            'Learned how directly writing quality affects whether a message is read and treated as credible.',
            'Adopted revision as a standard step rather than an optional improvement.',
        ]),
        ('h3', '2.6.5  Strategic Management'),
        ('p', 'Strategic management contributed the idea that activity should '
              'be aligned to objectives and that resources are finite. '
              'Prioritising accounts, concentrating research effort where it is '
              'most likely to matter and declining to pursue poorly matched '
              'prospects are all applications of that principle at a working '
              'level rather than at the level of corporate strategy.'),


        ('bullets', [
            'Prioritised accounts according to their fit with the service being offered.',
            'Concentrated research effort where it was most likely to influence an outcome.',
            'Learned to decline poorly matched prospects instead of pursuing them for volume.',
        ]),
        ('h3', '2.6.6  Business Analytics and Data Management'),
        ('p', 'Analytical thinking and basic data-management concepts were '
              'useful in lead generation and research. Organised information '
              'makes it easier to review records, identify missing details and '
              'support follow-up, and the internship demonstrated that even '
              'simple tracking practices contribute to a more systematic '
              'workflow. The subject also supplied the vocabulary for the '
              'distinction between activity metrics and outcome metrics, which '
              'became one of the most useful ideas I took from the whole '
              'period.'),


        ('bullets', [
            'Organised information so that records could be reviewed and gaps identified.',
            'Used simple tracking practices to make the workflow systematic rather than improvised.',
            'Acquired the vocabulary to separate activity metrics from outcome metrics.',
        ]),
        ('h2', '2.7  SKILLS DEVELOPED DURING THE INTERNSHIP'),
        ('h3', '2.7.1  Account and Industry Research'),
        ('p', 'The ability to research an organisation purposefully, establish '
              'why it might be relevant and stop at the point where the '
              'question is answered.'),
        ('h3', '2.7.2  Audience and Stakeholder Analysis'),
        ('p', 'The ability to identify which professional roles are likely to '
              'be involved in a decision and what each of them is likely to '
              'care about.'),
        ('h3', '2.7.3  Professional Written Communication'),
        ('p', 'Improved drafting of concise, relevant business messages for '
              'both a professional platform and email, with an appropriate tone '
              'and a proportionate request.'),
        ('h3', '2.7.4  Personalisation Judgement'),
        ('p', 'The ability to distinguish meaningful personalisation, grounded '
              'in verified context, from cosmetic personalisation that a '
              'recipient sees through.'),
        ('h3', '2.7.5  Data Organisation and Record Discipline'),
        ('p', 'The habit of maintaining consistent, checkable records with a '
              'clear status and next action, written for another reader rather '
              'than for myself.'),
        ('h3', '2.7.6  Attention to Detail'),
        ('p', 'A practical intolerance of unverified detail in anything '
              'intended for an external recipient, and the proofreading habit '
              'that supports it.'),
        ('h3', '2.7.7  Prioritisation and Self-Management'),
        ('p', 'The ability to manage several connected activities, identify '
              'blockers early and communicate them rather than allowing work to '
              'stall silently.'),
        ('h3', '2.7.8  Ethical and Privacy Awareness'),
        ('p', 'An understanding of responsible data handling, appropriate '
              'sourcing of contact information and respect for stated '
              'recipient preferences.'),

        ('h2', '2.8  KEY OBSERVATIONS FROM THE JOB'),
        ('bullets', [
            'Targeting precedes messaging. A well-written message sent to an '
            'irrelevant audience is still a failed message, which makes the '
            'research that establishes relevance the substantive work rather '
            'than the preparation for it.',
            'Research is a selection problem, not a collection problem. Public '
            'information about most organisations is effectively unlimited, and '
            'the skill lies in identifying the few facts that bear on the '
            'decision at hand.',
            'Personalisation is judged by the recipient, not by the sender. '
            'Inserting a company name into a generic message is visible as '
            'such, and it damages credibility more than a plainly generic '
            'message would.',
            'Volume and relevance pull against each other. Automated outreach '
            'raises activity counts, but poorly matched communication lowers '
            'engagement and can cause reputational harm that persists.',
            'A reply is not an opportunity. Interest, relevance, authority and '
            'timing are separate conditions, and a lead record that does not '
            'distinguish them will overstate the pipeline.',
            'Activity is easier to measure than outcome, which is precisely why '
            'activity is so often reported as though it were outcome.',
        ]),

        ('h2', '2.9  CHALLENGES ENCOUNTERED DURING THE INTERNSHIP'),
        ('h3', '2.9.1  Deciding What Information Is Relevant'),
        ('p', 'The most immediate practical challenge in marketing research is '
              'deciding which information matters. Publicly available material '
              'about an organisation can be extensive, and very little of it '
              'contributes to a specific marketing objective. Early on I '
              'collected more than was useful, which produced notes that were '
              'comprehensive and hard to act on. The learning was to keep '
              'research anchored to the account, role or business context that '
              'the task actually required, and to treat everything else as '
              'interesting rather than relevant.'),

        ('h3', '2.9.2  Personalising Without Becoming Lengthy'),
        ('p', 'Writing communication that is genuinely personalised without '
              'becoming long or over-familiar proved harder than expected. '
              'Having done the research, the temptation is to demonstrate it, '
              'which produces a message about the sender’s diligence rather '
              'than about the recipient’s situation. The resolution was to '
              'settle on one clear reason for contact, use only context that '
              'could be supported, and make the next step easy to understand '
              'and easy to decline.'),

        ('h3', '2.9.3  Maintaining Data Quality'),
        ('p', 'Lead and account information is frequently incomplete, '
              'inconsistent or out of date, and the pressure to fill a gap by '
              'inference is real. This reinforced the need to check '
              'information, to avoid guessing and to record uncertainty '
              'explicitly rather than tidily. A record that honestly says a '
              'field is unknown is more useful than one that quietly contains a '
              'plausible invention.'),

        ('h3', '2.9.4  Prioritising Among Pending Tasks'),
        ('p', 'When research, drafting and follow-up are all pending at once, '
              'the work does not sequence itself. I found that follow-up was '
              'the easiest thing to defer and the most costly to lose, because '
              'a lapsed follow-up quietly wastes all the research that preceded '
              'it. Learning to schedule the small continuation tasks rather '
              'than leaving them to be remembered was a genuine improvement.'),

        ('h3', '2.9.5  Working Without Measurable Feedback'),
        ('p', 'A final challenge was intrinsic to the work rather than to my '
              'inexperience. In a field with long evaluation cycles, the '
              'quality of an outreach effort is not revealed quickly, and '
              'silence is ambiguous: it may mean the message was wrong, or the '
              'timing was wrong, or the recipient is simply busy. Working '
              'carefully without immediate confirmation that the care was '
              'justified requires a kind of discipline that I had not needed '
              'before.'),

        ('h2', '2.10  OVERALL JOB EXPERIENCE'),
        ('p', 'The overall experience of the work was that digital marketing in '
              'a business to business setting is far more analytical than its '
              'public reputation suggests. I had expected a function centred on '
              'content and platforms. What I found was a function centred on '
              'judgement: which organisations are worth approaching, what can '
              'honestly be said to them, what the evidence actually supports '
              'and what the next appropriate step is.'),
        ('p', 'The four work areas turned out to be one activity seen from four '
              'positions. Account research determined who was worth '
              'approaching. Professional-platform outreach and email were two '
              'ways of approaching them. Lead records were how the approach was '
              'remembered and continued. Treating these as separate tasks '
              'produces fragmented work, and one of the clearer lessons of the '
              'closing phase was how much of the value sits in the connections '
              'between them.'),
        ('p', 'I should also be honest about the limits of a 35-day placement. '
              'Thirty-five days is long enough to learn how the work is done '
              'and short enough that no long-cycle outcome could be observed '
              'from beginning to end. I therefore left with a good '
              'understanding of method and a limited understanding of results, '
              'and I would rather state that plainly than imply an experience '
              'of campaign outcomes the period did not permit.'),
        ('h2', '2.11  SUMMARY OF RESPONSIBILITIES'),
        ('p', 'The table below consolidates the work areas of the internship '
              'and the nature of my involvement in each. It reflects the areas '
              'assigned to me and does not claim independent campaign '
              'ownership or attribute numerical results.'),
        ('table', {'rows': [
            ['S. No.', 'Area of Work', 'Major Responsibility'],
            ['1', 'Target-account research',
             'Reviewing public company, business and industry information for '
             'selected organisations to establish account relevance'],
            ['2', 'Account fit assessment',
             'Judging whether an organisation plausibly matched the services '
             'offered, and recording the reason either way'],
            ['3', 'Stakeholder context',
             'Identifying the professional roles likely to influence a digital '
             'product decision and what each would care about'],
            ['4', 'Personalisation of outreach',
             'Connecting a message to verified business context rather than to '
             'a cosmetic detail such as a company name'],
            ['5', 'LinkedIn audience research',
             'Establishing professional relevance of roles and organisations '
             'before any contact was made'],
            ['6', 'LinkedIn outreach',
             'Preparing concise messages with a clear reason for contact and a '
             'reasonable next step'],
            ['7', 'Email drafting',
             'Structuring subject line, opening, value proposition and a '
             'proportionate call to action in plain language'],
            ['8', 'Email follow-up',
             'Maintaining courteous follow-up correspondence and respecting '
             'stated recipient preferences'],
            ['9', 'Lead identification and qualification',
             'Identifying prospects and assessing fit, role relevance, need '
             'and timing rather than reachability alone'],
            ['10', 'Lead records and tracking',
             'Maintaining consistent fields, explicit status and a next action '
             'against every record'],
            ['11', 'Digital marketing research and content support',
             'Industry and audience research, source discrimination and '
             'separation of verified fact from interpretation'],
            ['12', 'Coordination, documentation and reporting',
             'Documenting work, communicating progress, raising incomplete '
             'information and reporting activity honestly'],
        ], 'widths': [1, 3, 6], 'col_bold': [True, True, False],
            'col_align': ['center', 'left', 'left'], 'row_height': 500}),

        ('h2', '2.12  CONCLUSION OF JOB / TASK DESCRIPTION'),
        ('p', 'The 35-day internship gave me practical exposure to four '
              'connected areas of business to business digital marketing: '
              'account-based marketing, LinkedIn marketing, email marketing and '
              'lead generation, together with the research, documentation and '
              'coordination that support them. The progression through '
              'orientation, account research, channel outreach and '
              'consolidation followed a coherent learning sequence, and by the '
              'closing phase I could see the areas as parts of a single process '
              'rather than as separate assignments.'),
        ('p', 'The chapter has deliberately described responsibilities and '
              'learning rather than results. No campaign outcomes, account '
              'counts, message volumes, response rates or lead totals are '
              'stated, because verified figures for them were not available to '
              'me, and inserting plausible numbers into an academic report '
              'would be a more serious fault than reporting less. What can be '
              'stated with confidence is the method I was taught, the standards '
              'I was held to and the judgement I began to acquire. The next '
              'chapter analyses how well I performed against those standards.'),
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

        ('h2', '3.1  BASIS OF PERFORMANCE ANALYSIS'),
        ('p_indent', 'The analysis in this chapter is qualitative. It examines '
                     'the nature of the work areas assigned to me and considers '
                     'work quality, research relevance, communication, time '
                     'management, adaptability and professional development. '
                     'Verified campaign dashboards, lead counts, response rates '
                     'and supervisor evaluation scores were not available to me, '
                     'and the chapter accordingly assigns no numerical ratings '
                     'and claims no specific business outcomes.'),
        ('p', 'For a digital marketing intern, performance can reasonably be '
              'understood along two dimensions. The first is task execution: '
              'following instructions, preparing accurate information, '
              'maintaining clear records and producing communication that fits '
              'its objective. The second is learning behaviour: asking relevant '
              'questions, applying feedback, adapting to unfamiliar tasks and '
              'understanding how an individual activity connects to a business '
              'goal. An intern who executes well but learns nothing has not '
              'really succeeded, and neither has one who understands everything '
              'but produces unusable work.'),
        ('h2', '3.2  QUALITY AND ACCURACY OF WORK'),
        ('p', 'Quality in this work begins with accuracy. Research-based '
              'communication has to rest on relevant and correct information, '
              'and prospect records have to be checked before they are used. '
              'Incorrect company details, inaccurate role information or an '
              'unsupported assumption will weaken the credibility of an '
              'outreach effort, and the damage is done at the moment the '
              'recipient notices. Careful review was therefore the first '
              'principle I was expected to work to, and I believe I applied it '
              'consistently, though not without early lapses.'),
        ('p', 'Assessing myself on this dimension, my accuracy improved '
              'materially over the 35 days. My early research notes were '
              'thorough but poorly organised, and my early drafts required more '
              'correction than they should have. By the later phases I was '
              'checking details before recording them rather than afterwards, '
              'which is a small change in sequence with a large effect on '
              'output quality.'),

        ('h2', '3.3  RESEARCH, TARGETING AND RELEVANCE'),
        ('p', 'Research and targeting are central to account-based marketing '
              'and lead generation, and they are where I spent most of the '
              'internship. A strong target list should reflect the intended '
              'business audience rather than being assembled to increase '
              'volume. Understanding an organisation’s context and the '
              'relevance of a particular professional role is what allows '
              'purposeful communication to be prepared at all.'),
        ('p', 'On this dimension I would rate my development as the strongest '
              'of the internship, largely because it was where I was most '
              'consistently corrected. My initial instinct was to treat a '
              'plausible-looking organisation as a relevant one. Learning to '
              'ask what specifically made an account a fit, and to accept that '
              'the honest answer was sometimes nothing, was the single most '
              'useful correction I received.'),

        ('h2', '3.4  COMMUNICATION AND PROFESSIONALISM'),
        ('p', 'Professional communication was relevant across both outreach '
              'channels. A message needs to be clear, respectful and '
              'appropriate to the recipient’s role and context. An effective '
              'opening establishes relevance, and a concise value proposition '
              'lets the recipient judge quickly whether the communication '
              'deserves their attention. Respecting that judgement, rather than '
              'attempting to override it, is part of the professionalism.'),
        ('p', 'The internship helped me recognise that communication of this '
              'kind is a judgement skill as much as a writing skill. The '
              'marketer decides what to include, what to leave out, how to '
              'express uncertainty and what next step is proportionate. Those '
              'decisions are less teachable than grammar and matter more. My '
              'writing was competent at the start of the internship; my '
              'judgement about what to write was not, and that is where the '
              'improvement occurred.'),

        ('h2', '3.5  TIME MANAGEMENT, COORDINATION AND ADAPTABILITY'),
        ('p', 'Digital marketing work involves several connected activities: '
              'research, data organisation, message preparation and follow-up. '
              'Managing them requires prioritisation and an understanding of '
              'deadlines. Because a task may depend on information from another '
              'source, it is important to identify a blocker early and '
              'communicate it rather than allowing the work to sit in an '
              'unclear state, which is the failure I had to guard against most '
              'often.'),
        ('p', 'The 35-day period gave me a setting in which to practise '
              'professional discipline and to see the value of organised work. '
              'I improved at identifying blockers early and at seeking feedback '
              'when a task was unfamiliar. Continued improvement in planning, '
              'estimating how long a task will take and maintaining consistent '
              'records will support greater efficiency in future assignments, '
              'and estimation in particular remains weak.'),

        ('h2', '3.6  STRENGTHS AND AREAS FOR IMPROVEMENT'),
        ('h3', '3.6.1  STRENGTHS DEMONSTRATED'),
        ('p', 'The following are offered as qualitative reflections on the '
              'internship work rather than as formal ratings.'),
        ('bullets', [
            'Willingness to learn: I approached the four work areas as '
            'connected parts of one function, and tried to build practical '
            'understanding through observation and involvement rather than '
            'waiting to be instructed.',
            'Research orientation: I developed the habit of establishing account '
            'and prospect context before treating any information as usable for '
            'outreach.',
            'Communication awareness: I acquired a stronger appreciation of '
            'concise, relevant and professional language, and of the difference '
            'between writing to inform and writing to impress.',
            'Attention to detail: research and lead organisation reinforced the '
            'need to check information and to resist filling gaps with '
            'assumption.',
            'Process awareness: I gained a clear understanding of how targeting, '
            'communication, lead records and follow-up form a connected '
            'workflow rather than a sequence of separate jobs.',
            'Intellectual honesty: I became comfortable recording that '
            'something was unknown, which is a smaller virtue than it sounds '
            'until one has felt the pressure to do otherwise.',
        ]),
        ('p', 'These strengths are a foundation rather than an accomplishment. '
              'They should be read as learning outcomes from a short placement '
              'and not as a substitute for a formal performance appraisal, '
              'which I did not receive.'),

        ('h3', '3.6.2  AREAS FOR IMPROVEMENT'),
        ('p', 'The internship was at least as informative about my gaps as '
              'about my strengths. The following development areas are stated '
              'specifically, because a general intention to improve is not '
              'actionable.'),
        ('bullets', [
            'Advanced account-based marketing planning: account scoring, '
            'stakeholder mapping, account prioritisation and the coordination '
            'between marketing and sales that the method assumes.',
            'Marketing analytics: interpreting engagement and lead-quality '
            'indicators, separating activity from outcome in practice rather '
            'than in principle, and preparing concise performance summaries.',
            'Customer relationship management and data practice: structured '
            'lead records, status definitions, data hygiene and the responsible '
            'handling of contact information at scale.',
            'Copywriting and personalisation: writing concise, '
            'audience-specific messages and adapting tone across different '
            'professional contexts without losing brevity.',
            'Email campaign fundamentals: deliverability, segmentation, '
            'testing, consent management and the correct interpretation of '
            'email metrics.',
            'Planning and prioritisation: task estimation, follow-up tracking '
            'and the systematic management of several concurrent activities.',
            'Commercial exposure: I saw the marketing side of business '
            'development but not the conversations that follow a qualified '
            'lead, which is a gap in my understanding of the full cycle.',
        ]),
        ('h2', '3.7  OVERALL PERFORMANCE'),
        ('p', 'The points below summarise the performance dimensions discussed '
              'in this chapter, the reflection drawn from the internship work '
              'areas and the focus for further development in each.'),
        ('bullets', [
            '**Work quality:** accurate research, organised records and clear '
            'messages determined the usability of every output. Further focus: '
            'consistent checklists and a review step before recording rather '
            'than after.',
            '**Targeting:** account-based marketing and lead generation depend '
            'on relevant account and contact selection. Further focus: '
            'stronger account-fit criteria and research discipline.',
            '**Communication:** both outreach channels required a professional '
            'tone and an evident purpose. Further focus: concise copywriting '
            'and audience-specific messaging.',
            '**Task management:** several connected activities required '
            'tracking and the timely raising of blockers. Further focus: '
            'planning, task estimation and follow-up routines.',
            '**Adaptability:** different work areas required different '
            'approaches and formats within short periods. Further focus: '
            'continued learning of tools, processes and channel practices.',
            '**Measurement:** marketing activity has to be connected to '
            'indicators that genuinely reflect the objective. Further focus: '
            'confidence with analytics, reporting and lead-quality '
            'assessment.',
        ]),
        ('p', 'Taken together, the analysis indicates that the internship '
              'succeeded as a practical learning experience. It strengthened my '
              'understanding of the standards expected in digital marketing '
              'support work and identified specific skills I can continue to '
              'develop. No numerical performance score is assigned, because no '
              'official rubric or verified measurement data was supplied to me, '
              'and constructing one for the sake of appearance would '
              'misrepresent the basis of this chapter.'),
        ('p', 'If I were to summarise my own performance in a sentence, it '
              'would be this: I was a reliable executor of assigned research '
              'and communication tasks who improved noticeably in judgement '
              'over 35 days, and who left with an accurate rather than an '
              'inflated sense of what he can currently do. The next chapter '
              'consolidates the knowledge and professional skills gained during '
              'the period.'),
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

        ('h2', '4.1  TECHNICAL KNOWLEDGE ACQUIRED'),
        ('p', 'The internship provided practical exposure to digital '
                     'marketing activities that support business to business '
                     'communication and business development. Before it, I '
                     'understood most marketing concepts as academic '
                     'frameworks. Working with account-based marketing, '
                     'LinkedIn marketing, email marketing and lead generation '
                     'let me see them as connected activities requiring '
                     'planning, execution and review. The four subsections '
                     'below set out what I learned in each area.'),


        ('bullets', [
            'Account selection and the assessment of account fit in a business '
            'to business context.',
            'Target-account research and the separation of verified '
            'information from inference.',
            'Stakeholder mapping and the tailoring of a message to a '
            'particular professional role.',
            'Professional-network conventions governing relevance, tone and an '
            'appropriate reason for contact.',
            'Business email structure, from subject line through to a '
            'proportionate call to action.',
            'Lead qualification on fit, role relevance, need and timing rather '
            'than on reachability.',
            'Lead record design, status definitions and the discipline of '
            'follow-up.',
            'Responsible data handling, consent and respect for stated '
            'recipient preferences.',
        ]),
        ('h3', '4.1.1  Account-Based Marketing'),
        ('p', 'Account-based marketing taught me the value of focus in business '
              'to business marketing. Treating selected organisations as '
              'individual markets requires more research and planning than '
              'broad outreach, and it obliges the marketer to understand '
              'account fit, identify relevant stakeholders and tailor '
              'communication to a credible business context rather than to a '
              'category.'),
        ('h3', '4.1.2  LinkedIn and Professional Network Marketing'),
        ('p', 'LinkedIn marketing showed me the role of professional platforms '
              'in business to business visibility and relationship-building. '
              'The platform is not only a place to publish; it supports '
              'professional discovery, industry conversation and relevant '
              'outreach, and those uses call for different approaches.'),
        ('h3', '4.1.3  Email Marketing'),
        ('p', 'Email marketing strengthened my understanding of structured '
              'written communication. A message needs to be clear from the '
              'subject line through to the call to action, and the recipient '
              'should be able to establish quickly why it is relevant and what, '
              'if anything, is being asked of them.'),
        ('h3', '4.1.4  Lead Generation'),
        ('p', 'Lead generation taught me the difference between collecting '
              'contact information and identifying a relevant potential '
              'opportunity. A useful lead record provides enough accurate '
              'context to support an appropriate next step while avoiding '
              'unnecessary data collection, and those two requirements pull '
              'against each other in practice.'),
        ('h2', '4.2  PRACTICAL EXPOSURE TO BUSINESS PROCESSES'),
        ('p', 'The internship showed me that digital marketing begins with the '
              'objective and the audience. Without a clear audience, '
              'communication becomes generic. Without a clear objective, '
              'activity produces no usable learning. Linking each task to a '
              'business purpose, and then reviewing whether the output actually '
              'serves that purpose, was the habit the work most consistently '
              'demanded.'),
        ('p', 'Observing the function within an operating company added '
              'something that no amount of reading supplies: an understanding '
              'of why the process constraints exist. Review steps, record '
              'standards and caution about claims can look like bureaucracy '
              'from outside. From inside, each of them is a response to a way '
              'that outreach can go wrong at the organisation’s expense.'),

        ('h2', '4.3  IMPROVEMENT IN ANALYTICAL AND STRATEGIC THINKING'),
        ('p', 'The internship encouraged me to think past task completion and '
              'to ask why an activity was being performed at all. Account '
              'research is useful when it improves targeting or communication. '
              'Lead organisation is useful when it supports follow-up. Message '
              'review is useful when it improves clarity and accuracy. Each of '
              'those is a test that a piece of work can fail while still being '
              'finished.'),
        ('p', 'I developed a much stronger appreciation of the difference '
              'between an activity metric and a business outcome. The number of '
              'records researched or messages prepared describes work '
              'completed; it establishes nothing about lead quality or '
              'commercial impact. Meaningful analysis requires indicators that '
              'relate to the objective and an understanding of what each one '
              'actually measures. This single distinction changed how I read '
              'marketing claims, including the ones I encountered while '
              'researching this report.'),
        ('h2', '4.4  SOFT SKILLS AND PROFESSIONAL TRAITS STRENGTHENED'),
        ('p', 'The internship supported the development of professional written '
              'communication in a way coursework had not. Both outreach '
              'channels required a tone that was clear, respectful and suited '
              'to a business audience, and writing to an unknown professional '
              'reader taught me to consider the recipient’s perspective and to '
              'state a purpose without unnecessary elaboration.'),
        ('bullets', [
            'Professional written communication addressed to an unknown '
            'business reader.',
            'Brevity, and the judgement of what to leave out of a message.',
            'Time management across research, drafting and follow-up running '
            'concurrently.',
            'Organisation, since scattered information makes several open '
            'tasks unmanageable.',
            'Receptiveness to feedback, including accepting a correction '
            'without defending the first attempt.',
            'Adaptability across differing task requirements, audiences and '
            'formats.',
            'Restraint, expressed as not claiming, not pressing and not '
            'overstating.',
        ]),
        ('p', 'A less obvious trait the internship strengthened was restraint. '
              'Much of professional marketing consists of not doing things: not '
              'claiming more than is known, not following up more often than is '
              'warranted, not reporting activity as though it were achievement. '
              'Learning that the discipline is often subtractive was a genuine '
              'change in how I think about the work.'),

        ('h2', '4.5  ALIGNMENT WITH ACADEMIC LEARNING'),
        ('p', 'The internship served as a practical extension of the subjects '
              'studied in the MBA programme. The table below maps each subject '
              'to the work in which it was applied.'),
        ('table', {'rows': [
            ['Academic Subject', 'Internship Application'],
            ['Marketing Management',
             'Segmentation, targeting and positioning, and the selection of '
             'communication channels according to the objective'],
            ['Business Communication',
             'Professional tone, concise writing, audience awareness and clear, '
             'proportionate calls to action'],
            ['Organisational Buying Behaviour',
             'Understanding that business decisions involve several '
             'stakeholders, extend over time and are evaluated against '
             'organisational criteria'],
            ['Marketing Research',
             'Collecting relevant information, judging source credibility and '
             'using research to support account targeting'],
            ['Strategic Management',
             'Aligning marketing activity with business objectives and '
             'prioritising accounts under finite time'],
            ['Business Analytics',
             'Distinguishing activity measures from outcome measures and '
             'recognising what an indicator does and does not establish'],
            ['Business Ethics',
             'Responsible communication, accurate claims, appropriate data '
             'handling and respect for recipient preferences'],
        ], 'widths': [3, 6], 'col_bold': [True, False],
            'col_align': ['center', 'left'], 'row_height': 500}),
        ('p', 'The internship also exposed the limits of purely academic '
              'preparation. Coursework describes a target segment as a set of '
              'attributes; practice required me to name an actual organisation, '
              'establish why it was relevant, find the right professional role '
              'and write something that person would be willing to read. The '
              'gap between a described audience and a contacted one is, in my '
              'view, the real content of an internship.'),

        ('h2', '4.6  ETHICAL, PRIVACY AND DATA-HANDLING AWARENESS'),
        ('p', 'Digital marketing involves communication and, in most cases, the '
              'use of business contact information, which makes responsible '
              'handling of that information a professional requirement rather '
              'than a preference. Marketers should use appropriate sources, '
              'collect only what is relevant to the task and follow '
              'organisational policy together with the applicable law, '
              'including the requirements of the Digital Personal Data '
              'Protection Act, 2023 (Government of India, 2023).'),
        ('p', 'Ethical communication requires accuracy and transparency. A '
              'message should not misrepresent the organisation, exaggerate its '
              'capabilities or imply knowledge of the recipient’s situation '
              'that has not been verified. Personalisation should rest on '
              'legitimate, relevant information and should not intrude on a '
              'recipient’s privacy, which is a line that enthusiastic research '
              'can cross without intending to.'),
        ('h2', '4.7  PROFESSIONAL INSIGHTS AND FUTURE DEVELOPMENT'),
        ('p', 'The internship sharpened my awareness of what a career in '
              'digital marketing actually requires. Practical effectiveness '
              'depends on a combination of research, writing, audience '
              'understanding, data organisation, analytical thinking and '
              'professional conduct. Developing one of these while neglecting '
              'the others is unlikely to support sustained growth, which is a '
              'more demanding conclusion than I expected to reach.'),

        ('bullets', [
            'Practical effectiveness in this field rests on research, writing, '
            'audience understanding, data organisation, analysis and conduct '
            'together.',
            'Relevance is established before a message is written, which makes '
            'research the substance of the work.',
            'Credibility accumulates slowly through accuracy and is lost '
            'quickly through a single unsupported claim.',
            'A marketing number is uninformative until one knows what it '
            'measures and what it omits.',
            'Long evaluation cycles mean that careful work often has to '
            'proceed without immediate confirmation.',
            'Process constraints such as review steps and record standards '
            'exist because of specific ways outreach goes wrong.',
            'Accuracy is a precondition for effectiveness in marketing rather '
            'than a constraint upon it.',
        ]),
        ('p', 'The broader professional insight is about the relationship '
              'between honesty and competence in this field. It would have been '
              'easy to write a more impressive report by inventing plausible '
              'numbers, and it would have been easy to run more impressive '
              'outreach by making claims that could not be supported. Both '
              'shortcuts fail in the same way and for the same reason. The '
              'internship left me with the conviction that in marketing, '
              'accuracy is not a constraint on effectiveness but a precondition '
              'for it.'),
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
                     'Doodleblue Innovations Private Limited, a Chennai-based '
                     'digital product engineering and digital transformation '
                     'company, over 35 days from [START DATE] to [END DATE], '
                     '2026, with the designation of Digital Marketing, under '
                     'the guidance of [NAME OF INDUSTRY MENTOR]. The internship '
                     'provided practical exposure to account-based marketing, '
                     'LinkedIn marketing, email marketing and lead generation, '
                     'together with the digital marketing research, '
                     'documentation and coordination that support them.'),
        ('p', 'The experience connected academic learning to practical '
              'marketing work in each of the four areas. Account-based '
              'marketing demonstrated the importance of selecting relevant '
              'accounts and understanding business context before any message '
              'is written. LinkedIn marketing highlighted professional audience '
              'relevance and the slow work of relationship-building. Email '
              'marketing reinforced the value of clear, structured '
              'communication with a proportionate request. Lead generation '
              'showed the importance of relevant prospect identification and '
              'organised follow-up, and of the difference between a contact and '
              'an opportunity.'),
        ('h2', '5.2  KEY TAKEAWAYS'),
        ('h3', '5.2.1  Targeting and Account Selection'),
        ('bullets', [
            'Learned that marketing communication is only as relevant as the '
            'audience definition behind it, and that targeting therefore '
            'precedes messaging rather than accompanying it.',
            'Understood that treating a small number of organisations as '
            'individual markets is a deliberate trade of reach for relevance, '
            'and that the trade has to be made consciously.',
            'Saw that attention given to one account is attention withheld from '
            'another, which makes account prioritisation a real decision rather '
            'than an administrative step.',
        ]),
        ('h3', '5.2.2  Research and Credibility'),
        ('bullets', [
            'Gained the ability to research an organisation purposefully, '
            'establishing why it might be relevant rather than accumulating '
            'whatever is available.',
            'Learned to separate verified information from interpretation in my '
            'own notes, so that an inference could not travel into outreach '
            'disguised as a fact.',
        ]),
        ('h3', '5.2.3  Professional Communication'),
        ('bullets', [
            'Improved my professional written communication across a '
            'professional platform and email, with attention to tone, brevity '
            'and a clear reason for contact.',
            'Learned that personalisation must connect to a genuine business '
            'context, because cosmetic customisation is visible to the '
            'recipient and costs more credibility than a plain message would.',
            'Understood that a proportionate request respects the recipient’s '
            'position, and that pressure and excessive follow-up work against '
            'the objective they are meant to serve.',
        ]),
        ('h3', '5.2.4  Lead Quality and Record Discipline'),
        ('bullets', [
            'Learned that lead quality depends on fit, role relevance and '
            'timing, and that a relevant, well-organised record is worth more '
            'than an unqualified list.',
            'Developed the habit of maintaining consistent records with an '
            'explicit status and next action, written so that another person '
            'could act on them unaided.',
            'Understood that follow-up is where research either realises its '
            'value or wastes it, and that it needs to be scheduled rather than '
            'remembered.',
        ]),
        ('h3', '5.2.5  Measurement and Honest Reporting'),
        ('bullets', [
            'Learned to distinguish activity measures from outcome measures, '
            'and to recognise that counts of work completed establish nothing '
            'about business impact.',
            'Understood that indicators should be selected against the '
            'objective, and that the easily counted is not therefore the '
            'meaningful.',
            'Learned that recording something as unknown is a professional act, '
            'and that a report is more useful when its limits are stated than '
            'when they are concealed.',
        ]),
        ('h3', '5.2.6  Process Improvement and Continuous Learning'),
        ('p', 'The points below are general process observations drawn from the '
              'learning themes of the internship. They are not claims that the '
              'organisation lacks these practices, and any application of them '
              'would need to align with its existing systems, policies and '
              'priorities.'),
        ('bullets', [
            'Consistent account and lead records preserve context across '
            'research, outreach and follow-up; shared definitions for fields '
            'such as source, research date, status and next action reduce '
            'ambiguity at handover.',
            'A short research and quality-check step, covering source review, '
            'accuracy, fit against the target profile and confirmation that '
            'unnecessary personal data has not been collected, prevents '
            'avoidable errors before they reach a recipient.',
            'Reviewing a message against its intended audience, the reason for '
            'contact and the desired next step keeps templates useful without '
            'letting them become generic.',
            'Separating activity measures from outcome measures in reporting '
            'makes both more informative, provided the indicators chosen '
            'reflect the objective and the verified data available.',
            'Short review discussions and a simple learning log help capture '
            'recurring questions, useful practices and development priorities, '
            'and make feedback specific enough to act on.',
        ]),

        ('h2', '5.3  CONCLUSION'),
        ('p', 'The 35-day internship at Doodleblue Innovations Private Limited '
              'was the point at which my study of marketing became practical. '
              'Over five phases I moved from orientation and industry '
              'familiarisation, through target-account research, to '
              'professional-platform outreach, business email communication and '
              'lead generation, and finally to review and consolidation. In '
              'doing so I acquired skills that are directly employable: account '
              'and industry research, stakeholder analysis, professional '
              'business writing, prospect qualification and record discipline.'),
        ('p', 'Beyond the technical content, three things changed. First, my '
              'understanding of marketing: in a business to business setting it '
              'is an analytical function before it is a creative one, and the '
              'research that establishes relevance is the substance of the work '
              'rather than its preparation. Second, my understanding of '
              'evidence: a marketing number means very little until one knows '
              'what it measures and what it does not, and the discipline of '
              'separating activity from outcome has changed how I read every '
              'claim in the field. Third, my understanding of myself. I learned '
              'that I am comfortable with detailed research work, that I write '
              'more clearly under a professional standard than under an '
              'academic one, and that I am willing to record an uncomfortable '
              'uncertainty rather than resolve it with a guess.'),
        ('p', 'I am equally clear about what remains to be developed: '
              'account-based marketing planning at a strategic level, marketing '
              'analytics and the interpretation of engagement data, customer '
              'relationship management practice, copywriting under real '
              'constraints, email campaign fundamentals including '
              'deliverability and consent, and exposure to the commercial '
              'conversations that follow a qualified lead. Knowing these gaps '
              'specifically, rather than as a general intention to improve, is '
              'itself an outcome of the internship.'),
        ('p', 'In conclusion, the internship achieved what a Summer Internship '
              'Programme is intended to achieve. It connected the MBA '
              'curriculum to live commercial work, it gave me practical '
              'experience of business to business digital marketing in a '
              'digital services company, and it settled my career interest '
              'towards research-led marketing and business development. I am '
              'grateful to the management of Doodleblue Innovations Private '
              'Limited for the opportunity, to [NAME OF INDUSTRY MENTOR] for '
              'guidance and review throughout the period, and to the marketing '
              'and business development teams for explaining their work to me. '
              'I leave the organisation with an accurate sense of what I can '
              'currently do, a specific agenda for what I need to learn next, '
              'and the confidence to contribute to a professional marketing '
              'team.'),
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
        ('p', 'The sources below provide the industry and sector context used '
              'in this report, together with general background on digital '
              'marketing, business to business marketing, professional '
              'networking, email communication and responsible data practice. '
              'The internship-specific content of the report is based on the '
              'work areas assigned to the author.'),
        ('bullets', [
            'American Marketing Association. (n.d.). Marketing definitions and '
            'resources. Retrieved September 2026, from https://www.ama.org/',

            'CNBC TV18. (2026, February). India tech to hit $315B in FY26, add '
            '135,000 jobs as AI emerges key revenue driver: NASSCOM. Retrieved '
            'September 2026, from https://www.cnbctv18.com/technology/',

            'Doodleblue Innovations. (n.d.). About us and services. Retrieved '
            'September 2026, from https://www.doodleblue.com/',

            'Doodleblue Innovations Private Limited. (2026). Internship '
            'completion certificate issued to the author.',

            'Economic Times. (2026a). Indian digital ad market likely to double '
            'to USD 22 bn by 2030: Report. Retrieved September 2026, from '
            'https://economictimes.indiatimes.com/industry/services/'
            'advertising/',

            'Economic Times. (2026b). IT’s FY26 revenues set to grow 6.1% to '
            '$315 billion. ETCIO. Retrieved September 2026, from '
            'https://cio.economictimes.indiatimes.com/',

            'ETBrandEquity. (2026). Pitch Madison Advertising Report 2026: '
            'digital crosses 60 per cent of Indian advertising expenditure. The '
            'Economic Times. Retrieved September 2026, from '
            'https://brandequity.economictimes.indiatimes.com/',

            'G2. (2026). Account-based marketing statistics. Retrieved '
            'September 2026, from '
            'https://learn.g2.com/account-based-marketing-statistics',

            'Government of India. (2023). Digital Personal Data Protection Act, '
            '2023. Ministry of Electronics and Information Technology. '
            'Retrieved September 2026, from https://www.meity.gov.in/',

            'Grand View Research. (n.d.). India digital advertising market size '
            'and outlook, 2033. Retrieved September 2026, from '
            'https://www.grandviewresearch.com/horizon/outlook/'
            'digital-advertising-market/india',

            'HubSpot. (n.d.). Account-based marketing and lead generation '
            'resources. Retrieved September 2026, from '
            'https://www.hubspot.com/',

            'IMARC Group. (n.d.). Indian advertising market size, share and '
            'growth 2034. Retrieved September 2026, from '
            'https://www.imarcgroup.com/advertising-industry-india',

            'Ipsos. (2025). The state of digital marketing in India 2025-26. '
            'Retrieved September 2026, from '
            'https://www.ipsos.com/en-in/state-digital-marketing-india-2025-26',

            'LinkedIn. (n.d.). Marketing solutions and business resources. '
            'Retrieved September 2026, from '
            'https://business.linkedin.com/marketing-solutions',

            'Livemint. (2025, August). India’s digital ad market to grow at 15% '
            'a year to hit $19 billion by 2029: Bain and Company report. '
            'Retrieved September 2026, from '
            'https://www.livemint.com/industry/advertising/',

            'Mailchimp. (n.d.). Email marketing resources and guides. Retrieved '
            'September 2026, from https://mailchimp.com/resources/',

            'Powered by Search. (2026). B2B account-based marketing statistics '
            'for 2026. Retrieved September 2026, from '
            'https://www.poweredbysearch.com/learn/b2b-abm-statistics/',

            'Salesforce. (n.d.). Account-based marketing and customer '
            'relationship management resources. Retrieved September 2026, from '
            'https://www.salesforce.com/',

            'Times of India. (2026, February). IT business to grow 6.1% in FY26 '
            'despite AI headwinds. Retrieved September 2026, from '
            'https://timesofindia.indiatimes.com/business/india-business/',

            'WPP Media. (2026, February). This Year Next Year: India '
            'advertising forecast. Retrieved September 2026, from '
            'https://www.wppmedia.com/news/wpp-media-india-tyny-report',
        ]),
    ],
}

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]
