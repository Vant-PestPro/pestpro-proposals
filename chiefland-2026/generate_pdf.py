#!/usr/bin/env python3
import base64, os
from weasyprint import HTML, CSS

# Encode logo as base64
logo_path = "/Users/vant/.openclaw/workspace/projects/pestpro-website/assets/logos/logo-official-transparent.png"
with open(logo_path, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

# Encode signature
sig_path = "/Users/vant/.openclaw/cleo-workspace/projects/pestpro-proposals/chiefland-2026/signature.png"
with open(sig_path, "rb") as f:
    sig_b64 = base64.b64encode(f.read()).decode()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page {{
    size: letter;
    margin: 0.85in 0.85in 0.85in 0.85in;
    @bottom-center {{
      content: "Pest Pro, LLC  |  3211 Vineland Road, #107, Kissimmee, FL 34746  |  (407) 922-2276  |  info@PestProLLC.com  |  FDACS License No. JB304313";
      font-size: 7.5pt;
      color: #666;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }}
    @bottom-right {{
      content: "Page " counter(page) " of " counter(pages);
      font-size: 7.5pt;
      color: #999;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }}
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 10pt;
    color: #1a1a1a;
    line-height: 1.55;
  }}

  /* ---- COVER HEADER ---- */
  .doc-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 3px solid #1a2557;
    padding-bottom: 18px;
    margin-bottom: 24px;
  }}
  .doc-header img {{
    height: 155px;
    width: auto;
  }}
  .doc-header-right {{
    text-align: right;
    font-size: 8.5pt;
    color: #444;
    line-height: 1.6;
  }}
  .doc-header-right strong {{
    display: block;
    font-size: 9pt;
    color: #1a2557;
    margin-bottom: 2px;
  }}

  /* ---- TITLE BLOCK ---- */
  .title-block {{
    background: #1a2557;
    color: #fff;
    padding: 20px 24px;
    border-radius: 4px;
    margin-bottom: 24px;
  }}
  .title-block h1 {{
    font-size: 17pt;
    font-weight: 700;
    letter-spacing: 0.3px;
    margin-bottom: 4px;
  }}
  .title-block .subtitle {{
    font-size: 10pt;
    color: #FFB800;
    font-weight: 600;
    letter-spacing: 0.2px;
  }}

  /* ---- META TABLE ---- */
  .meta-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 28px;
    font-size: 9.5pt;
  }}
  .meta-table td {{
    padding: 5px 10px;
    border: 1px solid #dde1ec;
  }}
  .meta-table td:first-child {{
    font-weight: 700;
    color: #1a2557;
    background: #f4f6fb;
    width: 38%;
  }}

  /* ---- SECTION HEADINGS ---- */
  h2 {{
    font-size: 12pt;
    font-weight: 700;
    color: #1a2557;
    border-bottom: 2px solid #FFB800;
    padding-bottom: 4px;
    margin: 28px 0 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.4px;
  }}
  h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #1a2557;
    margin: 18px 0 8px 0;
  }}
  h4 {{
    font-size: 10pt;
    font-weight: 700;
    color: #333;
    margin: 14px 0 6px 0;
  }}
  .property-address {{
    font-size: 9pt;
    color: #555;
    margin-bottom: 8px;
    font-style: italic;
  }}

  /* ---- BODY TEXT ---- */
  p {{
    margin-bottom: 8px;
  }}

  ul {{
    margin: 6px 0 10px 20px;
    padding: 0;
  }}
  ul li {{
    margin-bottom: 3px;
  }}

  /* ---- DATA TABLES ---- */
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 16px 0;
    font-size: 9.5pt;
  }}
  .data-table th {{
    background: #1a2557;
    color: #fff;
    padding: 7px 10px;
    text-align: left;
    font-weight: 600;
    font-size: 9pt;
  }}
  .data-table td {{
    padding: 6px 10px;
    border-bottom: 1px solid #e5e8f0;
    vertical-align: top;
  }}
  .data-table tr:nth-child(even) td {{
    background: #f7f8fc;
  }}
  .data-table .label-col {{
    font-weight: 600;
    color: #1a2557;
    width: 40%;
    background: #f4f6fb !important;
  }}

  /* ---- PRICING TABLE ---- */
  .pricing-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 6px 0;
    font-size: 10pt;
  }}
  .pricing-table th {{
    background: #1a2557;
    color: #fff;
    padding: 8px 12px;
    text-align: left;
    font-size: 9.5pt;
  }}
  .pricing-table th:last-child {{
    text-align: right;
  }}
  .pricing-table td {{
    padding: 7px 12px;
    border-bottom: 1px solid #e5e8f0;
  }}
  .pricing-table td:last-child {{
    text-align: right;
  }}
  .pricing-table tr:nth-child(even) td {{
    background: #f7f8fc;
  }}
  .pricing-total td {{
    background: #1a2557 !important;
    color: #fff;
    font-weight: 700;
    font-size: 10.5pt;
    padding: 9px 12px;
    border: none;
  }}
  .pricing-total td:last-child {{
    text-align: right;
    color: #FFB800;
    font-size: 12pt;
  }}

  .annual-note {{
    font-size: 9pt;
    color: #555;
    margin: 4px 0 16px 0;
  }}
  .annual-amount {{
    font-weight: 700;
    color: #1a2557;
  }}

  /* ---- NOTE BOX ---- */
  .note-box {{
    background: #f4f6fb;
    border-left: 4px solid #FFB800;
    padding: 9px 14px;
    margin: 10px 0 14px 0;
    font-size: 9pt;
    color: #333;
    border-radius: 0 4px 4px 0;
  }}

  /* ---- TERMS ---- */
  .term-block {{
    margin-bottom: 12px;
  }}
  .term-block .term-title {{
    font-weight: 700;
    color: #1a2557;
    font-size: 10pt;
  }}
  .term-block p {{
    margin: 3px 0 0 0;
    font-size: 9.5pt;
    color: #333;
  }}

  /* ---- SIGNATURE BLOCK ---- */
  .signature-section {{
    margin-top: 30px;
  }}
  .signature-grid {{
    display: flex;
    gap: 40px;
    margin-top: 18px;
  }}
  .sig-block {{
    flex: 1;
    border-top: 2px solid #1a2557;
    padding-top: 10px;
  }}
  .sig-block .sig-party {{
    font-size: 9.5pt;
    font-weight: 700;
    color: #1a2557;
    text-transform: uppercase;
    margin-bottom: 22px;
  }}
  .sig-line {{
    border-bottom: 1px solid #333;
    margin-bottom: 5px;
    height: 22px;
  }}
  .sig-label {{
    font-size: 8.5pt;
    color: #555;
    margin-bottom: 14px;
  }}
  .sig-filled {{
    font-size: 9.5pt;
    color: #1a1a1a;
    font-weight: 600;
    border-bottom: 1px solid #333;
    padding-bottom: 3px;
    margin-bottom: 3px;
  }}
  .sig-label-filled {{
    font-size: 8.5pt;
    color: #555;
    margin-bottom: 14px;
  }}

  /* ---- PAGE BREAKS ---- */
  .page-break {{ page-break-before: always; }}

  h2 {{
    page-break-after: avoid;
    page-break-inside: avoid;
  }}
  h3 {{
    page-break-after: avoid;
    page-break-inside: avoid;
  }}
  h4 {{
    page-break-after: avoid;
    page-break-inside: avoid;
  }}
  .property-card {{
    page-break-inside: avoid;
  }}
  .term-block {{
    page-break-inside: avoid;
  }}
  .signature-section {{
    page-break-inside: avoid;
  }}
  .signature-grid {{
    page-break-inside: avoid;
  }}
  .pricing-table {{
    page-break-inside: avoid;
  }}
  .note-box {{
    page-break-inside: avoid;
  }}
  .meta-table {{
    page-break-inside: avoid;
  }}
  .section-block {{
    page-break-inside: avoid;
  }}
  ul {{
    page-break-inside: avoid;
  }}
  p {{
    orphans: 3;
    widows: 3;
  }}

  /* ---- PROPERTY CARD ---- */
  .property-card {{
    border: 1px solid #dde1ec;
    border-radius: 4px;
    margin-bottom: 16px;
    overflow: hidden;
  }}
  .property-card-header {{
    background: #1a2557;
    color: #fff;
    padding: 8px 14px;
    font-weight: 700;
    font-size: 10pt;
  }}
  .property-card-header .prop-num {{
    color: #FFB800;
    margin-right: 6px;
  }}
  .property-card-body {{
    padding: 12px 14px;
  }}
