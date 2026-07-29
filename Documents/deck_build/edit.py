#!/usr/bin/env python
import sys
from defusedxml.minidom import parse
A='http://schemas.openxmlformats.org/drawingml/2006/main'
P='http://schemas.openxmlformats.org/presentationml/2006/main'
SLIDES='unpacked/ppt/slides/'

def shapes_by_name(doc):
    out={}
    for sp in doc.getElementsByTagNameNS(P,'sp'):
        nv=sp.getElementsByTagNameNS(P,'cNvPr')
        if nv: out[nv[0].getAttribute('name')]=sp
    return out

def prev_elem(node):
    p=node.previousSibling
    while p is not None and p.nodeType!=1: p=p.previousSibling
    return p

def set_text(t, s):
    # ensure a text child, set data, preserve spaces
    if t.firstChild is None:
        t.appendChild(t.ownerDocument.createTextNode(s))
    else:
        t.firstChild.data=s
    t.setAttribute('xml:space','preserve')

def edit_shape(shape, strings):
    runs=shape.getElementsByTagNameNS(A,'r')
    for i,r in enumerate(list(runs)):
        ts=r.getElementsByTagNameNS(A,'t')
        if i<len(strings):
            if ts: set_text(ts[0], strings[i])
        else:
            parent=r.parentNode
            pv=prev_elem(r)
            parent.removeChild(r)
            if pv is not None and pv.localName=='br':
                pv.parentNode.removeChild(pv)

def delete_shape(doc, name):
    for sp in doc.getElementsByTagNameNS(P,'sp'):
        nv=sp.getElementsByTagNameNS(P,'cNvPr')
        if nv and nv[0].getAttribute('name')==name:
            sp.parentNode.removeChild(sp); return True
    return False

def apply(fn, edits, deletes=()):
    doc=parse(SLIDES+fn)
    sh=shapes_by_name(doc)
    for name,strings in edits.items():
        if name not in sh:
            print(f"  !! {fn}: shape {name} NOT FOUND"); continue
        edit_shape(sh[name], strings)
    for name in deletes:
        if not delete_shape(doc,name):
            print(f"  !! {fn}: delete target {name} NOT FOUND")
    with open(SLIDES+fn,'w',encoding='utf-8') as f:
        f.write(doc.toxml())
    print(f"  edited {fn}")

# ---- template shape-name helpers ----
def three(p, title, L,Li, M,Mi, R,Ri):
    d={f'Google Shape;1639;{p}':[title],
       f'Google Shape;1640;{p}':[L], f'Google Shape;1644;{p}':[M], f'Google Shape;1645;{p}':[R]}
    for sid,txt in zip(['1643','1648','1651'],Li): d[f'Google Shape;{sid};{p}']=[txt]
    for sid,txt in zip(['1664','1668','1670'],Mi): d[f'Google Shape;{sid};{p}']=[txt]
    for sid,txt in zip(['1655','1658','1661'],Ri): d[f'Google Shape;{sid};{p}']=[txt]
    return d

def four(p, title, c1,c1i, c2,c2i, c3,c3i, c4,c4i):
    d={f'Google Shape;1676;{p}':[title],
       f'Google Shape;1677;{p}':[c1], f'Google Shape;1688;{p}':[c2],
       f'Google Shape;1709;{p}':[c3], f'Google Shape;1698;{p}':[c4]}
    for sid,txt in zip(['1681','1684','1687'],c1i): d[f'Google Shape;{sid};{p}']=[txt]
    for sid,txt in zip(['1691','1694','1697'],c2i): d[f'Google Shape;{sid};{p}']=[txt]
    for sid,txt in zip(['1713','1716','1719'],c3i): d[f'Google Shape;{sid};{p}']=[txt]
    for sid,txt in zip(['1702','1705','1708'],c4i): d[f'Google Shape;{sid};{p}']=[txt]
    return d

