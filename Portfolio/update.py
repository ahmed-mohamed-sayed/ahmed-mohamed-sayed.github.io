import re

with open('d:/Portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CHANGE 1
content = content.replace('<meta name="description" content="Ahmed Mohamed - Business Analyst, Business Intelligence, Data Analytics, and Enterprise Data. Turning Business Challenges into Data-Driven Decisions.">', '<meta name="description" content="Ahmed Mohamed Sayed — Senior Business Analyst specializing in Business Intelligence, Financial Analytics, and Digital Transformation. Turning business challenges into data-driven decisions across fintech and financial services.">')
content = content.replace('<title>Ahmed Mohamed | Business Analytics</title>', '<title>Ahmed Mohamed Sayed | Business Analytics Playbook</title>')
content = content.replace('>Ahmed Mohamed</p>', '>Ahmed Mohamed Sayed</p>')
content = content.replace('&copy; 2026 Ahmed Mohamed.', '&copy; 2026 Ahmed Mohamed Sayed.')

# CHANGE 2
old_svg = '''          <svg viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; opacity: 0.8;">
            <!-- Simple diagram nodes -->
            <rect x="150" y="20" width="100" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="45" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Business Problem</text>
            
            <line x1="200" y1="60" x2="200" y2="100" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <rect x="150" y="100" width="100" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="125" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Business Analysis</text>
            
            <line x1="200" y1="140" x2="200" y2="180" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <rect x="150" y="180" width="100" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="205" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Data Modeling</text>
            
            <line x1="200" y1="220" x2="200" y2="260" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <rect x="150" y="260" width="100" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--accent-primary)" stroke-width="2"/>
            <text x="200" y="285" fill="var(--accent-primary)" font-size="12" text-anchor="middle" font-weight="bold" font-family="var(--font-body)">Analytics</text>
            
            <line x1="200" y1="300" x2="200" y2="340" stroke="var(--accent-primary)" stroke-width="2"/>
            
            <rect x="130" y="340" width="140" height="40" rx="8" fill="var(--accent-primary)"/>
            <text x="200" y="365" fill="var(--bg-main)" font-size="12" text-anchor="middle" font-weight="bold" font-family="var(--font-body)">Business Decisions</text>
          </svg>'''

new_svg = '''          <svg viewBox="0 0 400 740" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; opacity: 0.8;">
            <!-- Node 1 -->
            <rect x="130" y="20" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="45" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Business Problem</text>
            <line x1="200" y1="60" x2="200" y2="100" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 2 -->
            <rect x="130" y="100" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="125" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Requirements Gathering</text>
            <line x1="200" y1="140" x2="200" y2="180" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 3 -->
            <rect x="130" y="180" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="205" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Business Analysis</text>
            <line x1="200" y1="220" x2="200" y2="260" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 4 -->
            <rect x="130" y="260" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="285" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Data Acquisition</text>
            <line x1="200" y1="300" x2="200" y2="340" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 5 -->
            <rect x="130" y="340" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="365" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Data Modeling</text>
            <line x1="200" y1="380" x2="200" y2="420" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 6 -->
            <rect x="130" y="420" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="445" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Data Validation</text>
            <line x1="200" y1="460" x2="200" y2="500" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 7 -->
            <rect x="130" y="500" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="525" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Dashboard Development</text>
            <line x1="200" y1="540" x2="200" y2="580" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 8 -->
            <rect x="130" y="580" width="140" height="40" rx="8" fill="var(--bg-surface)" stroke="var(--border-color)" stroke-width="2"/>
            <text x="200" y="605" fill="var(--text-secondary)" font-size="12" text-anchor="middle" font-family="var(--font-body)">Business Insights</text>
            <line x1="200" y1="620" x2="200" y2="660" stroke="var(--accent-primary)" stroke-width="2" stroke-dasharray="4"/>
            
            <!-- Node 9 -->
            <rect x="130" y="660" width="140" height="40" rx="8" fill="var(--accent-primary)"/>
            <text x="200" y="685" fill="var(--bg-main)" font-size="12" text-anchor="middle" font-weight="bold" font-family="var(--font-body)">Decision Support</text>
          </svg>'''
content = content.replace(old_svg, new_svg)

# CHANGE 3
content = content.replace('<div class="stat-label">Years Experience</div>', '<div class="stat-label">Years Experience</div>\n          <p class="stat-description" style="font-size: var(--text-sm); color: var(--text-secondary); margin-top: var(--spacing-2);">Spanning financial accounting, data analysis, BI, and enterprise data architecture.</p>')
content = content.replace('<div class="stat-label">Years Finance & Accounting</div>', '<div class="stat-label">Years Finance & Accounting</div>\n          <p class="stat-description" style="font-size: var(--text-sm); color: var(--text-secondary); margin-top: var(--spacing-2);">I understand financial KPIs from their source — not from a textbook. This lets me design analytics that finance stakeholders actually trust.</p>')
content = content.replace('<div class="stat-label">Years Analytics & Enterprise Data</div>', '<div class="stat-label">Years Analytics & Enterprise Data</div>\n          <p class="stat-description" style="font-size: var(--text-sm); color: var(--text-secondary); margin-top: var(--spacing-2);">End-to-end ownership from business requirements through data modeling, dashboard delivery, and decision support — without depending on multiple teams.</p>')

# CHANGE 4
content = content.replace('<span class="timeline-date">Accounting & Finance</span>', '<span class="timeline-date">2007 – 2019</span>')
content = content.replace('<p>Learned the language of business. Understanding how financial transactions flow into reporting and impact the bottom line.</p>', '<p>Learned the language of business. Understanding how financial transactions flow into reporting and impact the bottom line.</p>\n            <span class="timeline-company" style="display: block; font-size: var(--text-sm); color: var(--accent-primary); margin-top: var(--spacing-2); font-style: italic;">Branch Accountant → Accounting Manager | EGL & Trust Trans</span>')

content = content.replace('<span class="timeline-date">Financial Analysis</span>', '<span class="timeline-date">2019 – 2020</span>')
content = content.replace('<p>Shifted from backward-looking reporting to forward-looking analysis. Created business value through variance analysis and budgeting.</p>', '<p>Shifted from backward-looking reporting to forward-looking analysis. Created business value through variance analysis and budgeting.</p>\n            <span class="timeline-company" style="display: block; font-size: var(--text-sm); color: var(--accent-primary); margin-top: var(--spacing-2); font-style: italic;">Data Analyst | SmartLab Egypt</span>')

content = content.replace('<span class="timeline-date">Business Intelligence</span>', '<span class="timeline-date">2020 – 2023</span>')
content = content.replace('<p>Automated financial and operational reporting. Designed interactive dashboards for executive decision support.</p>', '<p>Automated financial and operational reporting. Designed interactive dashboards for executive decision support.</p>\n            <span class="timeline-company" style="display: block; font-size: var(--text-sm); color: var(--accent-primary); margin-top: var(--spacing-2); font-style: italic;">Data Analyst — BI | CIT VeriCash</span>')

content = content.replace('<span class="timeline-date">Enterprise Data</span>', '<span class="timeline-date">2023 – 2025</span>')
content = content.replace('<p>Moved upstream to design data warehouses, ensuring data quality, integration, and robust data modeling for the entire organization.</p>', '<p>Moved upstream to design data warehouses, ensuring data quality, integration, and robust data modeling for the entire organization.</p>\n            <span class="timeline-company" style="display: block; font-size: var(--text-sm); color: var(--accent-primary); margin-top: var(--spacing-2); font-style: italic;">Business Analytics & Data Specialist | AMAN Holding</span>')

content = content.replace('<span class="timeline-date">Business Analytics & Transformation</span>', '<span class="timeline-date">2025 – Present</span>')
content = content.replace('<p>Combining business strategy, technical execution, and stakeholder collaboration to drive full-scale digital transformation.</p>', '<p>Combining business strategy, technical execution, and stakeholder collaboration to drive full-scale digital transformation.</p>\n            <span class="timeline-company" style="display: block; font-size: var(--text-sm); color: var(--accent-primary); margin-top: var(--spacing-2); font-style: italic;">Senior Business & Analytics Specialist | AMAN Holding</span>')

# CHANGE 5
content = content.replace('<div class="card-icon">BA</div>', '<div class="card-icon">🎯</div>')
content = content.replace('<div class="card-icon">BI</div>', '<div class="card-icon">📊</div>')
content = content.replace('<div class="card-icon">DA</div>', '<div class="card-icon">🔍</div>')
content = content.replace('<div class="card-icon">ED</div>', '<div class="card-icon">🏗️</div>')
content = content.replace('<div class="card-icon">DT</div>', '<div class="card-icon">⚡</div>')

# CHANGE 6
content = content.replace('<p><strong>Impact:</strong> Enabled a trusted, centralized customer data foundation supporting analytics, CRM, and executive decision-making.</p>', '<p><strong>Impact:</strong> Delivered a trusted, unified customer data foundation across 5+ source systems — eliminating cross-report data discrepancies, enabling CRM teams to operate on clean consistent data, and reducing time-to-insight for customer analytics.</p>')
content = content.replace('<p><strong>Impact:</strong> Delivered secure API-based integration services that improved business process automation, data availability, and operational efficiency.</p>', '<p><strong>Impact:</strong> Standardized data exchange across internal systems and external partners via secure API gateway — improving business process automation, reducing integration effort for new services, and enabling reliable real-time data availability.</p>')
content = content.replace('<p><strong>Impact:</strong> Developed interactive Power BI reports that enabled continuous monitoring of delivery performance, release management, and project progress.</p>', '<p><strong>Impact:</strong> Gave engineering leadership objective DORA-based performance data for the first time — directly supporting quarterly performance reviews and enabling evidence-based DevOps investment decisions.</p>')
content = content.replace('<p><strong>Impact:</strong> Established a centralized analytical data platform enabling unified real-time analytics and reducing reporting time.</p>', '<p><strong>Impact:</strong> Decoupled analytics from production systems — enabling the analytics team to perform complex analysis without impacting live operations, and reducing report generation time significantly.</p>')
content = content.replace('<p><strong>Impact:</strong> Developed automation tools that significantly reduced manual effort, improved processing accuracy, and accelerated operational tasks.</p>', '<p><strong>Impact:</strong> Eliminated high-effort manual workflows — including a reporting task that previously took 7 hours, delivered in under 60 seconds after automation. Resolved a critical production blocker during a major system migration.</p>')
content = content.replace('<p><strong>Impact:</strong> Applied Monte Carlo simulation techniques using historical data to forecast timelines, supporting evidence-based planning.</p>', '<p><strong>Impact:</strong> Replaced subjective delivery estimates with a statistically grounded Monte Carlo forecasting model — improving business planning accuracy and stakeholder expectation management.</p>')
content = content.replace('<p><strong>Impact:</strong> Built AI-assisted CV ranking dashboard, Real-time Heat Stress monitoring, and Sales/profitability analytics dashboards.</p>', '<p><strong>Impact:</strong> Delivered lightweight end-to-end analytical applications combining data collection, processing, and visualization — including an AI-assisted CV ranking tool for HR, real-time safety monitoring, and profitability dashboards for business operations.</p>')

# CHANGE 7
old_demos = '''  <!-- Live Demos & Learning Journey -->
  <section class="section bg-surface">
    <div class="container">
      <div class="grid grid-2" style="gap: var(--spacing-12);">
        <!-- Live Demos -->
        <div class="reveal">
          <p class="subheading">Live Demos</p>
          <h2 style="margin-bottom: var(--spacing-8);">Working Prototypes</h2>
          <div class="grid grid-2">
            <div class="card" style="padding: var(--spacing-4);">
              <h4>Heat Stress Dashboard</h4>
              <p style="font-size: var(--text-sm);">Interactive safety compliance monitoring.</p>
              <a href="#" class="btn btn-secondary" style="font-size: var(--text-xs); padding: var(--spacing-2) var(--spacing-4);">Coming Soon</a>
            </div>
            <div class="card" style="padding: var(--spacing-4);">
              <h4>HR CV Analyzer</h4>
              <p style="font-size: var(--text-sm);">AI-driven recruitment screening tool.</p>
              <a href="#" class="btn btn-secondary" style="font-size: var(--text-xs); padding: var(--spacing-2) var(--spacing-4);">Coming Soon</a>
            </div>
          </div>
        </div>
        
        <!-- Learning Journey -->
        <div class="reveal delay-200">
          <p class="subheading">Continuous Growth</p>
          <h2 style="margin-bottom: var(--spacing-8);">Learning Journey</h2>
          <div class="tags-container">
            <span class="badge" style="border-color: var(--accent-primary);">Databricks / Lakehouse</span>
            <span class="badge" style="border-color: var(--accent-primary);">Microsoft Fabric</span>
            <span class="badge">Generative AI for Business</span>
            <span class="badge">dbt (Data Build Tool)</span>
            <span class="badge">Modern Data Stack</span>
          </div>
        </div>
      </div>
    </div>
  </section>'''

new_demos = '''  <section class="section bg-surface">
    <div class="container">
      <div class="section-header reveal">
        <p class="subheading">Continuous Growth</p>
        <h2>Learning Journey</h2>
        <p>Staying ahead of the modern data and analytics landscape.</p>
      </div>
      <div class="tags-container reveal" style="justify-content: center;">
        <span class="badge" style="border-color: var(--accent-primary);">Databricks / Lakehouse Architecture</span>
        <span class="badge" style="border-color: var(--accent-primary);">Databricks Data Engineering Associate — In Progress</span>
        <span class="badge" style="border-color: var(--accent-primary);">Microsoft Fabric</span>
        <span class="badge">Generative AI for Business</span>
        <span class="badge">dbt (Data Build Tool)</span>
        <span class="badge">Modern Data Stack</span>
      </div>
    </div>
  </section>'''
content = content.replace(old_demos, new_demos)

# CHANGE 8
content = content.replace('<h2 style="margin-bottom: var(--spacing-8);">Ready to Transform Your Data?</h2>', '<h2 style="margin-bottom: var(--spacing-8);">Looking for a Business Analyst who owns the full analytics lifecycle — from business requirements to executive dashboards? Let\'s talk.</h2>')

# CHANGE 9
old_avatar_spot = '''<div class="animate-fade-up">
          <p class="subheading delay-100">Ahmed Mohamed Sayed</p>'''
new_avatar_spot = '''<div class="animate-fade-up">
          <div class="hero-avatar" style="width: 100px; height: 100px; border-radius: 50%; background: var(--bg-surface); border: 3px solid var(--accent-primary); margin-bottom: var(--spacing-6); display: flex; align-items: center; justify-content: center; font-size: 2.5rem; color: var(--text-secondary);">
            👤
          </div>
          <p class="subheading delay-100">Ahmed Mohamed Sayed</p>'''
content = content.replace(old_avatar_spot, new_avatar_spot)

with open('d:/Portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