</style>
</head>
<body>

<!-- HEADER -->
<div class="doc-header">
  <img src="data:image/png;base64,{logo_b64}" alt="Pest Pro Logo">
  <div class="doc-header-right">
    <strong>Pest Pro, LLC</strong>
    3211 Vineland Road, #107, Kissimmee, FL 34746<br>
    (407) 922-2276 &nbsp;|&nbsp; info@PestProLLC.com<br>
    FDACS License No. JB304313
  </div>
</div>

<!-- TITLE -->
<div class="title-block">
  <h1>Commercial Pest Control Service Agreement</h1>
  <div class="subtitle">Chiefland Farmers Flea Market and Managed Properties</div>
</div>

<!-- AGREEMENT DETAILS -->
<table class="meta-table">
  <tr><td class="label-col">Client</td><td>Sam Ireson</td></tr>
  <tr><td class="label-col">Account</td><td>Chiefland Farmers Flea Market and Managed Properties</td></tr>
  <tr><td class="label-col">Prepared By</td><td>Daniel Rumsey, CPO, Pest Pro, LLC</td></tr>
  <tr><td class="label-col">Date</td><td>May 2026</td></tr>
  <tr><td class="label-col">Service Commencement</td><td>June 1, 2026</td></tr>
  <tr><td class="label-col">Contract Term</td><td>June 1, 2026 through May 31, 2027 (12 months)</td></tr>