def two(p, title, L,Li, R,Ri):
    d={f'Google Shape;1612;{p}':[title], f'Google Shape;1613;{p}':[L], f'Google Shape;1614;{p}':[R]}
    for sid,txt in zip(['1618','1621','1624'],Li): d[f'Google Shape;{sid};{p}']=[txt]
    for sid,txt in zip(['1628','1631','1634'],Ri): d[f'Google Shape;{sid};{p}']=[txt]
    return d

def divider(label,title,sub):
    return {'Google Shape;1170;p133':[label,title,sub]}

P3='p153'; P4='p154'; P2='p152'

# ===== 1. Cover =====
apply('slide14.xml', {
 'Google Shape;559;p68':['Rethinking Task Mining Client configuration'],
 'Google Shape;562;p68':['From fragmented setup to one guided capture journey'],
 'Google Shape;560;p68':['Product Design · Mahalakshmi Ravikumar'],
 'Google Shape;561;p68':['28 July 2026'],
})

# ===== 2. Agenda (5 items; delete 06-08) =====
apply('slide16.xml', {
 'Google Shape;1181;p135':['What we’ll cover'],
 'Google Shape;1187;p135':['The problem'],
 'Google Shape;1183;p135':['What research revealed'],
 'Google Shape;1185;p135':['The proposal — capture levels'],
 'Google Shape;1189;p135':['A single object-based structure'],
 'Google Shape;1199;p135':['Scope, metrics & the ask'],
}, deletes=['Google Shape;1194;p135','Google Shape;1195;p135',
            'Google Shape;1196;p135','Google Shape;1197;p135',
            'Google Shape;1200;p135','Google Shape;1201;p135'])

# ===== 3. Divider 01 =====
apply('slide15.xml', divider('01','The problem','Where admins lose the most time and confidence'))

# ===== 4. Three-col: where config breaks down =====
apply('slide25.xml', three(P3,
 'Three ways configuration breaks down today',
 'Fragmented setup',   ['Split across a Basic web app and an Advanced desktop editor',
                        'Most real setup needs the Advanced editor',
                        'Moving between them is manual and file-based'],
 'Windows-only editor', ['The Advanced editor runs only on Windows',
                         'Mac admins must procure or emulate a PC',
                         'Raised by every participant, including our own VEs'],
 'Opaque controls & noise', ['Technical labels like UIAA go unexplained',
                             'Events vs. logs never made intuitive sense',
                             'Everything captured by default buries the signal'],
))

# ===== 5. Divider 02 =====
apply('slide48.xml', divider('02','What research revealed','Interviews and tree testing with admins and value engineers'))

# ===== 6. Four-col: what admins told us =====
apply('slide26.xml', four(P4,
 'What admins told us',
 'Fragmented IA',  ['Basic vs. Advanced is confusing and restrictive',
                    'Core functions hidden behind multiple clicks',
                    'A one-way street between the two modes'],
 'Windows barrier',['The Advanced editor is Windows-only',
                    'Blocks setup before capture even begins',
                    'Directly delays time-to-value'],
 'Opaque controls',['Jargon with no in-product guidance',
                    'Admins pick options they don’t understand',
                    'Or stall waiting on support'],
 'Noisy defaults', ['Everything is captured by default',
                    'Many fields add no analytical value',
                    'Hard to tell signal from noise'],
))

# ===== 7. Statement (blue) bridge =====
apply('slide34.xml', {'Google Shape;1882;p163':
  ['Granularity isn’t the ','problem.','','Making it ','understandable is.']})

# ===== 8. Divider 03 =====
apply('slide49.xml', divider('03','The proposal','Capture levels, and one object-based structure'))

# ===== 9. Three-col: capture levels =====
apply('slide52.xml', three(P3,
 'One decision, three capture levels',
 'Full',   ['Captures everything — events, attributes and screenshots',
            'For processes you want to analyse in depth',
            'The default, matching how the client behaves today'],
 'Custom', ['Captures that an app was used, plus element names',
            'No typed text, selected values or screenshots',
            'For sensitive screens or a first discovery pass'],
 'Deny',   ['Captures nothing for that scope',
            'For apps or URLs to exclude entirely',
            'Nothing to redact or preview'],
))

