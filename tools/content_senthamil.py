# -*- coding: utf-8 -*-
"""
Content of the Summer Internship Project report of Senthamil Selvan V
(OSI2509099), MBA (Finance), ISSM Business School, Chennai.

Internship: ACTC Studio Pvt. Ltd., Annanagar, Chennai
Role: Business Development Executive and Event Co-ordinator
Domain per the internship certificate: Event Coordination and BTL Activities
Period: 11.05.2026 to 10.07.2026 (as recorded on the internship certificate)

Block vocabulary is documented in report_content.py.
"""

STUDENT = 'SENTHAMIL SELVAN V'
REG_NO = 'OSI2509099'
FIRM = 'ACTC Studio Pvt. Ltd.'
FIRM_SHORT = 'ACTC Studio'
MENTOR = 'Ms. Arezoo Karimaghaei'
MENTOR_ROLE = 'Senior Affiliate Manager'
PERIOD = '11th May 2026 to 10th July 2026'

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
          'authentic record of Mr. Senthamil Selvan V (OSI2509099) carried out '
          'at ACTC Studio Pvt. Ltd., Chennai, in partial fulfilment of the '
          'requirements for the award of the MBA degree.'),
    ('gap', 1),
    ('p', 'The project was completed under the guidance of Ms. Arezoo '
          'Karimaghaei, Senior Affiliate Manager, ACTC Studio Pvt. Ltd., during '
          'the period from May 11th to July 10th, 2026.'),
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
    ('p', 'I, Mr. Senthamil Selvan V, hereby declare that this SIP Project '
          'Report is based on my two months internship done at ACTC Studio Pvt. '
          'Ltd., Chennai, as a Business Development Executive and Event '
          'Co-ordinator, during the period from May 11th to July 10th, 2026, '
          'under the guidance of Ms. Arezoo Karimaghaei, Senior Affiliate '
          'Manager, ACTC Studio Pvt. Ltd. and Indian School of Science and '
          'Management, Chennai.'),
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
          'empowering Founder and Managing Director, Dr. PARKAVI MAHALINGAM, '
          'for her continuous support and meaningful guidance, which played a '
          'key role in our progress.'),
    ('p', 'I am highly indebted to our Academic Head, **Dr. KAVITHA '
          'MANIKANDAN**, '
          'for her guidance and constant supervision, for providing the '
          'necessary information regarding the project and for her support in '
          'completing it.'),
    ('p', 'I would also like to thank all the faculty members and staff of ISSM '
          'Business School who provided me with the facilities and the conducive '
          'conditions that were required for this project.'),
    ('p', 'My sincere gratitude to MS. AREZOO KARIMAGHAEI, SENIOR AFFILIATE '
          'MANAGER, ACTC STUDIO PVT. LTD., for mentoring me, reviewing my work '
          'and offering immense support and knowledge throughout the internship, '
          'and to the management of ACTC Studio Pvt. Ltd. for permitting me to '
          'undergo my Summer Internship Programme with the organisation.'),
    ('p', 'I am also thankful to the members of the creative, business '
          'development, production and logistics teams, who explained their work '
          'to me, involved me in live campaigns and events, and made it possible '
          'for me to contribute to real client and event deliverables.'),
    ('pagebreak',),

    # ---- executive summary ----
    ('gap', 1),
    ('big', 'The Executive Summary', 12),
    ('gap', 1),
    ('p', 'This report presents the work carried out during my Summer '
          'Internship Programme at ACTC Studio Pvt. Ltd., a Chennai based '
          'branding, digital marketing and events agency. The internship was '
          'undertaken on-site from 11 May 2026 to 10 July 2026, a period of two '
          'months covering nine working weeks, as a Business Development '
          'Executive and Event Co-ordinator, under the guidance of Ms. Arezoo '
          'Karimaghaei, Senior Affiliate Manager. The internship certificate '
          'records the domain of work as Event Coordination and BTL Activities.'),
    ('p', 'The internship was unusual in its breadth. An agency of this kind '
          'earns its revenue from two related activities: building a brand’s '
          'presence through digital and below-the-line marketing, and delivering '
          'live events in which that brand presence is experienced directly. I '
          'worked on both sides. On the business development side I learned the '
          'fundamentals of digital, affiliate, out-of-home, point-of-sale, '
          'television and radio advertising, collected company contacts and sent '
          'partnership proposals. On the event side I worked on live concert '
          'projects, sourcing partners, designing creatives, identifying '
          'influencers and supporting production and logistics on the ground.'),
    ('p', 'The work covered seven areas. The first was marketing, affiliate and '
          'point-of-sale marketing, through which I understood how a campaign is '
          'assembled from different channels and how affiliate and point-of-sale '
          'activity supports an event. The second was influencer marketing and '
          'outreach, in which I identified and collected the data of around two '
          'hundred influencers for promotional campaigns. The third was creative '
          'design and content creation, where I designed LinkedIn creatives and '
          'event creatives using Photoshop and Canva.'),
    ('p', 'The fourth area was partnership sourcing and coordination, which took '
          'me from identifying out-of-home advertising partners to contacting '
          'hotels and restaurants in Mumbai for a concert, and sourcing '
          'refreshment and food partners for another. The fifth was event '
          'logistics and management, in which I worked alongside the production '
          'and logistics team during a concert in Chennai and saw how an event is '
          'executed under real-time conditions. The sixth was data analytics and '
          'reporting, using Google Sheets together with Social IQ for Instagram '
          'and VidIQ for YouTube to organise and interpret campaign and creator '
          'data. The seventh was event promotion and coordination, where '
          'promotional activity for a concert was driven through influencer '
          'marketing in coordination with event partners.'),
    ('p', 'The projects on which this work was performed were live concert '
          'productions, including events associated with Ilayaraja, Prabhu Deva '
          'and Thaman, together with digital marketing proposals prepared for '
          'prospective client companies. Working on live events meant that '
          'deadlines were fixed by the event date and could not be moved, which '
          'is a discipline quite different from ordinary office work.'),
    ('p', 'Professionally, the internship gave me three things a classroom '
          'cannot. First, an understanding of marketing as an operating activity '
          'rather than a theory: a campaign is contacts made, partners signed, '
          'creatives delivered and logistics arranged, each with a date attached. '
          'Second, the experience of business outreach, since sourcing partners '
          'and influencers meant approaching people who had no obligation to '
          'reply. Third, an appreciation of coordination, because an event is '
          'delivered by several teams whose work must arrive at the same time. '
          'In summary, the internship converted my MBA coursework in marketing, '
          'communication and project coordination into work I can now perform, '
          'and it clarified my interest in brand, event and influencer '
          'marketing.'),
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

        ('h2', '1.1  GLOBAL MARKETING AND EXPERIENTIAL LANDSCAPE'),
        ('p_indent', 'Marketing has changed more in the last decade than in the '
                     'several decades before it. Advertising was once a matter of '
                     'buying space and time in a small number of mass channels; '
                     'it is now a continuous activity conducted across search, '
                     'social platforms, commerce sites, creator content, '
                     'out-of-home media and live experiences, with the results of '
                     'each measured almost immediately.'),
        ('p', 'Three developments have shaped the industry globally. The first is '
              'the shift of spending to digital and, within digital, to content '
              'and commerce. The second is the rise of the creator economy, in '
              'which individuals with audiences of their own have become a media '
              'channel that brands buy in the same way they once bought '
              'television spots. The third is the return of experience: as '
              'attention online has become harder and more expensive to hold, '
              'brands have moved back towards events, activations and '
              'below-the-line work where the audience is physically present and '
              'engaged.'),
        ('p', 'The consequence for agencies is that the work has become more '
              'integrated and more operational. A single campaign may combine a '
              'social creative, a set of creator collaborations, out-of-home '
              'placements, point-of-sale material and an event, all timed to a '
              'launch date. Delivering that requires an agency to be part '
              'creative studio, part media planner, part production house and '
              'part project manager, and it requires the people inside it to move '
              'between those roles. That was precisely the character of the '
              'internship described in this report.'),

        ('h2', '1.2  THE INDIAN ADVERTISING AND EVENTS CONTEXT'),
        ('p', 'India is among the fastest growing advertising markets in the '
              'world. Advertising revenue is projected to grow by about 9.7 per '
              'cent in 2026 to approximately ₹2,01,891 crore, an incremental '
              'addition of around ₹17,844 crore over the previous year, with '
              'digital accounting for roughly 68 per cent of the total (WPP '
              'Media, 2026). Industry estimates differ on definition but agree on '
              'direction: the Pitch Madison Advertising Report places Indian '
              'advertising expenditure at about ₹1.74 lakh crore in 2026 with '
              'digital at around 64 per cent, digital spending itself rising from '
              'about ₹93,156 crore in 2025 to ₹1,11,976 crore in 2026 '
              '(Storyboard18, 2026).'),
        ('p', 'Within that total, the fastest growth is in commerce-led '
              'advertising, reported at about 24 per cent, while print grows at '
              'roughly 4.4 per cent, television at 3.1 per cent and audio at 1.5 '
              'per cent (The Hindu, 2026). The practical meaning for an agency is '
              'that budgets are moving towards channels which can be measured and '
              'towards formats which sit close to the point of purchase, without '
              'traditional channels disappearing, since out-of-home, print and '
              'point-of-sale remain important for local and event-led campaigns.'),
        ('p', 'The second relevant development is the creator economy. India’s '
              'influencer marketing sector was valued at about ₹3,000 to ₹3,500 '
              'crore in 2025 and is projected to reach ₹4,500 to ₹5,000 crore by '
              '2027, sustaining a compound annual growth rate of about 22 per '
              'cent as the sector formalises (Kofluence, 2026). The country is '
              'estimated to have around 3.5 million creators, and creators in '
              'smaller cities now account for a substantial share of campaigns '
              'while delivering higher engagement rates than metropolitan '
              'creators at much lower cost (ETBrandEquity, 2026). This explains '
              'why identifying and cataloguing influencers, which formed a '
              'significant part of my internship, has become a standing agency '
              'activity rather than an occasional one.'),
        ('p', 'The third development is the growth of live events. India’s live '
              'events market is estimated at about ₹13,000 crore and is driving a '
              'shift towards experiential marketing, with reported evidence that '
              '59 per cent of attendees recall brands they engage with on the '
              'ground and 55 per cent report higher purchase intent after such '
              'interaction (EY and BookMyShow, 2026). The wider event and '
              'exhibition market is estimated to grow from about USD 6.15 billion '
              'in 2026 to USD 9.04 billion by 2031 (Mordor Intelligence, n.d.), '
              'and live entertainment in India is growing at roughly twice the '
              'global rate (MarketsandMarkets, n.d.). Music-led events in '
              'particular have expanded quickly, with the music tourism segment '
              'projected to grow at over seventeen per cent a year (IMARC Group, '
              'n.d.).'),
        ('p', 'For an agency in Chennai, these three currents meet in a single '
              'kind of assignment: a concert or a launch that must be promoted '
              'digitally, supported by creators, advertised through out-of-home '
              'and point-of-sale media, funded partly through partnerships, and '
              'delivered physically on a fixed date. That is the environment in '
              'which this internship took place.'),

        ('h2', '1.3  COMPANY OVERVIEW: ACTC STUDIO PRIVATE LIMITED'),
        ('h3', '1.3.1  BACKGROUND AND OPERATIONS'),
        ('p', 'ACTC Studio Pvt. Ltd. is a Chennai based agency working across '
              'branding, digital marketing and events. The organisation is about '
              'five years old and employs a team in the range of eleven to fifty '
              'people, which places it among the small and medium agencies that '
              'make up the majority of the Indian agency market. It describes '
              'itself as a full-service digital marketing agency helping brands '
              'grow through data-driven work, building presence on platforms such '
              'as Instagram, Facebook and LinkedIn alongside website development '
              'and related digital services (Clutch, n.d.). Its office is located '
              'at 3rd Street, AC Block, 6th Main Road, Annanagar, Chennai '
              '600 040.'),
        ('p', 'The distinctive feature of the organisation, and the reason the '
              'internship covered such varied ground, is that it combines '
              'agency-side marketing with event delivery. Alongside digital and '
              'below-the-line campaign work for client brands, it works on live '
              'events, which brings with it partnership sourcing, on-ground '
              'production, vendor management and logistics. An intern placed in '
              'this environment therefore sees a campaign from proposal through '
              'creative and promotion to physical execution, which is rarely '
              'possible in a larger and more compartmentalised organisation.'),
        ('p', 'Operationally the work divides into two related streams. The '
              'client stream involves prospecting, proposals, retained digital '
              'marketing, creative production and reporting. The event stream '
              'involves promotion, partnership and sponsorship sourcing, '
              'influencer-led campaigns, advertising placements and on-site '
              'coordination. Both streams draw on the same creative and business '
              'development capability, and during my internship I worked across '
              'both, including digital marketing proposals for prospective '
              'clients and promotional work for concert productions.'),
        ('h3', '1.3.2  SERVICE LINES'),
        ('p', 'The organisation’s work can be grouped into the service lines set '
              'out below. The grouping reflects the assignments I observed and '
              'worked on during the internship.'),
        ('table', {'rows': [
            ['Service Line', 'Nature of Work', 'Typical Deliverable'],
            ['Branding and Creative Design',
             'Brand identity, campaign creatives and content for social and '
             'professional platforms',
             'Creative assets, LinkedIn and social posts, campaign collateral'],
            ['Digital Marketing',
             'Presence and performance work across Instagram, Facebook, LinkedIn '
             'and related platforms, with website and content support',
             'Campaign plans, proposals, content calendars, analytics reports'],
            ['Affiliate and Below-the-Line Marketing',
             'Affiliate arrangements, point-of-sale material, out-of-home and '
             'print placements supporting a campaign or event',
             'BTL plans, POS collateral, OOH and newspaper placements'],
            ['Influencer Marketing',
             'Identification of creators, outreach, collaboration and promotional '
             'campaign management',
             'Influencer databases, campaign briefs, promotional posts'],
            ['Events and Experiential',
             'Promotion, partnership sourcing, production support and on-ground '
             'logistics for live events',
             'Partner and sponsor arrangements, event promotion, on-site '
             'execution'],
        ], 'widths': [3, 5, 4]}),

        ('h2', '1.4  STRATEGIC FOCUS AND CULTURE'),
        ('p', 'For an agency of this size, competitive strength does not come '
              'from scale of media buying or from proprietary technology. It '
              'comes from three things: creative quality that a client can see, '
              'reliability in delivery, and relationships, both with clients and '
              'with the partners, venues, vendors and creators who make an event '
              'or a campaign possible. The agency’s strategy is built on being '
              'able to carry an assignment from idea to execution without '
              'handing it to third parties at every stage.'),
        ('p', 'That integration is also the source of its commercial logic. When '
              'the same team handles creative, promotion, partnerships and '
              'logistics, the client deals with one accountable organisation, '
              'and the agency is able to earn from a larger part of the '
              'assignment than a purely creative or purely digital shop would.'),
        ('h3', '1.4.1  VALUES IN PRACTICE'),
        ('bullets', [
            '**The deadline is the event date:** for live projects the timeline '
            'is fixed externally, so planning works backwards from the date and '
            'nothing is allowed to drift.',
            '**Relationships are assets:** partners, venues, vendors and '
            'creators are approached professionally and kept informed, because '
            'the next project will need them again.',
            '**Creative work serves the brief:** a design is judged by whether '
            'it communicates for the client or the event, not by how elaborate it '
            'is.',
            '**Data supports the pitch:** platform analytics are used both to '
            'plan campaigns and to demonstrate results to clients and partners.',
            '**Everybody is operational:** in a team of this size the person who '
            'designs a creative may also be on site during the event, which '
            'keeps the work grounded.',
        ]),
        ('h3', '1.4.2  WORKPLACE CULTURE'),
        ('p', 'The working culture is fast-moving and collaborative, shaped by '
              'the fact that several projects with immovable dates run at the '
              'same time. Responsibility is given early, which is how an intern '
              'comes to be contacting potential partners in another city or '
              'assembling a database of two hundred creators within weeks of '
              'joining. Instructions are brief, feedback is immediate, and the '
              'measure of work is whether it is usable.'),
        ('p', 'Within this environment my work was guided by Ms. Arezoo '
              'Karimaghaei, Senior Affiliate Manager, who allocated assignments '
              'and reviewed output, and by colleagues in the creative, business '
              'development, production and logistics teams who explained how '
              'their part of a project worked. The culture is also unusually '
              'visible: because events are delivered in public, the result of the '
              'team’s work is seen by an audience on a particular evening, which '
              'creates a shared sense of accountability.'),
        ('h3', '1.4.3  STRATEGIC POSITIONING'),
        ('p', 'The Indian agency market is crowded at the smaller end, and '
              'Chennai alone has a very large number of digital marketing and '
              'advertising agencies. Competing on price in that market is '
              'unattractive, and competing on scale against network agencies is '
              'not possible. The organisation’s position instead rests on '
              'integration and responsiveness: a client or an event promoter can '
              'obtain creative, digital, below-the-line, influencer and on-ground '
              'delivery from one team, with direct access to the people doing the '
              'work.'),
        ('p', 'Live events reinforce that position, because they are difficult to '
              'deliver and therefore harder to commoditise. An agency that can '
              'source partners, place out-of-home and point-of-sale advertising, '
              'run an influencer campaign and support production on the day has a '
              'more defensible offering than one that only produces content. From '
              'my vantage point as an intern, this was the clearest strategic '
              'lesson of the internship: the difficult, operational parts of the '
              'work are where the agency’s value lies.'),

        ('h2', '1.5  SWOT ANALYSIS'),
        ('p', 'The following analysis is my own assessment, based on what I '
              'observed of the organisation’s working during the internship, and '
              'is presented from the perspective of a small integrated agency in '
              'a competitive market.'),
        ('h3', '1.5.1  STRENGTHS'),
        ('bullets', [
            '**Integrated offering:** branding, digital marketing, below-the-line '
            'work, influencer campaigns and event delivery are available from a '
            'single team.',
            '**Event delivery capability:** experience of live concert projects, '
            'including partnerships, advertising placements, production and '
            'logistics, is a capability many digital agencies do not have.',
            '**Agility:** a team of eleven to fifty people can respond to a '
            'brief or a change of plan far more quickly than a network agency.',
            '**Partner and creator networks:** working relationships with hotels, '
            'restaurants, out-of-home vendors, media and a growing base of '
            'influencers create reusable value.',
            '**Exposure of staff to the whole process:** people work across '
            'creative, business development and execution, which builds '
            'versatility.',
        ]),
        ('h3', '1.5.2  WEAKNESSES'),
        ('bullets', [
            '**Scale limits:** a small team constrains the number of large '
            'projects that can be handled at once, particularly when event dates '
            'coincide.',
            '**Dependence on key relationships:** client and partner '
            'relationships are held by a few individuals.',
            '**Project-based revenue:** event and campaign work is lumpy, so '
            'revenue is less predictable than retained work.',
            '**Manual processes:** databases, outreach and reporting rely '
            'substantially on spreadsheets and individual follow-up.',
            '**Brand visibility:** in a market with a very large number of '
            'agencies, being known outside the existing network requires '
            'continuous outreach.',
        ]),
        ('h3', '1.5.3  OPPORTUNITIES'),
        ('bullets', [
            '**Growth in advertising spend:** Indian advertising is projected to '
            'grow by about 9.7 per cent in 2026, with digital taking the largest '
            'share.',
            '**Formalisation of influencer marketing:** a sector growing at '
            'roughly 22 per cent a year, moving from one-off collaborations to '
            'structured partnerships, favours agencies that already maintain '
            'creator databases.',
            '**Experiential demand:** brands are investing more in live events '
            'because on-ground engagement demonstrably improves recall and '
            'purchase intent.',
            '**Regional creators:** creators outside the metros deliver higher '
            'engagement at lower cost, which suits regionally focused campaigns.',
            '**Retained digital mandates:** converting project clients into '
            'retained digital marketing accounts would smooth revenue.',
        ]),
        ('h3', '1.5.4  THREATS'),
        ('bullets', [
            '**Crowded market:** a very large number of agencies in Chennai and '
            'nationally, many competing on price.',
            '**Client concentration and churn:** project-based clients can leave '
            'at the end of an assignment.',
            '**Platform dependence:** reach and measurement depend on social '
            'platforms whose algorithms and costs change without notice.',
            '**Event risk:** a live event carries weather, permission, vendor and '
            'attendance risk that can affect both delivery and margin.',
            '**Talent mobility:** creative and business development staff are '
            'mobile, and losing them means losing relationships and craft.',
        ]),

        ('h2', '1.6  KEY COMPETITORS'),
        ('p', 'The organisation competes with three different groups, each '
              'positioned differently in the market. The tables below set out the '
              'categories with representative examples.'),
        ('h3', '1.6.1  NETWORK AND NATIONAL AGENCIES'),
        ('table', {'rows': [
            ['Category', 'Offering', 'Key Focus Area'],
            ['International network agencies',
             'Integrated advertising, media planning and buying at national scale',
             'Large national and multinational brand accounts'],
            ['National digital agencies',
             'Performance marketing, social media and content at scale',
             'Retained digital mandates for larger advertisers'],
            ['National event and experiential companies',
             'Large-format events, exhibitions and brand activations',
             'Enterprise and IP-led event properties'],
        ], 'widths': [3, 4, 4]}),
        ('h3', '1.6.2  REGIONAL AND CHENNAI-BASED AGENCIES'),
        ('table', {'rows': [
            ['Category', 'Offering', 'Key Focus Area'],
            ['Established Chennai creative agencies',
             'Branding, creative and digital services with long local presence',
             'Regional brands and mid-sized businesses'],
            ['Regional digital marketing agencies',
             'Social media management, SEO, paid media and websites',
             'Local businesses and small and medium enterprises'],
            ['Local event management firms',
             'Concerts, weddings, corporate events and on-ground execution',
             'Event promoters and corporate clients'],
        ], 'widths': [3, 4, 4]}),
        ('h3', '1.6.3  SPECIALIST PLATFORMS AND FREELANCE SUPPLY'),
        ('table', {'rows': [
            ['Category', 'Offering', 'Competitive Effect'],
            ['Influencer marketing platforms',
             'Creator discovery, campaign management and measurement through '
             'technology platforms',
             'Compete for influencer campaign budgets with data-led '
             'propositions'],
            ['Freelance designers and marketers',
             'Individual creative and social media services at low cost',
             'Set a low price expectation for standalone deliverables'],
            ['In-house brand teams',
             'Marketing and content produced by the client’s own team',
             'Reduce the scope outsourced to agencies, particularly routine '
             'content'],
        ], 'widths': [3, 4, 4]}),

        ('h2', '1.7  COMPETITIVE POSITIONING'),
        ('p', 'The competitive logic of the Indian agency market is that routine '
              'deliverables are becoming cheap while integrated delivery remains '
              'difficult. A single social creative or a standalone campaign can '
              'be bought from a freelancer or produced in-house; a concert that '
              'must be promoted digitally, supported by creators, advertised '
              'through out-of-home and point-of-sale media, funded partly through '
              'partnerships and delivered on a fixed evening cannot.'),
        ('p', 'ACTC Studio positions itself in that second space. Its advantage '
              'is not scale or price but the ability to hold a whole assignment '
              'together with a small, versatile team, and to be accessible while '
              'doing so. During my internship this was visible in practice: the '
              'same organisation was preparing digital marketing proposals for '
              'prospective clients, designing creatives, sourcing hospitality and '
              'food partners in two cities, building an influencer base for '
              'promotion and putting people on site during a concert in Chennai. '
              'Very few agencies of comparable size attempt all of that, and '
              'doing it credibly is the positioning.'),

        ('h2', '1.8  KEY MILESTONES'),
        ('p', 'As a privately held agency of about five years’ standing, the '
              'organisation’s development is not documented in public sources in '
              'the way a listed company’s would be. Specific dates and figures '
              'beyond those recorded here should therefore not be stated without '
              'confirmation from the company. What can be described, from the '
              'work observed during the internship and from the organisation’s '
              'own public description, is the shape of its growth.'),
        ('p', 'The first stage was establishment as a digital marketing and '
              'creative studio, offering brand presence on social platforms, '
              'creative work and website development for client businesses '
              '(Clutch, n.d.). This is the base on which agencies of this kind '
              'are built, because retained digital and creative work provides '
              'continuity of revenue and a reason for clients to stay in contact.'),
        ('p', 'The second stage was the addition of below-the-line and '
              'out-of-home capability: affiliate arrangements, point-of-sale '
              'material, out-of-home placements and print advertising. This '
              'widened the agency from a digital studio into a campaign '
              'organisation able to work across online and offline channels, '
              'which matters in a market where television, print and out-of-home '
              'continue to carry significant weight alongside digital.'),
        ('p', 'The third and most demanding stage was the move into live events. '
              'Working on concert productions requires partnership and sponsorship '
              'sourcing, vendor management, production support and on-ground '
              'logistics, and it exposes the agency to fixed dates and public '
              'delivery. The projects I worked on during the internship, '
              'including events associated with Ilayaraja, Prabhu Deva and '
              'Thaman, belong to this stage.'),
        ('p', 'The current stage, which I observed directly, is the integration '
              'of influencer marketing into both streams. Building a database of '
              'around two hundred creators and using platform analytics to assess '
              'them is an investment in a capability that can be applied to '
              'client campaigns and event promotion alike. For a student of '
              'management, the lesson in this progression is that a small agency '
              'grows by adding capabilities that are difficult to buy elsewhere, '
              'and that each addition brings a new coordination burden with it.'),
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
                     'practical work inside a functioning agency. The internship '
                     'was carried out at ACTC Studio Pvt. Ltd., Chennai, from 11 '
                     'May 2026 to 10 July 2026 as a Business Development '
                     'Executive and Event Co-ordinator, in the domain of event '
                     'coordination and below-the-line activities, under the '
                     'guidance of Ms. Arezoo Karimaghaei, Senior Affiliate '
                     'Manager.'),
        ('p', 'The specific objectives agreed at the start of the internship were '
              'as follows:'),
        ('bullets', [
            'To understand the fundamentals of marketing across digital, '
            'affiliate, out-of-home, point-of-sale, television and radio '
            'channels.',
            'To gain practical experience of business development through '
            'collecting company contacts and sending partnership proposals.',
            'To learn how partnerships and sponsorships are sourced for live '
            'events, including hospitality, food and advertising partners.',
            'To acquire practical creative design skills for campaign and '
            'platform-specific creatives.',
            'To understand influencer marketing, including identification of '
            'creators, collection of their data and their use in promotional '
            'campaigns.',
            'To gain exposure to event production and logistics under real-time '
            'event conditions.',
            'To learn how campaign and creator data is organised, analysed and '
            'reported using spreadsheets and platform analytics tools.',
            'To develop professional communication, negotiation, coordination and '
            'follow-up skills.',
        ]),
        ('h3', '2.1.1  METHODOLOGY AND APPROACH'),
        ('p', 'The internship followed a practical, project-led approach. Each '
              'area of work began with an explanation of the objective and the '
              'context of the campaign or event concerned, followed by supervised '
              'execution and then independent work with review before anything '
              'was sent to a partner, a client or a platform.'),
        ('p', 'Because the organisation works on live projects, the method was '
              'necessarily task-driven rather than sequential. Assignments were '
              'given according to what the current events and client pitches '
              'required, which meant that creative work, outreach, data '
              'collection and on-ground coordination often ran at the same time. '
              'Work was allocated and reviewed by Ms. Arezoo Karimaghaei, Senior '
              'Affiliate Manager, and day-to-day guidance came from the creative, '
              'business development, production and logistics teams.'),

        ('h2', '2.2  INITIAL ONBOARDING AND TRAINING'),
        ('p', 'The first week was used to build a foundation in marketing before '
              'live work began. The onboarding covered:'),
        ('bullets', [
            'An introduction to the organisation, its service lines and the '
            'structure of the team.',
            'The fundamentals of marketing across channels, covering digital '
            'marketing, affiliate marketing, out-of-home advertising, '
            'point-of-sale material, television and radio.',
            'An explanation of how an event-led campaign is assembled, and how '
            'promotion, partnerships, advertising placements and logistics fit '
            'together around a fixed event date.',
            'An introduction to the agency’s approach to business development, '
            'including how prospective partners and clients are identified and '
            'approached.',
            'Familiarisation with the working tools: Google Sheets for databases '
            'and trackers, Photoshop and Canva for creative work, and Social IQ '
            'and VidIQ for Instagram and YouTube analytics.',
            'Practical training in preparing and sending partnership proposals, '
            'including the tone and structure expected in professional outreach.',
        ]),
        ('p', 'This grounding mattered because the work that followed was live. '
              'Once I understood how the channels related to one another, a '
              'request to source out-of-home partners or design a LinkedIn '
              'creative was no longer an isolated task but a recognisable part of '
              'a campaign.'),

        ('h2', '2.3  WORK PLAN AND SCOPE'),
        ('p', 'The internship covered seven areas of work. They are described '
              'below in the order in which they were principally taken up, '
              'although in practice several ran in parallel because the projects '
              'they belonged to overlapped.'),
        ('h3', '2.3.1  Marketing, Affiliate and Point-of-Sale Marketing'),
        ('bullets', [
            'Learned the fundamentals of marketing across digital, affiliate, '
            'out-of-home, point-of-sale, television and radio advertising.',
            'Collected company contacts for business development and sent '
            'partnership proposals to prospective partners.',
            'Prepared digital marketing proposals for potential client companies, '
            'setting out the approach and deliverables being offered.',
            'Understood how affiliate arrangements and point-of-sale material '
            'support a campaign at the point where the audience makes a decision.',
            'Improved my communication and business outreach skills through '
            'repeated contact with companies and partners.',
        ]),
        ('h3', '2.3.2  Influencer Marketing and Outreach'),
        ('bullets', [
            'Identified influencers suitable for the promotional campaigns being '
            'planned, across the categories and audiences relevant to the events.',
            'Collected and organised the data of around two hundred influencers, '
            'including their platforms, reach and category of content.',
            'Used Social IQ for Instagram analytics and VidIQ for YouTube '
            'analytics to assess creators rather than relying on follower counts '
            'alone.',
            'Supported promotional activity delivered through influencer '
            'marketing for a concert project, coordinating what each creator was '
            'to post and when.',
            'Learned influencer marketing strategy and improved my data '
            'collection skills through the scale of the exercise.',
        ]),
        ('h3', '2.3.3  Creative Design and Content Creation'),
        ('bullets', [
            'Designed LinkedIn creatives for a concert project, working to the '
            'conventions of a professional platform rather than a consumer one.',
            'Designed creatives for the Ilayaraja concert campaign for use in '
            'promotional activity.',
            'Used Adobe Photoshop and Canva for design work, learning when each '
            'tool was the faster route to a usable output.',
            'Learned to work to a brief and to revise a design on feedback, which '
            'improved both my creative design skills and my speed.',
        ]),
        ('h3', '2.3.4  Partnership Sourcing and Coordination'),
        ('bullets', [
            'Sourced potential out-of-home advertising partners for a concert '
            'event.',
            'Identified and contacted hotels and restaurants in Mumbai for '
            'partnership opportunities for the Prabhu Deva concert.',
            'Sourced refreshment and food partners for the Thaman concert.',
            'Maintained the contact and status records for each partner approached '
            'so that follow-up was orderly.',
            'Learned business development, negotiation and professional '
            'communication with partners, including how to present an event as an '
            'opportunity rather than a request.',
        ]),
        ('h3', '2.3.5  Event Logistics and Management'),
        ('bullets', [
            'Worked on out-of-home, point-of-sale and newspaper advertising for '
            'the Ilayaraja concert in Chennai.',
            'Assisted the production and logistics team during the event itself.',
            'Coordinated between advertising placements, promotional activity and '
            'the requirements of the production team.',
            'Understood event execution, teamwork and coordination under '
            'real-time event conditions, where a problem has to be solved within '
            'minutes rather than days.',
        ]),
        ('h3', '2.3.6  Data Analytics and Reporting'),
        ('bullets', [
            'Maintained databases and trackers in Google Sheets for company '
            'contacts, partners approached and influencers identified.',
            'Used Social IQ and VidIQ to gather engagement and audience data for '
            'creators being considered for campaigns.',
            'Organised the collected data so that it could be filtered by '
            'platform, category and reach when a campaign required it.',
            'Learned to present information in a form that allowed a decision to '
            'be taken, rather than simply recording it.',
        ]),
        ('h3', '2.3.7  Event Promotion and Coordination'),
        ('bullets', [
            'Worked on promotional activities for the Prabhu Deva concert through '
            'influencer marketing.',
            'Coordinated with event partners and with the logistics team so that '
            'promotion and delivery were aligned.',
            'Tracked what had been committed by each partner and creator and '
            'followed up on what was outstanding.',
            'Developed coordination, planning and promotional campaign management '
            'skills through work on a live event with a fixed date.',
        ]),

        ('h2', '2.4  TIMELINE OF ACTIVITIES'),
        ('p', 'The internship ran from 11 May 2026 to 10 July 2026, nine working '
              'weeks in all. The week-by-week record below is taken from the '
              'daily internship diary maintained during the programme.'),
        ('h3', 'Week 1 (11 May – 16 May 2026): Basics of Marketing'),
        ('bullets', [
            'Learned the fundamentals of marketing, including digital marketing, '
            'affiliate marketing, out-of-home, point-of-sale, television and '
            'radio advertising.',
            'Collected company contacts and sent partnership proposals.',
            'Gained knowledge of the different marketing channels and improved my '
            'communication and business outreach skills.',
        ]),
        ('h3', 'Week 2 (18 May – 23 May 2026): LinkedIn Creatives and Partnership '
               'Sourcing'),
        ('bullets', [
            'Designed LinkedIn creatives for the Ilayaraja concert.',
            'Sourced potential out-of-home advertising partners for the event.',
            'Improved my creative design skills and learned how to identify and '
            'approach marketing partners.',
        ]),
        ('h3', 'Week 3 (25 May – 30 May 2026): Partnership Sourcing, Mumbai'),
        ('bullets', [
            'Identified and contacted hotels and restaurants in Mumbai for '
            'partnership opportunities for the Prabhu Deva concert.',
            'Maintained the record of partners approached and their responses.',
            'Learned business development, negotiation and professional '
            'communication with partners.',
        ]),
        ('h3', 'Week 4 (1 June – 6 June 2026): Event Marketing, Production and '
               'Logistics'),
        ('bullets', [
            'Worked on out-of-home, point-of-sale and newspaper advertising for '
            'the Ilayaraja concert in Chennai.',
            'Assisted the production and logistics team during the event.',
            'Understood event execution, teamwork and coordination under '
            'real-time event conditions.',
        ]),
        ('h3', 'Week 5 (8 June – 13 June 2026): Refreshment and Food Partner '
               'Sourcing'),
        ('bullets', [
            'Sourced refreshment and food partners for the Thaman concert.',
            'Followed up with the partners approached and recorded their '
            'requirements.',
            'Improved my sourcing and relationship-building skills.',
        ]),
        ('h3', 'Week 6 (15 June – 20 June 2026): Creative Design and Influencer '
               'Marketing'),
        ('bullets', [
            'Designed creatives for the Ilayaraja concert campaign.',
            'Collected the data of around two hundred influencers for promotional '
            'campaigns.',
            'Learned influencer marketing strategy and enhanced my data '
            'collection skills.',
        ]),
        ('h3', 'Week 7 (22 June – 27 June 2026): Event Promotion and Logistics'),
        ('bullets', [
            'Worked on promotional activities for the Prabhu Deva concert through '
            'influencer marketing.',
            'Coordinated with event partners and the logistics team.',
            'Developed coordination, planning and promotional campaign management '
            'skills.',
        ]),
        ('h3', 'Week 8 (29 June – 4 July 2026): Digital Marketing Proposals'),
        ('bullets', [
            'Prepared digital marketing proposals for potential client companies.',
            'Presented the approach, deliverables and channels proposed for each '
            'prospective client.',
            'Improved my proposal writing, presentation and digital marketing '
            'planning skills.',
        ]),
        ('h3', 'Week 9 (6 July – 10 July 2026): Consolidation and Handover'),
        ('bullets', [
            'Consolidated the influencer database, partner contact records and '
            'campaign trackers into the formats used by the team.',
            'Completed the pending follow-ups with partners and creators and '
            'recorded their status.',
            'Handed over the working files to the team, discussed the overall '
            'learning with my guide and completed the internship formalities.',
        ]),

        ('h2', '2.5  TOOLS AND SOFTWARE USED'),
        ('h3', '2.5.1  Google Sheets'),
        ('p', 'Google Sheets was the working surface for everything that had to '
              'be recorded, tracked or shared. I used it to maintain company '
              'contact lists for business development, the status of partners '
              'approached for each event, and the database of around two hundred '
              'influencers with their platforms, categories and reach.'),
        ('p', 'Because the sheets were shared with the team, I learned that a '
              'tracker is a communication tool as much as a record: if a column '
              'is ambiguous or a status is out of date, somebody else acts on '
              'wrong information. Sorting, filtering and simple formulas turned '
              'long lists into something a colleague could use to make a decision '
              'quickly.'),
        ('h3', '2.5.2  Adobe Photoshop'),
        ('p', 'Photoshop was used for the creative work that required control '
              'over images, layers and finish, including campaign creatives for '
              'the concert projects. Working on real deliverables taught me the '
              'practical side of design that a tutorial does not: keeping files '
              'organised for revision, exporting at the sizes each placement '
              'needs, and designing so that the message survives being seen for '
              'two seconds on a phone.'),
        ('h3', '2.5.3  Canva'),
        ('p', 'Canva was used where speed mattered more than fine control, '
              'particularly for platform-specific creatives such as the LinkedIn '
              'designs. Using both tools taught me to choose according to the '
              'deadline and the deliverable rather than out of habit, which is a '
              'practical judgement in an agency working to event dates.'),
        ('h3', '2.5.4  Social IQ (Instagram Analytics)'),
        ('p', 'Social IQ was used to assess Instagram creators for promotional '
              'campaigns. It allowed me to look past follower counts to '
              'engagement and audience indicators, which is essential because a '
              'creator with a smaller but genuinely engaged audience is often the '
              'better choice for an event campaign. This changed how I evaluated '
              'the influencers I was cataloguing.'),
        ('h3', '2.5.5  VidIQ (YouTube Analytics)'),
        ('p', 'VidIQ was used for the YouTube side of creator assessment, '
              'providing channel and video performance indicators for creators '
              'being considered for promotion. Working across two platform '
              'analytics tools taught me that each platform has its own measures '
              'of performance and that a creator strong on one is not '
              'automatically strong on the other.'),

        ('h2', '2.6  APPLICATION OF ACADEMIC KNOWLEDGE'),
        ('p', 'One of the most satisfying aspects of the internship was '
              'recognising, in live campaign work, a concept that had been taught '
              'in a classroom. The main areas of application were as follows.'),
        ('h3', '2.6.1  Marketing Management'),
        ('bullets', [
            'Applied the concept of the marketing mix in practice, since an '
            'event campaign combines product, price, place and promotion in a '
            'single deliverable.',
            'Used segmentation and targeting while selecting influencers and '
            'partners appropriate to the audience of each concert.',
            'Applied the idea of an integrated marketing communication campaign '
            'while working across digital, out-of-home, point-of-sale and '
            'newspaper channels for the same event.',
        ]),
        ('h3', '2.6.2  Digital and Social Media Marketing'),
        ('bullets', [
            'Applied platform-specific practice in designing for LinkedIn as '
            'against consumer social platforms.',
            'Used engagement and audience analytics from Social IQ and VidIQ to '
            'inform creator selection rather than relying on reach alone.',
            'Applied the logic of influencer marketing, in which credibility with '
            'an audience is the asset being purchased.',
        ]),
        ('h3', '2.6.3  Business Development and Negotiation'),
        ('bullets', [
            'Applied prospecting and outreach technique while collecting company '
            'contacts and sending partnership proposals.',
            'Used the principle of mutual benefit in partnership conversations '
            'with hotels, restaurants and food partners, presenting the event as '
            'an opportunity for visibility.',
            'Practised professional follow-up and record-keeping, which is what '
            'converts an approach into an arrangement.',
        ]),
        ('h3', '2.6.4  Project and Operations Coordination'),
        ('bullets', [
            'Applied project planning concepts by working backwards from a fixed '
            'event date to the deadlines for creatives, placements and '
            'partnerships.',
            'Used coordination and dependency management while aligning '
            'promotion, partners and the logistics team.',
            'Experienced real-time operations during the event itself, where '
            'decisions had to be taken immediately and communicated at once.',
        ]),
        ('h3', '2.6.5  Financial Awareness in Campaign Work'),
        ('bullets', [
            'Understood how partnerships and sponsorships reduce the net cost of '
            'an event, which is the commercial reason the sourcing work matters.',
            'Appreciated the cost differences between channels, since out-of-home '
            'and newspaper placements carry very different costs from creator '
            'collaborations for comparable reach.',
            'Applied the principle that marketing spending is justified by the '
            'return it produces, which is why measurement and reporting form part '
            'of the work.',
        ]),
        ('h3', '2.6.6  Business Communication'),
        ('bullets', [
            'Applied written communication in partnership proposals and digital '
            'marketing proposals for prospective clients.',
            'Applied spoken and telephone communication while contacting partners '
            'in Chennai and Mumbai and coordinating with creators.',
            'Learned to adjust tone between a professional platform, a partner '
            'approach and an internal update.',
        ]),

        ('h2', '2.7  SKILLS DEVELOPED DURING THE INTERNSHIP'),
        ('p', 'The internship developed both technical and behavioural skills, '
              'and in agency work the two are inseparable, because a good idea '
              'that is not delivered on time has no value.'),
        ('h3', '2.7.1  Business Outreach'),
        ('p', 'Collecting company contacts, sending partnership proposals and '
              'approaching hotels, restaurants and advertising vendors gave me '
              'genuine practice in initiating a professional conversation with '
              'somebody who has no obligation to reply.'),
        ('h3', '2.7.2  Creative Design'),
        ('p', 'Designing LinkedIn and campaign creatives in Photoshop and Canva '
              'improved both my technical ability and my judgement about what '
              'communicates quickly.'),
        ('h3', '2.7.3  Influencer Identification and Assessment'),
        ('p', 'Building a database of around two hundred creators and assessing '
              'them with platform analytics taught me to evaluate an audience '
              'rather than a follower number.'),
        ('h3', '2.7.4  Data Organisation'),
        ('p', 'Maintaining trackers in Google Sheets that other people relied on '
              'taught me to structure information for use, not merely for '
              'storage.'),
        ('h3', '2.7.5  Coordination and Follow-Up'),
        ('p', 'Keeping partners, creators and internal teams aligned on a live '
              'project developed the habit of recording what was promised, by '
              'whom and by when, and of chasing it politely until it arrived.'),
        ('h3', '2.7.6  Working Under Fixed Deadlines'),
        ('p', 'An event date cannot move, and working towards one taught me to '
              'plan backwards, to identify what was on the critical path and to '
              'raise a problem early rather than hope it would resolve itself.'),
        ('h3', '2.7.7  Teamwork Across Functions'),
        ('p', 'Working with creative, business development, production and '
              'logistics colleagues showed me how differently each function '
              'thinks about the same event, and how to communicate across those '
              'differences.'),
        ('h3', '2.7.8  Adaptability'),
        ('p', 'Seven areas of work across several live projects had to be learned '
              'within nine weeks, and I developed the habit of noting a process '
              'immediately after it was explained so that I could repeat it '
              'unaided.'),

        ('h2', '2.8  KEY OBSERVATIONS FROM THE JOB'),
        ('p', 'The clearest observation from the internship is that marketing in '
              'practice is largely operational. The strategy for a concert '
              'campaign can be described in a paragraph; delivering it means '
              'hundreds of contacts made, creatives revised, placements booked, '
              'creators briefed and vendors coordinated, each with a date.'),
        ('p', 'A second observation is that partnerships are built on mutual '
              'benefit, not persuasion. The hotels, restaurants and food partners '
              'who responded positively did so because the event offered them '
              'visibility with an audience they wanted, and the approaches that '
              'worked were the ones that made that clear quickly.'),
        ('p', 'A third observation concerns influencer marketing. Reach is the '
              'easiest number to obtain and the least useful on its own. The '
              'creators worth including in a campaign were those whose audience '
              'matched the event and whose engagement was genuine, which is why '
              'the analytics tools mattered and why the database had to record '
              'more than follower counts.'),
        ('p', 'Finally, I observed that an event exposes the quality of '
              'coordination in public. On the day of the concert in Chennai, '
              'everything that had been planned or left unplanned in the previous '
              'weeks became visible at once, which is a powerful argument for '
              'documentation and early follow-up.'),

        ('h2', '2.9  CHALLENGES ENCOUNTERED DURING THE INTERNSHIP'),
        ('p', 'The internship also presented practical difficulties, each of '
              'which contributed to the learning.'),
        ('h3', '2.9.1  Influencer Coordination'),
        ('p', 'The most demanding challenge was coordinating with influencers. '
              'Gathering complete and accurate information from creators was '
              'difficult, because they work independently, respond at their own '
              'pace and do not always share the details a campaign needs, and '
              'passing that information on to the team in a usable form was '
              'equally difficult when it arrived in fragments. I managed it by '
              'maintaining a single structured sheet in which every creator’s '
              'status was visible, by recording exactly what was still awaited '
              'from each of them, and by following up in short, specific messages '
              'rather than general reminders. It taught me that coordination '
              'problems are usually information problems, and that the remedy is '
              'a shared record rather than more conversation.'),
        ('h3', '2.9.2  Outreach Without Response'),
        ('p', 'A large proportion of partnership approaches received no reply. '
              'Learning not to treat silence as failure, keeping a follow-up '
              'schedule and continuing to add new prospects to the list were what '
              'produced the partners who did come through.'),
        ('h3', '2.9.3  Real-Time Event Conditions'),
        ('p', 'During the concert in Chennai, decisions had to be taken '
              'immediately and communicated to several people at once. This was '
              'unlike any deadline I had met in academic work, and it taught me to '
              'stay calm, confirm instructions and report back once a task was '
              'done.'),
        ('h3', '2.9.4  Volume of Data'),
        ('p', 'Identifying and recording around two hundred influencers, with '
              'platform and engagement details for each, was a substantial '
              'exercise in sustained accuracy. Working in defined blocks and '
              'settling the structure of the sheet before filling it were what '
              'kept the data consistent.'),
        ('h3', '2.9.5  Working Across Cities and Functions'),
        ('p', 'Sourcing partners in Mumbai for an event while supporting '
              'campaigns in Chennai, and moving between creative work and '
              'business development in the same week, required constant switching '
              'of context. Keeping a written list of what each project needed '
              'from me was the only practical way to avoid losing items.'),

        ('h2', '2.10  OVERALL JOB EXPERIENCE'),
        ('p', 'Taken as a whole, the internship gave me exposure across the full '
              'width of agency work rather than depth in a single task. Learning '
              'the marketing channels, designing creatives, sourcing partners, '
              'building an influencer base, supporting an event on the ground, '
              'preparing client proposals and reporting through analytics allowed '
              'me to see how the parts of a campaign connect.'),
        ('p', 'The experience also changed my understanding of marketing as a '
              'career. Before the internship I associated marketing mainly with '
              'ideas, creativity and communication. The work showed me that it is '
              'equally a discipline of execution: lists, follow-ups, deadlines, '
              'vendor coordination and records. The creative part is real, but it '
              'sits on an operational base.'),
        ('p', 'The progression over the nine weeks was from learning the '
              'fundamentals in the first week to handling partner sourcing in '
              'another city, building a creator database and contributing to the '
              'promotion and delivery of live concerts. By the closing weeks I was '
              'preparing digital marketing proposals for prospective clients, '
              'which is client-facing work, and that gave me a realistic sense of '
              'an entry-level role in an agency.'),

        ('h2', '2.11  SUMMARY OF RESPONSIBILITIES'),
        ('p', 'The responsibilities handled during the internship are summarised '
              'below.'),
        ('table', {'rows': [
            ['S. No.', 'Area of Work', 'Major Responsibility'],
            ['1', 'Marketing Fundamentals',
             'Learning digital, affiliate, out-of-home, point-of-sale, television '
             'and radio advertising'],
            ['2', 'Business Development',
             'Collection of company contacts and despatch of partnership '
             'proposals'],
            ['3', 'Creative Design',
             'LinkedIn and campaign creatives for concert projects in Photoshop '
             'and Canva'],
            ['4', 'Partnership Sourcing',
             'Out-of-home advertising partners, hotels and restaurants in Mumbai, '
             'refreshment and food partners'],
            ['5', 'Influencer Marketing',
             'Identification and data collection of around two hundred '
             'influencers for promotional campaigns'],
            ['6', 'Event Advertising',
             'Out-of-home, point-of-sale and newspaper advertising for the '
             'Ilayaraja concert in Chennai'],
            ['7', 'Event Logistics',
             'Support to the production and logistics team during the event'],
            ['8', 'Event Promotion',
             'Promotional activity for the Prabhu Deva concert through influencer '
             'marketing'],
            ['9', 'Data and Analytics',
             'Trackers in Google Sheets with Social IQ and VidIQ analytics for '
             'creator assessment'],
            ['10', 'Client Proposals',
             'Digital marketing proposals prepared for prospective client '
             'companies'],
        ], 'widths': [1, 3, 6], 'col_bold': [True, True, False],
            'col_align': ['center', 'left', 'left']}),
        ('p', 'These responsibilities provided exposure to several connected '
              'activities and made the relationship between promotion, '
              'partnerships and delivery visible.'),

        ('h2', '2.12  CONCLUSION OF JOB / TASK DESCRIPTION'),
        ('p', 'The work described in this chapter covered the full sequence of an '
              'event-led marketing assignment: understanding the channels '
              'available, generating prospects and partners, producing creatives, '
              'building and briefing an influencer base, placing advertising, '
              'supporting delivery on the day and reporting on what was done.'),
        ('p', 'It also allowed me to apply concepts from marketing management, '
              'digital and social media marketing, business development, project '
              'coordination and business communication to live projects, and to '
              'learn the tools on which agency work depends. The tasks were '
              'varied in form but consistent in their demand, since every one of '
              'them was tied to an event date or a client deadline.'),
        ('p', 'Most importantly, the chapter reflects a progression. The work I '
              'was given in the first week was foundational and closely '
              'supervised; by the closing weeks I was sourcing partners in '
              'another city, assessing creators with analytics tools and '
              'preparing proposals intended for prospective clients. That '
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
        ('p', 'This chapter is an assessment of how I performed during the '
              'internship. It is based on the work actually allotted to me, the '
              'feedback received from my guide and colleagues, and my own record '
              'of what I found straightforward and what I found difficult.'),

        ('h2', '3.1  QUALITY OF WORK'),
        ('p_indent', 'In an agency the quality of an intern’s work is judged by a '
                     'simple test: whether the output can be used. A creative '
                     'either goes out or is redone, a partner list either produces '
                     'conversations or does not, and an influencer database is '
                     'either complete enough to brief a campaign from or it is '
                     'not. By that test my work improved substantially over the '
                     'nine weeks.'),
        ('bullets', [
            'LinkedIn and campaign creatives were designed to brief and revised on '
            'feedback until they were fit for use in the concert campaigns.',
            'Company contacts were collected and partnership proposals sent, with '
            'the status of each approach recorded for follow-up.',
            'Hotels, restaurants and food partners were identified and contacted '
            'for the Prabhu Deva and Thaman concerts, and their responses '
            'documented.',
            'Out-of-home, point-of-sale and newspaper advertising for the '
            'Ilayaraja concert was worked on alongside the team and delivered in '
            'time for the event.',
            'A database of around two hundred influencers was built with platform, '
            'category and engagement details sufficient to support campaign '
            'selection.',
            'Digital marketing proposals were prepared for prospective client '
            'companies in a form suitable for presentation.',
        ]),
        ('p', 'In the early weeks my output required correction, mostly because I '
              'recorded information without structuring it for other people to '
              'use, and because my first creatives carried more detail than a '
              'viewer would absorb. Once I learned to settle the structure of a '
              'tracker before filling it, and to design for a two-second read, '
              'the work needed far less revision. The internship taught me that '
              'quality in agency work means usable, on time and complete, in that '
              'order.'),

        ('h2', '3.2  TIMELINESS AND TASK OWNERSHIP'),
        ('p', 'Event work has no flexible deadlines. An advertisement placed after '
              'the concert has no value, and a creative delivered late is simply '
              'not used. I completed the tasks allotted to me within the time '
              'available and reported the status of pending items so that my guide '
              'was never uncertain about where a project stood.'),
        ('bullets', [
            'Planned backwards from the event date for creatives, placements and '
            'partner confirmations.',
            'Followed up repeatedly with partners and influencers rather than '
            'allowing an unanswered approach to lapse.',
            'Kept the contact, partner and influencer trackers current so that the '
            'team could act on them without asking me.',
            'Was present and available during the event in Chennai, when '
            'availability itself is part of ownership.',
            'Raised difficulties early, particularly on influencer coordination, '
            'instead of reporting them after they had affected a deadline.',
        ]),
        ('p', 'Task ownership developed over the period. Early on I treated an '
              'assignment as complete when I had done my part of it; by the end I '
              'treated it as complete only when the information was in the shared '
              'file, the outstanding items were listed and somebody else could '
              'continue from where I had stopped.'),

        ('h2', '3.3  ADAPTABILITY AND LEARNING CURVE'),
        ('p', 'The internship required adaptation on several fronts at once: a new '
              'industry, five new tools, a role that combined business development '
              'with event coordination, and projects whose requirements changed as '
              'event dates approached. The steepest part of the curve was the '
              'first fortnight, in which I learned the marketing channels and '
              'immediately began outreach and creative work on live projects.'),
        ('bullets', [
            'Learned the fundamentals of digital, affiliate, out-of-home, '
            'point-of-sale, television and radio advertising in the first week and '
            'applied them from the second.',
            'Picked up Photoshop and Canva to the point of producing usable '
            'campaign creatives.',
            'Learned to use Social IQ and VidIQ to assess creators on engagement '
            'rather than reach.',
            'Moved from supervised outreach to contacting partners in another city '
            'independently.',
            'Adjusted to switching between creative work, outreach, data '
            'collection and on-ground coordination within the same week.',
            'Accepted feedback on creatives and trackers and applied it to the '
            'next piece of work.',
        ]),
        ('p', 'What made the adaptation possible was the agency’s practice of '
              'explaining a task in the context of the campaign it belonged to, '
              'together with the habit I formed of writing down a process '
              'immediately after it was explained. Those notes were what I relied '
              'on when a similar task came round for the next event.'),

        ('h2', '3.4  COMMUNICATION AND COLLABORATION'),
        ('p', 'This internship involved more external communication than most, '
              'because a large part of the work consisted of approaching people '
              'outside the organisation and persuading them to respond.'),
        ('bullets', [
            '**Partner outreach:** contacted companies, out-of-home vendors, '
            'hotels, restaurants and food partners in Chennai and Mumbai, '
            'presenting each event as an opportunity rather than a request.',
            '**Influencer coordination:** communicated with creators to obtain '
            'their details and to brief promotional activity, which required '
            'patience and repeated, specific follow-up.',
            '**Internal coordination:** worked with the creative, business '
            'development, production and logistics teams, each of which needed '
            'different information about the same event.',
            '**Written communication:** prepared partnership proposals and '
            'digital marketing proposals, and learned to adjust tone between a '
            'professional platform, a partner approach and an internal update.',
            '**Response to feedback:** took correction on creatives and on the '
            'structure of trackers as instruction, which improved the usability of '
            'my output.',
        ]),
        ('p', 'The specific lesson I take from this is that in agency work '
              'communication is the product as much as the medium. A campaign '
              'exists because somebody explained it convincingly to a partner, a '
              'creator and a client, and doing that repeatedly, without becoming '
              'discouraged by silence, is the skill the role demanded.'),

        ('h2', '3.5  STRENGTHS DEMONSTRATED'),
        ('bullets', [
            '**Initiative in outreach:** approached a large number of companies, '
            'vendors and partners, including in another city, without waiting to '
            'be prompted.',
            '**Creative ability:** produced LinkedIn and campaign creatives that '
            'were used in live concert promotion.',
            '**Persistence:** continued following up with partners and creators '
            'through repeated non-response, which is what produced results.',
            '**Organisation:** maintained trackers and a two-hundred-entry '
            'influencer database that colleagues could use directly.',
            '**Versatility:** moved between creative design, business '
            'development, data work and on-ground event support as required.',
            '**Reliability under event conditions:** was available and useful '
            'during the concert in Chennai, when the work is least predictable.',
        ]),

        ('h2', '3.6  AREAS FOR IMPROVEMENT'),
        ('bullets', [
            '**Influencer negotiation:** I became competent at identifying and '
            'cataloguing creators, but negotiating deliverables and timelines with '
            'them is a skill I need to develop further.',
            '**Design depth:** my Photoshop work improved, but advanced technique '
            'and a stronger sense of typography and layout would raise the quality '
            'of my creatives.',
            '**Analytics interpretation:** I can extract platform metrics, but '
            'drawing firmer conclusions from them, including campaign performance '
            'measurement after the event, needs more practice.',
            '**Proposal writing:** my digital marketing proposals were accepted, '
            'yet I would like to structure a commercial argument more '
            'persuasively, including pricing rationale.',
            '**Time management across projects:** running outreach, creative work '
            'and data collection at once was demanding, and I need better personal '
            'systems for prioritising between concurrent projects.',
            '**Financial detail of campaigns:** as an MBA (Finance) student I '
            'would like a firmer grasp of event budgeting, channel costing and '
            'return measurement, which would let me contribute to commercial '
            'decisions rather than only to execution.',
        ]),

        ('h2', '3.7  OVERALL PERFORMANCE'),
        ('p', 'Overall, I consider the internship to have been performed to the '
              'standard the agency expected, and in the closing weeks beyond it. '
              'Work on marketing fundamentals, creative design, partnership '
              'sourcing, influencer identification, event advertising, on-ground '
              'logistics, promotional coordination and client proposals was '
              'completed and used. The internship certificate records that I was '
              'actively involved in the end-to-end planning and execution of '
              'promotional campaigns, excelled in event coordination, showed '
              'organisational and vendor management ability, played a pivotal role '
              'in event marketing and assisted in developing below-the-line '
              'marketing strategies, which is consistent with my own assessment.'),
        ('p', 'The clearest evidence of progress is the change in the nature of '
              'the work given to me. In the first week it was learning and '
              'contact collection; by the eighth it was preparing proposals '
              'intended for prospective clients and coordinating promotional '
              'activity for a concert. Work moved from supervised to independent '
              'within nine weeks.'),
        ('p', 'Where I fell short was in negotiation, design depth, analytics '
              'interpretation and the financial side of campaign planning, and '
              'each is addressed in the previous section. Taken together, the '
              'performance gave me a realistic picture of what an agency expects: '
              'usable output delivered on time, persistence in outreach, accurate '
              'shared records and willingness to be wherever the project needs '
              'you on the day.'),
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
            '**Marketing channels:** working knowledge of digital, affiliate, '
            'out-of-home, point-of-sale, television and radio advertising and of '
            'the role each plays in an event-led campaign.',
            '**Business development:** the ability to build a contact list, '
            'prepare and send a partnership proposal and manage the follow-up that '
            'turns an approach into an arrangement.',
            '**Partnership sourcing:** practical experience of identifying and '
            'approaching out-of-home vendors, hotels, restaurants and food '
            'partners, including in another city.',
            '**Creative design:** the ability to produce platform-specific '
            'creatives in Photoshop and Canva and to revise them to a brief.',
            '**Influencer marketing:** the ability to identify creators, build a '
            'structured database of around two hundred of them and assess them on '
            'engagement using Social IQ and VidIQ.',
            '**Event marketing and logistics:** exposure to advertising '
            'placements, production support and on-ground coordination for a live '
            'concert.',
            '**Analytics and reporting:** the ability to maintain trackers in '
            'Google Sheets and to organise campaign and creator data so that a '
            'decision can be taken from it.',
            '**Proposal preparation:** experience of preparing digital marketing '
            'proposals for prospective client companies.',
        ]),

        ('h2', '4.2  PRACTICAL EXPOSURE TO BUSINESS PROCESSES'),
        ('p', 'The internship gave me a working map of how an agency operates '
              'that I did not have before. I now understand, from having worked '
              'on it, how an assignment moves from a prospect or an event brief, '
              'through proposal, creative production, partnership sourcing, '
              'promotion and advertising placement, to delivery and reporting.'),
        ('p', 'More importantly, I understood the commercial architecture behind '
              'it. Partnerships and sponsorships reduce the net cost of an event, '
              'which is why sourcing them is treated so seriously. Influencer '
              'collaborations buy credibility with a specific audience at a lower '
              'cost per unit of attention than mass media. Out-of-home, '
              'point-of-sale and newspaper placements buy visibility in the '
              'physical area around an event. Each channel has a cost and a '
              'purpose, and the campaign plan is a set of choices among them. '
              'Once I saw the campaign as a portfolio of channel decisions rather '
              'than a list of tasks, the reasoning behind my assignments became '
              'clear.'),

        ('h2', '4.3  IMPROVEMENT IN ANALYTICAL AND SYSTEM THINKING'),
        ('p', 'Analytically, the biggest change was learning to look past the '
              'obvious number. A creator with a large following is not necessarily '
              'a good fit for a concert campaign; engagement, audience composition '
              'and content category matter more, and the analytics tools existed '
              'precisely to make that judgement possible. The same principle '
              'applied to outreach, where the number of approaches made mattered '
              'less than the quality of the fit between the event and the partner.'),
        ('p', 'In terms of systems thinking, the internship showed me how '
              'dependencies run through an event. A creative cannot be placed '
              'until the placement is booked; a placement cannot be booked until '
              'the partner confirms; a creator cannot post until the creative and '
              'the brief reach them. One late link delays everything behind it, '
              'which is why shared trackers and early follow-up matter so much. '
              'Seeing those chains changed how carefully I treated work that '
              'looked administrative in isolation.'),

        ('h2', '4.4  SOFT SKILLS AND PROFESSIONAL TRAITS STRENGTHENED'),
        ('bullets', [
            '**Professional outreach:** approaching strangers on behalf of an '
            'organisation, clearly and courteously, by message and by telephone.',
            '**Persistence:** continuing after non-response without becoming '
            'discouraged or discourteous.',
            '**Coordination:** keeping partners, creators and internal teams '
            'aligned through written records rather than memory.',
            '**Working under fixed deadlines:** accepting that an event date is '
            'immovable and planning accordingly.',
            '**Teamwork across functions:** communicating usefully with creative, '
            'business development, production and logistics colleagues.',
            '**Composure:** staying calm and useful during live event conditions.',
            '**Receptiveness to feedback:** treating revision of a creative or a '
            'tracker as instruction rather than criticism.',
        ]),

        ('h2', '4.5  ALIGNMENT WITH ACADEMIC LEARNING'),
        ('p', 'The internship served as a practical extension of the subjects '
              'studied in the MBA programme. The table below maps each subject to '
              'the work in which it was applied.'),
        ('table', {'rows': [
            ['Academic Subject', 'Internship Application'],
            ['Marketing Management',
             'Channel selection across digital, affiliate, OOH, POS, television '
             'and radio for event-led campaigns'],
            ['Digital and Social Media Marketing',
             'Platform-specific creatives, influencer campaigns and analytics '
             'through Social IQ and VidIQ'],
            ['Consumer Behaviour',
             'Selection of creators and partners according to the audience of '
             'each concert'],
            ['Business Development and Negotiation',
             'Contact collection, partnership proposals and negotiation with '
             'hotels, restaurants and vendors'],
            ['Project and Operations Management',
             'Backward planning from event dates, dependency management and '
             'on-ground logistics support'],
            ['Financial Management',
             'Appreciation of event budgets, channel costs and the way '
             'partnerships reduce net event cost'],
            ['Business Communication',
             'Proposals, partner outreach, creator briefs and internal status '
             'reporting'],
        ], 'widths': [3, 6], 'col_bold': [True, False],
            'col_align': ['center', 'left'], 'row_height': 500}),
        ('p', 'The internship also exposed the limits of purely academic '
              'preparation. Coursework teaches the logic of a marketing campaign '
              'once the resources are assumed to exist; practice required me to '
              'create those resources by finding partners, persuading creators and '
              'producing the material myself. That gap between planning a campaign '
              'and assembling one is, in my view, the real content of an '
              'internship.'),

        ('h2', '4.6  OVERALL REALISATIONS'),
        ('bullets', [
            'Marketing is an operational discipline; the strategy is the short '
            'part and the execution is the long one.',
            'Partnerships succeed on mutual benefit, and the fastest way to a '
            'yes is to make the benefit obvious.',
            'Reach is the least useful metric on its own, and engagement with the '
            'right audience is what a campaign actually buys.',
            'A shared, structured record is worth more than any amount of '
            'conversation when several people depend on the same information.',
            'An event date is a hard constraint, and planning backwards from it is '
            'the only workable method.',
            'Non-response is normal in outreach, so volume and persistence are '
            'part of the technique rather than signs of failure.',
            'A small agency is an outstanding place to learn, because exposure is '
            'broad and responsibility arrives early.',
        ]),

        ('h2', '4.7  PROFESSIONAL INSIGHTS AND LEARNINGS'),
        ('p', 'Three insights from the internship will stay with me beyond the '
              'technical content.'),
        ('p', 'The first concerns the nature of agency work. An agency sells '
              'capability and reliability rather than a product, and its '
              'reputation is rebuilt on every project. That is why deadlines are '
              'treated as absolute and why the quality of coordination matters as '
              'much as the quality of ideas. Seeing a concert delivered in public '
              'made this vivid in a way no classroom case could.'),
        ('p', 'The second concerns learning inside an organisation. I learned most '
              'of what I know now by being given real work early, attempting it '
              'and having it corrected. My guide’s feedback on creatives and '
              'trackers told me precisely where my judgement was weak, and being '
              'willing to be corrected turned out to be the most efficient '
              'learning strategy available.'),
        ('p', 'The third concerns my own career direction. Before the internship '
              'my interest was general. Having worked across outreach, creative '
              'production, influencer marketing and event delivery, I now know '
              'that I am drawn to brand, event and influencer marketing, and '
              'particularly to the commercial side of it where partnerships, '
              'budgets and returns are decided. As an MBA (Finance) student I also '
              'see the value of combining that commercial understanding with the '
              'marketing experience I have gained, and I know the gaps I need to '
              'close to do so.'),
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
        ('p_indent', 'The Summer Internship Programme was carried out at ACTC '
                     'Studio Pvt. Ltd., Chennai, on-site, from 11 May 2026 to 10 '
                     'July 2026, as a Business Development Executive and Event '
                     'Co-ordinator in the domain of event coordination and '
                     'below-the-line activities, under the guidance of Ms. Arezoo '
                     'Karimaghaei, Senior Affiliate Manager. The nine-week '
                     'programme covered both agency-side marketing and live event '
                     'delivery.'),
        ('p', 'The internship began with the fundamentals of marketing across '
              'digital, affiliate, out-of-home, point-of-sale, television and '
              'radio channels, together with the collection of company contacts '
              'and the despatch of partnership proposals. It then moved into '
              'creative work, with LinkedIn creatives designed for a concert '
              'project and out-of-home advertising partners sourced for the same '
              'event.'),
        ('p', 'The middle weeks were devoted to partnerships and event delivery. '
              'I identified and contacted hotels and restaurants in Mumbai for '
              'partnership opportunities for the Prabhu Deva concert, worked on '
              'out-of-home, point-of-sale and newspaper advertising for the '
              'Ilayaraja concert in Chennai and assisted the production and '
              'logistics team during that event, and sourced refreshment and food '
              'partners for the Thaman concert.'),
        ('p', 'The later weeks concentrated on influencer marketing and '
              'promotion. I designed further campaign creatives, identified and '
              'collected the data of around two hundred influencers for '
              'promotional campaigns, and worked on promotional activity for the '
              'Prabhu Deva concert through influencer marketing in coordination '
              'with event partners and the logistics team. In the closing phase I '
              'prepared digital marketing proposals for potential client '
              'companies and consolidated the influencer, partner and campaign '
              'records for handover.'),
        ('p', 'The work was carried out using Google Sheets for databases and '
              'trackers, Adobe Photoshop and Canva for creative design, and '
              'Social IQ and VidIQ for Instagram and YouTube analytics.'),

        ('h2', '5.2  KEY TAKEAWAYS'),
        ('h3', '5.2.1  Understanding of Integrated Marketing'),
        ('bullets', [
            'Learned how digital, affiliate, out-of-home, point-of-sale and print '
            'channels combine in a single event-led campaign.',
            'Understood that each channel carries a different cost and serves a '
            'different purpose in the plan.',
            'Saw how promotion, partnerships and delivery have to be aligned '
            'around one fixed date.',
        ]),
        ('h3', '5.2.2  Business Development and Partnerships'),
        ('bullets', [
            'Gained real experience of contact building, proposal despatch and '
            'follow-up.',
            'Learned that partnerships are agreed on mutual benefit and that the '
            'benefit must be made obvious quickly.',
            'Understood how partnerships and sponsorships improve the economics '
            'of an event.',
        ]),
        ('h3', '5.2.3  Influencer Marketing'),
        ('bullets', [
            'Built a structured database of around two hundred creators for '
            'promotional campaigns.',
            'Learned to assess creators on engagement and audience fit using '
            'Social IQ and VidIQ rather than on follower counts.',
            'Experienced the coordination that influencer-led promotion requires, '
            'which was the most demanding part of the internship.',
        ]),
        ('h3', '5.2.4  Creative and Content Skills'),
        ('bullets', [
            'Developed practical design ability in Photoshop and Canva on live '
            'campaign deliverables.',
            'Learned to design for the platform and for a very short read.',
            'Learned to work to a brief and to revise quickly on feedback.',
        ]),
        ('h3', '5.2.5  Event Execution and Coordination'),
        ('bullets', [
            'Experienced event execution under real-time conditions alongside the '
            'production and logistics team.',
            'Learned to plan backwards from an event date and to identify what '
            'sits on the critical path.',
            'Developed the habit of recording commitments and chasing them before '
            'they became urgent.',
        ]),
        ('h3', '5.2.6  Professional Discipline'),
        ('bullets', [
            'Learned to maintain shared records that colleagues could rely on '
            'without asking.',
            'Developed persistence in outreach and composure under event '
            'pressure.',
            'Became comfortable moving between creative, commercial and '
            'operational work in the same week.',
        ]),

        ('h2', '5.3  CONCLUSION'),
        ('p', 'The internship at ACTC Studio Pvt. Ltd. was the point at which my '
              'study of management became practical. Over nine weeks I moved from '
              'learning the marketing channels to sourcing partners in another '
              'city, designing creatives used in live campaigns, building an '
              'influencer base of around two hundred creators, supporting a '
              'concert on the ground and preparing digital marketing proposals '
              'for prospective clients. In doing so I acquired skills that are '
              'directly employable: business outreach, partnership sourcing, '
              'creative design, influencer identification and assessment, event '
              'coordination and campaign reporting.'),
        ('p', 'Beyond the technical content, three things changed. First, my '
              'understanding of marketing: it is an operational discipline in '
              'which execution, records and follow-up decide whether a good idea '
              'ever reaches an audience. Second, my understanding of commercial '
              'relationships: partners, creators and clients all respond to clear '
              'mutual benefit, and building those relationships is a skill in '
              'itself. Third, my understanding of myself. I learned that I work '
              'well under a fixed deadline, that I can keep approaching people '
              'after repeated silence, and that I enjoy work which ends in '
              'something visible.'),
        ('p', 'I am also clear about what remains to be developed: negotiation '
              'with creators, depth in design, interpretation of campaign '
              'analytics, persuasive proposal writing and the financial side of '
              'event and campaign planning. Knowing these gaps precisely, rather '
              'than in general terms, is itself an outcome of the internship.'),
        ('p', 'In conclusion, the internship achieved what a Summer Internship '
              'Programme is intended to achieve. It connected the MBA curriculum '
              'to live professional work, it gave me the tools and habits used in '
              'an agency that combines branding, digital marketing and events, '
              'and it settled my career direction towards brand, event and '
              'influencer marketing with a commercial focus. I am grateful to the '
              'management of ACTC Studio Pvt. Ltd. for the opportunity, to Ms. '
              'Arezoo Karimaghaei for her supervision and guidance, and to the '
              'creative, business development, production and logistics teams for '
              'their support, and I leave the organisation with both the '
              'competence and the confidence to contribute to a professional '
              'marketing team.'),
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
            'Adobe. (n.d.). Adobe Photoshop. Retrieved September 2026, from '
            'https://www.adobe.com/products/photoshop.html',

            'Canva. (n.d.). Canva design platform. Retrieved September 2026, from '
            'https://www.canva.com/',

            'Clutch. (n.d.). ACTC Studio Pvt. Ltd.: Services and company '
            'information. Retrieved September 2026, from '
            'https://clutch.co/profile/actc-studio',

            'ETBrandEquity. (2026). Brands move beyond follower counts to build '
            'smarter creator partnerships. The Economic Times. Retrieved '
            'September 2026, from '
            'https://brandequity.economictimes.indiatimes.com/',

            'EY and BookMyShow. (2026, March). India’s ₹13,000 crore live events '
            'market fuels shift to experiential marketing. Retrieved September '
            '2026, from https://www.ey.com/en_in/newsroom/2026/03/',

            'IMARC Group. (n.d.). India music tourism market size, trends and '
            'forecast. Retrieved September 2026, from '
            'https://www.imarcgroup.com/india-music-tourism-market',

            'Kofluence. (2026). India influencer marketing report 2026. Reported '
            'in ETBrandEquity. Retrieved September 2026, from '
            'https://brandequity.economictimes.indiatimes.com/',

            'MarketsandMarkets. (n.d.). India live entertainment market size, '
            'share and growth analysis. Retrieved September 2026, from '
            'https://www.marketsandmarkets.com/Market-Reports/geography/'
            'live-entertainment-market/India',

            'Mordor Intelligence. (n.d.). India event and exhibition market size '
            'and trend analysis, 2031. Retrieved September 2026, from '
            'https://www.mordorintelligence.com/industry-reports/'
            'event-and-exhibition-market-india',

            'Storyboard18. (2026, February). Madison World projects India AdEx at '
            '₹1.74 lakh crore in 2026; digital to command 64% share. Retrieved '
            'September 2026, from https://www.storyboard18.com/advertising/',

            'The Hindu. (2026, February). Ad revenue projected to grow 9.7% in '
            '2026 to ₹2,01,891 crore: WPP Media report. Retrieved September 2026, '
            'from https://www.thehindu.com/business/',

            'VidIQ. (n.d.). YouTube analytics and channel optimisation. Retrieved '
            'September 2026, from https://vidiq.com/',

            'WPP Media. (2026, February 18). This Year Next Year: India '
            'advertising forecast. Retrieved September 2026, from '
            'https://www.wppmedia.com/news/wpp-media-india-tyny-report',
        ]),
    ],
}

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]