</table>

<!-- ABOUT -->
<h2>About Pest Pro, LLC</h2>
<p>Pest Pro, LLC has been protecting Florida homes and businesses since 1988. Based in Kissimmee, Florida, we deliver <strong>customized pest management systems</strong> built around the specific needs of each property. Our approach is rooted in <strong>Integrative Pest Management (IPM)</strong> principles, combining targeted treatments, environmental awareness, and ongoing monitoring to achieve lasting results. We are licensed by the Florida Department of Agriculture and Consumer Services and fully insured.</p>

<table class="data-table" style="margin-top:12px;">
  <tr><td class="label-col">License</td><td>JB304313 (GHP), FDACS</td></tr>
  <tr><td class="label-col">Insurance</td><td>Markel Insurance Company, Policy No. PCG7470-07</td></tr>
  <tr><td class="label-col">Liability Coverage</td><td>$1,000,000 per occurrence / $3,000,000 aggregate</td></tr>
  <tr><td class="label-col">Phone</td><td>(407) 922-2276</td></tr>
  <tr><td class="label-col">Email</td><td>info@PestProLLC.com</td></tr>
  <tr><td class="label-col">Mailing Address</td><td>3211 Vineland Road, #107, Kissimmee, FL 34746</td></tr>
</table>

<!-- PROPERTIES -->
<div class="section-block">
<h2>Properties Covered Under This Agreement</h2>
<p>This agreement covers pest control services for the following four properties under common management.</p>

<table class="data-table">
  <tr>
    <th style="width:5%">#</th>
    <th style="width:40%">Property</th>
    <th>Address</th>
  </tr>
  <tr><td>1</td><td>Chiefland Farmers Flea Market</td><td>1206 N Young Blvd (US HWY 19), Chiefland, FL 32626</td></tr>
  <tr><td>2</td><td>Manatee Springs RV Park</td><td>12570 NW 82nd Ct, Chiefland, FL 32626</td></tr>
  <tr><td>3</td><td>Chiefland RV Park</td><td>600 NW 11th Ave, Chiefland, FL 32626</td></tr>
  <tr><td>4</td><td>Flea Market RV Park</td><td>Chiefland, FL 32626</td></tr>
</table>
<p style="font-size:9pt; color:#555; font-style:italic;">All offices and common areas are included at each property.</p>
</div>

<!-- SCOPE -->
<h2>Scope of Services</h2>

<h3>General Household Pest (GHP) Program</h3>
<p>All four properties are enrolled in our <strong>Pest-Pro Active Ecological Maintenance</strong> program. Monthly interior and exterior treatments cover:</p>
<ul>
  <li>Ants</li>
  <li>Cockroaches (including American cockroach / Palmetto bug)</li>
  <li>Spiders</li>
  <li>Silverfish</li>
  <li>Other common household and structural insects</li>
</ul>
<p><strong>Treatment includes:</strong></p>
<ul>
  <li>Interior perimeter application (baseboards, entry points, harborage areas)</li>
  <li>Exterior perimeter application (foundation, eaves, window and door frames)</li>
  <li>Crack and crevice treatment where pest activity is found</li>
  <li>Product rotation to prevent resistance buildup</li>
</ul>

<h3>Property-by-Property Scope</h3>

