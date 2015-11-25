#!/usr/bin/env python
import os

from launchpadlib.launchpad import Launchpad
from jinja2 import Template

lp = Launchpad.login_with('lp-report-bot', 'production', version='devel')
prj = lp.projects['fuel']

tags = prj.official_bug_tags

people = """
    alekseyk-ru
    dshulyak
    rustyrobot
    ikalnitsky
    nmarkov
    aroma-x
    akislitsky
    kozhukalov
    dpyzhov
    a-gordeev
    ivankliuk
    vsharshov
    maciej-iai
    sbrzeczkowski
    ksambor
    prmtl
    pkaminski
    romcheg
    loles
    rmoe
""".split("\n    ")

teams = """
    fuel-python
    fuel-astute
    fuel-provisioning
    fuel-build
""".split("\n    ")

tag_ownership_tree = {
    'alekseyk-ru': [
        'feature-advanced-networking',
        'feature-bonding',
        'feature-hardware-change',
        'feature-multi-l2',
        'module-networks'],
    'dshulyak': [
        'feature-redeployment',
        'module-netcheck',
        'module-ostf',
        'module-serialization',
        'module-tasks'
    ],
    'rustyrobot': [
        'feature-plugins'
    ],
    'ikalnitsky': [
        'feature-logging',
        'feature-remote-repos',
        'feature-upgrade',
    ],
    'nmarkov': [
        'feature-demo-site',
        'feature-validation',
        'module-fuelmenu',
        'module-nailgun',
        'module-shotgun',
    ],
    'aroma-x': [
    ],
    'akislitsky': [
        'feature-deadlocks',
        'feature-mongo',
        'feature-security',
        'feature-simple-mode',
        'feature-stats',
    ],
    'kozhukalov': [
        'feature-native-provisioning',
        'module-build',
        'module-master-node-installation',
        'module-nailgun-agent',
        'module-volumes',
    ],
    'a-gordeev': [
        'feature-image-based',
    ],
    'ivankliuk': [
    ],
    'vsharshov': [
        'feature-progress-bar',
        'feature-reset-env',
        'feature-stop-deployment',
        'module-astute',
    ],
    'romcheg': [
        'module-client',
    ],
}

not_started_pre = "field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&"
started_pre = "field.status%3Alist=INPROGRESS&"
incomplete_pre = "field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&"
open_pre = not_started_pre + started_pre + incomplete_pre
ml_pre = "field.milestone%3Alist=68007&"
uri_base = "https://bugs.launchpad.net/fuel/+bugs?" + ml_pre
#pre = status_pre + ml_pre

def num_link(url):
    count = os.popen("curl '%s' 2> /dev/null | grep -B 1 -m 1 '            result' | head -n 1" % url).read()
    return "<a href='%s'>%s</a>" % (url, count.strip())

tag_ownership = {}

for owner in tag_ownership_tree.keys():
    for t in tag_ownership_tree[owner]:
        tag_ownership[t] = owner

for tag in tags:
    if tag and (tag.startswith("feature-") or tag.startswith("module-") or tag=="tech-debt" or tag=="customer-found" or tag=="feature"):
        if not tag_ownership.has_key(tag):
            tag_ownership[tag] = None

tag_report = []

for t in tag_ownership.keys():
    row = {
        'tag': t,
        'total': num_link(uri_base + open_pre + "field.tag=" + t),
        'in_queue': num_link(uri_base + not_started_pre + "field.tag=" + t),
        'in_progress': num_link(uri_base + started_pre + "field.tag=" + t),
        'incomplete': num_link(uri_base + incomplete_pre + "field.tag=" + t),
        'owner': tag_ownership[t],
    }
    tag_report.append(row)

people_report = []

for p in teams + people:
    row = {
        'name': p,
        'total': num_link(uri_base + open_pre + "field.assignee=" + p),
        'in_queue': num_link(uri_base + not_started_pre + "field.assignee=" + p),
        'in_progress': num_link(uri_base + started_pre + "field.assignee=" + p),
        'incomplete': num_link(uri_base + incomplete_pre + "field.assignee=" + p),
    }
    people_report.append(row)

template = """
<style type='text/css'>
th{background: #eee}
</style>
<h1>HCF readiness</h1>
<table>
<tr><th colspan=5>Tags</th></tr>
{% for group in tag_report|groupby('owner') %}
<tr><th colspan=5>Tag owner: {{group.grouper}}</th></tr>
<tr><th>Tag</th><th>Total</th><th>Not started</th><th>In progress</th>
<th>Incomplete</th></tr>
{% for row in group.list %}
<tr><th>{{row.tag}}</th><td>{{row.total}}</td><td>{{row.in_queue}}</td>
<td>{{row.in_progress}}</td><td>{{row.incomplete}}</td></tr>
{% endfor %}
{% endfor %}
<tr><th colspan=5>People</th></tr>
{% for p in people_report %}
<tr><th>{{p.name}}</th><td>{{p.total}}</td><td>{{p.in_queue}}</td>
<td>{{p.in_progress}}</td><td>{{p.incomplete}}</td></tr>
{% endfor %}
</table>
"""

html_report = Template(template)
print html_report.render(tag_report=tag_report, people_report=people_report)