# ===== 10. Comparison: two surfaces -> one journey =====
apply('slide40.xml', {
 'Google Shape;1981;p169':['Today'],
 'Google Shape;1982;p169':['Proposed'],
 'Google Shape;1983;p169':['Two surfaces'],
 'Google Shape;1984;p169':['One journey'],
 'Google Shape;1985;p169':['Configuring','capture'],
 'Google Shape;1986;p169':['Windows-only, file-based,','settings scattered across tabs'],
 'Google Shape;1998;p169':['Admins guess which mode','they need — and get stuck','moving between the two'],
 'Google Shape;1987;p169':['No Basic / Advanced split —','one guided path for everyone'],
 'Google Shape;1999;p169':['Full control stays,','now comprehensible','and in-context —','no longer Windows-only'],
})

# ===== 11. Three-col: object-based structure =====
apply('slide53.xml', three(P3,
 'One object-based structure',
 'Capture Rules',    ['The core: what Task Mining records, and where',
                      'Each rule sets scope, capture level and captured data',
                      'A default rule catches anything not covered'],
 'Privacy & Consent',['Redaction, with the ability to test the result',
                      'Hashing of usernames and machine IDs',
                      'User consent — all in one place'],
 'Behaviour & data', ['Client Behaviour: recording, startup, live monitor',
                      'Data Connection: where captured data is sent',
                      'SAP and other sources appear only when relevant'],
))

# ===== 12. Divider 04 =====
apply('slide50.xml', divider('04','Validation','What held up in navigation testing — and the one thing to fix'))

# ===== 13. Three-col: structure held up =====
apply('slide54.xml', three(P3,
 'The structure held up — one thing to fix',
 'IA validated',   ['Both VEs landed in the right area on every task',
                    'Privacy for redaction, Capture Rules for targeting',
                    'Safe to design and build against'],
 'The naming failed',['Neither could explain Full vs. Usage-only',
                      'The strongest signal across both sessions',
                      'The confusion lived in the level selector'],
 'What we changed',['Renamed Usage-only to Custom',
                    'Adding a “what this captures” summary',
                    'Re-testing the rename before hi-fi'],
))

# ===== 14. Divider 05 =====
apply('slide51.xml', divider('05','Scope, metrics & the ask','What ships first, and what we need to confirm'))

# ===== 15. Two-col: what ships first =====
apply('slide24.xml', two(P2,
 'What ships first',
 'MVP',      ['One unified, guided configuration surface',
              'Capture levels with clean, de-noised event lists',
              'Core privacy — redaction, hashing, consent'],
 'Post-MVP', ['Advanced redaction — GDPR/HIPAA libraries, test-on-sample',
              'Validation in EMS and the configuration simulator',
              'New projects only; reuse by duplicating rule sets'],
))

# ===== 16. Four-col: success metrics =====
apply('slide56.xml', four(P4,
 'How we’ll measure success',
 'Time-to-valid-config',['From starting a config','to a validated, deployable rule set','New flow vs. today’s baseline'],
 'Errors & rework',     ['Misconfigurations and re-uploads','Config-related support tickets','Read after launch'],
 'Task success',        ['Tree and usability test success','Directness of navigation','Can admins explain the levels'],
 'Redaction misses',    ['Sensitive values that slip through','Compliance escalations','Plus VE feedback on data quality'],
))

# ===== 17. Three-col: the ask =====
apply('slide55.xml', three(P3,
 'What we need from you',
 'Confirm scope', ['Sign off the MVP vs. Post-MVP split',
                   'And that capture levels sit within the MVP',
                   'Plus the new-projects-only guardrail'],
 'Own the PRD',   ['PM to own a short PRD',
                   'Set a baseline and goal per metric',
                   'Confirm engine behaviour and rule limits'],
 'Set timelines', ['Phase timelines with Engineering',
                   'Resolve open items — LEM access, Custom’s default set',
                   'Then this becomes the shared reference'],
))

print("ALL DONE")