<div class="property-card">
  <div class="property-card-header"><span class="prop-num">01</span> Chiefland Farmers Flea Market</div>
  <div class="property-card-body">
    <p class="property-address">1206 N Young Blvd (US HWY 19), Chiefland, FL 32626</p>
    <p>Monthly GHP service covering:</p>
    <ul>
      <li>Office and administrative areas</li>
      <li>Enclosed vendor booths (interior treatment, focused on harborage and entry points)</li>
      <li>Open-air booth areas and outdoor table grounds</li>
      <li>Bathrooms and restroom facilities</li>
      <li>Common areas and interior corridors</li>
      <li>Exterior courtyard</li>
      <li>Exterior perimeters (full building perimeter)</li>
      <li><strong>The Roost Beer and Wine Bar</strong> (interior and exterior, food-safe product application)</li>
      <li>The Roost outdoor seating area</li>
      <li>Food vendor staging area and surrounding zones</li>
    </ul>
    <div class="note-box">All treatments near food preparation and service areas are done using EPA-registered, food-safe products applied per label requirements.</div>
  </div>
</div>

<div class="property-card">
  <div class="property-card-header"><span class="prop-num">02</span> Manatee Springs RV Park</div>
  <div class="property-card-body">
    <p class="property-address">12570 NW 82nd Ct, Chiefland, FL 32626</p>
    <p>Monthly GHP service covering:</p>
    <ul>
      <li>Office and check-in area</li>
      <li>Common areas and shared resident facilities</li>
      <li>Bathrooms and laundry facilities</li>
      <li>Exterior perimeters and common grounds</li>
    </ul>
  </div>
</div>

<div class="property-card">
  <div class="property-card-header"><span class="prop-num">03</span> Chiefland RV Park</div>
  <div class="property-card-body">
    <p class="property-address">600 NW 11th Ave, Chiefland, FL 32626</p>
    <p>Monthly GHP service covering:</p>
    <ul>
      <li>Office and check-in area</li>
      <li>Common areas and shared resident facilities</li>
      <li>Bathrooms and laundry facilities</li>
      <li>Exterior perimeters and common grounds</li>
    </ul>
  </div>
</div>

<div class="property-card">
  <div class="property-card-header"><span class="prop-num">04</span> Flea Market RV Park</div>
  <div class="property-card-body">
    <p class="property-address">Chiefland, FL 32626</p>
    <p>Monthly GHP service covering:</p>
    <ul>
      <li>Office and check-in area</li>
      <li>Common areas and shared resident facilities</li>
      <li>Bathrooms and laundry facilities</li>
      <li>Exterior perimeters and common grounds</li>
    </ul>
  </div>
</div>

<h3>Rodent Control Program</h3>
<p><strong>Chiefland Farmers Flea Market and The Roost</strong></p>
<p>Twelve (12) tamper-resistant rodent bait stations will be installed along the exterior perimeter of the Chiefland Farmers Flea Market building and The Roost Beer and Wine Bar.</p>
<p><strong>Program includes:</strong></p>
<ul>
  <li>Installation of 12 tamper-resistant bait stations at selected perimeter locations</li>
  <li>Monthly inspection of all stations during scheduled service visits</li>
  <li>Monitoring, activity documentation, and bait replenishment as needed</li>
  <li>Activity log maintained per station</li>
  <li>Bait station placement map provided to management at time of installation</li>
</ul>
<div class="note-box">All bait stations meet OSHA and EPA requirements for commercial and public-access environments. All rodenticide products are registered with the Florida Department of Agriculture and Consumer Services.</div>

<!-- SERVICE SCHEDULE -->
<h2>Service Schedule</h2>
<table class="data-table">
  <tr>
    <th>Property</th>
    <th>Frequency</th>
  </tr>
  <tr><td>Chiefland Farmers Flea Market</td><td>Monthly</td></tr>
  <tr><td>Manatee Springs RV Park</td><td>Monthly</td></tr>
  <tr><td>Chiefland RV Park</td><td>Monthly</td></tr>
  <tr><td>Flea Market RV Park</td><td>Monthly</td></tr>
</table>
<p>Service days and times will be set with your on-site contact to avoid disruption to operations and tenants.</p>

<!-- INVESTMENT -->
<h2>Investment</h2>
<table class="pricing-table">
  <tr>
    <th>Service</th>
    <th>Monthly Rate</th>
  </tr>
  <tr>
    <td>GHP Pest Control (All Four Properties, bundled)</td>
    <td>$550.00</td>
  </tr>
  <tr>
    <td>Rodent Bait Station Program (12 stations, installation and monthly monitoring)</td>
    <td>Included</td>
  </tr>
  <tr class="pricing-total">
    <td>Total Monthly Investment</td>
    <td>$550.00</td>
  </tr>
</table>
<p class="annual-note">Annual Contract Value: <span class="annual-amount">$6,600.00</span> &nbsp;|&nbsp; All services listed above are included in the monthly rate. No additional fees.</p>

<!-- TERMS -->
<div class="page-break"></div>

<h2>Terms and Conditions</h2>

<div class="term-block">
  <div class="term-title">Contract Term</div>
  <p>This agreement runs for twelve (12) months, from June 1, 2026 through May 31, 2027, unless cancelled as described below.</p>
</div>

<div class="term-block">
  <div class="term-title">Cancellation</div>
  <p>Either party may cancel by giving thirty (30) days written notice to the other party.</p>
</div>

<div class="term-block">
  <div class="term-title">Payment Terms</div>
  <p>Invoices are sent on the 1st of each service month. Payment is due within thirty (30) days (Net 30). We accept check, ACH bank transfer, or credit card.</p>
</div>

<div class="term-block">
  <div class="term-title">Late Payments</div>
  <p>Accounts not paid within the Net 30 period may be placed on a service hold until the balance is paid.</p>
</div>

<div class="term-block">
  <div class="term-title">Access</div>
  <p>Client agrees to give Pest Pro, LLC access to all listed properties to perform the services in this agreement. Please let us know about any access restrictions or scheduling needs in advance.</p>
</div>

<div class="term-block">
  <div class="term-title">Questions and Service Requests</div>
  <p>For any service questions, re-service requests, or concerns, contact Pest Pro, LLC at (407) 922-2276 or info@PestProLLC.com.</p>
</div>

<div class="term-block">
  <div class="term-title">Re-Service Guarantee</div>
  <p>If covered pest activity comes back between scheduled visits, we will return and re-treat at no charge. Client must contact us during the active service period and provide access to the property.</p>
</div>

<div class="term-block">
  <div class="term-title">Chemical Safety</div>
  <p>All products used by Pest Pro, LLC are EPA-registered and approved by the Florida Department of Agriculture and Consumer Services. All work is performed by a Florida-licensed Certified Pest Operator or under their direct supervision.</p>
</div>

<!-- LICENSING -->
<div class="section-block">
<h2>Licensing and Insurance</h2>
<table class="data-table">
  <tr><td class="label-col">Business License Number</td><td>JB304313</td></tr>
  <tr><td class="label-col">License Type</td><td>Pest Control Business License, General Household Pest (GHP)</td></tr>
  <tr><td class="label-col">Issued By</td><td>Florida Department of Agriculture and Consumer Services (FDACS)</td></tr>
  <tr><td class="label-col">License Expiration</td><td>November 30, 2026</td></tr>
  <tr><td class="label-col">Liability Insurer</td><td>Markel Insurance Company (NAIC 38970)</td></tr>
  <tr><td class="label-col">Policy Number</td><td>PCG7470-07</td></tr>
  <tr><td class="label-col">Liability Coverage</td><td>$1,000,000 per occurrence / $3,000,000 aggregate</td></tr>
  <tr><td class="label-col">Policy Expiration</td><td>February 24, 2027</td></tr>
</table>
<p style="font-size:9pt; color:#555;">A certificate of insurance is available upon request.</p>
</div>

<!-- SIGNATURE -->
<h2>Agreement and Authorization</h2>
<p>By signing below, both parties agree to the terms and scope of services in this agreement.</p>

<div class="signature-section">
  <div class="signature-grid">
    <div class="sig-block">
      <div class="sig-party">Pest Pro, LLC</div>
      <img src="data:image/png;base64,{sig_b64}" style="height:55px; width:auto; margin-bottom:2px; display:block;">
      <div class="sig-label">Signature</div>
      <div class="sig-filled">Daniel Rumsey</div>
      <div class="sig-label-filled">Name</div>
      <div class="sig-filled">Owner / Certified Operator</div>
      <div class="sig-label-filled">Title</div>
      <div class="sig-filled">May 21, 2026</div>
      <div class="sig-label-filled">Date</div>
    </div>
    <div class="sig-block">
      <div class="sig-party">Chiefland Farmers Flea Market and Managed Properties</div>
      <div class="sig-line"></div>
      <div class="sig-label">Signature</div>
      <div class="sig-filled">Sam Ireson</div>
      <div class="sig-label-filled">Name</div>
      <div class="sig-line"></div>
      <div class="sig-label">Title</div>
      <div class="sig-line"></div>
      <div class="sig-label">Date</div>
    </div>
  </div>
</div>

</body>
</html>"""

output_path = "/Users/vant/.openclaw/cleo-workspace/projects/pestpro-proposals/chiefland-2026/PestPro-ServiceAgreement-Chiefland-2026.pdf"

HTML(string=html_content).write_pdf(
    output_path,
    stylesheets=[CSS(string="body { font-family: sans-serif; }")]
)

print(f"PDF generated: {output_path}")
print(f"Size: {os.path.getsize(output_path):,} bytes")
